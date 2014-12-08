

//
//  last commit by $Id: DPSelection.h,v 1.1 2012/05/30 12:56:26 sigamani Exp $
//
#ifndef DPSelection_h
#define DPSelection_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include "TH1F.h"
#include "TH2F.h"
#include <vector>
#include <string>
#include <map>
#include <iostream>

#include "GMSBTree_V3.h" 



class DPSelection: public GMSBTree_V3 {
public :

   DPSelection(TTree *tree=0);
   virtual ~DPSelection() { };

   virtual void     Loop(int nmaxevents, const char* outname);
   void SetFilename(const char* outname);
   bool HLTFilter();

private:

    char file[100];
    unsigned int originalEvents_;
    unsigned int selectedEvents_;

    std::vector<double> ptPhot;
    std::vector<double> ptPhotUp;
    std::vector<double> ptPhotDown;
    std::vector<double> etaPhot;
    std::vector<double> phiPhot;
    std::vector<double> sMinPhot;
    std::vector<double> sMajPhot;
    std::vector<double> sigmaIetaPhot;
    std::vector<double> aveTimePhot;
    std::vector<double> ptJet;
    std::vector<double> ptJetUp;
    std::vector<double> ptJetDown;
    std::vector<double> dxyConv;
    std::vector<double> dzConv;
    std::vector<double> etaConv;
    std::vector<double> phiConv;
    std::vector<double> deltaRward;
    std::vector<double> ConvChi2;
    std::vector<double> convMatched;
    std::vector<double> phoMatched;
    std::vector<double> phohovere;
    std::vector<double> chadiso;
    std::vector<double> nhadiso;
    std::vector<double> photiso;

};


#endif
