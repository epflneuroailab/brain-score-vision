# Created by David Coggan on 2024 06 25

import numpy as np
from brainscore_vision import load_stimulus_set, load_dataset, load_metric
from brainscore_vision.benchmarks import BenchmarkBase
from brainscore_vision.benchmark_helpers.screen import place_on_screen
from brainscore_core.metrics import Score
from brainscore_vision.model_interface import BrainModel
from brainscore_vision.utils import LazyLoad
from scipy.stats import sem
import pandas as pd

# the BIBTEX will be used to link to the publication from the benchmark for further details
BIBTEX = """@article {
    Tong.Coggan2024.behavior,
    author = {David D. Coggan and Frank Tong},
    title = {Modeling human visual recognition of occluded objects}},
    year = {2024},
    url = {},
    journal = {in prep}}"""


class Coggan2024_behavior_ConditionWiseLabelingAccuracySimilarity(BenchmarkBase):
    def __init__(self):
        self._metric = load_metric('accuracy_distance')
        self._assembly = LazyLoad(lambda: load_dataset('Coggan2024_behavior'))
        self._assembly['truth'] = self._assembly['object_class']  # the assembly is missing a 'truth' column which is
                                                                  #  required by the labeling task
        self._visual_degrees = 10
        self._number_of_trials = 1
        super(Coggan2024_behavior_ConditionWiseLabelingAccuracySimilarity, self).__init__(
            identifier='tong.Coggan2024_behavior-LabelingConditionWiseAccuracySimilarity',
            version=1,
            ceiling_func=lambda: self._metric.leave_one_out_ceiling(
                self._assembly,
                variables=['occluder_type', 'visibility', 'occluder_color'],
                chance_level=1/8),
            parent='behavior',
            bibtex=BIBTEX,
        )

    def __call__(self, candidate: BrainModel):
        choice_labels = set(self._assembly['object_class'].values)
        choice_labels = list(sorted(choice_labels))
        candidate.start_task(BrainModel.Task.label, choice_labels)
        stimulus_set = place_on_screen(self._assembly.stimulus_set,
                                       target_visual_degrees=candidate.visual_degrees(),
                                       source_visual_degrees=self._visual_degrees)
        labels = candidate.look_at(stimulus_set, number_of_trials=self._number_of_trials)
        raw_score = self._metric(labels, self._assembly, variables=['occluder_type', 'visibility', 'occluder_color'],
                                 chance_level=1/8)
        ceiling = self.ceiling
        score = raw_score / ceiling
        score.attrs['raw'] = raw_score
        score.attrs['ceiling'] = ceiling
        return score


class Coggan2024_behavior_ConditionWiseProbabilitiesAccuracySimilarity(BenchmarkBase):
    def __init__(self):
        self._metric = load_metric('accuracy_distance')
        self._fitting_stimuli = load_stimulus_set('Coggan2024_behavior_fitting')  # this fails is wrapped by LazyLoad
        self._assembly = LazyLoad(lambda: load_dataset('Coggan2024_behavior'))
        self._assembly['truth'] = self._assembly['object_class']  # the assembly is missing a 'truth' column which is
                                                                  #  required by the labeling task
        self._visual_degrees = 10
        self._number_of_trials = 1
        super(Coggan2024_behavior_ConditionWiseProbabilitiesAccuracySimilarity, self).__init__(
            identifier='tong.Coggan2024_behavior-LabelingConditionWiseAccuracySimilarity',
            version=1,
            ceiling_func=lambda: self._metric.ceiling(
                self._assembly,
                variables=['occluder_type', 'visibility', 'occluder_color'],
                chance_level=1/8
            ),
            parent='behavior',
            bibtex=BIBTEX,
        )

    def __call__(self, candidate: BrainModel):
        fitting_stimuli = place_on_screen(
            self._fitting_stimuli,
            target_visual_degrees=candidate.visual_degrees(),
            source_visual_degrees=self._visual_degrees)
        candidate.start_task(BrainModel.Task.probabilities, fitting_stimuli)
        stimulus_set = place_on_screen(self._assembly.stimulus_set,
                                       target_visual_degrees=candidate.visual_degrees(),
                                       source_visual_degrees=self._visual_degrees)
        probabilities = candidate.look_at(stimulus_set, number_of_trials=self._number_of_trials)
        labels = [probabilities.choice[c].values for c in probabilities.argmax(axis=1)]
        raw_score = self._metric(labels, self._assembly, variables=['occluder_type', 'visibility', 'occluder_color'],
                                 chance_level=1/8)
        ceiling = self.ceiling
        score = raw_score / ceiling
        score.attrs['raw'] = raw_score
        score.attrs['ceiling'] = ceiling
        return score


class Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(BenchmarkBase):
    def __init__(self, visibility='all', occluder_type='all'):
        self.visibility = visibility
        self.occluder_type = occluder_type
        self._metric = load_metric('accuracy')
        self._ceiling_func = lambda assembly: get_noise_ceiling(assembly)
        #self._assembly = load_dataset('Coggan2024_behavior')
        self._stimulus_set = load_dataset('Coggan2024_behavior').stimulus_set
        super(Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy, self).__init__(
            identifier='tong.Coggan2024_behavior-LabelingConditionWiseEngineeringAccuracy',
            version=1,
            ceiling_func=lambda: Score(1),
            parent='Coggan2024-top1',
            bibtex=BIBTEX,
        )

    def __call__(self, candidate: BrainModel):
        self.filter_occluders()
        choice_labels = set(self._stimulus_set['object_class'].values)
        choice_labels = list(sorted(choice_labels))
        candidate.start_task(BrainModel.Task.label, choice_labels)
        labels = candidate.look_at(self._stimulus_set)
        raw_score = self._metric(labels, self._stimulus_set['object_class'].values)
        ceiling = self.ceiling
        score = raw_score / ceiling
        score.attrs['raw'] = raw_score
        score.attrs['ceiling'] = ceiling
        return score

    def filter_occluders(self):
        """
        a method that filters both self._stimulus_set and self._assembly to only contain the values of
        self.visibility and self.occluder_type for their respective columns.
        """
        if self.visibility != 'all':
            self.filter_variable('visibility', self.visibility)
        if self.occluder_type != 'all':
            self.filter_variable('occluder_type', self.occluder_type)
        else:
            # remove unoccluded condition when looking at "all" conditions
            self._stimulus_set = self._stimulus_set[(self._stimulus_set['occluder_type'] != 'unoccluded')]

    def filter_variable(self, variable, filter):
        # Filter the stimulus set based on variable
        stimulus_set = self._stimulus_set.copy()
        filtered_stimulus_set = stimulus_set[(stimulus_set[variable] == filter)]
        self._stimulus_set = filtered_stimulus_set

        # grab the filtered stimulus ids to do easy selection in the assembly
        #filtered_stimulus_ids = filtered_stimulus_set['stimulus_id'].unique()
        #self._assembly = self._assembly.sel(stimulus_id=filtered_stimulus_ids)


