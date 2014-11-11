from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors
from os import system
from sys import argv
from os import mkdir
from os.path import exists
gStyle.SetNumberContours(255)
gStyle.SetPalette(55)
gROOT.SetBatch()
postfix=''
#foldername=''
if len(argv[1:])>0:
  postfix=argv[1]
  #foldername=argv[2]
#f=TFile(postfix,'READ')
filename_list=['trgout_bW1200'+postfix+'.root' , 'trgout_bW800'+postfix+'.root' , 'trgout_tH1200'+postfix+'.root' , 'trgout_tH800'+postfix+'.root']
# filename_list=['trgout_bW1200.root' , 'trgout_bW800.root' , 'trgout_tH1200.root' , 'trgout_tH800.root']
kinematic_names=["nBtag","nJet","HT","jetMass","jetPt","jetMass2","jetPt2","eta","nJet4","maxCSV","maxCSV2"]
efficiency_names=["HT","jetMass","jetPt","jetMass2","jetPt2","HTTH","jetMassTH","jetPtTH","jetMass2TH","jetPt2TH","maxCSV","maxCSVTH","maxCSV2","maxCSV2TH"]
efficiency_titles=["HT (GeV)","Leading jet mass (GeV)","Leading jet pT (GeV)","Subleading jet mass (GeV)","Subleading jet pt (GeV)","HT (GeV)","Leading jet mass (GeV)","Leading jet pT (GeV)","Subleading jet mass (GeV)","Subleading jet pT (GeV)","maximum CSV","maximum CSV","maximum CSV2","maximum CSV2"]
trigger_paths=["HLT_PFHT900_v1",
"HLT_AK8PFJet360TrimMod_Mass30_v1",
"HLT_AK8PFHT850_TrimR0p1PT0p03Mass50_v1",
"HLT_AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3_v1",
"HLT_AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p5_v1",
"HLT_AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p3_v1",
"HLT_AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p5_v1",
"HLT_AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3_DoubleJetC100_v1",
#"HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1",
#"HLT_Mu40_eta2p1_PFJet200_PFJet50_v1",
"HLT_PFHT750_4Jet_v1"]
trigger_names=[]
for trigger in trigger_paths:
  trigger_names.append(trigger[4:-3])

outfile=TFile("triggeranalysis"+postfix+".root","RECREATE")
outfile.cd()

folder='pdf'+postfix+'/'
if not exists(folder):
  mkdir(folder)

def compare(name,file_list,name_list,legend_list,normalize=False, useOutfile=False):
  c=TCanvas(name,'',600,600)
  c.SetLeftMargin(0.15)#
  c.SetRightMargin(0.05)#
  c.SetTopMargin(0.05)#
  c.SetBottomMargin(0.10)
  if not useOutfile:
    legend=TLegend(0.7,0.7,0.95,0.95)
  else:
    c.SetTopMargin(0.15)
    legend=TLegend(0.0,0.85,0.99,0.99)
  #legend=TLegend(0.35,0.2,0.85,0.5)
  legend.SetHeader('')
  #legend.SetTextSize(0.03)
  legend.SetBorderSize(0)
  legend.SetTextFont(42)
  legend.SetLineColor(1)
  legend.SetLineStyle(1)
  legend.SetLineWidth(1)
  legend.SetFillColor(0)
  legend.SetFillStyle(0)
  histo_list=[]
  tfile_list=[]
  maxy=0.0
  for i in range(len(name_list)):
    if not useOutfile:
      tfile_list.append(TFile(file_list[i],'READ'))
      histo_list.append(tfile_list[-1].Get(name_list[i]))
    else:
      histo_list.append(outfile.Get(file_list+name_list[i]))
    if normalize:
      histo_list[-1].Scale(1.0/(histo_list[-1].Integral()+0.00000001))
    if not useOutfile:
      histo_list[-1].SetStats(0)
    histo_list[-1].SetLineWidth(3)
    histo_list[-1].SetLineColor(i+1)
    histo_list[-1].SetTitle('')
    if not useOutfile:
      legend.AddEntry(histo_list[-1],legend_list[i],'l')
    else:
      legend.AddEntry(histo_list[-1],name_list[i],'l')
    maxy=max(maxy,histo_list[-1].GetMaximum()*1.05)
  for i in range(len(name_list)):
    if i==0:
      if not useOutfile:
        histo_list[i].SetMaximum(maxy)
      else:
        histo_list[i].SetMaximum(1.05)
        histo_list[i].SetMinimum(0.0)
      histo_list[i].Draw()
      if useOutfile:
        histo_list[i].GetXaxis().SetTitle(efficiency_titles[efficiency_names.index(file_list.split('_')[2])])
        histo_list[i].GetYaxis().SetTitle('Efficiency')
    else:
      histo_list[i].Draw('SAME')
  legend.Draw()
  outfile.cd()
  c.Write(name)
  c.SaveAs(folder+name+'.pdf')
  #c.SaveAs(folder+name+'.png')

