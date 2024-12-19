from brainio.assemblies import PropertyAssembly

from brainscore_vision import data_registry, stimulus_set_registry, load_stimulus_set
from brainscore_vision.data_helpers.s3 import load_assembly_from_s3, load_stimulus_set_from_s3


BIBTEX = """@article{malania2007,
            author = {Malania, Maka and Herzog, Michael H. and Westheimer, Gerald},
            title = "{Grouping of contextual elements that affect vernier thresholds}",
            journal = {Journal of Vision},
            volume = {7},
            number = {2},
            pages = {1-1},
            year = {2007},
            issn = {1534-7362},
            doi = {10.1167/7.2.1},
            url = {https://doi.org/10.1167/7.2.1}
        }"""


data_registry['Malania2007.equal2'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_equal-2',
    version_id="yFXK8xjGjEmuYTSfS58rGS_ah3.NGg0X",
    sha1="277b2fbffed00e16b6a69b488f73eeda5abaaf10",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.equal16'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_equal-16',
    version_id="SRZ7bs.Ek59GkeS084Pvdy38uTzFs4yw",
    sha1="ef49506238e8d2554918b113fbc60c133077186e",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.long2'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_long-2',
    version_id="2c1lWuXthb3rymB3seTQX1jVqiKUTn1f",
    sha1="9076a5b693948c4992b6c8e753f04a7acd2014a1",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.long16'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_long-16',
    version_id="qshNxhxjgusWyWiXnbfFN6gqjLgRh8fO",
    sha1="3106cf1f2fa9e66617ebf231df05d29077fc478f",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.short2'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_short-2',
    version_id="8CQ9MupuljAgkkKUXs3hiOliHg8xoDxb",
    sha1="85fb65ad76de48033c704b9c5689771e1ea0457d",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.short4'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_short-4',
    version_id=".ZUO0upSfQrWLPgd4oGwAaCbN4bz6S6H",
    sha1="75506be9a26ec38a223e41510f1a8cb32d5b0bc9",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.short6'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_short-6',
    version_id="q4FugpNGkT_FQP..qIVzye83hAQR2xfS",
    sha1="2901be6b352e67550da040d79d744819365b8626",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.short8'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_short-8',
    version_id="4_lcRl_I7Mp0RHxcfqZ9tkAZjVh.5oMU",
    sha1="6daf47b086cb969d75222e320f49453ed8437885",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.short16'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_short-16',
    version_id="fFqEIyIC9CHzqTEmv0MitjCgpeMX5pxJ",
    sha1="8ae0898caad718b747f85fce5888416affc3a569",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)
data_registry['Malania2007.vernier_only'] = lambda: load_assembly_from_s3(
    identifier='Malania2007_vernier-only',
    version_id="JLWf2pIR_UadQHqwtegJkC6XzWdbSNGi",
    sha1="1cf83e8b6141f8b0d67ea46994f342325f62001f",
    bucket="brainio-brainscore",
    cls=PropertyAssembly,
    stimulus_set_loader=None,
)


