# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/GEN-SIM-RAW --fileout file:B2G-Phys14DR-00039_step1.root --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM --mc --eventcontent RAWSIM --inputEventContent REGEN --pileup AVE_20_BX_25ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions PHYS14_25_V2 --step DIGI,L1,DIGI2RAW,HLT --magField 38T_PostLS1 --python_filename B2G-Phys14DR-00039_prova.py --processName=HLT2 --no_exec -n 3
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(3)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/00236237-FB66-E411-9F51-485B39800BF2.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/026EDAA9-E166-E411-8FDC-002590D0B00C.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/02DF97F6-F766-E411-A680-E0CB4E29C4D8.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0421B8A8-E166-E411-B4CB-002590D0AFC8.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/042F974A-EE66-E411-821E-20CF3027A5DC.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/043751A9-E166-E411-87D2-0025905280BE.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0A1688B0-E166-E411-A274-00259074AE7A.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0A3BA414-F166-E411-8E37-20CF30724B0A.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0AC0F0A2-0967-E411-A299-0025907B4ECA.root', 
        '/store/mc/Phys14DR/TprimeTprime_M_1000_Tune4C_13TeV-madgraph/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/0ACC4F06-E166-E411-8EBD-E0CB4EA0A8FA.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*', 
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:3'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:B2G-Phys14DR-00039_step1.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(20.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/001CB469-A91E-E311-9BFE-0025907FD24A.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/009CB248-A81C-E311-ACD8-00259073E4F0.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/009F81D5-B21C-E311-966C-BCAEC50971D0.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/00B5BB8C-A91E-E311-816A-782BCB1F5E6B.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/00B8F676-BA1C-E311-BA87-0019B9CABFB6.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/00DD7446-B51D-E311-B714-001E6739CEB1.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/021E1B53-101D-E311-886F-00145EDD7569.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/022A782D-A51C-E311-9856-80000048FE80.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/026FE678-BA1C-E311-BEF5-00D0680BF90A.root', '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/10000/02A10BDE-B21C-E311-AB59-00266CF327C0.root'])
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PHYS14_25_V2', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

