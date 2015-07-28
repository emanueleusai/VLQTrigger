void compFinal_trgout_bWrun2_jetPt2TH()
{
//=========Macro generated from canvas: compFinal_trgout_bWrun2_jetPt2TH/
//=========  (Mon Jul 27 18:54:42 2015) by ROOT version6.02/05
   TCanvas *compFinal_trgout_bWrun2_jetPt2TH = new TCanvas("compFinal_trgout_bWrun2_jetPt2TH", "",0,0,600,600);
   compFinal_trgout_bWrun2_jetPt2TH->SetHighLightColor(2);
   compFinal_trgout_bWrun2_jetPt2TH->Range(9.899995,-0.14,1263.9,1.26);
   compFinal_trgout_bWrun2_jetPt2TH->SetFillColor(0);
   compFinal_trgout_bWrun2_jetPt2TH->SetBorderMode(0);
   compFinal_trgout_bWrun2_jetPt2TH->SetBorderSize(2);
   compFinal_trgout_bWrun2_jetPt2TH->SetLeftMargin(0.15);
   compFinal_trgout_bWrun2_jetPt2TH->SetRightMargin(0.05);
   compFinal_trgout_bWrun2_jetPt2TH->SetTopMargin(0.15);
   compFinal_trgout_bWrun2_jetPt2TH->SetFrameBorderMode(0);
   compFinal_trgout_bWrun2_jetPt2TH->SetFrameBorderMode(0);
   
   Double_t _fx3246[13] = {
   100,
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
   Double_t _fy3246[13] = {
   0.1321408,
   0.272,
   0.3384321,
   0.6605923,
   0.9918699,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1};
   Double_t _felx3246[13] = {
   100,
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
   Double_t _fely3246[13] = {
   0.007996126,
   0.009315952,
   0.01029572,
   0.02280832,
   0.01196851,
   0.02144323,
   0.03322531,
   0.08458096,
   0.1513615,
   0.1513615,
   0.2496484,
   0.2496484,
   0.4369725};
   Double_t _fehx3246[13] = {
   100,
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
   Double_t _fehy3246[13] = {
   0.008279337,
   0.009451143,
   0.01039874,
   0.02232185,
   0.005918351,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(13,_fx3246,_fy3246,_felx3246,_fehx3246,_fely3246,_fehy3246);
   grae->SetName("");
   grae->SetTitle("");
   grae->SetFillColor(1);
   grae->SetLineColor(2);
   grae->SetLineWidth(3);
   
   TH1F *Graph_Graph3246 = new TH1F("Graph_Graph3246","",100,0,1320);
   Graph_Graph3246->SetMinimum(0);
   Graph_Graph3246->SetMaximum(1.05);
   Graph_Graph3246->SetDirectory(0);
   Graph_Graph3246->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Graph_Graph3246->SetLineColor(ci);
   Graph_Graph3246->GetXaxis()->SetTitle("Subleading jet pT (GeV)");
   Graph_Graph3246->GetXaxis()->SetRange(16,91);
   Graph_Graph3246->GetXaxis()->SetLabelFont(42);
   Graph_Graph3246->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3246->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3246->GetXaxis()->SetTitleFont(42);
   Graph_Graph3246->GetYaxis()->SetTitle("Efficiency");
   Graph_Graph3246->GetYaxis()->SetLabelFont(42);
   Graph_Graph3246->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3246->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3246->GetYaxis()->SetTitleFont(42);
   Graph_Graph3246->GetZaxis()->SetLabelFont(42);
   Graph_Graph3246->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3246->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3246->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3246);
   
   grae->Draw("ap");
   
   Double_t _fx3247[13] = {
   100,
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
   Double_t _fy3247[13] = {
   0.2129256,
   0.6186667,
   0.9373805,
   0.9681093,
   0.9837398,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1};
   Double_t _felx3247[13] = {
   100,
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
   Double_t _fely3247[13] = {
   0.009725222,
   0.01027707,
   0.005441137,
   0.009148893,
   0.0147125,
   0.02144323,
   0.03322531,
   0.08458096,
   0.1513615,
   0.1513615,
   0.2496484,
   0.2496484,
   0.4369725};
   Double_t _fehx3247[13] = {
   100,
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
   Double_t _fehy3247[13] = {
   0.009946184,
   0.01020671,
   0.005161985,
   0.007716839,
   0.009152476,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   grae = new TGraphAsymmErrors(13,_fx3247,_fy3247,_felx3247,_fehx3247,_fely3247,_fehy3247);
   grae->SetName("");
   grae->SetTitle("");
   grae->SetFillColor(1);
   grae->SetLineColor(3);
   grae->SetLineWidth(3);
   
   TH1F *Graph_Graph3247 = new TH1F("Graph_Graph3247","",100,0,1320);
   Graph_Graph3247->SetMinimum(0.1235204);
   Graph_Graph3247->SetMaximum(1.07968);
   Graph_Graph3247->SetDirectory(0);
   Graph_Graph3247->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph3247->SetLineColor(ci);
   Graph_Graph3247->GetXaxis()->SetLabelFont(42);
   Graph_Graph3247->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3247->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3247->GetXaxis()->SetTitleFont(42);
   Graph_Graph3247->GetYaxis()->SetLabelFont(42);
   Graph_Graph3247->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3247->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3247->GetYaxis()->SetTitleFont(42);
   Graph_Graph3247->GetZaxis()->SetLabelFont(42);
   Graph_Graph3247->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3247->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3247->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3247);
   
   grae->Draw("p");
   
   Double_t _fx3248[13] = {
   100,
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
   Double_t _fy3248[13] = {
   0.1084824,
   0.6582222,
   0.9608031,
   0.9749431,
   0.9837398,
   1,
   1,
   1,
   1,
   1,
   1,
   1,
   1};
   Double_t _felx3248[13] = {
   100,
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
   Double_t _fely3248[13] = {
   0.007323212,
   0.01004834,
   0.004395835,
   0.008246209,
   0.0147125,
   0.02144323,
   0.03322531,
   0.08458096,
   0.1513615,
   0.1513615,
   0.2496484,
   0.2496484,
   0.4369725};
   Double_t _fehx3248[13] = {
   100,
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
   Double_t _fehy3248[13] = {
   0.007624681,
   0.009954525,
   0.004101523,
   0.006788873,
   0.009152476,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0};
   grae = new TGraphAsymmErrors(13,_fx3248,_fy3248,_felx3248,_fehx3248,_fely3248,_fehy3248);
   grae->SetName("");
   grae->SetTitle("");
   grae->SetFillColor(1);
   grae->SetLineColor(4);
   grae->SetLineWidth(3);
   
   TH1F *Graph_Graph3248 = new TH1F("Graph_Graph3248","",100,0,1320);
   Graph_Graph3248->SetMinimum(0.01127511);
   Graph_Graph3248->SetMaximum(1.089884);
   Graph_Graph3248->SetDirectory(0);
   Graph_Graph3248->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph3248->SetLineColor(ci);
   Graph_Graph3248->GetXaxis()->SetLabelFont(42);
   Graph_Graph3248->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3248->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph3248->GetXaxis()->SetTitleFont(42);
   Graph_Graph3248->GetYaxis()->SetLabelFont(42);
   Graph_Graph3248->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3248->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph3248->GetYaxis()->SetTitleFont(42);
   Graph_Graph3248->GetZaxis()->SetLabelFont(42);
   Graph_Graph3248->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3248->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph3248->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3248);
   
   grae->Draw("p");
   Double_t xAxis36[14] = {0, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 900, 1200}; 
   
   TH1D *aaa36 = new TH1D("aaa36","Jet Pt",13, xAxis36);
   aaa36->SetBinContent(1,0.5132534);
   aaa36->SetBinContent(2,0.6663705);
   aaa36->SetBinContent(3,0.6195765);
   aaa36->SetBinContent(4,0.1300163);
   aaa36->SetBinContent(5,0.03642825);
   aaa36->SetBinContent(6,0.01540056);
   aaa36->SetBinContent(7,0.009773434);
   aaa36->SetBinContent(8,0.003553976);
   aaa36->SetBinContent(9,0.001776988);
   aaa36->SetBinContent(10,0.001776988);
   aaa36->SetBinContent(11,0.000888494);
   aaa36->SetBinContent(12,0.000888494);
   aaa36->SetBinContent(13,0.0002961647);
   aaa36->SetBinError(1,0.01232913);
   aaa36->SetBinError(2,0.01404832);
   aaa36->SetBinError(3,0.01354609);
   aaa36->SetBinError(4,0.006205339);
   aaa36->SetBinError(5,0.003284625);
   aaa36->SetBinError(6,0.002135674);
   aaa36->SetBinError(7,0.001701336);
   aaa36->SetBinError(8,0.001025945);
   aaa36->SetBinError(9,0.0007254523);
   aaa36->SetBinError(10,0.0007254523);
   aaa36->SetBinError(11,0.0005129723);
   aaa36->SetBinError(12,0.0005129723);
   aaa36->SetBinError(13,0.0002961647);
   aaa36->SetEntries(6753);

   ci = 1364;
   color = new TColor(ci, 0, 0, 1, " ", 0.35);
   aaa36->SetFillColor(ci);
   aaa36->SetFillStyle(3004);

   ci = TColor::GetColor("#000099");
   aaa36->SetLineColor(ci);
   aaa36->GetXaxis()->SetTitle("Subleading Jet Pt [GeV]");
   aaa36->GetXaxis()->SetRange(1,80);
   aaa36->GetXaxis()->SetLabelFont(42);
   aaa36->GetXaxis()->SetLabelSize(0.035);
   aaa36->GetXaxis()->SetTitleSize(0.035);
   aaa36->GetXaxis()->SetTitleFont(42);
   aaa36->GetYaxis()->SetLabelFont(42);
   aaa36->GetYaxis()->SetLabelSize(0.035);
   aaa36->GetYaxis()->SetTitleSize(0.035);
   aaa36->GetYaxis()->SetTitleFont(42);
   aaa36->GetZaxis()->SetLabelFont(42);
   aaa36->GetZaxis()->SetLabelSize(0.035);
   aaa36->GetZaxis()->SetTitleSize(0.035);
   aaa36->GetZaxis()->SetTitleFont(42);
   aaa36->Draw("SAMEHIST");
   
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
   compFinal_trgout_bWrun2_jetPt2TH->Modified();
   compFinal_trgout_bWrun2_jetPt2TH->cd();
   compFinal_trgout_bWrun2_jetPt2TH->SetSelected(compFinal_trgout_bWrun2_jetPt2TH);
}