stimulus_set_registry['Malania2007.equal2'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_equal-2',
    bucket="brainio-brainscore",
    csv_sha1="36f3c92a1335895b10c4150f5c25a68ab4576d4a",
    zip_sha1="80be52e8701ecb8e7fbb81c0bff9c148ddc2b401",
    csv_version_id="lkbpUNzhET3.hR.9StpSVvoxh05aWzoi",
    zip_version_id="Wd7Fc3QVn1baC53Iy.E5ha4YqWvdybM3"
)
stimulus_set_registry['Malania2007.equal2_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_equal-2_fit',
    bucket="brainio-brainscore",
    csv_sha1="b7105f44d5d781f5e06159008a3f63c9f774c2d1",
    zip_sha1="ba5c1bacbb4afe40c5a19eddb07fc9f98312ec69",
    csv_version_id="qhsx4_OM0FSCl7SU0hXhhmiJvLnDU6Dm",
    zip_version_id="PzGnzHtpGghaHGK6MO4DeSy7w.rDUfRN"
)
stimulus_set_registry['Malania2007.equal16'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_equal-16',
    bucket="brainio-brainscore",
    csv_sha1="14f9f7098831691811abf9953766951edc952203",
    zip_sha1="5127e88eaed1ef64247c7cb4262868533fb4ebae",
    csv_version_id="bgBDFK3666NPXwINqGcdouvtWy12yqyY",
    zip_version_id="zlkMQOE9wfTQHPohmxol4uAR6y0zqwjI"
)
stimulus_set_registry['Malania2007.equal16_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_equal-16_fit',
    bucket="brainio-brainscore",
    csv_sha1="2ff7f2f97250b9bcce3d2753be6e5b98e083892b",
    zip_sha1="db07ef4862fd9cb65c1e726cacc5914821296a5b",
    csv_version_id="cVYkl_N7c36UfjbWqAffYrHVDbPhmiwa",
    zip_version_id="azu8FTnJVmsou98co5iVE2G8OemMIl4H"
)
stimulus_set_registry['Malania2007.long2'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_long-2',
    bucket="brainio-brainscore",
    csv_sha1="153b987c4c6b8a22efb88be26aaa46bd36912c9b",
    zip_sha1="07bb413d56ac77fc71823559780cdb16e4df563d",
    csv_version_id="nKEYl_hb8tBKOg47O28iLY5.oYyimmAf",
    zip_version_id="3BS.xmMHnND1C3bjDsut8qILlzMIJhHQ"
)
stimulus_set_registry['Malania2007.long2_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_long-2_fit',
    bucket="brainio-brainscore",
    csv_sha1="8b6d1557879e6271554c0fcb67bf6b2941dad2c8",
    zip_sha1="66205529af748ffd88579caef86b107838c0b0da",
    csv_version_id="ut0_Zbq97vwzmkk9MY.0h5phJZqp_McX",
    zip_version_id="qcGk5zy7KN.vEmLgtZKRYn0OXyWoER9G"
)
stimulus_set_registry['Malania2007.long16'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_long-16',
    bucket="brainio-brainscore",
    csv_sha1="6c5d45b489bc290e41013d211d18570368012c9b",
    zip_sha1="10944e5b65e8da9e52087d3cbbdc6575538c2847",
    csv_version_id="sswWsVsgFbPU1psGfoIS.0Goi6b.9Dn2",
    zip_version_id="5.gegdwQMNpqcP3FnW4DkTZ7s3bT0j75"
)
stimulus_set_registry['Malania2007.long16_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_long-16_fit',
    bucket="brainio-brainscore",
    csv_sha1="603dc8edb169f39e322f8980972eda1930c300ed",
    zip_sha1="a67330e18f1e5d9ad3829d8d8c000487fe3e4d48",
    csv_version_id=".qV8En95o4QR_jgvr145ww8xvgAnoIs5",
    zip_version_id="h_IWMOSq4uJe91XgOEHFSVwa01vH74.H"
)
stimulus_set_registry['Malania2007.short2'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-2',
    bucket="brainio-brainscore",
    csv_sha1="c8bb84c5468a43348149afe24d5c0ebda233d54e",
    zip_sha1="1739226e7e32f60a7bb060fecc14c4a6353ca2ad",
    csv_version_id="sGDRldX6CEbDguYsikFArt1P5aMMCueM",
    zip_version_id="1RjSss5KIKKfK7UzeGRyQgBu.I47xcIQ"
)
stimulus_set_registry['Malania2007.short2_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-2_fit',
    bucket="brainio-brainscore",
    csv_sha1="600c754811aa27d80a155c8ac643a81f2347ce3a",
    zip_sha1="a1a121dbbbf761caea0a086c2a74ab511f296ed5",
    csv_version_id="X7c1h_64KB18noSoG2uaGo2baYTvblKa",
    zip_version_id="hx5Of92KkReH_GXPll4MnFrJ.yI3UQhH"
)
stimulus_set_registry['Malania2007.short4'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-4',
    bucket="brainio-brainscore",
    csv_sha1="181c912c03fdb3e4f89a737584a3a0816859f816",
    zip_sha1="820019a7f68db60fac11a5c5f3e42037cf205248",
    csv_version_id="pjGwais_x1SzlK9kOWzypnEjWOqIJejt",
    zip_version_id="uHY9JlyoIKF7QY.7h2YnaMjoGMOLTS0Y"
)
stimulus_set_registry['Malania2007.short4_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-4_fit',
    bucket="brainio-brainscore",
    csv_sha1="65af7b5d3845a7ea284aefba21734e1d298742c8",
    zip_sha1="5234b449c05a43e726543029137fe26930157b09",
    csv_version_id=".HhdLMWwnSAJTeBICSys3fjbWpa9V3ee",
    zip_version_id="M1eKvnklDoUFZ70K4x9EFiYycyIAybXY"
)
stimulus_set_registry['Malania2007.short6'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-6',
    bucket="brainio-brainscore",
    csv_sha1="57813230e337a09c4c423da927c1f33e62054547",
    zip_sha1="dab58e8e996f91af643a0b61247e7ef87f35338d",
    csv_version_id="4GLCXr_ii4r7jHsOoRbTZWgdQMrChMwy",
    zip_version_id="WQ.jkGJuKabBAt9br9oAYB4wDstDVPer"
)
stimulus_set_registry['Malania2007.short6_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-6_fit',
    bucket="brainio-brainscore",
    csv_sha1="ea7eb26b42fe9e4fc1ac2ed6e9bad439e8077ce1",
    zip_sha1="895e69c835b22b07ee66a0f5f53e7a108ac8287c",
    csv_version_id="agzJvrPzCyMsHVPuJeHnu.kWLqCOgTyv",
    zip_version_id="6ArqgIEm9wZoihx6_swTilr.fBtd14Gw"
)
stimulus_set_registry['Malania2007.short8'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-8',
    bucket="brainio-brainscore",
    csv_sha1="3df9a38605a4590eac8a1151779ba68c3cd54dc1",
    zip_sha1="7626364e0776b2809ae36d9cb713c6ff9a0d0c05",
    csv_version_id="8OV0COxeMrzgsJnm_vC3q9pEB44LSllC",
    zip_version_id="YmcL0kN4_sDVMxegHdurephfduxWHFua"
)
stimulus_set_registry['Malania2007.short8_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-8_fit',
    bucket="brainio-brainscore",
    csv_sha1="2782c818056b374e86195cbdb0ab1a52ef0d01da",
    zip_sha1="ec2fa2a261d965455ffa81acdb0fddef447ad4ff",
    csv_version_id="iInrw3cTlTQw0NxQ0bvpbar.jD64IkYh",
    zip_version_id="hCWq6yFtO6LlDrAY46B0fhHVWaxJSDGY"
)
stimulus_set_registry['Malania2007.short16'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-16',
    bucket="brainio-brainscore",
    csv_sha1="9f5f4e3597006c50530017ce769c8689d43b06f5",
    zip_sha1="b67b1e70e8ba698907c95614bcb16eea6ff2f090",
    csv_version_id="syxlZTsmHlr6eL8L4aI9ddWbKhr8tLUk",
    zip_version_id="6kSKtajsISK6TTE6Ej3UG0oGblFzU9dk"
)
stimulus_set_registry['Malania2007.short16_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_short-16_fit',
    bucket="brainio-brainscore",
    csv_sha1="5bc0314a6c16095a70049fa5e8df5e9b94345f30",
    zip_sha1="0ca3930831ca926ea8b8c3600695b639ff05ddb5",
    csv_version_id="HZWWB5vyyMoaTCyM7t.4RwfnNtP4e64I",
    zip_version_id="aWy0F_It4iUGAgGJCECz6NOJ__JHr2ib"
)
stimulus_set_registry['Malania2007.vernier_only'] = lambda: load_stimulus_set_from_s3(
    identifier='Malania2007_vernier-only',
    bucket="brainio-brainscore",
    csv_sha1="c71f654fccf1265a95dd0585c186232a2519e944",
    zip_sha1="eadff359975c3ba250224ce1942544b091415095",
    csv_version_id="PQoHljauNff1yWCMNKd5JEzR8Y38_j.0",
    zip_version_id="6gE8TX1J89BnsHmdqb7rIGvRMw.sZdo6"
)
stimulus_set_registry['VernierEngineering2024.short2_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-2_fit',
    bucket="brainio-brainscore",
    csv_sha1="84fb3ecb17ae54f787830240e98bfa9448115224",
    zip_sha1="5378dc85a485b0b58a7f11740e511750670320e3",
    csv_version_id="WzXvc5hWjJ5GwxxB_gIVJuNqwbR0aJwC",
    zip_version_id="2bP0TX8VEZr_UWaapH7cTXc_eLUCMSLi"
)
stimulus_set_registry['VernierEngineering2024.short2_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-2_test',
    bucket="brainio-brainscore",
    csv_sha1="f0835dcc0606ef6d2f71d353b855a8549ddf9043",
    zip_sha1="ff4956e8a0ce03929632a2eca03ca18077e27e6b",
    csv_version_id="U_4nI99u4m__0I2Q8eAhKoW9oCW68Pd2",
    zip_version_id="VNHG2h8RbyV_yHIHOkTrmh.dpKzkqNB4"
)
stimulus_set_registry['VernierEngineering2024.short4_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-4_fit',
    bucket="brainio-brainscore",
    csv_sha1="17ba7167847862229e86c3d635eccc99c3e5ce9d",
    zip_sha1="2012ff6aba8c3eb51a53bb97d4b321c269aadc39",
    csv_version_id="x445JqodYBDBGf8ynIp7T_ZFvs1zzA8A",
    zip_version_id="r16EZ9_qLdpPCE4hXZJu79A5K2urBNo3"
)
stimulus_set_registry['VernierEngineering2024.short4_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-4_test',
    bucket="brainio-brainscore",
    csv_sha1="eba0a4e2d1134556fd0c76f744a4c67d042fb02b",
    zip_sha1="e1492bd61cff0746d23b9abd027cfb549127e0d2",
    csv_version_id="adaYBQAeIrgTXnihxKhXesvwUyF_3juh",
    zip_version_id="Vwc.g51HAqQvN3SM3TLLIEznsuuxoNcf"
)
stimulus_set_registry['VernierEngineering2024.short6_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-6_fit',
    bucket="brainio-brainscore",
    csv_sha1="44846bee8dcae893edb2d4999e91d75feab084df",
    zip_sha1="7b820eba167d68c8d0f59ee129a2480e8661a023",
    csv_version_id="Ec6sRFlbQcQ9EOfoUFKoZuPaQcXhod_G",
    zip_version_id="87xSejgRbUWgbcPueIfK07G4VnBzfbz3"
)
stimulus_set_registry['VernierEngineering2024.short6_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-6_test',
    bucket="brainio-brainscore",
    csv_sha1="8c4e09102a75a1d9ac063ba68472af8d5ba19499",
    zip_sha1="237b52465fa268e3c76d10c784139aa011085f42",
    csv_version_id="c38AFNxpFnhLm0OC5VbXYXPO5tXiOcqb",
    zip_version_id="3dXM70Xp2zwZcbkz48wkaGYGm21jxnrV"
)
stimulus_set_registry['VernierEngineering2024.short8_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-8_fit',
    bucket="brainio-brainscore",
    csv_sha1="f9f0c86805d6d87c91de119632af9f6ce3e113d2",
    zip_sha1="e3d6dc6fc05c1aea52aa862e868e1b907fb4b1e5",
    csv_version_id="foQ4hDhY7LehAmkB1fC.qMMjGOY8bpPV",
    zip_version_id="gu_1yn48iWOX1X2MGJutNzFTVEfh2oaO"
)
stimulus_set_registry['VernierEngineering2024.short8_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-8_test',
    bucket="brainio-brainscore",
    csv_sha1="f7d5f44decf06ae8756b445d64f6bb8b27d19fb6",
    zip_sha1="75611f6050c85f37f8d5b22918dcee207bbcf8ce",
    csv_version_id="3rH5KneB_CKUB183Kl2QLpK7Er4TiM1a",
    zip_version_id="SJwgfvuYh0UpJT9RYEuSaFCCNBRitH0c"
)
stimulus_set_registry['VernierEngineering2024.short16_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-16_fit',
    bucket="brainio-brainscore",
    csv_sha1="9f7d4e83b1c167218f910bb3c5dc33405edf9e9b",
    zip_sha1="276dfc4759e745be4acf2e2b020a50dc2ebc718b",
    csv_version_id="E21ZA3u3t1vLVUqOJmP6xcfhSN.cI.Mb",
    zip_version_id="Yg.GvFFykAaUT9RjQyDXmypRQrMTNrf_"
)
stimulus_set_registry['VernierEngineering2024.short16_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_short-16_test',
    bucket="brainio-brainscore",
    csv_sha1="098181690548d28afc584b23ae8302193a87acb1",
    zip_sha1="98513feb8d110efd8f9a2591c623f45033356468",
    csv_version_id="LHQnaplsWYyff1q.cKpfntXkvWt358cj",
    zip_version_id="Vnyas9ZrbGmjUTu5SwkiEjGLEoK98Hb1"
)
stimulus_set_registry['VernierEngineering2024.equal2_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_equal-2_fit',
    bucket="brainio-brainscore",
    csv_sha1="d47c43f68eb61424efb4a42703d0eb10abc6cdae",
    zip_sha1="155872f2733305f556e7f8dd97c2a56c5491b113",
    csv_version_id="rddzygIx4CAGTYltdXR7fKpXERv13vec",
    zip_version_id="5H6YbqhM5qDoDLF49drKRb1D8LR_EPk7"
)
stimulus_set_registry['VernierEngineering2024.equal2_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_equal-2_test',
    bucket="brainio-brainscore",
    csv_sha1="17525ede2b8bf581fc47a58abf533d59c2ede3fd",
    zip_sha1="64370057f58c3e5a2b024d0f8dc57d14789055af",
    csv_version_id="bzAJHuOaHvHXajIZakhPN95Ore7QyyO7",
    zip_version_id="ONMUPWkaPqNCunxteM5AsoYuIytEJDoI"
)
stimulus_set_registry['VernierEngineering2024.equal16_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_equal-16_fit',
    bucket="brainio-brainscore",
    csv_sha1="19759f8dcbbad62f31fba9ad77c8ecea30f1af4f",
    zip_sha1="1f170c07efd918beefb9855d9d8e724eb4711f2d",
    csv_version_id="ef6Ai4jwL3aUXbMiCCXV1AC6WT2VYGLM",
    zip_version_id=".DMyKejBOsPZTMXl_CsYeOvi8x4yjwLY"
)
stimulus_set_registry['VernierEngineering2024.equal16_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_equal-16_test',
    bucket="brainio-brainscore",
    csv_sha1="2b8f3f21a95e901e62e205f4abcdf69cf376596b",
    zip_sha1="4b5c1531bfa42c53887d71e7aa0e3ee7e3b587b2",
    csv_version_id="gXA.Oeb3fN4Zj5BwtXRsNlpoOHVgRTpp",
    zip_version_id="BhDCeRhNQAFAy7du9wwi2.1y84jIdZrO"
)
stimulus_set_registry['VernierEngineering2024.long2_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_long-2_fit',
    bucket="brainio-brainscore",
    csv_sha1="1a96112c3e2a961a551eedee6841983e025dbef2",
    zip_sha1="7b1bed2a3509b4f219eda3a419ca63833e22b214",
    csv_version_id=".rg.pxyyBc.6J5PB0mqtEtsIKMv2iSYE",
    zip_version_id="mFYQFFNCajZJE0RUWIFKiAiEY36nq8AD"
)
stimulus_set_registry['VernierEngineering2024.long2_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_long-2_test',
    bucket="brainio-brainscore",
    csv_sha1="bbd2005d6029347a404c448df6f16d5704690f9c",
    zip_sha1="16e8c6122dc34e4a051fd43a33af852a9b554dbe",
    csv_version_id="lOU8IGFMJXRbpPX7IkqG6u..P7pB7vaW",
    zip_version_id="H87NqzPLeqUYC_ss7UZSG1sUAfbRSVCg"
)
stimulus_set_registry['VernierEngineering2024.long16_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_long-16_fit',
    bucket="brainio-brainscore",
    csv_sha1="cc88faba62bf15cf45ec176b6b931cbbc86fcc8e",
    zip_sha1="654b1c98905a51655cf528780a5238c49766e7f3",
    csv_version_id="bXrE5sUuvK25.cwUZ6TI5bRbH.iIiBYi",
    zip_version_id="YYhkWAod1qEn4Uc7nT.JqEyZrzs5OOy3"
)
stimulus_set_registry['VernierEngineering2024.long16_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_long-16_test',
    bucket="brainio-brainscore",
    csv_sha1="3d74c214c64023bd8d67b84cdd5f3e6c0cdccd77",
    zip_sha1="6d64a3a3d6543cae0781e37ad5f5565353890e56",
    csv_version_id="RXtLgF1tUCsP9igXai5UfGETyAyztALg",
    zip_version_id="UXIsQX9dvqIEFkYd82.FJSEHv9bR.PN0"
)
stimulus_set_registry['VernierEngineering2024.vernier_only_fit'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_vernier-only_fit',
    bucket="brainio-brainscore",
    csv_sha1="1b2edc7593cfc86f42e6c60059ba068977b327d7",
    zip_sha1="0dca6b49e6ea0b3f4d0b77d4b94eee6a0f9af4ec",
    csv_version_id="WU..KxQPhkjWmC2e2Yq3tyN.UO5ZJZKp",
    zip_version_id="wXsZKE9t7P_.pOg6VWaEzFu3_xR9x.J."
)
stimulus_set_registry['VernierEngineering2024.vernier_only_test'] = lambda: load_stimulus_set_from_s3(
    identifier='VernierEngineering2024_vernier-only_test',
    bucket="brainio-brainscore",
    csv_sha1="0c84e11761bce93ed6d039ec49dbdc2212deb6cf",
    zip_sha1="5f0478de6d142d5517a28d8ccfbf4c51520f04ff",
    csv_version_id="8jAU8j9vVFiKyY81xpGPnSxz5R6bTjku",
    zip_version_id="ML40c90TzIGb7Ig6vRKXNmtNICKnrhsK"
)