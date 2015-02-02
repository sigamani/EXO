from ROOT import *
from array import array
from math import fabs, sqrt
import CMS_lumi, tdrstyle

#set the tdr style 
tdrstyle.setTDRStyle()

def loop(vec,histo):

    for i in vec:                            
        tree = i.Get("DPAnalysis")
        entr = tree.GetEntries()
        print 'total events ' + str(entr)
        for event in tree:
            if (event.met < 30):
               continue
            if (event.nJets < 2):
               continue
            if (event.nPhotons < 2):
               continue
            if (event.nVertices < 0): 
               continue
            
            if (len(event.convDxy) < 1):
                continue 
            for each in range(len(event.convR)):
                if (event.convChi2[each] > 0.01 and abs(event.convDxy[each]) < 0.3 ):
                    histo.Fill(event.convR[each])    
 
    return histo

def function ():

    listdata = ["../DPAnalysis/test/v24/Run2012A.root","../DPAnalysis/test/v24/Run2012B.root","../DPAnalysis/test/v24/Run2012C_1.root","../DPAnalysis/test/v24/Run2012C_2.root","../DPAnalysis/test/v24/Run2012C_3.root","../DPAnalysis/test/v24/Run2012D_1.root","../DPAnalysis/test/v24/Run2012D_2.root","../DPAnalysis/test/v24/Run2012D_3.root"]
    listMC = ["../DPAnalysis/test/v24/TTJets.root","../DPAnalysis/test/v24/QCD_Pt-80to120.root","../DPAnalysis/test/v24/QCD_Pt-120to170.root","../DPAnalysis/test/v24/QCD_Pt-170to300.root","../DPAnalysis/test/v24/QCD_Pt-470to600.root","../DPAnalysis/test/v24/QCD_Pt-600to800.root","../DPAnalysis/test/v24/QCD_Pt-800to1000.root","../DPAnalysis/test/v24/QCD_Pt-1000to1400.root","../DPAnalysis/test/v24/G_Pt-50to80.root","../DPAnalysis/test/v24/G_Pt-80to120.root","../DPAnalysis/test/v24/G_Pt-120to170.root","../DPAnalysis/test/v24/G_Pt-170to300.root","../DPAnalysis/test/v24/G_Pt-300to470.root","../DPAnalysis/test/v24/G_Pt-470to800.root"]
    
    vecfiles = []
    for item in listdata:
        temp = TFile.Open(item)
        vecfiles.append(temp)

    vecfilesMC = []
    for item in listMC:
        temp = TFile.Open(item)
        vecfilesMC.append(temp)

    convrdata = TH1D("ConvRdata","",50,0,100)
    convrMC = TH1D("ConvRMC","",50,0,100)

    convrdata.Sumw2()
    convrMC.Sumw2()

    convrdata = loop(vecfiles, convrdata)
    convrMC = loop(vecfilesMC,convrMC)

    convrMC.Scale(convrdata.Integral()/convrMC.Integral())

    output = TFile.Open("convRbkgMCstep1.root","recreate")

    convrdata.Write()
    convrMC.Write()
    
    output.Close()

    return [convrdata,convrMC]

def main():

    ding = function()
    data = ding[0]
    MC = ding[1]

    data.SetMarkerColor(1)
    data.SetLineColor(1)
    data.SetMarkerStyle(8)
    MC.SetMarkerColor(2)
    MC.SetLineColor(2)
    MC.SetMarkerStyle(8)
    
    
    leg = TLegend(0.55,0.75,0.94,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.038)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)

    leg.AddEntry(data, "Data","p")
    leg.AddEntry(MC, "MC background", "p")

    data.GetYaxis().SetRangeUser(0.,800)
    data.GetYaxis().SetTitleSize(0.05)
    data.GetYaxis().SetTitleOffset(1.2)
    data.GetYaxis().SetTitle("Events")
    data.GetXaxis().SetTitle("Conversion radius (cm)")
    data.GetXaxis().SetTitleSize(0.05)
    data.GetXaxis().SetTitleOffset(1.)

    gStyle.SetOptStat(0)

    #change the CMS_lumi variables (see CMS_lumi.py)

    CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
    CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
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

    canvas1 = TCanvas("c2","c2",50,50,W,H)
    canvas1.SetFillColor(0)
    canvas1.SetBorderMode(0)
    canvas1.SetFrameFillStyle(0)
    canvas1.SetFrameBorderMode(0)
    canvas1.SetLeftMargin( L/W )
    canvas1.SetRightMargin( R/W )
    canvas1.SetTopMargin( T/H )
    canvas1.SetBottomMargin( B/H )
    canvas1.SetTickx(0)
    canvas1.SetTicky(0)
    #canvas1.SetLogy()

    n = MC.GetNbinsX()
    x = array('d',[])
    y = array('d',[])
    ex = array('d',[])
    ey = array('d',[])

    for km in range(n):
        x.append(float(MC.GetBinCenter(km+1)))
        y.append(float(MC.GetBinContent(km+1)))
        ex.append(float(MC.GetBinWidth(km+1)/2))
        ey.append(float(MC.GetBinError(km+1)))

    errhist = TGraphErrors(n,x,y,ex,ey)
    errhist.SetFillColor(2)
    errhist.SetLineWidth(3)
    errhist.SetFillStyle(3005)

    data.Draw("PE")
    MC.Draw("HISTsame")
    leg.Draw("same")
    errhist.Draw("2 sames")

    CMS_lumi.extraText = ""
    #draw the lumi text on the canvas

    CMS_lumi.CMS_lumi(canvas1, 2, iPos)

    canvas1.cd()
    canvas1.Update()
    canvas1.RedrawAxis()
    frame = canvas1.GetFrame()
    frame.Draw()

    canvas1.SaveAs("./convRbkgMCstep1.png")

if __name__ == "__main__":
    main()
