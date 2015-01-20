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
        #print 'total events ' + str(entr)
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
            for ding in event.ptPhot:
                nPhot = nPhot + 1
            if (len(dxytemp) < 1):
                continue
            if (dxytemp[-1] < dxy or dxytemp[-1] > (dxy+2)):
                continue
            for ding in event.dxyConv:
                nDxy = nDxy + 1
        
    vecnumber = [nPhot,nDxy]

    print vecnumber
    
    return vecnumber

def function (phot):

    listMC = ["./v24/G_Pt-50to80.root","./v24/G_Pt-80to120.root","./v24/G_Pt-120to170.root","./v24/G_Pt-170to300.root","./v24/G_Pt-300to470.root","./v24/G_Pt-470to800.root", "./v24/QCD_Pt-80to120.root","./v24/QCD_Pt-120to170.root","./v24/QCD_Pt-170to300.root","./v24/QCD_Pt-470to600.root","./v24/QCD_Pt-600to800.root","./v24/QCD_Pt-800to1000.root","./v24/QCD_Pt-1000to1400.root", "./v24/TTJets.root"]
    listdata = ["./v24/Run2012Aisolow20.root","./v24/Run2012Bisolow20.root","./v24/Run2012C_1isolow20.root","./v24/Run2012C_2isolow20.root","./v24/Run2012C_3isolow20.root","./v24/Run2012D_1isolow20.root","./v24/Run2012D_2isolow20.root","./v24/Run2012D_3isolow20.root"]

    vecfilesMC = []
    for item in listMC:
        temp = TFile.Open(item)
        vecfilesMC.append(temp)
    vecfilesdata = []
    for item in listdata:
        temp = TFile.Open(item)
        vecfilesdata.append(temp)

    #arrays of nphot and nconversion for different photpt
    nPhotMC = [None]*13
    nConverMC = [None]*13
    nPhotData = [None]*13
    nConverData = [None]*13

    biglistMC = [None]*13
    biglistData = [None]*13

    biglistMC[0] = loop(vecfilesMC, 0,phot)
    biglistMC[1] = loop(vecfilesMC, 0.5,phot)
    biglistMC[2] = loop(vecfilesMC, 1,phot)
    biglistMC[3] = loop(vecfilesMC, 1.5,phot)
    biglistMC[4] = loop(vecfilesMC, 2,phot)
    biglistMC[5] = loop(vecfilesMC, 2.5,phot)
    biglistMC[6] = loop(vecfilesMC, 3,phot)
    biglistMC[7] = loop(vecfilesMC, 3.5,phot)
    biglistMC[8] = loop(vecfilesMC, 4,phot)
    biglistMC[9] = loop(vecfilesMC, 4.5,phot)
    biglistMC[10] = loop(vecfilesMC, 5,phot)
    biglistMC[11] = loop(vecfilesMC, 5.5,phot)
    biglistMC[12] = loop(vecfilesMC, 6,phot)


    biglistData[0] = loop(vecfilesdata, 0,phot)
    biglistData[1] = loop(vecfilesdata, 0.5,phot)
    biglistData[2] = loop(vecfilesdata, 1,phot)
    biglistData[3] = loop(vecfilesdata, 1.5,phot)
    biglistData[4] = loop(vecfilesdata, 2,phot)
    biglistData[5] = loop(vecfilesdata, 2.5,phot)
    biglistData[6] = loop(vecfilesdata, 3,phot)
    biglistData[7] = loop(vecfilesdata, 3.5,phot)
    biglistData[8] = loop(vecfilesdata, 4,phot)
    biglistData[9] = loop(vecfilesdata, 4.5,phot)
    biglistData[10] = loop(vecfilesdata, 5,phot)
    biglistData[11] = loop(vecfilesdata, 5.5,phot)
    biglistData[12] = loop(vecfilesdata, 6,phot)

    # biglistMC[0] = loop(vecfilesMC, 0,phot)
    # biglistMC[1] = loop(vecfilesMC, 2,phot)
    # biglistMC[2] = loop(vecfilesMC, 4,phot)
    # biglistMC[3] = loop(vecfilesMC, 6,phot)
    # biglistMC[4] = loop(vecfilesMC, 8,phot)
    # biglistMC[5] = loop(vecfilesMC, 10,phot)
    # biglistMC[6] = loop(vecfilesMC, 12,phot)
    # biglistMC[7] = loop(vecfilesMC, 14,phot)
    # biglistMC[8] = loop(vecfilesMC, 16,phot)
    # biglistMC[9] = loop(vecfilesMC, 18,phot)
    # biglistMC[10] = loop(vecfilesMC, 20,phot)
    # biglistMC[11] = loop(vecfilesMC, 22,phot)
    # biglistMC[12] = loop(vecfilesMC, 24,phot)

    
    # biglistData[0] = loop(vecfilesdata, 0,phot)
    # biglistData[1] = loop(vecfilesdata, 2,phot)
    # biglistData[2] = loop(vecfilesdata, 4,phot)
    # biglistData[3] = loop(vecfilesdata, 6,phot)
    # biglistData[4] = loop(vecfilesdata, 8,phot)
    # biglistData[5] = loop(vecfilesdata, 10,phot)
    # biglistData[6] = loop(vecfilesdata, 12,phot)
    # biglistData[7] = loop(vecfilesdata, 14,phot)
    # biglistData[8] = loop(vecfilesdata, 16,phot)
    # biglistData[9] = loop(vecfilesdata, 18,phot)
    # biglistData[10] = loop(vecfilesdata, 20,phot)
    # biglistData[11] = loop(vecfilesdata, 22,phot)
    # biglistData[12] = loop(vecfilesdata, 24,phot)

    for i in range(len(biglistMC)):
        nPhotMC[i] = biglistMC[i][0]
        nConverMC[i] = biglistMC[i][1]

    for i in range(len(biglistData)):
        nPhotData[i] = biglistData[i][0]
        nConverData[i] = biglistData[i][1]

    EfficienciesMC = [None]*13
    ErrorsMC = [None]*13
    EfficienciesData = [None]*13
    ErrorsData = [None]*13

    EfficiencyHistMC = TH1D("EfficienciesMC","",13,0,6)
    EfficiencyHistMC.Sumw2()
    EfficiencyHistMC.SetMarkerSize(0.7)

    EfficiencyHistData = TH1D("EfficienciesData","",13,0,6)
    EfficiencyHistData.Sumw2()
    EfficiencyHistData.SetMarkerSize(0.7)
    
    for i in range(len(nPhotMC)):
        if (nConverMC[i] != 0):
            EfficienciesMC[i] = float(nConverMC[i])/nPhotMC[i]
            ErrorsMC[i] = (float(nConverMC[i])/nPhotMC[i]) * ((1./sqrt(nConverMC[i]))+(1./sqrt(nPhotMC[i])))            
        else:
            EfficienciesMC[i] = 0
            ErrorsMC[i] = 0

        #print Efficiencies[i]
        EfficiencyHistMC.SetBinContent(i+1,EfficienciesMC[i])
        
        EfficiencyHistMC.SetBinError(i+1,ErrorsMC[i])
        
    for i in range(len(nPhotData)):
        if (nConverData[i] != 0):
            EfficienciesData[i] = float(nConverData[i])/nPhotData[i]
            ErrorsData[i] = (float(nConverData[i])/nPhotData[i]) * ((1./sqrt(nConverData[i]))+(1./sqrt(nPhotData[i])))
        else:
            EfficienciesData[i] = 0
            ErrorsData[i] = 0

        #print Efficiencies[i]

        EfficiencyHistData.SetBinContent(i+1,EfficienciesData[i])

        EfficiencyHistData.SetBinError(i+1,ErrorsData[i])

    return EfficiencyHistMC, EfficiencyHistData

