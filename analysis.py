from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors,kOrange,kViolet,kBlue,TLatex,TColor,TLegendEntry,TPad,TGaxis,kGreen,Double
from os import system
from sys import argv
from os import mkdir
from os.path import exists
from array import array
gStyle.SetNumberContours(255)
gStyle.SetPalette(55)
gROOT.SetBatch()
postfix=''
#foldername=''
if len(argv[1:])>0:
  postfix=argv[1]
  #foldername=argv[2]
#f=TFile(postfix,'READ')
filename_list=[
# 'trgout_ZpM500W5'+postfix+'.root',
# 'trgout_ZpM500W50'+postfix+'.root',
# 'trgout_ZpM1000W10'+postfix+'.root',
# 'trgout_ZpM1500W15'+postfix+'.root',
# 'trgout_ZpM1500W150'+postfix+'.root',
# 'trgout_ZpM2000W20'+postfix+'.root',
# 'trgout_ZpM2000W200'+postfix+'.root',
# 'trgout_ZpM2500W25'+postfix+'.root',
# 'trgout_ZpM3000W30'+postfix+'.root',
# 'trgout_ZpM3000W300'+postfix+'.root',
# 'trgout_RSG1250'+postfix+'.root',
# 'trgout_RSG3000'+postfix+'.root',
# 'trgout_RSG4000'+postfix+'.root',
# 'trgout_Z1250'+postfix+'.root',
# 'trgout_Z1500'+postfix+'.root',
# 'trgout_Z2500'+postfix+'.root',
# 'trgout_Z4000'+postfix+'.root',

#'trgout_Zp'+postfix+'.root',
#'trgout_Zp15'+postfix+'.root',
'trgout_bW'+postfix+'.root',
'trgout_tW'+postfix+'.root',
]
touse='_ak8trim'
#filename_list=['trgout_Zp'+postfix+'.root']#['trgout_bW1200'+postfix+'.root' , 'trgout_bW800'+postfix+'.root' ]
#filename_list=['trgout_Zp'+postfix+'.root','trgout_bW1200'+postfix+'.root' , 'trgout_bW800'+postfix+'.root' , 'trgout_tH1200'+postfix+'.root' , 'trgout_tH800'+postfix+'.root', 'trgout_TpTp'+postfix+'.root']
# filename_list=['trgout_bW1200.root' , 'trgout_bW800.root' , 'trgout_tH1200.root' , 'trgout_tH800.root']
kinematic_names=["nBtag","nJet","HT","jetMass","jetPt","jetMass2","jetPt2","eta","nJet4","maxCSV","maxCSV2"]
efficiency_names=['nevts','nevtsTH',"HT","jetMass","jetPt","jetMass2","jetPt2","HTTH","jetMassTH","jetPtTH","jetMass2TH","jetPt2TH"]#,"maxCSV","maxCSVTH","maxCSV2","maxCSV2TH"]
efficiency_titles=['Number of events','Number of events',"HT (GeV)","Leading jet mass (GeV)","Leading jet pT (GeV)","Subleading jet mass (GeV)","Subleading jet pt (GeV)","HT (GeV)","Leading jet mass (GeV)","Leading jet pT (GeV)","Subleading jet mass (GeV)","Subleading jet pT (GeV)"]#,"maximum CSV","maximum CSV","maximum CSV2","maximum CSV2"]

