// greate a work histograms
{
  cout << "----------------------------------------------------------------------" << endl;
  cout << "start filling histograms" << endl;
  cout << "----------------------------------------------------------------------" << endl;
  
  TString ha_name("ha");
  TString ha_title_start("adc ");
  TString ha_title_end(" histogram");
  
  TString ht_name("ht");
  TString ht_title_start("tdc ");
  TString ht_title_end(" histogram");
  
  // number of ADC and TDC channels to be used
  
  const  Int_t n_adc = 16;
  const  Int_t n_tdc = 16;
  
  Int_t n_adc_chan = 4096;
  Int_t n_tdc_chan = 4096;
  
  // create the adc histos
  TH1F* h_adc[n_adc];
  for (Int_t i = 0; i < n_adc; i++){
    TString h_num = TString::Format("%d", i);
    TString h_name = ha_name + h_num;
    TString h_title = ha_title_start + h_num + ha_title_end;
    
    h_adc[i] = new TH1F(h_name, h_title, n_adc_chan, 0., Float_t(n_adc_chan)); 
  }

 // fill the histograms
  for (Int_t i = 0; i < n_adc; i++){
    TString adc_v = TString::Format("adc[%d]",i);
    TCut a_cut = adc_v + "> 0.";
    vme->Project( h_adc[i].GetName(), adc_v, a_cut);
  }

  // create the tdc histos
  TH1F* h_tdc[n_tdc];
  for (Int_t i = 0; i < n_tdc; i++){
    TString h_num = TString::Format("%d", i);
    TString h_name = ht_name + h_num;
    TString h_title = ht_title_start + h_num + ht_title_end;
    
    h_tdc[i] = new TH1F(h_name, h_title, n_tdc_chan, 0., Float_t(n_tdc_chan)); 
  }

 // fill the histograms
  for (Int_t i = 0; i < n_tdc; i++){
    TString tdc_v = TString::Format("tdc[%d]",i);
    TCut t_cut = tdc_v + "> 0.";
    vme->Project( h_tdc[i].GetName(), tdc_v, t_cut);
  }

  cout << "----------------------------------------------------------------------" << endl;
  cout << "histograms are ready " << endl;
  cout << "----------------------------------------------------------------------" << endl;
}

