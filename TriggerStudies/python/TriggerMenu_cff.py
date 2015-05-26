import FWCore.ParameterSet.Config as cms


minHT_par = "0"
minMass_par = "20"
minPt_par = "100"
minCSV_par = "0.814"

minMass_par = "100"#tH
minMass8_par = "60"#bW
minPt8_par = "200"#tH bW


triggermenu=[

'HLT_AK8PFJet360_TrimMass30_v1',
'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1',
'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_v1',
'HLT_PFHT750_4Jet_v1',
'HLT_PFHT900_v1',
'HLT_QuadJet45_TripleCSV0p5_v1',
'HLT_DoubleJet90_Double30_TripleCSV0p5_v1',
'HLT_PFHT450_SixJet40_PFBTagCSV_v1',
# 'HLT_PFHT400_SixJet30_BTagCSV0p5_2PFBTagCSV_v1',
# 'HLT_PFHT450_SixJet40_v1',
# 'HLT_PFHT400_SixJet30_v1',



#'HLT_AK8PFJet360TrimMod_Mass30_v1',
#'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1',
#'HLT_PFHT750_4Jet_v1',
#'HLT_PFHT900_v1',
#'HLT_QuadJet45_TripleCSV0p5_v1',
#'HLT_DoubleJet90_Double30_TripleCSV0p5_v1',
#'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_v1'

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
    pfJets = cms.InputTag( "slimmedJets" ),
    #pfJets = cms.InputTag( "ak4PFJetsCHS" ),
    #pfJets8 = cms.InputTag( "ak8PFJetsTrimmed" ),
    #pfJets8 = cms.InputTag( "ak8PFJetsCHS" ),
    pfJets8 = cms.InputTag( "slimmedJetsAK8" ),
    minHT = cms.double(minHT_par),
    minMass = cms.double(minMass_par),
    minPt = cms.double(minPt_par),
    minCSV = cms.double(minCSV_par),
    minMass8 = cms.double(minMass8_par),
    minPt8 = cms.double(minPt8_par)
    )
  globals()[triggerpath[4:-3]+'_ak8trim']=cms.EDAnalyzer("TriggerStudies",

    triggerPath = cms.string( triggerpath ),
    pfJets = cms.InputTag( "slimmedJets" ),
    #pfJets = cms.InputTag( "ak4PFJetsCHS" ),
    #pfJets8 = cms.InputTag( "ak8PFJetsTrimmed" ),
    #pfJets8 = cms.InputTag( "ak8PFJetsCHS" ),
    pfJets8 = cms.InputTag( "ak8PFJetsTrimmed" ),
    minHT = cms.double(minHT_par),
    minMass = cms.double(minMass_par),
    minPt = cms.double(minPt_par),
    minCSV = cms.double(minCSV_par),
    minMass8 = cms.double(minMass8_par),
    minPt8 = cms.double(minPt8_par)
    )
  globals()[triggerpath[4:-3]+'_ak15trim']=cms.EDAnalyzer("TriggerStudies",

    triggerPath = cms.string( triggerpath ),
    pfJets = cms.InputTag( "slimmedJets" ),
    #pfJets = cms.InputTag( "ak4PFJetsCHS" ),
    #pfJets8 = cms.InputTag( "ak8PFJetsTrimmed" ),
    #pfJets8 = cms.InputTag( "ak8PFJetsCHS" ),
    pfJets8 = cms.InputTag( "ak15PFJetsTrimmed" ),
    minHT = cms.double(minHT_par),
    minMass = cms.double(minMass_par),
    minPt = cms.double(minPt_par),
    minCSV = cms.double(minCSV_par),
    minMass8 = cms.double(minMass8_par),
    minPt8 = cms.double(minPt8_par)
    )


from RecoJets.JetProducers.ak4PFJetsTrimmed_cfi import ak4PFJetsTrimmed
#from RecoJets.JetProducers.ak4PFJetsFiltered_cfi import ak4PFJetsFiltered

chs = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))

ak8PFJetsTrimmed=ak4PFJetsTrimmed.clone(src = cms.InputTag("chs"))
ak8PFJetsTrimmed.rParam = cms.double(0.8)
ak8PFJetsTrimmed.rFilt = cms.double(0.1)
ak8PFJetsTrimmed.trimPtFracMin = cms.double(0.03)


# from RecoJets.JetProducers.ak5PFJetsFiltered_cfi import ak5PFJetsFiltered
# ca15CHSJetsFiltered = ak5PFJetsFiltered.clone(
#         src = 'chs',
#         jetAlgorithm = cms.string("CambridgeAachen"),
#         rParam       = cms.double(1.5),
#         writeCompound = cms.bool(True),
#         doAreaFastjet = cms.bool(True),
#         jetPtMin = cms.double(100.0)
# )

ak15PFJetsTrimmed=ak4PFJetsTrimmed.clone(src = cms.InputTag("chs"))
ak15PFJetsTrimmed.rParam = cms.double(1.5)
ak15PFJetsTrimmed.rFilt = cms.double(0.1)
ak15PFJetsTrimmed.trimPtFracMin = cms.double(0.03)

percorso=chs
percorso+=ak8PFJetsTrimmed
percorso+=ak15PFJetsTrimmed
#percorso+=globals()[triggermenu[0][4:-3]]
for triggerpath in triggermenu:
  percorso+=globals()[triggerpath[4:-3]]
  percorso+=globals()[triggerpath[4:-3]+'_ak8trim']
  percorso+=globals()[triggerpath[4:-3]+'_ak15trim']
p=cms.Path(percorso)

