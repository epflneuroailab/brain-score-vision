from brainscore_vision import benchmark_registry
from . import benchmark

benchmark_registry['Lonnqvist2024_InlabInstructionsBehavioralAccuracyDistance'] = lambda: benchmark._Lonnqvist2024BehavioralAccuracyDistanceInlabInstructions()
benchmark_registry['Lonnqvist2024_InlabNoInstructionsBehavioralAccuracyDistance'] = lambda: benchmark._Lonnqvist2024BehavioralAccuracyDistanceInlabNoInstructions()
benchmark_registry['Lonnqvist2024_OnlineNoInstructionsBehavioralAccuracyDistance'] = lambda: benchmark._Lonnqvist2024BehavioralAccuracyDistanceOnlineNoInstructions()

benchmark_registry['Lonnqvist2024_EngineeringAccuracy'] = lambda: benchmark._Lonnqvist2024EngineeringAccuracy()

benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.20'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(20)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.30'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(30)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.40'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(40)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.50'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(50)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.60'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(60)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.70'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(70)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.80'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(80)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.90'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(90)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.100'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(100)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.110'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(110)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.120'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(120)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.130'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(130)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.140'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(140)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.150'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(150)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.160'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(160)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.170'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(170)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.180'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(180)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.190'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(190)
benchmark_registry['_Lonnqvist2024IndividualCurvesEngineeringAccuracy.200'] = lambda: benchmark._Lonnqvist2024IndividualCurvesEngineeringAccuracy(200)