from brainscore_vision import load_benchmark, load_model

"""
This is an example file for usage of the pathfinder engineering accuracy benchmark.
"""

DATASETS = [
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
    200
]


def score_pathfinder_model(model_name, curve_length):
    model = load_model(model_name)
    benchmark = load_benchmark(f"_Lonnqvist2024IndividualCurvesEngineeringAccuracy.{curve_length}")
    score = benchmark(model)
    return score


if __name__ == '__main__':
    for dataset in DATASETS:
        print(f"Dataset: {dataset}")
        score = score_pathfinder_model('alexnet', dataset)
        print(score)
