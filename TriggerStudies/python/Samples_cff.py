import FWCore.ParameterSet.Config as cms

testlist=['file:step3.root']

# 

Zplist=[
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_0_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_10_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_11_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_12_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_13_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_14_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_15_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_16_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_17_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_18_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_19_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_1_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_20_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_21_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_22_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_23_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_24_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_25_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_26_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_27_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_28_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_29_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_2_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_30_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_31_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_32_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_33_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_34_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_35_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_36_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_37_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_38_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_39_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_3_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_40_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_41_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_42_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_43_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_44_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_45_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_46_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_47_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_48_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_49_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_4_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_50_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_51_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_52_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_53_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_54_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_5_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_6_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_7_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_8_step3.root',
'file:/nfs/dust/cms/user/usaiem/gc-output/TrgStudiesBoost/step3/step3_9_step3.root',
]


dizionario={'test':testlist, 'Zp':Zplist
}

# 'tH800':tH800list,'tH1200':tH1200list,'TpTp':TpTplist, 
#  'Zp':Zplist, 'bW800':bW800list,'bW1200':bW1200list,
# 'ZpM500W5':M500W5list,
# 'ZpM500W50':M500W50list,
# 'ZpM1000W10':M1000W10list,
# 'ZpM1500W15':M1500W15list,
# 'ZpM1500W150':M1500W150list,
# 'ZpM2000W20':M2000W20list,
# 'ZpM2000W200':M2000W200list,
# 'ZpM2500W25':M2500W25list,
# 'ZpM3000W30':M3000W30list,
# 'ZpM3000W300':M3000W300list,
# 'RSG1250':RSG1250list,
# 'RSG3000':RSG3000list,
# 'RSG4000':RSG4000list,
# 'Z1250':Z1250list,
# 'Z1500':Z1500list,
# 'Z2500':Z2500list,
# 'Z3000':Z3000list,
# 'Z4000':Z4000list,

#M500W5list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M500W5/22F33CD7-90FF-E411-B76A-00259073E466.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M500W5/A035156E-48FF-E411-BD37-842B2B7682C7.root',
# ]
# M500W50list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M500W50/9ABC1087-F0FD-E411-A6CF-0CC47A13CECE.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M500W50/402581E2-FCFD-E411-B3B7-00266CFF0234.root',
# ]
# M1000W10list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M1000W10/7838F292-E5FD-E411-B966-0002C92A1024.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M1000W10/FCC56CDE-E5FD-E411-A847-002481E7451E.root',
# ]
# M1500W15list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M1500W15/C0C6D157-25FD-E411-8EF5-00259073E488.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M1500W15/CEF7DD24-E4FD-E411-9350-0030483354DE.root',
# ]
# M1500W150list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M1500W150/08E8AB2C-07FE-E411-9A7C-842B2B7680DF.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M1500W150/BC0A7127-07FE-E411-9E2D-6CC21739C400.root',
# ]
# M2000W20list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M2000W20/7AC40821-E9FE-E411-A3D7-F45214C748D2.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M2000W20/7690725B-F5FE-E411-959A-00259074AE9A.root',
# ]
# M2000W200list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M2000W200/0E5497A5-4FFD-E411-85AD-002590D9D9BC.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M2000W200/DE2C0D8F-00FE-E411-9DEF-0025901AEBD6.root',
# ]
# M2500W25list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M2500W25/00700F93-8BFD-E411-B839-0025904A91F6.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M2500W25/CE8FB8E2-90FD-E411-9DF2-003048F5B2A0.root',
# ]
# M3000W30list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M3000W30/08412BCF-BDFE-E411-9AE2-001E67397E90.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M3000W30/FC16ED87-F1FE-E411-A890-00259073E4B8.root',
# ]
# M3000W300list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/M3000W300/4EFF6C38-A6FD-E411-8194-0025905A6110.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/M3000W300/449999B8-A5FD-E411-AEA3-0025905B85B2.root',
# ]

# RSG1250list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/RSG1250/A8A6F5CB-AD00-E511-93F4-008CFA197B54.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/RSG1250/AA4F5EF9-AD00-E511-93A6-008CFA197AC4.root',
# ]

# RSG3000list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/RSG3000/26C3219C-7001-E511-B182-0025905B8572.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/RSG3000/74E60777-7001-E511-BBCB-0025905B8562.root',
# ]

# RSG4000list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/RSG4000/A28A7A95-8501-E511-903F-00259073E456.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/RSG4000/D419142C-2A02-E511-A4F3-14DAE93E5699.root',
# ]

# Z1250list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/Z1250/9ABDB122-FF01-E511-A2EF-549F358EB7E4.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/Z1250/EC8F310A-CE01-E511-B3CD-008CFA1980B8.root',
# ]

# Z1500list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/Z1500/22E9C253-B500-E511-BB9E-00259029E84C.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/Z1500/7833CB7E-7C01-E511-AFF8-002590D9D9DA.root',
# ]

# Z2500list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/Z2500/10976E7D-D901-E511-8282-00304865C2D0.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/Z2500/66390E02-2602-E511-8528-F45214C748CE.root',
# ]

# Z3000list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/Z3000/',
# 'file:/nfs/dust/cms/user/usaiem/run2/Z3000/',
# ]

# Z4000list=[
# 'file:/nfs/dust/cms/user/usaiem/run2/Z4000/880CA4F6-2302-E511-96A5-002590A370FE.root',
# 'file:/nfs/dust/cms/user/usaiem/run2/Z4000/92A1DB97-7F01-E511-B7AD-002590D0AF50.root',
# ]

