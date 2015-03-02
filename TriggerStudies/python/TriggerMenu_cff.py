import FWCore.ParameterSet.Config as cms


minHT_par = "0"
minMass_par = "20"
minPt_par = "100"
minCSV_par = "0.814"

minMass_par = "100"#tH
minMass8_par = "60"#bW
minPt8_par = "200"#tH bW


triggermenu=[

'HLT_AK8PFJet360TrimMod_Mass30_v1',
'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1',
'HLT_PFHT750_4Jet_v1',
'HLT_PFHT900_v1',
'HLT_QuadJet45_TripleCSV0p5_v1',
'HLT_DoubleJet90_Double30_TripleCSV0p5_v1',
'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_v1'

 # "HLT_PFHT900_v1",
 # "HLT_AK8PFJet360TrimMod_Mass30_v1"
# "HLT_AK8PFHT850_TrimR0p1PT0p03Mass50_v1",
# "HLT_AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3_v1",
# "HLT_AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p5_v1",
# "HLT_AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p3_v1",
# "HLT_AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p5_v1",
# "HLT_AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3_DoubleJetC100_v1",
# #"HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1",
# #"HLT_Mu40_eta2p1_PFJet200_PFJet50_v1",
# "HLT_PFHT750_4Jet_v1"
]

for triggerpath in triggermenu:
  globals()[triggerpath[4:-3]]=cms.EDAnalyzer("TriggerStudies",
    triggerPath = cms.string( triggerpath ),
    pfJets = cms.InputTag( "ak4PFJetsCHS" ),
    pfJets8 = cms.InputTag( "ak8PFJetsCHS" ),
    minHT = cms.double(minHT_par),
    minMass = cms.double(minMass_par),
    minPt = cms.double(minPt_par),
    minCSV = cms.double(minCSV_par),
    minMass8 = cms.double(minMass8_par),
    minPt8 = cms.double(minPt8_par)
    )

percorso=globals()[triggermenu[0][4:-3]]
for triggerpath in triggermenu[1:]:
  percorso+=globals()[triggerpath[4:-3]]
p=cms.Path(percorso)

