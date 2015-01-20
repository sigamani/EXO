from ROOT import *
from array import array
from math import fabs, sqrt
import CMS_lumi, tdrstyle

#set the tdr style                                                                                                                                                                                                                             
tdrstyle.setTDRStyle()

def loop(vec,vechist):
    for i in range(len(vec)):
        tree = vec[i].Get("anaTree")
        entr = tree.GetEntries()
        print 'total events ' + str(entr)
        for event in tree:
            for each in event.dxyConv:
                vechist[i].Fill( each )

    return vechist

def function():

    files = ["./v22/GMSB_L180-CTAU10.root","./v22/GMSB_L180-CTAU50.root","./v22/GMSB_L180-CTAU250.root","./v22/GMSB_L180-CTAU500.root"]
    vecfiles = []
    
    for item in files:
        temp = TFile.Open(item)
        vecfiles.append(temp)

    dxy10 = TH1D("Dxy10","",50,-20,20)
    dxy50 = TH1D("Dxy50","",50,-20,20)
    dxy250 = TH1D("Dxy250","",50,-20,20)
    dxy500 = TH1D("Dxy500","",50,-20,20)

    dxy = [dxy10,dxy50,dxy250,dxy500]

    dxy = loop(vecfiles,dxy)

    return dxy

def plot(dxy):
    dxy[0].SetLineWidth(2)
    dxy[1].SetLineWidth(2)
    dxy[2].SetLineWidth(2)
    dxy[3].SetLineWidth(2)
    dxy[0].SetLineColor(kRed)
    dxy[1].SetLineColor(kGreen)
    dxy[2].SetLineColor(kOrange)
    dxy[3].SetLineColor(kBlue)

    leg = TLegend(0.65,0.75,0.89,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.03)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)
    leg.AddEntry(dxy[0], "GMSB (180,10)","l")
    leg.AddEntry(dxy[1], "GMSB (180,50)","l")
    leg.AddEntry(dxy[2], "GMSB (180,250)","l")
    leg.AddEntry(dxy[3], "GMSB (180,500)","l")
    
    
    dxy[0].GetXaxis().SetTitle("Conversion d_{XY} (cm)")
    dxy[0].GetXaxis().SetTitleSize(0.05)
    dxy[0].GetYaxis().SetTitleSize(0.05)
    dxy[0].GetYaxis().SetTitle("Events")

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
    canvas.SetLogy()


    dxy[0].Draw()
    dxy[1].Draw("same")
    dxy[2].Draw("same")
    dxy[3].Draw("same")
    leg.Draw("same")
    
    #draw the lumi text on the canvas 
    CMS_lumi.CMS_lumi(canvas, 2, iPos)

    canvas.cd()
    canvas.Update()
    canvas.RedrawAxis()
    frame = canvas.GetFrame()
    frame.Draw()


    canvas.SaveAs("dxycomparisonsignal.png")
    canvas.Close()

def main():
    dxy = function()
    plot(dxy)

if __name__ == "__main__":
    main()

