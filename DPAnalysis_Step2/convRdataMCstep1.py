from ROOT import *
from array import array
from math import fabs, sqrt
import CMS_lumi, tdrstyle

#set the tdr style 
tdrstyle.setTDRStyle()


def loop(vec,histo, phot):

    for i in vec:                            
        tree = i.Get("anaTree")
        entr = tree.GetEntries()
        j=0
        print 'total events ' + str(entr)
        for event in tree:
            #if (event.ptPhot[0] < 85):
            #    continue
            #if (event.nPhot < phot):
            #    continue
            #if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
            #    continue
            #if (event.ptJet[0] < 35):
            #    continue
            #if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
            #    continue
            if (len(event.dxyConv) < 1):
                continue 
            for each in range(len(event.conversionR)):
                if (event.ConvChi2[each] > 0.01 and abs(event.dxyConv[each]) < 0.3 ):
                    histo.Fill(event.conversionR[each])

    
    return histo

def function (lamb,ctau,phot):

    listsig = ["./v24/GMSB_L"+lamb+"-CTAU"+ctau+".root"]
    listdata = ["../DPAnalysis/test/v24/Run2012A.root","../DPAnalysis/test/v24/Run2012B.root","../DPAnalysis/test/v24/Run2012C_1.root","../DPAnalysis/test/v24/Run2012C_2.root","../DPAnalysis/test/v24/Run2012C_3.root","../DPAnalysis/test/v24/Run2012D_1.root","../DPAnalysis/test/v24/Run2012D_2.root","../DPAnalysis/test/v24/Run2012D_3.root"]

    
    vecfilessig = []
    for item in listsig:
        temp = TFile.Open(item)
        vecfilessig.append(temp)
    vecfiles = []
    for item in listdata:
        temp = TFile.Open(item)
        vecfiles.append(temp)

    convrsig = TH1D("ConvRsig","",50,0,100)
    convr = TH1D("ConvR","",50,0,100)

    convrsig.Sumw2()
    convr.Sumw2()

    convrsig = loop(vecfilessig, convrsig, phot)
    convr = loop(vecfiles, convr, phot)
    
    return [convrsig,convr]

def main():

    CTAU10 = function("160","10",0)
    
    CTAU10[0].SetMarkerColor(2)
    CTAU10[0].SetLineColor(2)
    CTAU10[0].SetMarkerStyle(8)
    CTAU10[1].SetMarkerColor(1)
    CTAU10[1].SetLineColor(1)
    CTAU10[1].SetMarkerStyle(8)

    leg0 = TLegend(0.55,0.75,0.94,0.89)
    leg0.SetFillColor(kWhite)
    leg0.SetTextSize(0.038)
    leg0.SetTextFont(42)
    leg0.SetBorderSize(0)
    
    leg1 = TLegend(0.55,0.75,0.94,0.89)
    leg1.SetFillColor(kWhite)
    leg1.SetTextSize(0.038)
    leg1.SetTextFont(42)
    leg1.SetBorderSize(0)

    leg0.AddEntry(CTAU10[0], "GMSB(160 GeV, 1 cm)","")
    leg1.AddEntry(CTAU10[1], "data","")


    CTAU10[0].GetYaxis().SetRangeUser(0.,1500)
    CTAU10[0].GetYaxis().SetTitleSize(0.05)
    CTAU10[0].GetYaxis().SetTitleOffset(1.2)
    CTAU10[0].GetYaxis().SetTitle("Events")
    CTAU10[0].GetXaxis().SetTitle("Conversion radius (cm)")
    CTAU10[0].GetXaxis().SetTitleSize(0.05)
    CTAU10[0].GetXaxis().SetTitleOffset(1.)

    CTAU10[1].GetYaxis().SetRangeUser(0.,30)
    CTAU10[1].GetYaxis().SetTitleSize(0.05)
    CTAU10[1].GetYaxis().SetTitleOffset(1.2)
    CTAU10[1].GetYaxis().SetTitle("Events")
    CTAU10[1].GetXaxis().SetTitle("Conversion radius (cm)")
    CTAU10[1].GetXaxis().SetTitleSize(0.05)
    CTAU10[1].GetXaxis().SetTitleOffset(1.)

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

    canvas0 = TCanvas("c1","c1",50,50,W,H)
    canvas0.SetFillColor(0)
    canvas0.SetBorderMode(0)
    canvas0.SetFrameFillStyle(0)
    canvas0.SetFrameBorderMode(0)
    canvas0.SetLeftMargin( L/W )
    canvas0.SetRightMargin( R/W )
    canvas0.SetTopMargin( T/H )
    canvas0.SetBottomMargin( B/H )
    canvas0.SetTickx(0)
    canvas0.SetTicky(0)
    #canvas0.SetLogy()

    n = CTAU10[0].GetNbinsX()
    x = array('d',[])
    y = array('d',[])
    ex = array('d',[])
    ey = array('d',[])

    for km in range(n):
        
        x.append(float(CTAU10[0].GetBinCenter(km+1)))
        y.append(float(CTAU10[0].GetBinContent(km+1)))
        ex.append(float(CTAU10[0].GetBinWidth(km+1)/2))
        ey.append(float(CTAU10[0].GetBinError(km+1)))

    errhist = TGraphErrors(n,x,y,ex,ey)
    errhist.SetFillColor(2)
    errhist.SetLineWidth(3)
    errhist.SetFillStyle(3005)

    CTAU10[0].Draw("HIST")
    leg0.Draw("same")
    errhist.Draw("2 sames")

    #draw the lumi text on the canvas                                                                                                                                                                                                          
    CMS_lumi.CMS_lumi(canvas0, 2, iPos)

    canvas0.cd()
    canvas0.Update()
    canvas0.RedrawAxis()
    frame = canvas0.GetFrame()
    frame.Draw()

    canvas0.SaveAs("./convRMC.png")


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

    n = CTAU10[1].GetNbinsX()
    x = array('d',[])
    y = array('d',[])
    ex = array('d',[])
    ey = array('d',[])

    print CTAU10[1].Integral()

    for km in range(n):
        x.append(float(CTAU10[1].GetBinCenter(km+1)))
        y.append(float(CTAU10[1].GetBinContent(km+1)))
        ex.append(float(CTAU10[1].GetBinWidth(km+1)/2))
        ey.append(float(CTAU10[1].GetBinError(km+1)))

    errhist = TGraphErrors(n,x,y,ex,ey)
    errhist.SetFillColor(1)
    errhist.SetLineWidth(3)
    errhist.SetFillStyle(3005)

    CTAU10[1].Draw("HIST")
    leg1.Draw("same")
    errhist.Draw("2 sames")

    CMS_lumi.extraText = ""
    #draw the lumi text on the canvas                                                                                                                                                                                                          
    CMS_lumi.CMS_lumi(canvas1, 2, iPos)

    canvas1.cd()
    canvas1.Update()
    canvas1.RedrawAxis()
    frame = canvas1.GetFrame()
    frame.Draw()

    canvas1.SaveAs("./convRdata.png")

if __name__ == "__main__":
    main()

