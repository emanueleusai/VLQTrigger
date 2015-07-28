void compFinal_trgout_tWrun2_jetPt2TH()
{
//=========Macro generated from canvas: compFinal_trgout_tWrun2_jetPt2TH/
//=========  (Mon Jul 27 18:54:46 2015) by ROOT version6.02/05
   TCanvas *compFinal_trgout_tWrun2_jetPt2TH = new TCanvas("compFinal_trgout_tWrun2_jetPt2TH", "",0,0,600,600);
   compFinal_trgout_tWrun2_jetPt2TH->SetHighLightColor(2);
   compFinal_trgout_tWrun2_jetPt2TH->Range(6.999995,-0.14,1267,1.26);
   compFinal_trgout_tWrun2_jetPt2TH->SetFillColor(0);
   compFinal_trgout_tWrun2_jetPt2TH->SetBorderMode(0);
   compFinal_trgout_tWrun2_jetPt2TH->SetBorderSize(2);
   compFinal_trgout_tWrun2_jetPt2TH->SetLeftMargin(0.15);
   compFinal_trgout_tWrun2_jetPt2TH->SetRightMargin(0.05);
   compFinal_trgout_tWrun2_jetPt2TH->SetTopMargin(0.15);
   compFinal_trgout_tWrun2_jetPt2TH->SetFrameBorderMode(0);
   compFinal_trgout_tWrun2_jetPt2TH->SetFrameBorderMode(0);
   
   Double_t _fx3494[12] = {
   225,
   275,
   325,
   375,
   425,
   475,
   525,
   575,
   625,
   675,
   800,
   1050};
   Double_t _fy3494[12] = {
   0.4708995,
   0.5677083,
   0.9545455,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1};
   Double_t _felx3494[12] = {
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   100,
   150};
   Double_t _fely3494[12] = {
   0.03603887,
   0.03582466,
   0.03077355,
   0.02698293,
   0.0586742,
   0.119839,
   0.1337716,
   0.2052842,
   0.3181538,
   0.2052842,
   0.1513615,
   0.4369725};
   Double_t _fehx3494[12] = {
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   100,
   150};
   Double_t _fehy3494[12] = {
   0.0362425,
   0.0353582,
   0.02141822,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(12,_fx3494,_fy3494,_felx3494,_fehx3494,_fely3494,_fehy3494);
   grae->SetName("");
   grae->SetTitle("");
   grae->SetFillColor(1);
   grae->SetLineColor(2);
   grae->SetLineWidth(3);
   
   TH1F *Graph_Graph3494 = new TH1F("Graph_Graph3494","",100,100,1300);
   Graph_Graph3494->SetMinimum(0);
   Graph_Graph3494->SetMaximum(1.05);
   Graph_Graph3494->SetDirectory(0);
   Graph_Graph3494->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph3494->SetLineColor(ci);
   Graph_Graph3494->GetXaxis()->SetTitle("Subleading jet pT (GeV)");
   Graph_Graph3494->GetXaxis()->SetRange(9,92);
   Graph_Graph3494->GetXaxis()->SetLabelFont(42);
   Graph_Graph3494->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3494->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3494->GetXaxis()->SetTitleFont(42);
   Graph_Graph3494->GetYaxis()->SetTitle("Efficiency");
   Graph_Graph3494->GetYaxis()->SetLabelFont(42);
   Graph_Graph3494->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3494->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3494->GetYaxis()->SetTitleFont(42);
   Graph_Graph3494->GetZaxis()->SetLabelFont(42);
   Graph_Graph3494->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3494->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3494->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3494);
   
   grae->Draw("ap");
   
   Double_t _fx3495[12] = {
   225,
   275,
   325,
   375,
   425,
   475,
   525,
   575,
   625,
   675,
   800,
   1050};
   Double_t _fy3495[12] = {
   0.7671958,
   0.9791667,
   0.9848485,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1};
   Double_t _felx3495[12] = {
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   100,
   150};
   Double_t _fely3495[12] = {
   0.03156383,
   0.01224293,
   0.02192489,
   0.02698293,
   0.0586742,
   0.119839,
   0.1337716,
   0.2052842,
   0.3181538,
   0.2052842,
   0.1513615,
   0.4369725};
   Double_t _fehx3495[12] = {
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   100,
   150};
   Double_t _fehy3495[12] = {
   0.02969179,
   0.008820879,
   0.01097634,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   grae = new TGraphAsymmErrors(12,_fx3495,_fy3495,_felx3495,_fehx3495,_fely3495,_fehy3495);
   grae->SetName("");
   grae->SetTitle("");
   grae->SetFillColor(1);
   grae->SetLineColor(3);
   grae->SetLineWidth(3);
   
   TH1F *Graph_Graph3495 = new TH1F("Graph_Graph3495","",100,100,1300);
   Graph_Graph3495->SetMinimum(0.5193303);
   Graph_Graph3495->SetMaximum(1.043697);
   Graph_Graph3495->SetDirectory(0);
   Graph_Graph3495->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph3495->SetLineColor(ci);
   Graph_Graph3495->GetXaxis()->SetLabelFont(42);
   Graph_Graph3495->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3495->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3495->GetXaxis()->SetTitleFont(42);
   Graph_Graph3495->GetYaxis()->SetLabelFont(42);
   Graph_Graph3495->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3495->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3495->GetYaxis()->SetTitleFont(42);
   Graph_Graph3495->GetZaxis()->SetLabelFont(42);
   Graph_Graph3495->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3495->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3495->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3495);
   
   grae->Draw("p");
   
   Double_t _fx3496[12] = {
   225,
   275,
   325,
   375,
   425,
   475,
   525,
   575,
   625,
   675,
   800,
   1050};
   Double_t _fy3496[12] = {
   0.8412698,
   0.9895833,
   0.9848485,
   0.9756098,
   0.9444444,
   1,
   1,
   1,
   1,
   1,
   1,
   1};
   Double_t _felx3496[12] = {
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   100,
   150};
   Double_t _fely3496[12] = {
   0.02770964,
   0.009511153,
   0.02192489,
   0.03450945,
   0.07294832,
   0.119839,
   0.1337716,
   0.2052842,
   0.3181538,
   0.2052842,
   0.1513615,
   0.4369725};
   Double_t _fehx3496[12] = {
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   25,
   100,
   150};
   Double_t _fehy3496[12] = {
   0.02531489,
   0.005882977,
   0.01097634,
   0.01755622,
   0.03912018,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   grae = new TGraphAsymmErrors(12,_fx3496,_fy3496,_felx3496,_fehx3496,_fely3496,_fehy3496);
   grae->SetName("");
   grae->SetTitle("");
   grae->SetFillColor(1);
   grae->SetLineColor(4);
   grae->SetLineWidth(3);
   
   TH1F *Graph_Graph3496 = new TH1F("Graph_Graph3496","",100,100,1300);
   Graph_Graph3496->SetMinimum(0.5193303);
   Graph_Graph3496->SetMaximum(1.043697);
   Graph_Graph3496->SetDirectory(0);
   Graph_Graph3496->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph3496->SetLineColor(ci);
   Graph_Graph3496->GetXaxis()->SetLabelFont(42);
   Graph_Graph3496->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3496->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3496->GetXaxis()->SetTitleFont(42);
   Graph_Graph3496->GetYaxis()->SetLabelFont(42);
   Graph_Graph3496->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3496->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3496->GetYaxis()->SetTitleFont(42);
   Graph_Graph3496->GetZaxis()->SetLabelFont(42);
   Graph_Graph3496->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3496->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3496->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3496);
   
   grae->Draw("p");
   Double_t xAxis72[14] = {0, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 900, 1200}; 
   
   TH1D *aaa72 = new TH1D("aaa72","Jet Pt",13, xAxis72);
   aaa72->SetBinContent(2,0.7026022);
   aaa72->SetBinContent(3,0.7137546);
   aaa72->SetBinContent(4,0.2453532);
   aaa72->SetBinContent(5,0.1524164);
   aaa72->SetBinContent(6,0.0669145);
   aaa72->SetBinContent(7,0.02973978);
   aaa72->SetBinContent(8,0.0260223);
   aaa72->SetBinContent(9,0.01486989);
   aaa72->SetBinContent(10,0.007434944);
   aaa72->SetBinContent(11,0.01486989);
   aaa72->SetBinContent(12,0.02230483);
   aaa72->SetBinContent(13,0.003717472);
   aaa72->SetBinError(2,0.05110679);
   aaa72->SetBinError(3,0.0515108);
   aaa72->SetBinError(4,0.03020089);
   aaa72->SetBinError(5,0.02380344);
   aaa72->SetBinError(6,0.0157719);
   aaa72->SetBinError(7,0.0105146);
   aaa72->SetBinError(8,0.009835507);
   aaa72->SetBinError(9,0.007434944);
   aaa72->SetBinError(10,0.005257299);
   aaa72->SetBinError(11,0.007434944);
   aaa72->SetBinError(12,0.00910591);
   aaa72->SetBinError(13,0.003717472);
   aaa72->SetEntries(538);

   ci = 1550;
   color = new TColor(ci, 0, 0, 1, " ", 0.35);
   aaa72->SetFillColor(ci);
   aaa72->SetFillStyle(3004);

   ci = TColor::GetColor("#000099");
   aaa72->SetLineColor(ci);
   aaa72->GetXaxis()->SetTitle("Subleading Jet Pt [GeV]");
   aaa72->GetXaxis()->SetRange(1,80);
   aaa72->GetXaxis()->SetLabelFont(42);
   aaa72->GetXaxis()->SetLabelSize(0.035);
   aaa72->GetXaxis()->SetTitleSize(0.035);
   aaa72->GetXaxis()->SetTitleFont(42);
   aaa72->GetYaxis()->SetLabelFont(42);
   aaa72->GetYaxis()->SetLabelSize(0.035);
   aaa72->GetYaxis()->SetTitleSize(0.035);
   aaa72->GetYaxis()->SetTitleFont(42);
   aaa72->GetZaxis()->SetLabelFont(42);
   aaa72->GetZaxis()->SetLabelSize(0.035);
   aaa72->GetZaxis()->SetTitleSize(0.035);
   aaa72->GetZaxis()->SetTitleFont(42);
   aaa72->Draw("SAMEHIST");
   
   TLegend *leg = new TLegend(0,0.85,0.99,0.99,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("NULL","","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("","PFHT800","l");
   entry->SetLineColor(2);
   entry->SetLineStyle(1);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("","AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45","l");
   entry->SetLineColor(3);
   entry->SetLineStyle(1);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("","AK8DiPFJet250_200_TrimMass30_BTagCSV0p45","l");
   entry->SetLineColor(4);
   entry->SetLineStyle(1);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   compFinal_trgout_tWrun2_jetPt2TH->Modified();
   compFinal_trgout_tWrun2_jetPt2TH->cd();
   compFinal_trgout_tWrun2_jetPt2TH->SetSelected(compFinal_trgout_tWrun2_jetPt2TH);
}
