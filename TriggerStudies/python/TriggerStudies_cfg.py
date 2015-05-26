# import FWCore.ParameterSet.Config as cms
# import sys

# NAME = sys.argv[2]

# process = cms.Process("TriggerStudies")

# process.load("FWCore.MessageService.MessageLogger_cfi")

# process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )





# from VLQTrigger.TriggerStudies.Samples_cff import *


# process.TFileService=cms.Service("TFileService",
# fileName=cms.string('trgout_'+NAME+'test.root'))
import FWCore.ParameterSet.Config as cms
import sys
NAME = sys.argv[2]
process = cms.Process("TriggerStudies")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
from VLQTrigger.TriggerStudies.Samples_cff import dizionario
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(dizionario[NAME]),
    skipBadFiles= cms.untracked.bool(True)
)
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('MCRUN2_74_V9A::All')

process.load("VLQTrigger.TriggerStudies.TriggerMenu_cff")

process.TFileService=cms.Service("TFileService",
fileName=cms.string('trgout_'+NAME+'run2.root'))

# bTagDiscriminators = [
#     'pfCombinedInclusiveSecondaryVertexV2BJetTags'
# ]
# from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
# addJetCollection(
#     process,
#     labelName = 'ca15CHSJetsFiltered',
#     jetSource = cms.InputTag('ca15CHSJetsFiltered'),
#     pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
#     pfCandidates = cms.InputTag('chs'),
#     svSource = cms.InputTag('slimmedSecondaryVertices'),
#     btagDiscriminators = bTagDiscriminators,
#     jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
#     genJetCollection = cms.InputTag('slimmedGenJetsAK8'),
#     genParticles = cms.InputTag('prunedGenParticles'),
#     algo = 'CA',
#     rParam = 1.5
# )

# process.OUT = cms.OutputModule("PoolOutputModule",
#     fileName = cms.untracked.string('test.root'),
# )

# process.endpath= cms.EndPath(process.OUT)

# process.options = cms.untracked.PSet(
#         allowUnscheduled = cms.untracked.bool(True)
# )

# from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
# addJetCollection(
#     process,
#     labelName = 'AK4PFCHS',
#     jetSource = cms.InputTag('ak4PFJetsCHS'),
#     pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
#     pfCandidates = cms.InputTag('packedPFCandidates'),
#     svSource = cms.InputTag('slimmedSecondaryVertices'),
#     btagDiscriminators = bTagDiscriminators,
#     jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
#     genJetCollection = cms.InputTag('ak4GenJetsNoNu'),
#     genParticles = cms.InputTag('prunedGenParticles'),
#     algo = 'AK',
#     rParam = 0.4
# )

# #process.triggerstudies = cms.EDAnalyzer('TriggerStudies'
# #)

# process.load("VLQTrigger.TriggerStudies.TriggerMenu_cff")



# process.selectedMuons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedMuons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
#        (pfIsolationR04().sumChargedHadronPt+
# 	max(0.,pfIsolationR04().sumNeutralHadronEt+
# 	pfIsolationR04().sumPhotonEt-
# 	0.50*pfIsolationR04().sumPUPt))/pt < 0.20 && 
# 	(isPFMuon && (isGlobalMuon || isTrackerMuon) )'''))
# process.selectedElectrons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedElectrons"), cut = cms.string('''abs(eta)<2.5 && pt>20. &&
# 	gsfTrack.isAvailable() &&
# 	gsfTrack.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\') < 2 &&
# 	(pfIsolationVariables().sumChargedHadronPt+
# 	max(0.,pfIsolationVariables().sumNeutralHadronEt+
# 	pfIsolationVariables().sumPhotonEt-
# 	0.5*pfIsolationVariables().sumPUPt))/pt < 0.15'''))
# ## Do projections
# process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
# process.pfNoMuonCHS =  cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfCHS"), veto = cms.InputTag("selectedMuons"))
# process.pfNoElectronsCHS = cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfNoMuonCHS"), veto = cms.InputTag("selectedElectrons"))

# #Import RECO jet producer for ak4 PF and GEN jet
# from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
# from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
# process.ak4PFJetsCHS = ak4PFJets.clone(src = 'pfNoElectronsCHS', doAreaFastjet = True)
# process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16"))
# process.ak4GenJetsNoNu = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNu')

# # The following is make patJets, but EI is done with the above
# process.load("Configuration.StandardSequences.MagneticField_cff")
# process.load("Configuration.Geometry.GeometryRecoDB_cff")
# process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')

# bTagDiscriminators = [
#     'pfCombinedInclusiveSecondaryVertexV2BJetTags'
# ]

