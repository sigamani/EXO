from ROOT import *
from array import array
from math import fabs, sqrt
import CMS_lumi, tdrstyle

#set the tdr style 
tdrstyle.setTDRStyle()


def loop(vec, dxy, phot):

    nPhot = 0
    nDxy = 0
    
    for i in vec:                            
        tree = i.Get("anaTree")
        entr = tree.GetEntries()
        j=0
        print 'total events ' + str(entr)
        for event in tree:
            dxytemp = []
            for i in range(len(event.dxyConv)):
                if (event.ConvChi2[i] > 0.01):
                    dxytemp.append(fabs(event.dxyConv[i]))
            dxytemp = sorted(dxytemp)

            if (event.ptPhot[0] < 85):
                continue
            if (event.nPhot < phot):
                continue
            if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                continue
            if (event.ptJet[0] < 35):
                continue
            if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
                continue
            if (event.sMajPhot[0] > 1.35):
                continue
            if (len(dxytemp) < 1):
                continue
            if (dxytemp[-1] < dxy or dxytemp[-1] > (dxy+2)):
                continue
            for ding in event.ptPhot:
                nPhot = nPhot + 1
            for ding in event.dxyConv:
                nDxy = nDxy + 1
        
    vecnumber = [nPhot,nDxy]
    
    print vecnumber

    return vecnumber

def function (lamb,ctau,phot):

    listsig = ["./v21/GMSB_L"+lamb+"-CTAU"+ctau+".root"]
    
    vecfilessig = []
    for item in listsig:
        temp = TFile.Open(item)
        vecfilessig.append(temp)

    #arrays of nphot and nconversion for different photpt
    nPhotSig = [None]*6
    nConverSig = [None]*6


    nPhotSig[0] = loop(vecfilessig, 4,phot)[0]
    nPhotSig[1] = loop(vecfilessig, 8,phot)[0]
    nPhotSig[2] = loop(vecfilessig, 12,phot)[0]
    nPhotSig[3] = loop(vecfilessig, 16,phot)[0]
    nPhotSig[4] = loop(vecfilessig, 20,phot)[0]
    nPhotSig[5] = loop(vecfilessig, 24,phot)[0]

    nConverSig[0] = loop(vecfilessig, 4,phot)[1]
    nConverSig[1] = loop(vecfilessig, 8,phot)[1]
    nConverSig[2] = loop(vecfilessig, 12,phot)[1]
    nConverSig[3] = loop(vecfilessig, 16,phot)[1]
    nConverSig[4] = loop(vecfilessig, 20,phot)[1]
    nConverSig[5] = loop(vecfilessig, 24,phot)[1]

    Efficiencies = [None]*6
    EfficiencyHist = TH1D("Efficiencies","",6,0,24)
    EfficiencyHist.SetMarkerStyle(3)
    EfficiencyHist.SetMarkerSize(1.1)
    
    for i in range(len(nPhotSig)):
        #print "nConv: " + str(nConverSig[i]) + " for photpt " + str(50+i*10) + "GeV"
        #print "nPhot: "+ str(nPhotSig[i]) + " for photpt " +str(50+i*10) + "GeV"
        if (nPhotSig[i] == 0):
            Efficiencies[i] = 0
        else:
            Efficiencies[i] = float(nConverSig[i])/nPhotSig[i]
        #print Efficiencies[i]
        EfficiencyHist.SetBinContent(i+1,Efficiencies[i])

    return EfficiencyHist

def main():
    CTAU10 = function("180","10",2)
    CTAU50 = function("180","50",2)
    CTAU250 = function("180","250",2)
    CTAU500 = function("180","500",2)

    # CTAU10 = function("160","10",2)
    # CTAU50 = function("160","50",2)
    # CTAU100 = function("160","100",2)
    # CTAU500 = function("160","500",2)

    CTAU10.SetMarkerColor(1)
    CTAU50.SetMarkerColor(2)
    CTAU250.SetMarkerColor(3)
    #CTAU100.SetMarkerColor(5)
    CTAU500.SetMarkerColor(4)


    leg = TLegend(0.55,0.70,0.94,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.038)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)

    leg.AddEntry(CTAU10, "GMSB(180 TeV, 1 cm)","p")
    leg.AddEntry(CTAU50, "GMSB(180 TeV, 5 cm)","p")
    leg.AddEntry(CTAU250, "GMSB(180 TeV, 25 cm)","p")
    leg.AddEntry(CTAU500, "GMSB(180 TeV, 50 cm)","p")

    # leg.AddEntry(CTAU10, "GMSB(160 GeV, 1 cm)","p")
    # leg.AddEntry(CTAU50, "GMSB(160 GeV, 5 cm)","p")
    # leg.AddEntry(CTAU100, "GMSB(160 GeV, 10 cm)","p")
    # leg.AddEntry(CTAU500, "GMSB(160 GeV, 50 cm)","p")


    CTAU10.GetYaxis().SetRangeUser(0.4,0.9)
    CTAU10.GetYaxis().SetTitleSize(0.05)
    CTAU10.GetYaxis().SetTitleOffset(1.2)
    CTAU10.GetYaxis().SetTitle("Conversion Reconstruction Efficiency")
    CTAU10.GetXaxis().SetTitle("Conversion d_{XY} (cm)")
    CTAU10.GetXaxis().SetTitleSize(0.05)
    CTAU10.GetXaxis().SetTitleOffset(1.)


    gStyle.SetOptStat(0)

    #change the CMS_lumi variables (see CMS_lumi.py)

    CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
    CMS_lumi.lumi_8TeV = "19.3 fb^{-1}"
    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = "Simulation"

    iPos = 11
    if( iPos==0 ): CMS_lumi.relPosX = 0.12

    H_ref = 600;
    W_ref = 800;
    W = W_ref
    H  = H_ref

    # Simple example of macro: plot with CMS name and lumi text
    #  (this script does not pretend to work in all configurations)
    # iPeriod = 1*(0/1 7 TeV) + 2*(0/1 8 TeV)  + 4*(0/1 13 TeV)
    # For instance:
    #               iPeriod = 3 means: 7 TeV + 8 TeV
    #               iPeriod = 7 means: 7 TeV + 8 TeV + 13 TeV
    # references for T, B, L, R

    T = 0.08*H_ref
    B = 0.12*H_ref
    L = 0.12*W_ref
    R = 0.04*W_ref

    canvas = TCanvas("c2","c2",50,50,W,H)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetLeftMargin( L/W )
    canvas.SetRightMargin( R/W )
    canvas.SetTopMargin( T/H )
    canvas.SetBottomMargin( B/H )
    canvas.SetTickx(0)
    canvas.SetTicky(0)


    CTAU10.Draw("P")
    CTAU50.Draw("Psame")
    CTAU250.Draw("Psame")
    #CTAU100.Draw("Psame")
    CTAU500.Draw("Psame")
    leg.Draw("same")


    #draw the lumi text on the canvas
    CMS_lumi.CMS_lumi(canvas, 2, iPos)

    canvas.cd()
    canvas.Update()
    canvas.RedrawAxis()
    frame = canvas.GetFrame()
    frame.Draw()
  
    canvas.SaveAs("./dxyefficiencyL180.png")
    #canvas.SaveAs("./dxyefficiencyL160.png")

if __name__ == "__main__":
    main()

