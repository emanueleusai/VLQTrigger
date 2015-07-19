import FWCore.ParameterSet.Config as cms


minHT_par = "0"
minMass_par = "20"
minPt_par = "100"
minCSV_par = "0.814"

minMass_par = "100"#tH
minMass8_par = "60"#bW
minPt8_par = "200"#tH bW


triggermenu=[

'HLT_PFHT800_v1',
'HLT_AK8PFJet360_TrimMass30_v2',
'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v2',
'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_v2',
'HLT_PFHT450_SixJet40_PFBTagCSV0p72_v2',
'HLT_PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72_v2',
#to be tuned
'HLT_AK8PFJet260_TrimMass30_v2',
'HLT_AK8PFHT500_TrimR0p1PT0p03Mass50_v2',
'HLT_AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45_v2',
'HLT_AK8DiPFJet200_200_TrimMass30_BTagCSV0p45_v2',

]

triggertune=
[

[-1],
[-1],
[-1],
[-1],
[-1],
[-1],
#to be tuned
[280,290,300,310,320,330,340,350,360],
[600,620,640,650,660,670,680,690,700],
[600,620,640,650,660,670,680,690,700],
[200,210,220,230,240,250,260,270,280],

]

for i in range(len(triggermenu):
  for j in triggertune[i]:
    triggerpath=triggermenu[i]
    if j>0:
      triggerpath=triggerpath+str(j)
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
    minCSV = cms.double(j),
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
    minCSV = cms.double(j),
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
    minCSV = cms.double(j),
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

