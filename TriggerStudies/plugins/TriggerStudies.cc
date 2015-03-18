// -*- C++ -*-
//
// Package:    MyStudies/TriggerStudies
// Class:      TriggerStudies
// 
/**\class TriggerStudies TriggerStudies.cc MyStudies/TriggerStudies/plugins/TriggerStudies.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Emanuele Usai
//         Created:  Fri, 10 Oct 2014 09:59:19 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH2.h"
#include "TH1.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/BTauReco/interface/JetTag.h"
#include <TLorentzVector.h>
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

//
// class declaration
//

class TriggerStudies : public edm::EDAnalyzer {
   public:
      explicit TriggerStudies(const edm::ParameterSet&);
      ~TriggerStudies();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
      static bool compare_JetMass(const TLorentzVector jet1, const TLorentzVector jet2){
	return ( jet1.M() > jet2.M() );}
      static bool compare_JetPt(const TLorentzVector jet1, const TLorentzVector jet2){
	return ( jet1.Pt() > jet2.Pt() );}


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      std::map< std::string, TH2D* > histos2D_;
      std::map< std::string, TH1D* > histos1D_;
      
      edm::InputTag pfJets;
      edm::InputTag pfJets8;
      std::string triggerPath;
      double minHT;
      double minMass;
      double minPt;
      double minCSV;
      double minMass8;
      double minPt8;
      //double nCSV;
      
      HLTConfigProvider hltConfig;
      int triggerBit;
      int triggerBit2;
      int triggerBit3;
      
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
TriggerStudies::TriggerStudies(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
   pfJets	= iConfig.getParameter<edm::InputTag> ( "pfJets" ); // Obtain inputs
   pfJets8	= iConfig.getParameter<edm::InputTag> ( "pfJets8" );
   triggerPath	= iConfig.getParameter<std::string> ( "triggerPath" ); // Obtain inputs
   minHT         = iConfig.getParameter<double> ( "minHT" ); // Obtain inputs
   minMass	= iConfig.getParameter<double> ( "minMass" );
   minPt 	= iConfig.getParameter<double> ( "minPt" );
   minCSV 	= iConfig.getParameter<double> ( "minCSV" );
   minMass8 	= iConfig.getParameter<double> ( "minMass8" );
   minPt8 	= iConfig.getParameter<double> ( "minPt8" );
}


TriggerStudies::~TriggerStudies()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TriggerStudies::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;


// #ifdef THIS_IS_AN_EVENT_EXAMPLE
//    Handle<ExampleData> pIn;
//    iEvent.getByLabel("example",pIn);
// #endif
//    
// #ifdef THIS_IS_AN_EVENTSETUP_EXAMPLEminMass
//    ESHandle<SetupData> pSetup;
//    iSetup.get<SetupRecord>().get(pSetup);
// #endif
   
   bool changedConfig = false;
   if (!hltConfig.init(iEvent.getRun(), iSetup, "HLT2", changedConfig)) {
     cout << "Initialization of HLTConfigProvider failed!!" << endl;
     return;
   }
   if (changedConfig){
     std::cout << "the curent menu is " << hltConfig.tableName() << std::endl;
     triggerBit = -1;
     triggerBit2 = -1;
     triggerBit3 = -1;
     hltConfig.dump("Triggers");
     for (size_t j = 0; j < hltConfig.triggerNames().size(); j++) {
       std::cout << TString(hltConfig.triggerNames()[j]) << std::endl;
       if (TString(hltConfig.triggerNames()[j]).Contains(triggerPath)) triggerBit = j;
       if (TString(hltConfig.triggerNames()[j]).Contains("HLT_AK8PFJet360TrimMod_Mass30_v1")) triggerBit2 = j;
       if (TString(hltConfig.triggerNames()[j]).Contains("HLT_PFHT900_v1")) triggerBit3 = j;
     }
     //std::cout << triggerBit << std::endl;
     if (triggerBit == -1) cout << "HLT path not found" << endl;
     if (triggerBit2 == -1) cout << "HLT path 2 not found" << endl;
     if (triggerBit3 == -1) cout << "HLT path 3 not found" << endl;
   }
   
   edm::InputTag triggerResultsLabel = edm::InputTag("TriggerResults", "", "HLT2");
   edm::Handle<edm::TriggerResults> triggerResults;
   iEvent.getByLabel(triggerResultsLabel, triggerResults);

   edm::Handle<edm::View<reco::PFJet> > pfjets;
   iEvent.getByLabel(pfJets,pfjets);
   std::vector< TLorentzVector > pfJetsCollection;
   
   edm::Handle<edm::View<reco::PFJet> > pfjets8;
   iEvent.getByLabel(pfJets8,pfjets8);
   std::vector< TLorentzVector > pfJets8Collection;
   
   edm::Handle<reco::JetTagCollection> tagHandle;
   iEvent.getByLabel("combinedInclusiveSecondaryVertexV2BJetTags", tagHandle);//IVFCSVv2
   //iEvent.getByLabel("combinedSecondaryVertexBJetTags", tagHandle);//CSV
   const reco::JetTagCollection & tagColl = *(tagHandle.product());
   //std::cout << "Found " << tagColl.size() << " B candidates in collection " << pfjets->size()<<std::endl;
   
   
   // edm::Handle<GenEventInfoProduct> genEventInfoProduct;
   // iEvent.getByLabel("generator", genEventInfoProduct);
   // const GenEventInfoProduct& genEventInfo = *(genEventInfoProduct.product());
   // double theWeight = genEventInfo.weight();
   // cout<<theWeight<<endl;
   
   //count btags
   float maxCSV=0;
   int nbtags=0;
   for (reco::JetTagCollection::const_iterator tagI = tagColl.begin(); tagI != tagColl.end(); ++tagI) {
     if (tagI->second>maxCSV && tagI->first->pt()>20.0 && fabs(tagI->first->eta())<2.5)
     {
       maxCSV=tagI->second;
     }
     if (tagI->second>minCSV && tagI->first->pt()>20.0 && fabs(tagI->first->eta())<2.5)
     {
       nbtags++;
     }
       //std::cout<<" jet pt = " << tagI->first->pt() << "  btag discriminator value = " << tagI->second << std::endl;
   }
   
   
   //calculate HT and AK4 pT, mass
   double HT = 0;
   for(edm::View<reco::PFJet>::const_iterator ijet=pfjets->begin(); ijet!=pfjets->end();ijet++){
     if ( ijet->pt() < 40.0 || fabs( ijet->eta() ) > 2.5 ) continue;
     HT += ijet->pt();
     pfJetsCollection.push_back( TLorentzVector( ijet->px(), ijet->py(), ijet->pz(), ijet->energy() ) );
   }
//    float AK4LeadingMass=0;
//    float AK4SubleadingMass=0;
//    sort( pfJetsCollection.begin(), pfJetsCollection.end(), compare_JetMass);
//    AK4LeadingMass=pfJetsCollection[0].M();
//    AK4SubleadingMass=pfJetsCollection[1].M();
//    float AK4LeadingPt=0;
//    float AK4SubleadingPt=0;
//    sort( pfJetsCollection.begin(), pfJetsCollection.end(), compare_JetPt);
//    AK4LeadingPt=pfJetsCollection[0].Pt();
//    AK4SubleadingPt=pfJetsCollection[1].Pt();
  
   for(edm::View<reco::PFJet>::const_iterator ijet=pfjets8->begin(); ijet!=pfjets8->end();ijet++){
     if ( ijet->pt() < 40.0 || fabs( ijet->eta() ) > 2.5 ) continue;
     pfJets8Collection.push_back( TLorentzVector( ijet->px(), ijet->py(), ijet->pz(), ijet->energy() ) );
   }
   float AK8LeadingMass=0;
   float AK8SubleadingMass=0;
   sort( pfJets8Collection.begin(), pfJets8Collection.end(), compare_JetMass);
   if (pfJets8Collection.size()>0) AK8LeadingMass=pfJets8Collection[0].M();
   if (pfJets8Collection.size()>1) AK8SubleadingMass=pfJets8Collection[1].M();
   float AK8LeadingPt=0;
   float AK8LeadingEta=100;
   float AK8SubleadingPt=0;
   sort( pfJets8Collection.begin(), pfJets8Collection.end(), compare_JetPt);
   if (pfJets8Collection.size()>0)
   {
     AK8LeadingPt=pfJets8Collection[0].Pt();
     AK8LeadingEta=pfJets8Collection[0].Eta();
     // cout<<pfJets8Collection[0].Eta()<<endl;
   }
   if (pfJets8Collection.size()>1) AK8SubleadingPt=pfJets8Collection[1].Pt();
   //sort( pfJets8Collection.begin(), pfJets8Collection.end(), compare_JetPt);
   
   //additional trigger selection
    //bool base_dijet_trigger_cut = triggerResults->accept(triggerBit2);
   
   ////bW selection
   // //pT threshold AK8
   // bool bW_AK8_pT_cut = (AK8LeadingPt > minPt8);
   // //bool bW_AK8_pT_cut = (AK8SubleadingPt > minPt8);
   // //at least one btag
   // bool bW_AK4_btag_cut = (nbtags > 0);
   // //W mass requirement
   // bool bW_AK8_mass_cut = (AK8LeadingMass > minMass8);
   // //final combined cut
   // bool bW_selection = bW_AK8_pT_cut && bW_AK4_btag_cut && bW_AK8_mass_cut;// && base_dijet_trigger_cut;
   
   
   ////tH selection
   bool tH_AK8_pT_cut = (AK8SubleadingPt > minPt8);
   //at least one btag
   bool tH_AK4_btag_cut = (nbtags > 1);
   //W mass requirement
   bool tH_AK8_mass_cut = (AK8LeadingMass > minMass);
   //final combined cut
   bool tH_selection = tH_AK8_pT_cut && tH_AK4_btag_cut && tH_AK8_mass_cut;// && base_dijet_trigger_cut;
   
   float maxCSV2=-log(1-maxCSV);

   histos1D_[ "nBtag" ]->Fill( nbtags );
   histos1D_[ "maxCSV" ]->Fill( maxCSV );
   histos1D_[ "maxCSV2" ]->Fill( maxCSV2 );
   histos1D_[ "nJet" ]->Fill( pfJets8Collection.size() );
   histos1D_[ "nJet4" ]->Fill( pfJetsCollection.size() );
   histos1D_[ "HT" ]->Fill( HT );
   histos1D_[ "jetMass" ]->Fill( AK8LeadingMass );
   histos1D_[ "jetPt" ]->Fill( AK8LeadingPt );
   histos1D_[ "jetMass2" ]->Fill( AK8SubleadingMass );
   histos1D_[ "jetPt2" ]->Fill( AK8SubleadingPt );
   histos1D_[ "eta" ]->Fill( AK8LeadingEta );
   
   //if(bW_selection)
    if(tH_selection)//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   {
     histos1D_[ "maxCSVDenom" ]->Fill( maxCSV );
     histos1D_[ "maxCSV2Denom" ]->Fill( maxCSV2 );
     histos1D_[ "HTDenom" ]->Fill( HT );
     histos1D_[ "jetMassDenom" ]->Fill( AK8LeadingMass );
     histos1D_[ "jetPtDenom" ]->Fill( AK8LeadingPt );
     histos1D_[ "jetMass2Denom" ]->Fill( AK8SubleadingMass );
     histos1D_[ "jetPt2Denom" ]->Fill( AK8SubleadingPt );
     //if (triggerResults->accept(triggerBit))
      if (triggerResults->accept(triggerBit) || triggerResults->accept(triggerBit2)) //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//     if (triggerResults->accept(triggerBit) || triggerResults->accept(triggerBit2) || triggerResults->accept(triggerBit3))//!!!!!!!!!!!!!!!!!
     {
       histos1D_[ "maxCSVPassing" ]->Fill( maxCSV );
       histos1D_[ "maxCSV2Passing" ]->Fill( maxCSV2 );
       histos1D_[ "HTPassing" ]->Fill( HT );
       histos1D_[ "jetMassPassing" ]->Fill( AK8LeadingMass );
       histos1D_[ "jetPtPassing" ]->Fill( AK8LeadingPt );
       histos1D_[ "jetMass2Passing" ]->Fill( AK8SubleadingMass );
       histos1D_[ "jetPt2Passing" ]->Fill( AK8SubleadingPt );
     }
   }
   
   if(tH_selection)
   {
     histos1D_[ "maxCSVTHDenom" ]->Fill( maxCSV );
     histos1D_[ "maxCSV2THDenom" ]->Fill( maxCSV2 );
     histos1D_[ "HTTHDenom" ]->Fill( HT );
     histos1D_[ "jetMassTHDenom" ]->Fill( AK8LeadingMass );
     histos1D_[ "jetPtTHDenom" ]->Fill( AK8LeadingPt );
     histos1D_[ "jetMass2THDenom" ]->Fill( AK8SubleadingMass );
     histos1D_[ "jetPt2THDenom" ]->Fill( AK8SubleadingPt );
     if (triggerResults->accept(triggerBit))
//     if (triggerResults->accept(triggerBit) || triggerResults->accept(triggerBit2) || triggerResults->accept(triggerBit3))//!!!!!!!!!!!!!!!!!!!!!!!!
     {
       histos1D_[ "maxCSVTHPassing" ]->Fill( maxCSV );
       histos1D_[ "maxCSV2THPassing" ]->Fill( maxCSV2 );
       histos1D_[ "HTTHPassing" ]->Fill( HT );
       histos1D_[ "jetMassTHPassing" ]->Fill( AK8LeadingMass );
       histos1D_[ "jetPtTHPassing" ]->Fill( AK8LeadingPt );
       histos1D_[ "jetMass2THPassing" ]->Fill( AK8SubleadingMass );
       histos1D_[ "jetPt2THPassing" ]->Fill( AK8SubleadingPt );
     }
   }
   
   
   
//    if( HT > minHT && pfJetsCollection[0].M() > minMass ) {
//      sort( pfJetsCollection.begin(), pfJetsCollection.end(), compare_JetMass);
//      histos1D_[ "HTDenom" ]->Fill( HT );
//      histos1D_[ "jetMassDenom" ]->Fill( pfJetsCollection[0].M() );
//      histos2D_[ "jetMassHTDenom" ]->Fill( HT, pfJetsCollection[0].M() );
//      histos2D_[ "jetMassPtDenom" ]->Fill( pfJetsCollection[0].Pt(), pfJetsCollection[0].M() );
//      if (triggerResults->accept(triggerBit)){
//        histos1D_[ "HTPassing" ]->Fill( HT );
//        histos1D_[ "jetMassPassing" ]->Fill( pfJetsCollection[0].M() );
//        histos2D_[ "jetMassHTPassing" ]->Fill( HT, pfJetsCollection[0].M() );
//        histos2D_[ "jetMassPtPassing" ]->Fill( pfJetsCollection[0].Pt(), pfJetsCollection[0].M() );
//        cout<<"accept"<<endl;
//      }
//    }
//    
//    cout<<"HT:"<<HT<<" pT8:"<<pfJets8Collection[0].Pt()<<" M:"<<pfJetsCollection[0].M()<<endl;
//    for (unsigned int i=0;i<pfJets8Collection.size();i++)
//    {
//      cout<<"mass:"<<pfJets8Collection[i].M()<<" pt:"<<pfJets8Collection[i].Pt()<<endl;
//    }
   
//    edm::InputTag triggerEvent = edm::InputTag("hltTriggerSummaryAOD");
//    edm::Handle< trigger::TriggerEvent > dummy_TriggerEvent;
//    iEvent.getByLabel( edm::InputTag(triggerEvent.label(), triggerEvent.instance()), dummy_TriggerEvent );
//    
//    const edm::Provenance *meta = dummy_TriggerEvent.provenance();
//    std::string nameProcess = meta->processName();
//    edm::InputTag triggerResultTag = edm::InputTag("TriggerResults","","HLT");
//    triggerResultTag = edm::InputTag( triggerResultTag.label(), triggerResultTag.instance(), nameProcess );
//    
//    edm::Handle<edm::TriggerResults> trigger;
//    iEvent.getByLabel(triggerResultTag, trigger);
//    const edm::TriggerResults& trig = *(trigger.product());
//    
//    edm::Service<edm::service::TriggerNamesService> tns;
//    std::vector<std::string> triggerNames_all;
//    tns->getTrigPaths(trig,triggerNames_all);
//    
//    for(unsigned int i=0;i<triggerNames_all.size();i++)
//    cout<<triggerNames_all[i]<<endl;
   
   
   
//    edm::Handle<edm::TriggerResults> trigResults; //our trigger result object
//    edm::InputTag trigResultsTag("TriggerResults","","HLT"); //make sure have correct process on MC
//    
//    iEvent.getByLabel(trigResultsTag,trigResults);
//    const edm::TriggerNames& trigNames = iEvent.triggerNames(*trigResults);
//    std::vector<std::string> nomi=trigNames.triggerNames();
//    
//    for(unsigned int i=0;i<nomi.size();i++)
//     cout<<nomi[i]<<endl;
//    
//     std::string pathName="dslkh";
//    cout<<"index:"<<trigNames.triggerIndex(pathName)<<endl;
//     bool passTrig=trigResults->accept(1);  
//    cout<<"pass:"<<passTrig<<endl;
}


// ------------ method called once each job just before starting event loop  ------------
void 
TriggerStudies::beginJob()
{
  
  edm::Service< TFileService > fileService;
//   histos2D_[ "jetMassHTDenom" ] = fileService->make< TH2D >( "jetMassHTDenom", "HT vs Leading Jet Mass", 20, 0., 2000, 16, 0., 400. );
//   histos2D_[ "jetMassHTDenom" ]->SetXTitle( "HT [GeV]" );
//   histos2D_[ "jetMassHTDenom" ]->SetYTitle( "Leading Jet Mass [GeV]" );
//   histos2D_[ "jetMassHTPassing" ] = fileService->make< TH2D >( "jetMassHTPassing", "HT vs Leading Jet Mass passing path", 20, 0., 2000, 16, 0., 400. );
//   histos2D_[ "jetMassHTPassing" ]->SetXTitle( "HT [GeV]" );
//   histos2D_[ "jetMassHTPassing" ]->SetYTitle( "Leading Jet Mass [GeV]" );
//   histos2D_[ "jetMassHT2Defficiency" ] = fileService->make< TH2D >( "jetMassHT2Defficiency", "Comparative efficiency", 20, 0., 2000, 16, 0., 400. );
//   histos2D_[ "jetMassHT2Defficiency" ]->SetXTitle( "HT [GeV]" );
//   histos2D_[ "jetMassHT2Defficiency" ]->SetYTitle( "Leading Jet Mass [GeV]" );
//   histos2D_[ "jetMassPtDenom" ] = fileService->make< TH2D >( "jetMassPtDenom", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
//   histos2D_[ "jetMassPtDenom" ]->SetXTitle( "Leading Jet Pt [GeV]" );
//   histos2D_[ "jetMassPtDenom" ]->SetYTitle( "Leading Jet Mass [GeV]" );
//   histos2D_[ "jetMassPtPassing" ] = fileService->make< TH2D >( "jetMassPtPassing", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
//   histos2D_[ "jetMassPtPassing" ]->SetXTitle( "Leading Jet Pt [GeV]" );
//   histos2D_[ "jetMassPtPassing" ]->SetYTitle( "Leading Jet Mass [GeV]" );
//   histos2D_[ "jetMassPt2Defficiency" ] = fileService->make< TH2D >( "jetMassPt2Defficiency", "Leading Jet Mass vs Pt", 10, 0., 1000, 16, 0., 400. );
//   histos2D_[ "jetMassPt2Defficiency" ]->SetXTitle( "Leading Jet Pt [GeV]" );
//   histos2D_[ "jetMassPt2Defficiency" ]->SetYTitle( "Leading Jet Mass [GeV]" );
//   histos1D_[ "jetMassDenom" ] = fileService->make< TH1D >( "jetMassDenom", "Jet mass", 40, 0., 400);
//   histos1D_[ "jetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
//   histos1D_[ "jetMassDenom" ]->Sumw2();
//   histos1D_[ "jetMassPassing" ] = fileService->make< TH1D >( "jetMassPassing", "Jet mass passing", 40, 0., 400);
//   histos1D_[ "jetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
//   histos1D_[ "jetMassPassing" ]->Sumw2();
//   histos1D_[ "jetMassEfficiency" ] = fileService->make< TH1D >( "jetMassEfficiency", "Leading jet mass efficiency", 40, 0., 400);
//   histos1D_[ "jetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
//   histos1D_[ "jetMassEfficiency" ]->SetYTitle( "Efficiency" );
//   histos1D_[ "HTDenom" ] = fileService->make< TH1D >( "HTDenom", "HT", 200, 0., 2000);
//   histos1D_[ "HTDenom" ]->SetXTitle( "HT [GeV]" );
//   histos1D_[ "HTDenom" ]->Sumw2();
//   histos1D_[ "HTPassing" ] = fileService->make< TH1D >( "HTPassing", "HT passing", 200, 0., 2000);
//   histos1D_[ "HTPassing" ]->SetXTitle( "HT [GeV]" );
//   histos1D_[ "HTPassing" ]->Sumw2();
//   histos1D_[ "HTEfficiency" ] = fileService->make< TH1D >( "HTEfficiency", "HT efficiency", 200, 0., 2000);
//   histos1D_[ "HTEfficiency" ]->SetXTitle( "HT [GeV]" );
//   histos1D_[ "HTEfficiency" ]->SetYTitle( "Efficiency" );
//   
//   "jetMass"
//   "jetPt"
//   "HT"
//   "nBtag"
//   "nJet"
  
  
  histos1D_[ "jetMass" ] = fileService->make< TH1D >( "jetMass", "Jet mass", 40, 0., 400);
  histos1D_[ "jetMass" ]->SetXTitle( "Leading Jet Mass [GeV]" );
  histos1D_[ "jetMass" ]->Sumw2();
  histos1D_[ "jetMassDenom" ] = fileService->make< TH1D >( "jetMassDenom", "Jet mass", 40, 0., 400);
  histos1D_[ "jetMassDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
  histos1D_[ "jetMassDenom" ]->Sumw2();
  histos1D_[ "jetMassPassing" ] = fileService->make< TH1D >( "jetMassPassing", "Jet mass passing", 40, 0., 400);
  histos1D_[ "jetMassPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
  histos1D_[ "jetMassPassing" ]->Sumw2();
  histos1D_[ "jetMassEfficiency" ] = fileService->make< TH1D >( "jetMassEfficiency", "Leading jet mass efficiency", 40, 0., 400);
  histos1D_[ "jetMassEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
  histos1D_[ "jetMassEfficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "jetPt" ] = fileService->make< TH1D >( "jetPt", "Jet Pt", 40, 0., 1000);
  histos1D_[ "jetPt" ]->SetXTitle( "Leading Jet Pt [GeV]" );
  histos1D_[ "jetPt" ]->Sumw2();
  histos1D_[ "jetPtDenom" ] = fileService->make< TH1D >( "jetPtDenom", "Jet Pt", 40, 0., 1000);
  histos1D_[ "jetPtDenom" ]->SetXTitle( "Leading Jet Pt [GeV]" );
  histos1D_[ "jetPtDenom" ]->Sumw2();
  histos1D_[ "jetPtPassing" ] = fileService->make< TH1D >( "jetPtPassing", "Jet Pt passing", 40, 0., 1000);
  histos1D_[ "jetPtPassing" ]->SetXTitle( "Leading Jet Pt [GeV]" );
  histos1D_[ "jetPtPassing" ]->Sumw2();
  histos1D_[ "jetPtEfficiency" ] = fileService->make< TH1D >( "jetPtEfficiency", "Leading jet Pt efficiency", 40, 0., 1000);
  histos1D_[ "jetPtEfficiency" ]->SetXTitle( "Leading Jet Pt [GeV]" );
  histos1D_[ "jetPtEfficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "jetMass2" ] = fileService->make< TH1D >( "jetMass2", "Jet mass", 40, 0., 400);
  histos1D_[ "jetMass2" ]->SetXTitle( "Subleading Jet Mass [GeV]" );
  histos1D_[ "jetMass2" ]->Sumw2();
  histos1D_[ "jetMass2Denom" ] = fileService->make< TH1D >( "jetMass2Denom", "Jet mass", 40, 0., 400);
  histos1D_[ "jetMass2Denom" ]->SetXTitle( "Subleading Jet Mass [GeV]" );
  histos1D_[ "jetMass2Denom" ]->Sumw2();
  histos1D_[ "jetMass2Passing" ] = fileService->make< TH1D >( "jetMass2Passing", "Jet mass passing", 40, 0., 400);
  histos1D_[ "jetMass2Passing" ]->SetXTitle( "Subleading Jet Mass [GeV]" );
  histos1D_[ "jetMass2Passing" ]->Sumw2();
  histos1D_[ "jetMass2Efficiency" ] = fileService->make< TH1D >( "jetMass2Efficiency", "Leading jet mass efficiency", 40, 0., 400);
  histos1D_[ "jetMass2Efficiency" ]->SetXTitle( "Subleading Jet Mass [GeV]" );
  histos1D_[ "jetMass2Efficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "jetPt2" ] = fileService->make< TH1D >( "jetPt2", "Jet Pt", 40, 0., 1000);
  histos1D_[ "jetPt2" ]->SetXTitle( "Subleading Jet Pt [GeV]" );
  histos1D_[ "jetPt2" ]->Sumw2();
  histos1D_[ "jetPt2Denom" ] = fileService->make< TH1D >( "jetPt2Denom", "Jet Pt", 40, 0., 1000);
  histos1D_[ "jetPt2Denom" ]->SetXTitle( "Subleading Jet Pt [GeV]" );
  histos1D_[ "jetPt2Denom" ]->Sumw2();
  histos1D_[ "jetPt2Passing" ] = fileService->make< TH1D >( "jetPt2Passing", "Jet Pt passing", 40, 0., 1000);
  histos1D_[ "jetPt2Passing" ]->SetXTitle( "Subleading Jet Pt [GeV]" );
  histos1D_[ "jetPt2Passing" ]->Sumw2();
  histos1D_[ "jetPt2Efficiency" ] = fileService->make< TH1D >( "jetPt2Efficiency", "Leading jet Pt efficiency", 40, 0., 1000);
  histos1D_[ "jetPt2Efficiency" ]->SetXTitle( "Subleading Jet Pt [GeV]" );
  histos1D_[ "jetPt2Efficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "HT" ] = fileService->make< TH1D >( "HT", "HT", 40, 0., 2000);
  histos1D_[ "HT" ]->SetXTitle( "HT [GeV]" );
  histos1D_[ "HT" ]->Sumw2();
  histos1D_[ "HTDenom" ] = fileService->make< TH1D >( "HTDenom", "HT", 40, 0., 2000);
  histos1D_[ "HTDenom" ]->SetXTitle( "HT [GeV]" );
  histos1D_[ "HTDenom" ]->Sumw2();
  histos1D_[ "HTPassing" ] = fileService->make< TH1D >( "HTPassing", "HT passing", 40, 0., 2000);
  histos1D_[ "HTPassing" ]->SetXTitle( "HT [GeV]" );
  histos1D_[ "HTPassing" ]->Sumw2();
  histos1D_[ "HTEfficiency" ] = fileService->make< TH1D >( "HTEfficiency", "HT efficiency", 40, 0., 2000);
  histos1D_[ "HTEfficiency" ]->SetXTitle( "HT [GeV]" );
  histos1D_[ "HTEfficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "nBtag" ] = fileService->make< TH1D >( "nBtag", "nBtag", 6, 0., 6);
  histos1D_[ "nBtag" ]->SetXTitle( "nBtag" );
  histos1D_[ "nBtag" ]->Sumw2();
  
  histos1D_[ "nJet" ] = fileService->make< TH1D >( "nJet", "nJet", 12, 0., 12);
  histos1D_[ "nJet" ]->SetXTitle( "nJet" );
  histos1D_[ "nJet" ]->Sumw2();
  
  histos1D_[ "eta" ] = fileService->make< TH1D >( "eta", "eta", 40, -5, 5);
  histos1D_[ "eta" ]->SetXTitle( "eta" );
  histos1D_[ "eta" ]->Sumw2();
  
  histos1D_[ "nJet4" ] = fileService->make< TH1D >( "nJet4", "nJet4", 12, 0., 12);
  histos1D_[ "nJet4" ]->SetXTitle( "nJetAK4" );
  histos1D_[ "nJet4" ]->Sumw2();
  
  histos1D_[ "jetMassTHDenom" ] = fileService->make< TH1D >( "jetMassTHDenom", "Jet mass", 40, 0., 400);
  histos1D_[ "jetMassTHDenom" ]->SetXTitle( "Leading Jet Mass [GeV]" );
  histos1D_[ "jetMassTHDenom" ]->Sumw2();
  histos1D_[ "jetMassTHPassing" ] = fileService->make< TH1D >( "jetMassTHPassing", "Jet mass passing", 40, 0., 400);
  histos1D_[ "jetMassTHPassing" ]->SetXTitle( "Leading Jet Mass [GeV]" );
  histos1D_[ "jetMassTHPassing" ]->Sumw2();
  histos1D_[ "jetMassTHEfficiency" ] = fileService->make< TH1D >( "jetMassTHEfficiency", "Leading jet mass efficiency", 40, 0., 400);
  histos1D_[ "jetMassTHEfficiency" ]->SetXTitle( "Leading Jet Mass [GeV]" );
  histos1D_[ "jetMassTHEfficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "jetPtTHDenom" ] = fileService->make< TH1D >( "jetPtTHDenom", "Jet Pt", 40, 0., 1000);
  histos1D_[ "jetPtTHDenom" ]->SetXTitle( "Leading Jet Pt [GeV]" );
  histos1D_[ "jetPtTHDenom" ]->Sumw2();
  histos1D_[ "jetPtTHPassing" ] = fileService->make< TH1D >( "jetPtTHPassing", "Jet Pt passing", 40, 0., 1000);
  histos1D_[ "jetPtTHPassing" ]->SetXTitle( "Leading Jet Pt [GeV]" );
  histos1D_[ "jetPtTHPassing" ]->Sumw2();
  histos1D_[ "jetPtTHEfficiency" ] = fileService->make< TH1D >( "jetPtTHEfficiency", "Leading jet Pt efficiency", 40, 0., 1000);
  histos1D_[ "jetPtTHEfficiency" ]->SetXTitle( "Leading Jet Pt [GeV]" );
  histos1D_[ "jetPtTHEfficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "jetMass2THDenom" ] = fileService->make< TH1D >( "jetMass2THDenom", "Jet mass", 40, 0., 400);
  histos1D_[ "jetMass2THDenom" ]->SetXTitle( "Subleading Jet Mass [GeV]" );
  histos1D_[ "jetMass2THDenom" ]->Sumw2();
  histos1D_[ "jetMass2THPassing" ] = fileService->make< TH1D >( "jetMass2THPassing", "Jet mass passing", 40, 0., 400);
  histos1D_[ "jetMass2THPassing" ]->SetXTitle( "Subleading Jet Mass [GeV]" );
  histos1D_[ "jetMass2THPassing" ]->Sumw2();
  histos1D_[ "jetMass2THEfficiency" ] = fileService->make< TH1D >( "jetMass2THEfficiency", "Leading jet mass efficiency", 40, 0., 400);
  histos1D_[ "jetMass2THEfficiency" ]->SetXTitle( "Subleading Jet Mass [GeV]" );
  histos1D_[ "jetMass2THEfficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "jetPt2THDenom" ] = fileService->make< TH1D >( "jetPt2THDenom", "Jet Pt", 40, 0., 1000);
  histos1D_[ "jetPt2THDenom" ]->SetXTitle( "Subleading Jet Pt [GeV]" );
  histos1D_[ "jetPt2THDenom" ]->Sumw2();
  histos1D_[ "jetPt2THPassing" ] = fileService->make< TH1D >( "jetPt2THPassing", "Jet Pt passing", 40, 0., 1000);
  histos1D_[ "jetPt2THPassing" ]->SetXTitle( "Subleading Jet Pt [GeV]" );
  histos1D_[ "jetPt2THPassing" ]->Sumw2();
  histos1D_[ "jetPt2THEfficiency" ] = fileService->make< TH1D >( "jetPt2THEfficiency", "Leading jet Pt efficiency", 40, 0., 1000);
  histos1D_[ "jetPt2THEfficiency" ]->SetXTitle( "Subleading Jet Pt [GeV]" );
  histos1D_[ "jetPt2THEfficiency" ]->SetYTitle( "Efficiency" );
  
  histos1D_[ "HTTHDenom" ] = fileService->make< TH1D >( "HTTHDenom", "HT", 40, 0., 2000);
  histos1D_[ "HTTHDenom" ]->SetXTitle( "HT [GeV]" );
  histos1D_[ "HTTHDenom" ]->Sumw2();
  histos1D_[ "HTTHPassing" ] = fileService->make< TH1D >( "HTTHPassing", "HT passing", 40, 0., 2000);
  histos1D_[ "HTTHPassing" ]->SetXTitle( "HT [GeV]" );
  histos1D_[ "HTTHPassing" ]->Sumw2();
  histos1D_[ "HTTHEfficiency" ] = fileService->make< TH1D >( "HTTHEfficiency", "HT efficiency", 40, 0., 2000);
  histos1D_[ "HTTHEfficiency" ]->SetXTitle( "HT [GeV]" );
  histos1D_[ "HTTHEfficiency" ]->SetYTitle( "Efficiency" );



  histos1D_[ "maxCSV" ] = fileService->make< TH1D >( "maxCSV", "maxCSV", 40, 0., 1.);
  histos1D_[ "maxCSV" ]->SetXTitle( "maxCSV" );
  histos1D_[ "maxCSV" ]->Sumw2();
  histos1D_[ "maxCSVDenom" ] = fileService->make< TH1D >( "maxCSVDenom", "maxCSV", 40, 0., 1.);
  histos1D_[ "maxCSVDenom" ]->SetXTitle( "maxCSV" );
  histos1D_[ "maxCSVDenom" ]->Sumw2();
  histos1D_[ "maxCSVPassing" ] = fileService->make< TH1D >( "maxCSVPassing", "maxCSV passing", 40, 0., 1.);
  histos1D_[ "maxCSVPassing" ]->SetXTitle( "maxCSV" );
  histos1D_[ "maxCSVPassing" ]->Sumw2();
  histos1D_[ "maxCSVEfficiency" ] = fileService->make< TH1D >( "maxCSVEfficiency", "maxCSV efficiency", 40, 0., 1.);
  histos1D_[ "maxCSVEfficiency" ]->SetXTitle( "maxCSV" );
  histos1D_[ "maxCSVEfficiency" ]->SetYTitle( "Efficiency" );

  histos1D_[ "maxCSVTHDenom" ] = fileService->make< TH1D >( "maxCSVTHDenom", "maxCSV", 40, 0., 1.);
  histos1D_[ "maxCSVTHDenom" ]->SetXTitle( "maxCSV" );
  histos1D_[ "maxCSVTHDenom" ]->Sumw2();
  histos1D_[ "maxCSVTHPassing" ] = fileService->make< TH1D >( "maxCSVTHPassing", "maxCSV passing", 40, 0., 1.);
  histos1D_[ "maxCSVTHPassing" ]->SetXTitle( "maxCSV" );
  histos1D_[ "maxCSVTHPassing" ]->Sumw2();
  histos1D_[ "maxCSVTHEfficiency" ] = fileService->make< TH1D >( "maxCSVTHEfficiency", "maxCSV efficiency", 40, 0., 1.);
  histos1D_[ "maxCSVTHEfficiency" ]->SetXTitle( "maxCSV" );
  histos1D_[ "maxCSVTHEfficiency" ]->SetYTitle( "Efficiency" );



  histos1D_[ "maxCSV2" ] = fileService->make< TH1D >( "maxCSV2", "maxCSV2", 40, 0., 7.);
  histos1D_[ "maxCSV2" ]->SetXTitle( "maxCSV2" );
  histos1D_[ "maxCSV2" ]->Sumw2();
  histos1D_[ "maxCSV2Denom" ] = fileService->make< TH1D >( "maxCSV2Denom", "maxCSV2", 40, 0., 7.);
  histos1D_[ "maxCSV2Denom" ]->SetXTitle( "maxCSV2" );
  histos1D_[ "maxCSV2Denom" ]->Sumw2();
  histos1D_[ "maxCSV2Passing" ] = fileService->make< TH1D >( "maxCSV2Passing", "maxCSV2 passing", 40, 0., 7.);
  histos1D_[ "maxCSV2Passing" ]->SetXTitle( "maxCSV2" );
  histos1D_[ "maxCSV2Passing" ]->Sumw2();
  histos1D_[ "maxCSV2Efficiency" ] = fileService->make< TH1D >( "maxCSV2Efficiency", "maxCSV2 efficiency", 40, 0., 7.);
  histos1D_[ "maxCSV2Efficiency" ]->SetXTitle( "maxCSV2" );
  histos1D_[ "maxCSV2Efficiency" ]->SetYTitle( "Efficiency" );

  histos1D_[ "maxCSV2THDenom" ] = fileService->make< TH1D >( "maxCSV2THDenom", "maxCSV2", 40, 0., 7.);
  histos1D_[ "maxCSV2THDenom" ]->SetXTitle( "maxCSV2" );
  histos1D_[ "maxCSV2THDenom" ]->Sumw2();
  histos1D_[ "maxCSV2THPassing" ] = fileService->make< TH1D >( "maxCSV2THPassing", "maxCSV2 passing", 40, 0., 7.);
  histos1D_[ "maxCSV2THPassing" ]->SetXTitle( "maxCSV2" );
  histos1D_[ "maxCSV2THPassing" ]->Sumw2();
  histos1D_[ "maxCSV2THEfficiency" ] = fileService->make< TH1D >( "maxCSV2THEfficiency", "maxCSV2 efficiency", 40, 0., 7.);
  histos1D_[ "maxCSV2THEfficiency" ]->SetXTitle( "max2CSV" );
  histos1D_[ "maxCSV2THEfficiency" ]->SetYTitle( "Efficiency" );

//  histos1D_[ "nBtagDenom" ] = fileService->make< TH1D >( "nBtagDenom", "nBtag", 6, 0., 6);
//  histos1D_[ "nBtagDenom" ]->SetXTitle( "nBtag" );
//  histos1D_[ "nBtagDenom" ]->Sumw2();
//  histos1D_[ "nBtagPassing" ] = fileService->make< TH1D >( "nBtagPassing", "nBtag", 6, 0., 6);
//  histos1D_[ "nBtagPassing" ]->SetXTitle( "nBtag" );
//  histos1D_[ "nBtagPassing" ]->Sumw2();
//  histos1D_[ "nBtagEfficiency" ] = fileService->make< TH1D >( "nBtag", "nBtag", 6, 0., 6);
//  histos1D_[ "nBtagEfficiency" ]->SetXTitle( "nBtag" );
//  histos1D_[ "nBtagEfficiency" ]->Sumw2();

  
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TriggerStudies::endJob() 
{
  
  histos1D_[ "jetPtEfficiency" ]->Sumw2();
  histos1D_[ "jetPtEfficiency" ]->Divide(histos1D_[ "jetPtPassing" ], histos1D_[ "jetPtDenom" ], 1,1,"B");
  histos1D_[ "jetMassEfficiency" ]->Sumw2();
  histos1D_[ "jetMassEfficiency" ]->Divide(histos1D_[ "jetMassPassing" ], histos1D_[ "jetMassDenom" ], 1,1,"B");
  
  histos1D_[ "jetPt2Efficiency" ]->Sumw2();
  histos1D_[ "jetPt2Efficiency" ]->Divide(histos1D_[ "jetPt2Passing" ], histos1D_[ "jetPt2Denom" ], 1,1,"B");
  histos1D_[ "jetMass2Efficiency" ]->Sumw2();
  histos1D_[ "jetMass2Efficiency" ]->Divide(histos1D_[ "jetMass2Passing" ], histos1D_[ "jetMass2Denom" ], 1,1,"B");
  
  histos1D_[ "HTEfficiency" ]->Sumw2();
  histos1D_[ "HTEfficiency" ]->Divide(histos1D_[ "HTPassing" ], histos1D_[ "HTDenom" ], 1,1,"B");
  
  
  histos1D_[ "jetPtTHEfficiency" ]->Sumw2();
  histos1D_[ "jetPtTHEfficiency" ]->Divide(histos1D_[ "jetPtTHPassing" ], histos1D_[ "jetPtTHDenom" ], 1,1,"B");
  histos1D_[ "jetMassTHEfficiency" ]->Sumw2();
  histos1D_[ "jetMassTHEfficiency" ]->Divide(histos1D_[ "jetMassTHPassing" ], histos1D_[ "jetMassTHDenom" ], 1,1,"B");
  
  histos1D_[ "jetPt2THEfficiency" ]->Sumw2();
  histos1D_[ "jetPt2THEfficiency" ]->Divide(histos1D_[ "jetPt2THPassing" ], histos1D_[ "jetPt2THDenom" ], 1,1,"B");
  histos1D_[ "jetMass2THEfficiency" ]->Sumw2();
  histos1D_[ "jetMass2THEfficiency" ]->Divide(histos1D_[ "jetMass2THPassing" ], histos1D_[ "jetMass2THDenom" ], 1,1,"B");
  
  histos1D_[ "HTTHEfficiency" ]->Sumw2();
  histos1D_[ "HTTHEfficiency" ]->Divide(histos1D_[ "HTTHPassing" ], histos1D_[ "HTTHDenom" ], 1,1,"B");

  histos1D_[ "maxCSVEfficiency" ]->Sumw2();
  histos1D_[ "maxCSVEfficiency" ]->Divide(histos1D_[ "maxCSVPassing" ], histos1D_[ "maxCSVDenom" ], 1,1,"B");
  histos1D_[ "maxCSVTHEfficiency" ]->Sumw2();
  histos1D_[ "maxCSVTHEfficiency" ]->Divide(histos1D_[ "maxCSVTHPassing" ], histos1D_[ "maxCSVTHDenom" ], 1,1,"B");
  
}

// ------------ method called when starting to processes a run  ------------
/*
void 
TriggerStudies::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
TriggerStudies::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
TriggerStudies::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
TriggerStudies::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TriggerStudies::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TriggerStudies);
