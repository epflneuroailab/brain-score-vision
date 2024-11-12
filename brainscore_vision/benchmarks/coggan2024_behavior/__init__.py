# Created by David Coggan on 2024 06 25

from brainscore_vision import benchmark_registry
from .benchmark import (
    Coggan2024_behavior_ConditionWiseLabelingAccuracySimilarity,
    Coggan2024_behavior_ConditionWiseProbabilitiesAccuracySimilarity,
    Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy,
)


benchmark_registry['tong.Coggan2024_behavior-ConditionWiseLabelingAccuracySimilarity'] = Coggan2024_behavior_ConditionWiseLabelingAccuracySimilarity
benchmark_registry['tong.Coggan2024_behavior-ConditionWiseProbabilitiesAccuracySimilarity'] = Coggan2024_behavior_ConditionWiseProbabilitiesAccuracySimilarity
benchmark_registry['tong.Coggan2024_behavior-ConditionWiseLabelingEngineeringAccuracy'] = Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy

# 10% visibility
benchmark_registry['Coggan2024_visibility_01_occludertype_polkasquare'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='polkasquare')
benchmark_registry['Coggan2024_visibility_01_occludertype_polkadot'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='polkadot')
benchmark_registry['Coggan2024_visibility_01_occludertype_barObl04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='barObl04')
benchmark_registry['Coggan2024_visibility_01_occludertype_naturalUntexturedCropped2'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='naturalUntexturedCropped2')
benchmark_registry['Coggan2024_visibility_01_occludertype_barVert04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='barVert04')
benchmark_registry['Coggan2024_visibility_01_occludertype_barHorz04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='barHorz04')
benchmark_registry['Coggan2024_visibility_01_occludertype_mudsplash'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='mudsplash')
benchmark_registry['Coggan2024_visibility_01_occludertype_crossBarOblique'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='crossBarOblique')
benchmark_registry['Coggan2024_visibility_01_occludertype_crossBarCardinal'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.1, occluder_type='crossBarCardinal')

# 20% visibility
benchmark_registry['Coggan2024_visibility_02_occludertype_polkasquare'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='polkasquare')
benchmark_registry['Coggan2024_visibility_02_occludertype_polkadot'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='polkadot')
benchmark_registry['Coggan2024_visibility_02_occludertype_barObl04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='barObl04')
benchmark_registry['Coggan2024_visibility_02_occludertype_naturalUntexturedCropped2'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='naturalUntexturedCropped2')
benchmark_registry['Coggan2024_visibility_02_occludertype_barVert04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='barVert04')
benchmark_registry['Coggan2024_visibility_02_occludertype_barHorz04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='barHorz04')
benchmark_registry['Coggan2024_visibility_02_occludertype_mudsplash'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='mudsplash')
benchmark_registry['Coggan2024_visibility_02_occludertype_crossBarOblique'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='crossBarOblique')
benchmark_registry['Coggan2024_visibility_02_occludertype_crossBarCardinal'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.2, occluder_type='crossBarCardinal')

# 40% visibility
benchmark_registry['Coggan2024_visibility_04_occludertype_polkasquare'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='polkasquare')
benchmark_registry['Coggan2024_visibility_04_occludertype_polkadot'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='polkadot')
benchmark_registry['Coggan2024_visibility_04_occludertype_barObl04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='barObl04')
benchmark_registry['Coggan2024_visibility_04_occludertype_naturalUntexturedCropped2'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='naturalUntexturedCropped2')
benchmark_registry['Coggan2024_visibility_04_occludertype_barVert04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='barVert04')
benchmark_registry['Coggan2024_visibility_04_occludertype_barHorz04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='barHorz04')
benchmark_registry['Coggan2024_visibility_04_occludertype_mudsplash'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='mudsplash')
benchmark_registry['Coggan2024_visibility_04_occludertype_crossBarOblique'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='crossBarOblique')
benchmark_registry['Coggan2024_visibility_04_occludertype_crossBarCardinal'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.4, occluder_type='crossBarCardinal')

# 60% visibility
benchmark_registry['Coggan2024_visibility_06_occludertype_polkasquare'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='polkasquare')
benchmark_registry['Coggan2024_visibility_06_occludertype_polkadot'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='polkadot')
benchmark_registry['Coggan2024_visibility_06_occludertype_barObl04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='barObl04')
benchmark_registry['Coggan2024_visibility_06_occludertype_naturalUntexturedCropped2'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='naturalUntexturedCropped2')
benchmark_registry['Coggan2024_visibility_06_occludertype_barVert04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='barVert04')
benchmark_registry['Coggan2024_visibility_06_occludertype_barHorz04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='barHorz04')
benchmark_registry['Coggan2024_visibility_06_occludertype_mudsplash'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='mudsplash')
benchmark_registry['Coggan2024_visibility_06_occludertype_crossBarOblique'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='crossBarOblique')
benchmark_registry['Coggan2024_visibility_06_occludertype_crossBarCardinal'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.6, occluder_type='crossBarCardinal')

# 80% visibility
benchmark_registry['Coggan2024_visibility_08_occludertype_polkasquare'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='polkasquare')
benchmark_registry['Coggan2024_visibility_08_occludertype_polkadot'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='polkadot')
benchmark_registry['Coggan2024_visibility_08_occludertype_barObl04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='barObl04')
benchmark_registry['Coggan2024_visibility_08_occludertype_naturalUntexturedCropped2'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='naturalUntexturedCropped2')
benchmark_registry['Coggan2024_visibility_08_occludertype_barVert04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='barVert04')
benchmark_registry['Coggan2024_visibility_08_occludertype_barHorz04'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='barHorz04')
benchmark_registry['Coggan2024_visibility_08_occludertype_mudsplash'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='mudsplash')
benchmark_registry['Coggan2024_visibility_08_occludertype_crossBarOblique'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='crossBarOblique')
benchmark_registry['Coggan2024_visibility_08_occludertype_crossBarCardinal'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=0.8, occluder_type='crossBarCardinal')

# 100% visibility
benchmark_registry['Coggan2024_visibility_10_occludertype_unoccluded'] = lambda: Coggan2024_behavior_ConditionWiseLabelingEngineeringAccuracy(visibility=1.0, occluder_type='unoccluded')
