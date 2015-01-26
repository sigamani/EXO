from ROOT import *
from array import array
from math import fabs, sqrt
import CMS_lumi, tdrstyle

#set the tdr style 
tdrstyle.setTDRStyle()

def loop(vec,histo, phot):

    for i in vec:                            
        tree = i.Get("DPAnalysis")
        #entr = tree.GetEntries()
        #j=0
        #print 'total events ' + str(entr)
        for event in tree:
            if (event.met < 30):
                continue
            if (event.nJets < 2):
                continue
            if (event.nPhotons < 2):
                continue
            if (event.nVertices < 0): 
                continue
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
            if (len(event.convDxy) < 1):
                continue 
            for each in range(len(event.convR)):
                if (event.convChi2[each] > 0.01 and abs(event.convDxy[each]) < 0.3 ):
                    histo.Fill(event.convR[each])
    
    return histo

def function (phot):

    listdata = ["../DPAnalysis/test/v24/Run2012A.root","../DPAnalysis/test/v24/Run2012B.root","../DPAnalysis/test/v24/Run2012C_1.root","../DPAnalysis/test/v24/Run2012C_2.root","../DPAnalysis/test/v24/Run2012C_3.root","../DPAnalysis/test/v24/Run2012D_1.root","../DPAnalysis/test/v24/Run2012D_2.root","../DPAnalysis/test/v24/Run2012D_3.root"]

    
    vecfiles = []
    for item in listdata:
        temp = TFile.Open(item)
        vecfiles.append(temp)
from ROOT import *
from array import array
from math import fabs, sqrt
import CMS_lumi, tdrstyle

#set the tdr style 
tdrstyle.setTDRStyle()

def loop(vec,histo, phot):

    for i in vec:                            
        tree = i.Get("DPAnalysis")
        #entr = tree.GetEntries()
        #j=0
        #print 'total events ' + str(entr)
        for event in tree:
            if (event.met < 30):
                continue
            if (nJet < 2):
                continue
            if (nPhot < 2):
                continue
            if (nGoodVtx < 0): 
                continue
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

def function (phot):

    listdata = ["../DPAnalysis/test/v24/Run2012A.root","../DPAnalysis/test/v24/Run2012B.root","../DPAnalysis/test/v24/Run2012C_1.root","../DPAnalysis/test/v24/Run2012C_2.root","../DPAnalysis/test/v24/Run2012C_3.root","../DPAnalysis/test/v24/Run2012D_1.root","../DPAnalysis/test/v24/Run2012D_2.root","../DPAnalysis/test/v24/Run2012D_3.root"]

    
    vecfiles = []
    for item in listdata:
        temp = TFile.Open(item)
        vecfiles.append(temp)

    convr = TH1D("ConvR","",50,0,100)

    convr.Sumw2()

    convr = loop(vecfiles, convr, phot)
    
    return convr

def main():

    CTAU10 = function(0)
    
    CTAU10.SetMarkerColor(1)
    CTAU10.SetLineColor(1)
    CTAU10.SetMarkerStyle(8)
    
    leg1 = TLegend(0.55,0.75,0.94,0.89)
    leg1.SetFillColor(kWhite)
    leg1.SetTextSize(0.038)
    leg1.SetTextFont(42)
    leg1.SetBorderSize(0)

    leg1.AddEntry(CTAU10[1], "data","")


    CTAU10.GetYaxis().SetRangeUser(0.,30)
    CTAU10.GetYaxis().SetTitleSize(0.05)
    CTAU10.GetYaxis().SetTitleOffset(1.2)
    CTAU10.GetYaxis().SetTitle("Events")
    CTAU10.GetXaxis().SetTitle("Conversion radius (cm)")
    CTAU10.GetXaxis().SetTitleSize(0.05)
    CTAU10.GetXaxis().SetTitleOffset(1.)

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

    n = CTAU10[1].GetNbinsX()
    x = array('d',[])
    y = array('d',[])
    ex = array('d',[])
    ey = array('d',[])

    print CTAU10[1].Integral()

    for km in range(n):
        x.append(float(CTAU10.GetBinCenter(km+1)))
        y.append(float(CTAU10.GetBinContent(km+1)))
        ex.append(float(CTAU10.GetBinWidth(km+1)/2))
        ey.append(float(CTAU10.GetBinError(km+1)))

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


    convr = TH1D("ConvR","",50,0,100)

    convr.Sumw2()

    convr = loop(vecfiles, convr, phot)
    
    return convr

def main():

    CTAU10 = function(0)
    
    CTAU10.SetMarkerColor(1)
    CTAU10.SetLineColor(1)
    CTAU10.SetMarkerStyle(8)
    
    leg1 = TLegend(0.55,0.75,0.94,0.89)
    leg1.SetFillColor(kWhite)
    leg1.SetTextSize(0.038)
    leg1.SetTextFont(42)
    leg1.SetBorderSize(0)

    leg1.AddEntry(CTAU10[1], "data","")


    CTAU10.GetYaxis().SetRangeUser(0.,30)
    CTAU10.GetYaxis().SetTitleSize(0.05)
    CTAU10.GetYaxis().SetTitleOffset(1.2)
    CTAU10.GetYaxis().SetTitle("Events")
    CTAU10.GetXaxis().SetTitle("Conversion radius (cm)")
    CTAU10.GetXaxis().SetTitleSize(0.05)
    CTAU10.GetXaxis().SetTitleOffset(1.)

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

    n = CTAU10[1].GetNbinsX()
    x = array('d',[])
    y = array('d',[])
    ex = array('d',[])
    ey = array('d',[])

    print CTAU10[1].Integral()

    for km in range(n):
        x.append(float(CTAU10.GetBinCenter(km+1)))
        y.append(float(CTAU10.GetBinContent(km+1)))
        ex.append(float(CTAU10.GetBinWidth(km+1)/2))
        ey.append(float(CTAU10.GetBinError(km+1)))

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

