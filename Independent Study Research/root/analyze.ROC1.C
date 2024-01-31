//
// analyze a coda file : before running this you need to create a 
//                       TCodafile object named C and open a file
//

/* Register Masks for the TDC */
#ifndef SETUP
#define SETUP

#define C775_BITSET1_MASK   0x0098
#define C775_INTLEVEL_MASK  0x0007
#define C775_INTVECTOR_MASK 0x00ff
#define C775_STATUS1_MASK   0x01ff
#define C775_CONTROL1_MASK  0x0034
#define C775_STATUS2_MASK   0x00f6
#define C775_BITSET2_MASK   0x7fff
#define C775_EVTRIGGER_MASK 0x001f
#define C775_FSR_MASK       0x00ff

#define C775_DATA_ID_MASK    0x07000000
#define C775_WORDCOUNT_MASK  0x00003f00
#define C775_CHANNEL_MASK    0x003f0000
#define C775_CRATE_MASK      0x00ff0000
#define C775_EVENTCOUNT_MASK 0x00ffffff
#define C775_GEO_ADDR_MASK   0xf8000000
#define C775_TDC_DATA_MASK   0x00000fff

/* Register Masks */
#define C792_BITSET1_MASK   0x0098
#define C792_INTLEVEL_MASK  0x0007
#define C792_INTVECTOR_MASK 0x00ff
#define C792_STATUS1_MASK   0x01ff
#define C792_CONTROL1_MASK  0x0034
#define C792_STATUS2_MASK   0x00f6
#define C792_BITSET2_MASK   0x7fff
#define C792_EVTRIGGER_MASK 0x001f

#define C792_DATA_ID_MASK    0x07000000
#define C792_WORDCOUNT_MASK  0x00003f00
#define C792_CHANNEL_MASK    0x003f0000
#define C792_CRATE_MASK      0x00ff0000
#define C792_EVENTCOUNT_MASK 0x00ffffff
#define C792_GEO_ADDR_MASK   0xf8000000
#define C792_ADC_DATA_MASK   0x00000fff



// define TDC codes
#define TDC0 7750000
#define QDC0 7920000

#endif

{

  Int_t iret;

  Int_t physics = 1;
  // contains the tdc and adc values

  const Int_t max_channels=32;

  Float_t tdc[max_channels];
  Float_t adc[max_channels];

  TTree *vme = new TTree("vme", "vme read out");

  // add the branches
  TString tdc_type = TString::Format("tdc[%d]/F", max_channels);
  TString adc_type = TString::Format("adc[%d]/F", max_channels);
  vme->Branch("tdc", tdc, tdc_type);
  vme->Branch("adc", adc, adc_type);

  // create a Codafile Object
  TCodafile *C = new TCodafile(); // create the object
  C->OpenFile("codafile.ROC1");       // open the file

  Int_t EV_nwords;

  Int_t TDC_nwords;
  UInt_t TDC_header;
  UInt_t TDC_data;
  UInt_t TDC_trailer;

  Int_t i_dataword;

  UInt_t tdc_channel;
  UInt_t tdc_value;

  Int_t QDC_nwords;
  UInt_t QDC_header;
  UInt_t QDC_data;
  UInt_t QDC_trailer;

  UInt_t qdc_channel;
  UInt_t qdc_value;

  
  Int_t nev = 0;
  Int_t TDC_0;
  
  Bool_t skip_event;
  Int_t n_skip = 0;

  // look at a few events
  while( ! C->GetEvent() ){

    nev++;

    // clear tdc/adc arrays
    memset(tdc, 0, sizeof(tdc));
    memset(adc, 0, sizeof(adc));

    if (C->GetTag() == physics){
      skip_event = kFALSE;
      // loop over event  content
      for (Int_t k=1; k <= C->GetLength(); k++){
	
	if (C->GetWord(k) == TDC0) {
	  // 775 tdc words found
	  i_dataword = k+1;
	  TDC_header = C->GetWord(i_dataword);
	  TDC_nwords = (TDC_header & C775_WORDCOUNT_MASK)>>8;
	  // cout << TDC_nwords << " TDC values found" << endl;
	  // read all the values
	  for (Int_t j = 0; j<TDC_nwords; j++){
	    i_dataword++;
	    TDC_data = (UInt_t)C->GetWord(i_dataword);
	    tdc_channel = (UInt_t)((TDC_data & C775_CHANNEL_MASK)>>16);
	    tdc_value = (UInt_t) (TDC_data & C775_TDC_DATA_MASK);
	    // store  TDC value in the arrays for the root Tree
	    if (tdc_channel >= max_channels){
	      cout << "Invalid TDC channel = " << tdc_channel << "  max = " << max_channels << endl;
	      skip_event = kTRUE;
	    }
	    else
	      tdc[tdc_channel] = tdc_value;
	  }
	  // advance loop counter as these words have been dealt with
	  k = i_dataword;
	}
	if (C->GetWord(k) == QDC0) {
	  // 775 tdc words found
	  i_dataword = k+1;
	  QDC_header = C->GetWord(i_dataword);
	  QDC_nwords = (QDC_header & C792_WORDCOUNT_MASK)>>8;
	  // cout << QDC_nwords << " QDC values found" << endl;
	  // read all the values
	  for (Int_t j = 0; j<QDC_nwords; j++){
	    i_dataword++;
	    QDC_data = (UInt_t)C->GetWord(i_dataword);
	    qdc_channel = (UInt_t)((QDC_data & C792_CHANNEL_MASK)>>16);
	    qdc_value = (UInt_t) (QDC_data & C792_ADC_DATA_MASK);
	    if (qdc_channel >= max_channels){
	      cout << "Invalid ADC channel = " << qdc_channel << "  max = " << max_channels << endl;
	      skip_event = kTRUE;
	    }
	    else
	      adc[qdc_channel] = qdc_value;
	  }
	  // advance loop counter as these words have been dealt with
	  k = i_dataword;
	}
      }
      if (! skip_event )
	vme->Fill();
      else
	n_skip++;
    }
    if (nev%1000 == 0) {
      cout << "event : " << nev << endl;
    }
  }
  cout << "----------------------------------------------------------------------" << endl;
  cout << "analyzed " << nev <<  " physics events, skipped " << n_skip << endl ;
  cout << "----------------------------------------------------------------------" << endl;
}


