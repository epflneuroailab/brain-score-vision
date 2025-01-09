from brainscore_vision import load_benchmark, load_model

"""
This is an example file for usage of the vernier engineering accuracy benchmark.
"""

DATASETS = [
    'vernier_only',
    'short2',
    'short4',
    'short6',
    'short8',
    'short16',
    'equal2',
    'long2',
    'equal16',
    'long16'
]


def score_vernier_model(model_name, vernier_condition):
    model = load_model(model_name)
    #benchmark = load_benchmark(f"VernierEngineeringAccuracy2024.{vernier_condition}")
    benchmark = load_benchmark(f"_Malania2007AccuracyAtThreshold.{vernier_condition}")
    score = benchmark(model)
    return score


if __name__ == '__main__':
    for dataset in DATASETS:
        print(f"Dataset: {dataset}")
        score = score_vernier_model('alexnet', dataset)
        print(score)