trigger_names=['PFHT800', 'PFHT800_ak8trim', 'PFHT800_ak15trim', 'AK8PFJet360_TrimMass30', 'AK8PFJet360_TrimMass30_ak8trim', 'AK8PFJet360_TrimMass30_ak15trim', 'AK8PFHT700_TrimR0p1PT0p03Mass50', 'AK8PFHT700_TrimR0p1PT0p03Mass50_ak8trim', 'AK8PFHT700_TrimR0p1PT0p03Mass50_ak15trim', 'AK8DiPFJet280_200_TrimMass30_BTagCSV0p45', 'AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_ak8trim', 'AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_ak15trim', 'PFHT450_SixJet40_PFBTagCSV0p72', 'PFHT450_SixJet40_PFBTagCSV0p72_ak8trim', 'PFHT450_SixJet40_PFBTagCSV0p72_ak15trim', 'PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72', 'PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72_ak8trim', 'PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72_ak15trim', 'AK8PFJet260_TrimMass30280', 'AK8PFJet260_TrimMass30280_ak8trim', 'AK8PFJet260_TrimMass30280_ak15trim', 'AK8PFJet260_TrimMass30290', 'AK8PFJet260_TrimMass30290_ak8trim', 'AK8PFJet260_TrimMass30290_ak15trim', 'AK8PFJet260_TrimMass30300', 'AK8PFJet260_TrimMass30300_ak8trim', 'AK8PFJet260_TrimMass30300_ak15trim', 'AK8PFJet260_TrimMass30310', 'AK8PFJet260_TrimMass30310_ak8trim', 'AK8PFJet260_TrimMass30310_ak15trim', 'AK8PFJet260_TrimMass30320', 'AK8PFJet260_TrimMass30320_ak8trim', 'AK8PFJet260_TrimMass30320_ak15trim', 'AK8PFJet260_TrimMass30330', 'AK8PFJet260_TrimMass30330_ak8trim', 'AK8PFJet260_TrimMass30330_ak15trim', 'AK8PFJet260_TrimMass30340', 'AK8PFJet260_TrimMass30340_ak8trim', 'AK8PFJet260_TrimMass30340_ak15trim', 'AK8PFJet260_TrimMass30350', 'AK8PFJet260_TrimMass30350_ak8trim', 'AK8PFJet260_TrimMass30350_ak15trim', 'AK8PFJet260_TrimMass30360', 'AK8PFJet260_TrimMass30360_ak8trim', 'AK8PFJet260_TrimMass30360_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50600', 'AK8PFHT500_TrimR0p1PT0p03Mass50600_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50600_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50620', 'AK8PFHT500_TrimR0p1PT0p03Mass50620_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50620_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50640', 'AK8PFHT500_TrimR0p1PT0p03Mass50640_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50640_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50650', 'AK8PFHT500_TrimR0p1PT0p03Mass50650_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50650_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50660', 'AK8PFHT500_TrimR0p1PT0p03Mass50660_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50660_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50670', 'AK8PFHT500_TrimR0p1PT0p03Mass50670_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50670_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50680', 'AK8PFHT500_TrimR0p1PT0p03Mass50680_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50680_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50690', 'AK8PFHT500_TrimR0p1PT0p03Mass50690_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50690_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50700', 'AK8PFHT500_TrimR0p1PT0p03Mass50700_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50700_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45600', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45600_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45600_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45620', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45620_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45620_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45640', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45640_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45640_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45650', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45650_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45650_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45660', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45660_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45660_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45670', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45670_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45670_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45680', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45680_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45680_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45690', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45690_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45690_ak15trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45700', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45700_ak8trim', 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45700_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45200', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45200_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45200_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45210', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45210_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45210_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45220', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45220_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45220_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45230', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45230_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45230_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45240', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45240_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45240_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45250', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45250_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45250_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45260', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45260_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45260_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45270', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45270_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45270_ak15trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45280', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45280_ak8trim', 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45280_ak15trim']

# trigger_paths=[
# 'HLT_AK8PFJet360_TrimMass30_v1',
# 'HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v1',
# 'HLT_PFHT750_4Jet_v1',
# 'HLT_PFHT900_v1',
# 'HLT_QuadJet45_TripleCSV0p5_v1',
# 'HLT_DoubleJet90_Double30_TripleCSV0p5_v1',
# 'HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_v1',
# 'HLT_PFHT450_SixJet40_PFBTagCSV_v1'
# ]
# trigger_names=[]
# for trigger in trigger_paths:
#   trigger_names.append(trigger[4:-3])
#   trigger_names.append(trigger[4:-3]+'_ak8trim')
#   trigger_names.append(trigger[4:-3]+'_ak15trim')

outfile=TFile("triggeranalysis"+postfix+".root","RECREATE")
outfile.cd()

folder='pdf'+postfix+'/'
if not exists(folder):
  mkdir(folder)