class Coggan2024_behavior_ConditionWiseAccuracySimilarity_Correlation(BenchmarkBase):
    ### DEPRECATED IN FAVOR OF Coggan2024_behavior_ConditionWiseLabelingAccuracySimilarity
    ### Here for future comparison/reference/proofing
    """
    This benchmark measures classification accuracy for a set of occluded object images, then attains the mean accuracy
    for each of the 18 occlusion conditions. This is then correlated with the corresponding accuracies for each of the
    30 human subjects in the behavioral experiment to obtain the brain score.
    Note: Because the object-occluder pairings were randomized for each subject, image-level metrics (e.g., error
    consistency) have limited utility here as a ceiling cannot be calculated.
    """

    def __init__(self):
        self._fitting_stimuli = load_stimulus_set('Coggan2024_behavior_fitting')  # this fails is wrapped by LazyLoad
        self._assembly = LazyLoad(lambda: load_dataset('Coggan2024_behavior'))
        self._visual_degrees = 10
        self._number_of_trials = 1
        self._ceiling_func = lambda assembly: get_noise_ceiling(assembly)
        super(Coggan2024_behavior_ConditionWiseAccuracySimilarity_Correlation, self).__init__(
            identifier='tong.Coggan2024_behavior-ConditionWiseAccuracySimilarity',
            version=1,
            ceiling_func=lambda df: get_noise_ceiling(df),
            parent='behavior',
            bibtex=BIBTEX,
        )

    def __call__(self, candidate: BrainModel) -> Score:

        fitting_stimuli = place_on_screen(
            self._fitting_stimuli,
            target_visual_degrees=candidate.visual_degrees(),
            source_visual_degrees=self._visual_degrees)
        candidate.start_task(BrainModel.Task.probabilities, fitting_stimuli)
        stimulus_set = place_on_screen(
            self._assembly.stimulus_set,
            target_visual_degrees=candidate.visual_degrees(),
            source_visual_degrees=self._visual_degrees)
        probabilities = candidate.look_at(
            stimulus_set, number_of_trials=self._number_of_trials)
        model_predictions = [
            probabilities.choice[c].values for c in probabilities.argmax(axis=1)]

        data = pd.DataFrame(dict(
            subject=self._assembly.subject,
            object_class=self._assembly.object_class,
            occluder_type=self._assembly.occluder_type,
            occluder_color=self._assembly.occluder_color,
            visibility=self._assembly.visibility,
            human_prediction=self._assembly.values,
            human_accuracy=self._assembly.human_accuracy,
            model_prediction=model_predictions
        ))
        data['model_accuracy'] = pd.Series(
            data.model_prediction == data.object_class, dtype=int)

        # get correlation between model and human performance across conditions
        performance = (
            data[data.visibility < 1]
            .groupby(['subject', 'occluder_type', 'occluder_color'])
            .mean(numeric_only=True)
            .reset_index()
        )
        scores = performance.groupby('subject').apply(
            lambda df: np.corrcoef(df.human_accuracy, df.model_accuracy)[0, 1])
        score = Score(np.mean(scores))
        score.attrs['raw'] = scores

        # get ceiled score
        ceiled_score = ceiler(score, self._ceiling_func(performance))
        ceiled_score.attrs['raw'] = score

        return ceiled_score


def get_noise_ceiling(performance: pd.DataFrame) -> Score:
    """
    Returns the noise ceiling for human similarity estimates. This is the lower bound of typical noise-ceiling range
    (e.g. Nili et al., 2014), i.e., the correlation of condition-wise accuracies between each individual subject and
    the mean of the remaining subjects in the sample. This matches how the model is scored, if the group values are
    substituted for model values.
    """
    nc = []
    for subject in performance.subject.unique():
        performance_ind = performance[performance.subject == subject]
        performance_grp = performance[performance.subject != subject]
        numeric_cols = performance_grp.select_dtypes(include=np.number).columns
        performance_grp = performance_grp.groupby(['occluder_type', 'occluder_color'])[numeric_cols].mean()
        merged_df = performance_ind.merge(
            performance_grp, on=['occluder_type', 'occluder_color'])
        nc.append(np.corrcoef(merged_df.human_accuracy_x, merged_df.human_accuracy_y)[0, 1])
    ceiling = Score(np.mean(nc))
    ceiling.attrs['raw'] = nc
    ceiling.attrs['error'] = sem(nc)
    return ceiling


def ceiler(score: Score, ceiling: Score) -> Score:
    # ro(X, Y)
    # = (r(X, Y) / sqrt(r(X, X) * r(Y, Y)))^2
    # = (r(X, Y) / sqrt(r(Y, Y) * r(Y, Y)))^2  # assuming that r(Y, Y) ~ r(X, X) following Yamins 2014
    # = (r(X, Y) / r(Y, Y))^2
    r_square = np.power(score.values / ceiling.values, 2)
    ceiled_score = Score(r_square)
    if 'error' in score.attrs:
        ceiled_score.attrs['error'] = score.attrs['error']
    ceiled_score.attrs[Score.RAW_VALUES_KEY] = score
    ceiled_score.attrs['ceiling'] = ceiling
    return ceiled_score


def remove_nans(data):
    """
    removes nans from the data and replaces them with a string 'none'. uses pandas to simultaneously hand numeric
    and non-numeric data.
    """
    for coord in data.coords:
        data[coord] = data[coord].where(~pd.isna(data[coord]), 'none')
    return data