def main():
    thing = function(2)
    MC = thing[0]
    data = thing[1]

    MC.SetMarkerColor(1)
    MC.SetLineColor(1)
    MC.SetMarkerStyle(8)
    data.SetMarkerColor(2)
    data.SetLineColor(2)
    data.SetMarkerStyle(8) 
    

    leg = TLegend(0.55,0.70,0.94,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.038)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)

    leg.AddEntry(MC, "MC","p")
    leg.AddEntry(data, "DD bkg","p")
   
    MC.GetYaxis().SetRangeUser(0.0001,0.2)
    MC.GetYaxis().SetTitleSize(0.05)
    MC.GetYaxis().SetTitleOffset(1.2)
    MC.GetYaxis().SetTitle("Efficiency")
    MC.GetXaxis().SetTitle("Conversion d_{XY} (cm)")
    MC.GetXaxis().SetTitleSize(0.05)
    MC.GetXaxis().SetTitleOffset(1.)


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
    #canvas.SetLogy()


    MC.Draw("PE")
    data.Draw("PEsame")
    leg.Draw("same")


    #draw the lumi text on the canvas
    CMS_lumi.CMS_lumi(canvas, 2, iPos)

    canvas.cd()
    canvas.Update()
    canvas.RedrawAxis()
    frame = canvas.GetFrame()
    frame.Draw()
  
    canvas.SaveAs("./dxyefficiencyifodxyL180bkg.png")

if __name__ == "__main__":
    main()

