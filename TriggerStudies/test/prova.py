import FWCore.ParameterSet.Config as cms

#set up a process , for e.g. RECO in this case
processName = "trgprova"
process = cms.Process(processName)


process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('PRE_LS172_V16::All')

# this inputs the input files
process.source = cms.Source ("PoolSource",
                        fileNames=cms.untracked.vstring(
                #'file:/nfs/dust/cms/user/marchesi/RECO_files/CMSSW_7_2_0_pre7/tprime_RECO_TpjM1200_bW_13TeV_1.root',
                "file:/nfs/dust/cms/user/usaiem/trigger/CMSSW_7_2_0_pre8/src/MyTrigger/B2G-Spring14dr-00019.root",
        )
                )

# loads your analyzer
process.MyModule = cms.EDAnalyzer('HLTEventAnalyzerAOD'#,
              #  triggerName = cms.string("bla")

                #numBins = cms.untracked.int32(100),
                #minBin  = cms.untracked.double(0),
                #maxBin  = cms.untracked.double(100),
                #rootPlotFile = cms.untracked.string("myfile.root")
        )

# talk to output module
process.out = cms.OutputModule("PoolOutputModule",
                fileName = cms.untracked.string("test2.root")
        )

# Defines which modules and sequences to run
process.mypath = cms.Path(process.MyModule)

# A list of analyzers or output modules to be run after all paths have been run.
process.outpath = cms.EndPath(process.out)