# from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
# addJetCollection(
#     process,
#     labelName = 'AK4PFCHS',
#     jetSource = cms.InputTag('ak4PFJetsCHS'),
#     pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
#     pfCandidates = cms.InputTag('packedPFCandidates'),
#     svSource = cms.InputTag('slimmedSecondaryVertices'),
#     btagDiscriminators = bTagDiscriminators,
#     jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
#     genJetCollection = cms.InputTag('ak4GenJetsNoNu'),
#     genParticles = cms.InputTag('prunedGenParticles'),
#     algo = 'AK',
#     rParam = 0.4
# )

# #adjust PV used for Jet Corrections
# process.patJetCorrFactorsAK4PFCHS.primaryVertices = "offlineSlimmedPrimaryVertices"

# process.options = cms.untracked.PSet(
#         allowUnscheduled = cms.untracked.bool(True)
# )

# process.out = cms.OutputModule("PoolOutputModule",
#                 fileName = cms.untracked.string("file:/nfs/dust/cms/user/usaiem/test2.root")
#         )
# process.outpath=cms.EndPath(process.out)

# import FWCore.ParameterSet.Config as cms

# process = cms.Process("EX")
# # Input source
# process.source = cms.Source("PoolSource",
#                                 fileNames = cms.untracked.vstring(
#         'file:miniAOD-prod_PAT.root'
#     )
# )

# process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#select isolated  muons and electrons collections
#tune the requirements to whatever ID and isolation you prefer 

# process.selectedMuons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedMuons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
#        (pfIsolationR04().sumChargedHadronPt+
# 	max(0.,pfIsolationR04().sumNeutralHadronEt+
# 	pfIsolationR04().sumPhotonEt-
# 	0.50*pfIsolationR04().sumPUPt))/pt < 0.20 && 
# 	(isPFMuon && (isGlobalMuon || isTrackerMuon) )'''))
# process.selectedElectrons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedElectrons"), cut = cms.string('''abs(eta)<2.5 && pt>20. &&
# 	gsfTrack.isAvailable() &&
# 	gsfTrack.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\') < 2 &&
# 	(pfIsolationVariables().sumChargedHadronPt+
# 	max(0.,pfIsolationVariables().sumNeutralHadronEt+
# 	pfIsolationVariables().sumPhotonEt-
# 	0.5*pfIsolationVariables().sumPUPt))/pt < 0.15'''))
# ## Do projections
# process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
# process.pfNoMuonCHS =  cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfCHS"), veto = cms.InputTag("selectedMuons"))
# process.pfNoElectronsCHS = cms.EDProducer("CandPtrProjector", src = cms.InputTag("pfNoMuonCHS"), veto = cms.InputTag("selectedElectrons"))

# #Import RECO jet producer for ak4 PF and GEN jet
# from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
# from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
# process.ak4PFJetsCHS = ak4PFJets.clone(src = 'pfNoElectronsCHS', doAreaFastjet = True)
# process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16"))
# process.ak4GenJetsNoNu = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNu')

# # The following is make patJets, but EI is done with the above
# process.load("Configuration.StandardSequences.MagneticField_cff")
# process.load("Configuration.Geometry.GeometryRecoDB_cff")
# process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9::All')

# bTagDiscriminators = [
#     'pfCombinedInclusiveSecondaryVertexV2BJetTags'
# ]

# from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
# addJetCollection(
#     process,
#     labelName = 'AK4PFCHS',
#     jetSource = cms.InputTag('ak4PFJetsCHS'),
#     pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
#     pfCandidates = cms.InputTag('packedPFCandidates'),
#     svSource = cms.InputTag('slimmedSecondaryVertices'),
#     btagDiscriminators = bTagDiscriminators,
#     jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
#     genJetCollection = cms.InputTag('ak4GenJetsNoNu'),
#     genParticles = cms.InputTag('prunedGenParticles'),
#     algo = 'AK',
#     rParam = 0.4
# )

# #adjust PV used for Jet Corrections
# process.patJetCorrFactorsAK4PFCHS.primaryVertices = "offlineSlimmedPrimaryVertices"

#new PAT default running is "unscheduled" so we just need to say in the outputCommands what we want to store


# process.OUT = cms.OutputModule("PoolOutputModule",
#     fileName = cms.untracked.string('test.root'),
#     outputCommands = cms.untracked.vstring(['drop *','keep patJets_patJetsAK4PFCHS_*_*','keep *_*_*_PAT'])
# )
# 
# process.endpath= cms.EndPath(process.OUT)
