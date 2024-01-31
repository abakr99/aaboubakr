

{

  // create a Codafile Object
    

  gROOT->Reset();

  gROOT->LoadMacro("root/save_adc.C");

  TCodafile *C = new TCodafile(); // create the object

  bar_c = new TControlBar("vertical", "Analysis Control");

  bar_c->AddButton("analyze new codafile adc only",".x ./root/analyze.ROC1_adc.C", "analyze codafile.dat");
  bar_c->AddButton("analyze new codafile",".x ./root/analyze.ROC1.C", "analyze codafile.dat");
  bar_c->AddButton("make histograms",".x ./root/make_histo.ROC1.C", "create histograms");
  bar_c->AddButton("QUIT",".x ./root/quit.C", "Quit Root");

  bar_d = new TControlBar("vertical", "Display Control");


  Int_t  n_adc_channels = 16;
  Int_t start_adc_channel = 10;
  for (Int_t i=start_adc_channel; i<n_adc_channels; i++){
    
    TString a_name = TString::Format("         adc%d         ", i);
    TString a_command = TString::Format("ha%d->Draw()",i);
    TString a_comment = TString::Format("ADC channel %d", i);
    bar_d->AddButton(a_name,a_command, a_comment);
  }

  bar_s = new TControlBar("vertical", "Save  Control");

  for (Int_t i=start_adc_channel; i<n_adc_channels; i++){
    
    TString a_name = TString::Format(" save  adc%d    ", i);
    TString a_command = TString::Format("save_adc(%d, ha%d)",i,i);
    TString a_comment = TString::Format("ADC channel %d", i);
    bar_s->AddButton(a_name,a_command, a_comment);
  }

  

  Int_t  n_tdc_channels = 16;
  Int_t start_tdc_channel = 10;
  for (Int_t i=start_tdc_channel; i<n_tdc_channels; i++){
    TString t_name = TString::Format("   tdc%d    ", i);
    TString t_command = TString::Format("ht%d->Draw()",i);
    TString t_comment = TString::Format("TDC channel %d", i);
    bar_d->AddButton(t_name,t_command, t_comment);
    
  }



  bar_c->Show();
  bar_d->Show();
  bar_s->Show();

  gROOT->SaveContext();

}
