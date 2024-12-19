import csv
from pathlib import Path
from collections import defaultdict, Counter
import random

from brainio.stimuli import StimulusSet
from brainio.packaging import package_stimulus_set


# every stimulus set is separate, incl. baseline condition
STIMULUS_SETS = ['short-2', 'short-4', 'short-6', 'short-8', 'short-16', 'equal-2',
                 'long-2', 'equal-16', 'long-16', 'vernier-only']
# DATASET_LENGTHS = {'test': 50, 'fit': 500}

# Define constants for default split percentage
FIT_SPLIT_PERCENTAGE = 0.8  # 80% for training by default


# Updated function
def collect_vernier_stimulus_set_with_split(root_directory, dataset, fit_percentage=FIT_SPLIT_PERCENTAGE):
    """
    Collects stimuli from a single dataset and splits into fit and test sets.

    Parameters:
        root_directory (Path): Path to the root directory containing the dataset.
        dataset (str): Name of the dataset folder.
        fit_percentage (float): Proportion of data to allocate to the fit (train) split.

    Returns:
        Tuple[StimulusSet, StimulusSet]: Two StimulusSets, one for fit and one for test.
    """
    stimuli = []
    stimulus_paths = {}

    metadata_directory = Path(f'{root_directory}/{dataset}/metadata.csv')
    image_directory = Path(f'{root_directory}/{dataset}/images')

    # Group stimuli by `vernier_offset_arcsec`
    stimuli_by_offset = defaultdict(list)
    with open(metadata_directory, 'r') as metadata:
        reader = csv.DictReader(metadata)
        for row in reader:
            stimulus = {
                'image_size_x_pix': int(row['image_size_x_pix']),
                'image_size_y_pix': int(row['image_size_y_pix']),
                'image_size_c': int(row['image_size_c']),
                'image_size_degrees': float(row['image_size_degrees']),
                'vernier_height_arcsec': float(row['vernier_height_arcsec']),
                'vernier_offset_arcsec': float(row['vernier_offset_arcsec']),
                'image_label': row['image_label'],
                'flanker_height_arcsec': float(row['flanker_height_arcsec']),
                'flanker_spacing_arcsec': float(row['flanker_spacing_arcsec']),
                'line_width_arcsec': float(row['line_width_arcsec']),
                'flanker_distance_arcsec': float(row['flanker_distance_arcsec']),
                'num_flankers': int(row['num_flankers']),
                'vernier_position_x_pix': int(row['vernier_position_x_pix']),
                'vernier_position_y_pix': int(row['vernier_position_y_pix']),
                'stimulus_id': str(row['stimulus_id']),
            }
            stimuli_by_offset[row['vernier_offset_arcsec']].append(stimulus)
            stimulus_paths[row['stimulus_id']] = Path(f'{image_directory}/{row["filename"]}')

    # Split stimuli into fit and test sets
    fit_stimuli = []
    test_stimuli = []
    for offset, group in stimuli_by_offset.items():
        random.shuffle(group)  # Shuffle group for randomness
        split_index = int(len(group) * fit_percentage)
        fit_stimuli.extend(group[:split_index])
        test_stimuli.extend(group[split_index:])

    # Create StimulusSet objects for fit and test
    fit_set = StimulusSet(fit_stimuli)
    test_set = StimulusSet(test_stimuli)

    # Assign stimulus paths and metadata
    fit_set.stimulus_paths = {stimulus['stimulus_id']: stimulus_paths[stimulus['stimulus_id']] for stimulus in fit_stimuli}
    test_set.stimulus_paths = {stimulus['stimulus_id']: stimulus_paths[stimulus['stimulus_id']] for stimulus in test_stimuli}

    fit_set.name = f'VernierEngineering2024_{dataset}_fit'
    test_set.name = f'VernierEngineering2024_{dataset}_test'

    fit_set.identifier = f'VernierEngineering2024_{dataset}_fit'
    test_set.identifier = f'VernierEngineering2024_{dataset}_test'
    offset_counts = Counter([stimulus['vernier_offset_arcsec'] for stimulus in fit_stimuli])
    offset_counts = dict(offset_counts)
    print(offset_counts)

    # count the number of each of the two 'image_label's in the fit set
    print(f"Number of 'image_label' in fit set: {len([stimulus['image_label'] == 'left' for stimulus in fit_stimuli])}")

    return fit_set, test_set


if __name__ == '__main__':
    root_directory = Path(r'C:\Users\loennqvi\Github\neuroai_brainscore\brain-score-vision\brainscore_vision\data\malania2007\data_packaging\VernierEngineeringStimulusSet')
    dataset = "VernierEngineering2024"  # Update with your actual dataset name

    # Split dataset
    for stimulus_set in STIMULUS_SETS:
        fit_set, test_set = collect_vernier_stimulus_set_with_split(root_directory, stimulus_set, fit_percentage=0.8)
        print(len(fit_set))
        # Example usage: Upload the splits to S3
        prints_fit = package_stimulus_set(catalog_name=None,
                                          proto_stimulus_set=fit_set,
                                          stimulus_set_identifier=fit_set.name,
                                          bucket_name="brainio-brainscore")
        print(prints_fit)

        prints_test = package_stimulus_set(catalog_name=None,
                                           proto_stimulus_set=test_set,
                                           stimulus_set_identifier=test_set.name,
                                           bucket_name="brainio-brainscore")
        print(prints_test)