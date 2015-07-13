
TH1F* unroll2Dhisto(const TH2F* hin, char* histoname ){


  int M = hin->GetNbinsX();
  int N = hin->GetNbinsY(); 
  int Mxmin = hin->ProjectionX()->GetXaxis()->GetXmin();
  int Mxmax = hin->ProjectionX()->GetXaxis()->GetXmax();
  int Nxmin = hin->ProjectionY()->GetXaxis()->GetXmin();
  int Nxmax = hin->ProjectionY()->GetXaxis()->GetXmax();

 
  TH1F* hout = new TH1F(TString(histoname), TString(histoname), M*N, Mxmin, M*N);

     //     std::cout << "before: "<< hin->Integral() << std::endl;

          for(int i = 1; i<= N*M ; i++){

                      float bin = hin->GetBinContent(i);
                      hout->SetBinContent( i , bin );  
         }

   //       std::cout << "after: "<< hout->Integral() << std::endl;
   return hout;

}
