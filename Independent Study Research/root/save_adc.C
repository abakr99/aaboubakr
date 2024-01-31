void save_adc(Int_t i, TH1F *h):
{
  Int_t run_nr;
  cout << "enter current run number:";
  cin >> run_nr;
  TString f_name = TString::Format("adc%d_%d.root",i, run_nr);
  o = new TFile(f_name,"recreate");
  h->Write();
  o->Close();
  cout << f_name << "  saved " <<endl;

}