def doeff(filename, histoname, triggername):
  tmp_file=TFile(filename,'READ')
  numerator=tmp_file.Get(triggername+'/'+histoname+'Passing')
  denominator=tmp_file.Get(triggername+'/'+histoname+'Denom')
  n_num=numerator.Integral()
  n_den=denominator.Integral()
  error_bars=TGraphAsymmErrors()
  error_bars.Divide(numerator,denominator,"cl=0.683 b(1,1) mode")
  outfile.cd()
  error_bars.Write(filename.split('.')[0]+'_'+histoname+'_'+triggername)
  return n_num/n_den
  
for i in kinematic_names:
  compare(i,filename_list,['PFHT900/'+i,'PFHT900/'+i,'PFHT900/'+i,'PFHT900/'+i],['bW 1.2 TeV','bW 800 GeV','tH 1.2 TeV','tH 800 GeV'],True)
  for j in ['bW','tH']:
    compare(j+'_'+i,['trgout_'+j+'1200'+postfix+'.root' , 'trgout_'+j+'800'+postfix+'.root'],['PFHT900/'+i,'PFHT900/'+i],[j+' 1.2 TeV',j+' 800 GeV'],True)

efficiencies=[]
for filename in range(len(filename_list)):
  efficiencies.append([])
  for histoname in range(len(efficiency_names)):
    for triggername in range(len(trigger_names)):
      print filename_list[filename],efficiency_names[histoname],trigger_names[triggername]
      eff_tmp=doeff(filename_list[filename],efficiency_names[histoname],trigger_names[triggername])
      if ('bW' in filename_list[filename]) and (efficiency_names[histoname]=='jetPt'):
        efficiencies[-1].append(eff_tmp)
      if ('tH' in filename_list[filename]) and (efficiency_names[histoname]=='jetPtTH'):
        efficiencies[-1].append(eff_tmp)

for filename in filename_list:
  for histoname in efficiency_names:
    for triggername in trigger_names: 
      compare("eff_"+filename.split('.')[0]+'_'+histoname+'_'+triggername,filename.split('.')[0]+"_"+histoname+"_",[triggername],[],False, True)

for filename in filename_list:
  for histoname in ['jetPt','jetPtTH']: 
      compare("comp1_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3','AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p3'],[],False, True)
      compare("comp2_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p5','AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p5'],[],False, True)
      compare("comp3_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p3','AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p5'],[],False, True)
      compare("comp4_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3','AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p5'],[],False, True)


# for filename in filename_list:
#   for histoname in efficiency_names:
#     for triggername in trigger_names: 
#       compare("compare_"+filename.split('.')[0]+'_'+histoname+'_'+triggername,filename.split('.')[0]+"_"+histoname+"_",["AK8PFJet360TrimMod_Mass30","AK8PFHT850_TrimR0p1PT0p03Mass50",triggername],[],False, True)


# for filename in filename_list:
#   for histoname in efficiency_names:
#     for triggername in ['_Mass30_BTagCSVLoose0p3','_Mass30_BTagCSVLoose0p5','_Mass30_BTagCSVMed0p7','_Mass30','_DiMass30']: 
#       compare("special_"+filename.split('.')[0]+'_'+histoname+'_'+triggername,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet280_250TrimMod'+triggername,'AK8DiPFJet300_250TrimMod'+triggername,'AK8DiPFJet300_200TrimMod'+triggername],[],False, True)      

# for filename in filename_list:
#   for histoname in efficiency_names:
#     compare("special2_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",
#       ['AK8DiPFJet300_200TrimMod_Mass30','AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3','AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p5'],[],False, True)
#     compare("special3_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",
#       ['AK8DiPFJet300_200TrimMod_Mass30','AK8DiPFJet300_200TrimMod_DiMass30','AK8PFJet300TrimMod_Mass30_AK4PFJet200'],[],False, True)
#     compare("special4_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",
#       ['AK8DiPFJet300_200TrimMod_Mass30','AK8PFHT850_TrimR0p1PT0p03Mass50'],[],False, True)


print filename_list
print trigger_names
print efficiencies
aa=zip(*efficiencies)
for i in range(len(aa)):
  print aa[i]
    #for kinematic_name in kinematic_names:
  #for sample in ['trgout_bW1200.root' , 'trgout_bW800.root']:
    
  #for sample in ['trgout_tH1200.root' , 'trgout_tH800.root']:
    