colors=[kOrange+7,kGreen+2,kViolet-5,1,2,3,4,kOrange+1,kViolet-6,8,9,5,6,7,11,12,13,14,15,16,17,18,19]
markertypes=[22,21,20,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def compare(name,file_list,name_list,legend_list,normalize=False, useOutfile=False,overlayKin=False,filename='',drawoption='',xmin=0,ymax=0,xmax=0):
  c=TCanvas('','',0,45,800,600)
  c.SetHighLightColor(2)
  c.Range(0,0,1,1)
  c.SetFillColor(0)
  c.SetBorderMode(0)
  c.SetBorderSize(2)
  c.SetTickx(1)
  c.SetTicky(1)
  c.SetFrameBorderMode(0);
  # c.SetLeftMargin(0.15)#
  # c.SetRightMargin(0.05)#
  # c.SetTopMargin(0.05)#
  # c.SetBottomMargin(0.10)
  gStyle.SetOptStat(0)
  pad0 = TPad("pad0", "",0,0,1,1)
  pad0.Draw()
  pad0.cd()
  pad0.Range(112.5,-4.2801,987.5,3.305596)
  if 'HT' in name:
    pad0.Range(200,-3.595907,2200,2.960984)
  pad0.SetFillColor(0)
  pad0.SetFillStyle(4000)
  pad0.SetBorderMode(0)
  pad0.SetBorderSize(2)
  pad0.SetLogy()
  pad0.SetTickx(1)
  pad0.SetFrameBorderMode(0)
  pad0.SetFrameBorderMode(0)
  
  if overlayKin and not 'nevts' in name:
      ttfile=TFile(filename,'READ')
      overlay=ttfile.Get('PFHT800'+touse+'/'+name.split('_')[-1].split('TH')[0]+"Denom")
      if 'Pt2' in name:
        overlay=ttfile.Get('PFHT800'+touse+'/'+name.split('_')[-1].split('TH')[0]+"Denom").Rebin(11,'aaa',array('d',[200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 900]))
      if 'HT' in name:
        overlay=ttfile.Get('PFHT800'+touse+'/'+name.split('_')[-1].split('TH')[0]+"Denom").Rebin(17,'aaa',array('d',[400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1400, 1600, 2000]))

      #overlay.Scale(2.0/(overlay.Integral()+0.00000001))
      
      #Int_t ci;      // for color index setting
      #TColor *color; // for color definition with alpha
      
      
      
      ci = TColor.GetColor("#000099")
      overlay.SetTitle("")
      overlay.SetLineColor(ci)
      overlay.SetLineWidth(2)
      overlay.SetLineStyle(2)
      overlay.GetXaxis().SetTitle("p_{T}(2nd AK8 jet) [GeV]")
      if 'HT' in name:
        overlay.GetXaxis().SetTitle("H_{T} (AK8 jets) [GeV]")
      overlay.GetXaxis().SetLabelFont(42)
      overlay.GetXaxis().SetLabelSize(0.035)
      overlay.GetXaxis().SetTitleSize(0.035)
      overlay.GetXaxis().SetTitleFont(42)
      overlay.GetXaxis().SetTitleOffset(1.2)
      if 'Pt2' in name:
      	overlay.GetXaxis().SetRangeUser(200,900)
      else:
      	overlay.GetXaxis().SetRangeUser(400,2000)
      overlay.GetYaxis().SetTitle("A.U.")
      overlay.GetYaxis().SetLabelFont(42)
      overlay.GetYaxis().SetLabelSize(0.035)
      overlay.GetYaxis().SetTitleSize(0.035)
      overlay.GetYaxis().SetTitleFont(42)
      overlay.GetZaxis().SetLabelFont(42)
      overlay.GetZaxis().SetLabelSize(0.035)
      overlay.GetZaxis().SetTitleSize(0.035)
      overlay.GetZaxis().SetTitleFont(42)
      overlay.SetMinimum(2)
      if 'HT' in name:
        overlay.SetMaximum(overlay.GetMaximum()*100)
      else:
        overlay.SetMaximum(overlay.GetMaximum()*1000)
      
      overlay.Draw("histo")
      pad0.Modified()

  xAxis2=array('d',[200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 900, 1200])
  xAxis1=array('d',[200, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1400, 1600, 2000])

  pad1 = TPad("pad1", "",0,0,1,1)
  pad1.Draw()
  pad1.cd()
  pad1.Range(112.5,-0.275,987.5,1.975)
  if 'HT' in name:
    pad1.Range(200,-0.275,2200,1.975)
  pad1.SetFillColor(0)
  pad1.SetFillStyle(4000)
  pad1.SetBorderMode(0)
  pad1.SetBorderSize(2)
  pad1.SetFrameBorderMode(0)

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
    histo_list[-1].SetLineWidth(2)
    histo_list[-1].SetTitle('')
    histo_list[-1].SetLineColor(colors[i])
    histo_list[-1].SetMarkerColor(colors[i])
    histo_list[-1].SetMarkerStyle(markertypes[i])
    if 'nevts' in name:
    	print name_list[i]
    	xx=Double(0)
    	yy=Double(0)
    	histo_list[-1].GetPoint(0,xx,yy)
    	print xx,yy
    if 'Pt2' in name:
      	histo_list[-1].GetXaxis().SetRangeUser(200,900)
    else:
      	histo_list[-1].GetXaxis().SetRangeUser(400,2000)
    #if i>8:
    #  histo_list[-1].SetLineColor(i+2)
    histo_list[-1].SetTitle('')
    if len(legend_list)>0:
      legend.AddEntry(histo_list[-1],legend_list[i],'l')
    else:
      legend.AddEntry(histo_list[-1],name_list[i],'l')
    maxy=max(maxy,histo_list[-1].GetMaximum()*1.05)
  for i in range(len(name_list)):
    if i==0:
      if not useOutfile:
        histo_list[i].SetMaximum(maxy)
        #if xmin!=0:
        #  histo_list[i].GetXaxis().SetRangeUser(xmin,10000)
        if ymax!=0:
          histo_list[i].SetMaximum(ymax)
      else:
        histo_list[i].SetMaximum(1.05)
        histo_list[i].SetMinimum(0.0)
        #if xmax!=0:
        #  histo_list[i].GetXaxis().SetRangeUser(xmin,xmax)
      histo_list[i].Draw(drawoption)
      pad1.Modified()
      if useOutfile:
        if len(file_list.split('_'))>1:
          histo_list[i].GetXaxis().SetTitle(efficiency_titles[efficiency_names.index(file_list.split('_')[2])])
        else:  
          histo_list[i].GetXaxis().SetTitle('Leading jet pT [GeV]')
        histo_list[i].GetYaxis().SetTitle('Efficiency')
    else:
      drawoption2= drawoption.replace("a", "")
      histo_list[i].Draw('SAME'+drawoption2)
      pad1.Modified()
      #pad0.Draw()
      #pad0.Modified()
      #c.cd()

      #overlay.SetFillStyle(3004)
      #overlay.SetFillColorAlpha(kBlue, 0.35)



      #overlay.Draw('SAMEHIST')
  #legend.Draw()
  #gaxis=0
  if 'HT' in name:
    gaxis = TGaxis(2000,-0.05,2000,1.75,-0.05,1.75,50510,"+L")
  else:
    gaxis = TGaxis(900,-0.05,900,1.75,-0.05,1.75,50510,"+L")
  gaxis.SetLabelOffset(0.005)
  gaxis.SetLabelSize(0.035)
  gaxis.SetTickSize(0.03)
  gaxis.SetGridLength(0)
  gaxis.SetTitleOffset(1.2)
  gaxis.SetTitleSize(0.035)
  gaxis.SetTitleColor(1)
  gaxis.SetTitleFont(42)
  gaxis.SetTitle("Efficiency")
  gaxis.SetLabelFont(42)
  gaxis.Draw()


  leg = TLegend(0.12,0.6,0.52,0.89,'',"brNDC")
  leg.SetBorderSize(0)
  leg.SetTextFont(62)
  leg.SetTextSize(0.025)
  leg.SetLineColor(1)
  leg.SetLineStyle(1)
  leg.SetLineWidth(1)
  leg.SetFillColor(0)
  leg.SetFillStyle(1001)
  entry=0
  if 'tW' in name:
    entry=leg.AddEntry("ptak82nd","pp #rightarrow B(tW)bj, M(B) = 700 GeV","l")
  else:
    entry=leg.AddEntry("ptak82nd","pp #rightarrow T(bW)bj, M(T) = 700 GeV","l")

  ci = TColor.GetColor("#000099")
  entry.SetLineColor(ci)
  entry.SetLineStyle(2)
  entry.SetLineWidth(2)
  entry.SetMarkerColor(1)
  entry.SetMarkerStyle(21)
  entry.SetMarkerSize(1)
  entry.SetTextFont(62)
  entry=leg.AddEntry("HLT_PFHT800","Eff. (AK4 H_{T} > 800 GeV)","lp")
  entry.SetLineColor(colors[0])
  entry.SetLineStyle(1)
  entry.SetLineWidth(2)
  entry.SetMarkerColor(colors[0])
  entry.SetMarkerStyle(22)
  entry.SetMarkerSize(1)
  entry.SetTextFont(62)
  entry=leg.AddEntry("HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45","Eff. (AK8 H_{T} > 600 GeV, trimmed AK8 jet mass > 50 GeV, #geq1 loose b-tag )","lp")
  entry.SetLineColor(colors[1])
  entry.SetLineStyle(1)
  entry.SetLineWidth(2)
  entry.SetMarkerColor(colors[1])
  entry.SetMarkerStyle(21)
  entry.SetMarkerSize(1)
  entry.SetTextFont(62)
  entry=leg.AddEntry("HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV0p45","Eff. (Trimmed AK8 jet mass > 30 GeV, p_{T}^{jet1} > 250 GeV, p_{T}^{jet2} > 200 GeV, #geq1 loose b-tag )","lp")
  entry.SetLineColor(colors[2])
  entry.SetLineStyle(1)
  entry.SetLineWidth(2)
  entry.SetMarkerColor(colors[2])
  entry.SetMarkerStyle(20)
  entry.SetMarkerSize(1)
  entry.SetTextFont(62)
  leg.Draw()

  tex = TLatex(0.9,0.92," 2015, 13 TeV")
  tex.SetNDC()
  tex.SetTextAlign(31)
  tex.SetTextFont(42)
  tex.SetTextSize(0.0342)
  tex.SetLineWidth(2)
  tex.Draw()
  tex2 = TLatex(0.864,0.872,"CMS")
  tex2.SetNDC()
  tex2.SetTextAlign(33)
  tex2.SetTextFont(61)
  tex2.SetTextSize(0.045)
  tex2.SetLineWidth(2)
  tex2.Draw()
  tex3 = TLatex(0.864,0.818,"Simulation")
  tex3.SetNDC()
  tex3.SetTextAlign(33)
  tex3.SetTextFont(52)
  tex3.SetTextSize(0.0342)
  tex3.SetLineWidth(2)
  tex3.Draw()

  outfile.cd()
  c.Write(name)
  if not 'nevts' in name:
    c.SaveAs(folder+name+'.pdf')
    c.SaveAs(folder+name+'.png')
  #c.SaveAs(folder+name+'.C')
  #c.SaveAs(folder+name+'.png')

def doeff(filename, histoname, triggername, rebin=1):
  tmp_file=TFile(filename,'READ')
  numerator=tmp_file.Get(triggername+'/'+histoname+'Passing')
  denominator=tmp_file.Get(triggername+'/'+histoname+'Denom')
  #if 'Pt' in histoname:
  #  numerator=numerator.Rebin(21,triggername+'_'+histoname+'Passing',array('d',[0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 600, 700, 800]))
  #  denominator=denominator.Rebin(21,triggername+'_'+histoname+'Denom',array('d',[0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 600, 700, 800]))
  if 'HT' in histoname:
    numerator=numerator.Rebin(17,triggername+'_'+histoname+'Passing',array('d',[400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1400, 1600, 2000]))
    denominator=denominator.Rebin(17,triggername+'_'+histoname+'Denom',array('d',[400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1400, 1600, 2000]))
  if 'Pt2' in histoname:
    numerator=numerator.Rebin(11,triggername+'_'+histoname+'Passing',array('d',[200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 900]))
    denominator=denominator.Rebin(11,triggername+'_'+histoname+'Denom',array('d',[200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 900]))

  n_num=numerator.Integral()
  n_den=denominator.Integral()
  numerator.Rebin(rebin)
  denominator.Rebin(rebin)
  error_bars=TGraphAsymmErrors()
  error_bars.Divide(numerator,denominator,"cl=0.683 b(1,1) mode")
  outfile.cd()
  error_bars.Write(filename.split('.')[0]+'_'+histoname+'_'+triggername)
  return n_num/(n_den+0.00001)
  
# for i in kinematic_names:
#   compare(i,filename_list,['PFHT900/'+i]*6,["Z' 1 TeV","T'#rightarrow bW 1.2 TeV" , "T'#rightarrow bW 0.8 TeV" , "T'#rightarrow tH 1.2 TeV" , "T'#rightarrow tH 0.8 TeV", "T'T' 1 TeV"],True)



  # compare(i,filename_list,['PFHT900/'+i,'PFHT900/'+i,'PFHT900/'+i,'PFHT900/'+i],['bW 1.2 TeV','bW 800 GeV','tH 1.2 TeV','tH 800 GeV'],True)
  # for j in ['bW','tH']:
  #   compare(j+'_'+i,['trgout_'+j+'1200'+postfix+'.root' , 'trgout_'+j+'800'+postfix+'.root'],['PFHT900/'+i,'PFHT900/'+i],[j+' 1.2 TeV',j+' 800 GeV'],True)

efficiencies=[]
for filename in range(len(filename_list)):
  efficiencies.append([])
  for histoname in range(len(efficiency_names)):
    for triggername in range(len(trigger_names)):
      print filename_list[filename],efficiency_names[histoname],trigger_names[triggername]
      rebinna=1
      if 'M500' in filename_list[filename]:
        rebinna=4
      eff_tmp=doeff(filename_list[filename],efficiency_names[histoname],trigger_names[triggername],rebin=rebinna)

      if ('bW' in filename_list[filename]) and (efficiency_names[histoname]=='jetPt'):
        efficiencies[-1].append(eff_tmp)
      if ('Zp' in filename_list[filename]) and (efficiency_names[histoname]=='jetPtTH'):
        efficiencies[-1].append(eff_tmp)

# for filename in filename_list:
#   for histoname in efficiency_names:
#     for triggername in trigger_names: 
#       compare("eff_"+filename.split('.')[0]+'_'+histoname+'_'+triggername,filename.split('.')[0]+"_"+histoname+"_",[triggername],[],False, True)

# for filename in filename_list:
#   #compare("comp2_"+filename.split('.')[0]+'_jetPtTH','',[filename.split('.')[0]+"_jetPtTH_"+'AK8PFJet360TrimMod_Mass30',filename.split('.')[0]+"_jetPtTH_"+'AK8DiPFJet280_200_TrimMass30_BTagCSV0p41',filename.split('.')[0]+"_jetPt_"+'AK8DiPFJet280_200_TrimMass30_BTagCSV0p41'],[],False, True, True,filename)
#   for histoname in ['HTTH','jetPtTH','jetMassTH','HT','jetPt','jetMass','jetPt2','jetPt2TH','jetMass2','jetMass2TH','maxCSV','maxCSVTH','maxCSV2','maxCSV2TH']:#['HTTH','jetPtTH','HT','jetPt','jetMass','jetMassTH','maxCSV','maxCSVTH','maxCSV2','maxCSV2TH']: 
#     if 'M500' in filename:
#       compare("comp1_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['PFHT900','AK8PFJet360_TrimMass30','AK8DiPFJet280_200_TrimMass30_BTagCSV0p41','AK8PFHT700_TrimR0p1PT0p03Mass50','PFHT450_SixJet40_PFBTagCSV'],[],False, True, True,filename)
#       compare("compak8trim_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['PFHT900_ak8trim','AK8PFJet360_TrimMass30_ak8trim','AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_ak8trim','AK8PFHT700_TrimR0p1PT0p03Mass50_ak8trim','PFHT450_SixJet40_PFBTagCSV_ak8trim'],[],False, True, True,filename)
#       compare("compak15trim_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['PFHT900_ak15trim','AK8PFJet360_TrimMass30_ak15trim','AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_ak15trim','AK8PFHT700_TrimR0p1PT0p03Mass50_ak15trim','PFHT450_SixJet40_PFBTagCSV_ak15trim'],[],False, True, True,filename)
#     else:
#       xmassimo=0
#       if 'Pt' in histoname:
#         xmassimo=800
#       if 'HT' in histoname:
#         xmassimo=2000
#       compare("comp1_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['PFHT900','AK8PFJet360_TrimMass30','AK8DiPFJet280_200_TrimMass30_BTagCSV0p41','AK8PFHT700_TrimR0p1PT0p03Mass50'],[],False, True, True,filename,xmax=xmassimo)
#       compare("compak8trim_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['PFHT900_ak8trim','AK8PFJet360_TrimMass30_ak8trim','AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_ak8trim','AK8PFHT700_TrimR0p1PT0p03Mass50_ak8trim'],[],False, True, True,filename,xmax=xmassimo)
#       compare("compak15trim_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['PFHT900_ak15trim','AK8PFJet360_TrimMass30_ak15trim','AK8DiPFJet280_200_TrimMass30_BTagCSV0p41_ak15trim','AK8PFHT700_TrimR0p1PT0p03Mass50_ak15trim'],[],False, True, True,filename,xmax=xmassimo)
#       #compare("comp1_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3','AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p3'],[],False, True)
#       # compare("comp2_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p5','AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p5'],[],False, True)
#       # compare("comp3_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p3','AK8DiPFJet280_200TrimMod_Mass30_BTagCSVLoose0p5'],[],False, True)
#       # compare("comp4_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",['AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p3','AK8DiPFJet300_200TrimMod_Mass30_BTagCSVLoose0p5'],[],False, True)

for filename in filename_list:
  if 'Zp15' in filename:
    touse='_ak15trim'
  elif 'Zp'in filename:
    touse='_ak8trim'
  elif 'bW'in filename:
    touse='_ak8trim'
  elif 'tW'in filename:
    touse='_ak8trim'
  for histoname in ['nevtsTH','HTTH',"jetPt2TH"]:#['nevts','nevtsTH','HT','HTTH','jetPt','jetPtTH',"jetPt2","jetPt2TH"]:
    # xmassimo=1
    # if 'Pt' in histoname:
    #     xmassimo=800
    # if 'HT' in histoname:
    #     xmassimo=2000
    # triglist=['AK8PFJet360_TrimMass30'+touse,
    # 'AK8PFJet260_TrimMass30280'+touse,
    # #'AK8PFJet260_TrimMass30290'+touse,
    # 'AK8PFJet260_TrimMass30300'+touse,
    # #'AK8PFJet260_TrimMass30310'+touse,
    # 'AK8PFJet260_TrimMass30320'+touse,
    # #'AK8PFJet260_TrimMass30330'+touse,
    # 'AK8PFJet260_TrimMass30340'+touse,
    # #'AK8PFJet260_TrimMass30350'+touse,
    # 'PFHT800'+touse
    # ]
    # leglist=['AK8PFJet360_TrimMass30',
    # 'AK8PFJet280_TrimMass30',
    # #'AK8PFJet290_TrimMass30',
    # 'AK8PFJet300_TrimMass30',
    # #'AK8PFJet310_TrimMass30',
    # 'AK8PFJet320_TrimMass30',
    # #'AK8PFJet330_TrimMass30',
    # 'AK8PFJet340_TrimMass30',
    # #'AK8PFJet350_TrimMass30',
    # 'PFHT800'
    # ]
    # compare("compSingleJet_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",triglist,leglist,False, True, True,filename,xmax=xmassimo)


    # triglist=['AK8PFHT700_TrimR0p1PT0p03Mass50'+touse,
    # 'AK8PFHT500_TrimR0p1PT0p03Mass50600'+touse,
    # #'AK8PFHT500_TrimR0p1PT0p03Mass50620'+touse,
    # 'AK8PFHT500_TrimR0p1PT0p03Mass50640'+touse,
    # #'AK8PFHT500_TrimR0p1PT0p03Mass50650'+touse,
    # 'AK8PFHT500_TrimR0p1PT0p03Mass50660'+touse,
    # #'AK8PFHT500_TrimR0p1PT0p03Mass50670'+touse,
    # 'AK8PFHT500_TrimR0p1PT0p03Mass50680'+touse,
    # #'AK8PFHT500_TrimR0p1PT0p03Mass50690'+touse,
    # 'PFHT800'+touse
    # ]
    # leglist=['AK8PFHT700_TrimR0p1PT0p03Mass50',
    # 'AK8PFHT600_TrimR0p1PT0p03Mass50',
    # #'AK8PFHT620_TrimR0p1PT0p03Mass50',
    # 'AK8PFHT640_TrimR0p1PT0p03Mass50',
    # #'AK8PFHT650_TrimR0p1PT0p03Mass50',
    # 'AK8PFHT660_TrimR0p1PT0p03Mass50',
    # #'AK8PFHT670_TrimR0p1PT0p03Mass50',
    # 'AK8PFHT680_TrimR0p1PT0p03Mass50',
    # #'AK8PFHT690_TrimR0p1PT0p03Mass50',
    # 'PFHT800'
    # ]
    # compare("compHTJet_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",triglist,leglist,False, True, True,filename,xmax=xmassimo)


    # triglist=['AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45700'+touse,
    # 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45600'+touse,
    # #'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45620'+touse,
    # 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45640'+touse,
    # #'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45650'+touse,
    # 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45660'+touse,
    # #'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45670'+touse,
    # 'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45680'+touse,
    # #'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45690'+touse,
    # 'PFHT800'+touse
    # ]
    # leglist=['AK8PFHT700_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # 'AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # #'AK8PFHT620_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # 'AK8PFHT640_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # #'AK8PFHT650_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # 'AK8PFHT660_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # #'AK8PFHT670_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # 'AK8PFHT680_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # #'AK8PFHT690_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    # 'PFHT800'
    # ]
    # compare("compHTJetBtag_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",triglist,leglist,False, True, True,filename,xmax=xmassimo)


    # triglist=['AK8DiPFJet280_200_TrimMass30_BTagCSV0p45'+touse,
    # 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45200'+touse,
    # #'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45210'+touse,
    # 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45220'+touse,
    # #'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45230'+touse,
    # 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45240'+touse,
    # #'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45250'+touse,
    # 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45260'+touse,
    # #'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45270'+touse,
    # 'PFHT800'+touse
    # ]
    # leglist=['AK8DiPFJet280_200_TrimMass30_BTagCSV0p45',
    # 'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45',
    # #'AK8DiPFJet210_200_TrimMass30_BTagCSV0p45',
    # 'AK8DiPFJet220_200_TrimMass30_BTagCSV0p45',
    # #'AK8DiPFJet230_200_TrimMass30_BTagCSV0p45',
    # 'AK8DiPFJet240_200_TrimMass30_BTagCSV0p45',
    # #'AK8DiPFJet250_200_TrimMass30_BTagCSV0p45',
    # 'AK8DiPFJet260_200_TrimMass30_BTagCSV0p45',
    # #'AK8DiPFJet270_200_TrimMass30_BTagCSV0p45',
    # 'PFHT800'
    # ]
    # compare("compDijet_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",triglist,leglist,False, True, True,filename,xmax=xmassimo)


    # triglist=[
    # 'PFHT800'+touse,
    # 'AK8PFJet360_TrimMass30'+touse,
    # 'AK8PFHT700_TrimR0p1PT0p03Mass50'+touse,
    # 'AK8DiPFJet280_200_TrimMass30_BTagCSV0p45'+touse,
    # ]
    # leglist=[
    # 'PFHT800',
    # 'AK8PFJet360_TrimMass30',
    # 'AK8PFHT700_TrimR0p1PT0p03Mass50',
    # 'AK8DiPFJet280_200_TrimMass30_BTagCSV0p45',
    # ]
    # compare("compCurrent_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",triglist,leglist,False, True, True,filename,xmax=xmassimo)
    print touse
    #final plots
    triglist=[
    'PFHT800'+touse,
    #'AK8PFJet360_TrimMass30'+touse,
    #'AK8PFHT500_TrimR0p1PT0p03Mass50650'+touse,
    'AK8PFHT500_TrimR0p1PT0p03Mass50_BTagCSV0p45600'+touse,
    'AK8DiPFJet200_200_TrimMass30_BTagCSV0p45250'+touse,
    ]
    leglist=[
    'PFHT800',
    #'AK8PFJet360_TrimMass30',
    #'AK8PFHT650_TrimR0p1PT0p03Mass50',
    'AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45',
    'AK8DiPFJet250_200_TrimMass30_BTagCSV0p45',
    ]
    # xminimo=0
    # if 'HT' in histoname:
    #   xminimo=300
    xmassimo=1
    #if 'Pt' in histoname:
    #    xmassimo=700
    if 'HT' in histoname:
        xmassimo=2000
    if 'Pt2' in histoname:
        xmassimo=1200
    xminimo=1
    #if 'Pt' in histoname:
    #    xminimo=200
    if 'HT' in histoname:
        xminimo=200
    if 'Pt2' in histoname:
        xminimo=200
    compare("compFinal_"+filename.split('.')[0]+'_'+histoname,filename.split('.')[0]+"_"+histoname+"_",triglist,leglist,False, True, True,
      filename,xmax=xmassimo,xmin=xminimo,drawoption='p')

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

# merge=0
# merge_ak8trim=0
# merge_ak15trim=0
# merge_list=[]
# for filename in filename_list:
#   f=TFile(filename)
#   #merge_list.append(f)
#   jm=f.Get('PFHT900/jetMassPt')
#   jm_ak8trim=f.Get('PFHT900_ak8trim/jetMassPt')
#   jm_ak15trim=f.Get('PFHT900_ak15trim/jetMassPt')
#   outfile.cd()
#   if merge==0:
#     merge=jm.Clone("merge")
#   else:
#     merge.Add(jm)
#   if merge_ak8trim==0:
#     merge_ak8trim=jm_ak8trim.Clone("merge_ak8trim")
#   else:
#     merge_ak8trim.Add(jm_ak8trim)
#   if merge_ak15trim==0:
#     merge_ak15trim=jm_ak15trim.Clone("merge_ak15trim")
#   else:
#     merge_ak15trim.Add(jm_ak15trim)
#   #f.Close()
# merge.Write()
# merge_ak8trim.Write()
# merge_ak15trim.Write()

# for histoname in kinematic_names:
#   compare(
#     name='kin'+histoname,
#     file_list=['trgout_ZpM500W5'+postfix+'.root',
# 'trgout_ZpM1000W10'+postfix+'.root',
# 'trgout_ZpM1500W15'+postfix+'.root',
# 'trgout_ZpM2000W20'+postfix+'.root',
# 'trgout_ZpM2500W25'+postfix+'.root',
# 'trgout_ZpM3000W30'+postfix+'.root',],
#     name_list=['PFHT900/'+histoname]*6,
#     legend_list=['ZpM500W5',
# 'ZpM1000W10',
# 'ZpM1500W15',
# 'ZpM2000W20',
# 'ZpM2500W25',
# 'ZpM3000W30',],
#     normalize=True,
#     useOutfile=False,
#     overlayKin=False,
#     filename='',
#     drawoption='HIST',
#     xmin=100,
#     ymax=0.18
#     )

#   compare(
#     name='kin_ak8trim'+histoname,
#     file_list=['trgout_ZpM500W5'+postfix+'.root',
# 'trgout_ZpM1000W10'+postfix+'.root',
# 'trgout_ZpM1500W15'+postfix+'.root',
# 'trgout_ZpM2000W20'+postfix+'.root',
# 'trgout_ZpM2500W25'+postfix+'.root',
# 'trgout_ZpM3000W30'+postfix+'.root',],
#     name_list=['PFHT900_ak8trim/'+histoname]*6,
#     legend_list=['ZpM500W5',
# 'ZpM1000W10',
# 'ZpM1500W15',
# 'ZpM2000W20',
# 'ZpM2500W25',
# 'ZpM3000W30',],
#     normalize=True,
#     useOutfile=False,
#     overlayKin=False,
#     filename='',
#     drawoption='HIST',
#     xmin=100,
#     ymax=0.18
#     )

#   compare(
#     name='kin_ak15trim'+histoname,
#     file_list=['trgout_ZpM500W5'+postfix+'.root',
# 'trgout_ZpM1000W10'+postfix+'.root',
# 'trgout_ZpM1500W15'+postfix+'.root',
# 'trgout_ZpM2000W20'+postfix+'.root',
# 'trgout_ZpM2500W25'+postfix+'.root',
# 'trgout_ZpM3000W30'+postfix+'.root',],
#     name_list=['PFHT900_ak15trim/'+histoname]*6,
#     legend_list=['ZpM500W5',
# 'ZpM1000W10',
# 'ZpM1500W15',
# 'ZpM2000W20',
# 'ZpM2500W25',
# 'ZpM3000W30',],
#     normalize=True,
#     useOutfile=False,
#     overlayKin=False,
#     filename='',
#     drawoption='HIST',
#     xmin=100,
#     ymax=0.18
#     )


print filename_list
print trigger_names
print efficiencies
aa=zip(*efficiencies)
for i in range(len(aa)):
  print aa[i]
    #for kinematic_name in kinematic_names:
  #for sample in ['trgout_bW1200.root' , 'trgout_bW800.root']:
    
  #for sample in ['trgout_tH1200.root' , 'trgout_tH800.root']:
    
