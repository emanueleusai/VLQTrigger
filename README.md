VLQTrigger
==========

This code serves the purpose of assessing the feasibility of VLQ searches in the all hadronic final state during Run2. In particular, the trigger efficiency is studied.

This is a CMSSW package

version >=7_2_0_pre8

TriggerStudies EDMAnalyzer produces efficiency histograms

run with cmsRun python/TriggerStudies_cfg.py dataset_type (see "runna" for example)

analysis.py generates efficiency plots and comparisons

run with python analysis.py filename_postfix

savepdf.py saves all plots of a root file folder in pdf
