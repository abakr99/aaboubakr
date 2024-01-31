#ifdef __CLING__
#pragma cling optimize(0)
#endif
void Canvas()
{
//=========Macro generated from canvas: tcanvas1/tcanvas1
//=========  (Tue Mar 21 09:53:42 2023) by ROOT version 6.26/04
   TCanvas *tcanvas1 = new TCanvas("tcanvas1", "tcanvas1",1,1,4,4);
   tcanvas1->Range(0,0,1,1);
   tcanvas1->SetBorderMode(0);
   tcanvas1->SetBorderSize(0);
   tcanvas1->SetFrameFillColor(0);
   tcanvas1->SetFrameBorderMode(0);
   
   TH1F *ha15__1 = new TH1F("ha15__1","adc 15 histogram",4096,0,4096);
   ha15__1->SetBinContent(180,6);
   ha15__1->SetBinContent(181,63);
   ha15__1->SetBinContent(182,474);
   ha15__1->SetBinContent(183,1707);
   ha15__1->SetBinContent(184,2675);
   ha15__1->SetBinContent(185,1611);
   ha15__1->SetBinContent(186,773);
   ha15__1->SetBinContent(187,673);
   ha15__1->SetBinContent(188,806);
   ha15__1->SetBinContent(189,1084);
   ha15__1->SetBinContent(190,1359);
   ha15__1->SetBinContent(191,1704);
   ha15__1->SetBinContent(192,1839);
   ha15__1->SetBinContent(193,1839);
   ha15__1->SetBinContent(194,1924);
   ha15__1->SetBinContent(195,1602);
   ha15__1->SetBinContent(196,1413);
   ha15__1->SetBinContent(197,1330);
   ha15__1->SetBinContent(198,1301);
   ha15__1->SetBinContent(199,1351);
   ha15__1->SetBinContent(200,1270);
   ha15__1->SetBinContent(201,1268);
   ha15__1->SetBinContent(202,1256);
   ha15__1->SetBinContent(203,1260);
   ha15__1->SetBinContent(204,1084);
   ha15__1->SetBinContent(205,1013);
   ha15__1->SetBinContent(206,953);
   ha15__1->SetBinContent(207,865);
   ha15__1->SetBinContent(208,797);
   ha15__1->SetBinContent(209,765);
   ha15__1->SetBinContent(210,718);
   ha15__1->SetBinContent(211,668);
   ha15__1->SetBinContent(212,580);
   ha15__1->SetBinContent(213,553);
   ha15__1->SetBinContent(214,490);
   ha15__1->SetBinContent(215,426);
   ha15__1->SetBinContent(216,432);
   ha15__1->SetBinContent(217,386);
   ha15__1->SetBinContent(218,346);
   ha15__1->SetBinContent(219,319);
   ha15__1->SetBinContent(220,286);
   ha15__1->SetBinContent(221,240);
   ha15__1->SetBinContent(222,214);
   ha15__1->SetBinContent(223,187);
   ha15__1->SetBinContent(224,179);
   ha15__1->SetBinContent(225,162);
   ha15__1->SetBinContent(226,169);
   ha15__1->SetBinContent(227,93);
   ha15__1->SetBinContent(228,104);
   ha15__1->SetBinContent(229,96);
   ha15__1->SetBinContent(230,76);
   ha15__1->SetBinContent(231,83);
   ha15__1->SetBinContent(232,64);
   ha15__1->SetBinContent(233,69);
   ha15__1->SetBinContent(234,58);
   ha15__1->SetBinContent(235,57);
   ha15__1->SetBinContent(236,39);
   ha15__1->SetBinContent(237,29);
   ha15__1->SetBinContent(238,26);
   ha15__1->SetBinContent(239,31);
   ha15__1->SetBinContent(240,24);
   ha15__1->SetBinContent(241,17);
   ha15__1->SetBinContent(242,13);
   ha15__1->SetBinContent(243,16);
   ha15__1->SetBinContent(244,19);
   ha15__1->SetBinContent(245,12);
   ha15__1->SetBinContent(246,7);
   ha15__1->SetBinContent(247,8);
   ha15__1->SetBinContent(248,5);
   ha15__1->SetBinContent(249,7);
   ha15__1->SetBinContent(250,3);
   ha15__1->SetBinContent(251,6);
   ha15__1->SetBinContent(252,5);
   ha15__1->SetBinContent(253,7);
   ha15__1->SetBinContent(254,2);
   ha15__1->SetBinContent(255,6);
   ha15__1->SetBinContent(256,2);
   ha15__1->SetBinContent(257,1);
   ha15__1->SetBinContent(258,3);
   ha15__1->SetBinContent(259,3);
   ha15__1->SetBinContent(261,1);
   ha15__1->SetBinContent(266,2);
   ha15__1->SetBinContent(270,1);
   ha15__1->SetEntries(43415);
   
   TPaveStats *ptstats = new TPaveStats(0.78,0.775,0.98,0.935,"brNDC");
   ptstats->SetName("stats");
   ptstats->SetBorderSize(1);
   ptstats->SetFillColor(0);
   ptstats->SetTextAlign(12);
   ptstats->SetTextFont(42);
   TText *ptstats_LaTex = ptstats->AddText("ha15");
   ptstats_LaTex->SetTextSize(0.0368);
   ptstats_LaTex = ptstats->AddText("Entries = 43415  ");
   ptstats_LaTex = ptstats->AddText("Mean  =  197.6");
   ptstats_LaTex = ptstats->AddText("RMS   =   11.7");
   ptstats->SetOptStat(1111);
   ptstats->SetOptFit(0);
   ptstats->Draw();
   ha15__1->GetListOfFunctions()->Add(ptstats);
   ptstats->SetParent(ha15__1);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   ha15__1->SetLineColor(ci);
   ha15__1->GetXaxis()->SetLabelFont(42);
   ha15__1->GetXaxis()->SetTitleOffset(1);
   ha15__1->GetXaxis()->SetTitleFont(42);
   ha15__1->GetYaxis()->SetLabelFont(42);
   ha15__1->GetYaxis()->SetTitleOffset(1);
   ha15__1->GetYaxis()->SetTitleFont(42);
   ha15__1->GetZaxis()->SetLabelFont(42);
   ha15__1->GetZaxis()->SetTitleOffset(1);
   ha15__1->GetZaxis()->SetTitleFont(42);
   ha15__1->Draw("hist");
   tcanvas1->Modified();
   tcanvas1->cd();
   tcanvas1->SetSelected(tcanvas1);
}
