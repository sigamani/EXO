//
// last commit by $Id: analysis.cc,v 1.1 2011/06/03 14:19:02 sigamani Exp $
//
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
 
#include <TTree.h>
#include <TChain.h>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2.h>
#include <TH1F.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TVector2.h>
#include <TVector3.h>
#include <TAxis.h>
 
#include "DPSelection.cc"
 
using namespace std;
 
void help(int argc, char* argv[]) {
  cout << "usage: \n"
       << "\t<required var>: required arguments\n"
       << "\t[optional]    : optional argument\n"
       << "analysis <listfile>  <outputdir> [nevents]" << endl;
       exit(0);
}
 
int main(int argc, char* argv[]) {
 
     //================ Parameters
     if( argc <3  ) help(argc,argv);
 
      // Input list
      char listName[500];
      sprintf(listName,argv[1]);
 
      // Set .root filename
      char filename[100];
      sprintf(filename,"%s",argv[2]);
 
      // nevents
      int nevents = 1000000000;
      if(argc >= 4 ) {  // specify nevents
         nevents = atoi( argv[3] );  
         cout << "Processing only " << nevents << " events." << endl;
      }
 
      // Name of input tree objects in (.root) files
      char treeName[100] = "DPAnalysis";
 
 
      //================ Creating chain
      TChain *chain = new TChain(treeName);
      char pName[500];
      ifstream is(listName);
      if(! is.good()) {
         cout << "int main() >> ERROR : file " << listName << " not read" << endl;
         is.close();
         exit(-1);
      }
      cout << "Reading list : " << listName << " ......." << endl;

      cout << "Adding following files to the chain"  << endl;
      int nfiles(0);
      while( is.getline(pName, 500, '\n') ) {
         if (pName[0] == '#') continue;
           chain->Add(pName);
           nfiles++;
           cout << "\t" << pName << endl;
      }
      cout << "Number of files: " << nfiles << endl;
         
       //================ Run analysis
       DPSelection tree( chain );
       tree.SetFilename(filename);
       tree.Loop(nevents, filename);
 
       return 0;
}
