from ROOT import TFile,TCanvas,gROOT,gStyle
from os import system
from sys import argv
from os import mkdir
from os.path import exists
gStyle.SetNumberContours(255)
gStyle.SetPalette(55)
postfix=''
foldername=''
if len(argv[1:])>0:
  postfix=argv[1]
  foldername=argv[2]
f=TFile(postfix,'READ')
if not exists('/nfs/dust/cms/user/usaiem/trigger/CMSSW_7_2_0_pre7/src/pdf/'+foldername+'/'):
  mkdir('/nfs/dust/cms/user/usaiem/trigger/CMSSW_7_2_0_pre7/src/pdf/'+foldername+'/')
if not exists('/nfs/dust/cms/user/usaiem/trigger/CMSSW_7_2_0_pre7/src/pdf/'+foldername+'/'+postfix.split('.')[0]+'/'):
  mkdir('/nfs/dust/cms/user/usaiem/trigger/CMSSW_7_2_0_pre7/src/pdf/'+foldername+'/'+postfix.split('.')[0]+'/')
gROOT.SetBatch()
folder=f.Get(foldername)
histohash=folder.GetListOfKeys()
histokeyiter=histohash.MakeIterator()
key=histokeyiter()
while key:
  obj=key.ReadObj()

  outname= '/nfs/dust/cms/user/usaiem/trigger/CMSSW_7_2_0_pre7/src/pdf/'+foldername+'/'+postfix.split('.')[0]+'/'+obj.GetName()+'.pdf'
  if obj.ClassName()=='TCanvas':
    obj.SaveAs(outname)
    #obj.SaveAs('/afs/desy.de/user/u/usaiem/code/ZprimeFullHadAnalysis/pdf/'+obj.GetName()+'.C')
  else:
    if 'Efficiency' not in obj.GetName():
      key=histokeyiter()
      continue
    c=TCanvas(obj.GetName())
    obj.SetStats(0)
    obj.SetLineWidth(3)
    obj.Draw()
    c.SaveAs(outname)
  #system('convert -density 300 -trim '+outname+' '+outname[:-4]+'.png')
  #system('mogrify -bordercolor White -border 20 '+outname[:-4]+'.png')
  key=histokeyiter()
f.Close()