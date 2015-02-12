
from ROOT import *
from array import array
from math import fabs, sqrt

def function ():
    gStyle.SetOptStat(0)

    binxmet = 0
    binxmetR = 0

    rootfile = TFile.Open("./forMichael.root")
    rootfile.ls()

    #Hmet = TH1D("Hmet","Hmet",40,0,200)
    #HmetR = TH1D("HmetR","HmetR",40,0,200)

    c1 = TCanvas("c1","c1",600,500)
    c1.cd()

    Hmet = gROOT.FindObject('h_met')
   
    for i in range(Hmet.GetNbinsX()):
        if (Hmet.GetBinContent(i) > binxmet):
            binxmet = Hmet.GetBinContent(i)

    Hmet.SetMarkerStyle(20)
    Hmet.SetMarkerSize(0.5)
    Hmet.SetMarkerColor(kRed)
    HmetR = gROOT.FindObject("h_met_R2g0p035")

    for i in range(Hmet.GetNbinsX()):
        if (HmetR.GetBinContent(i) > binxmetR):
            binxmetR = HmetR.GetBinContent(i)
 
    scale = binxmetR/binxmet
    #scale = HmetR.Integral()/Hmet.Integral()

    HmetR.SetMarkerStyle(20)
    HmetR.SetMarkerSize(0.5)
    HmetR.SetMarkerColor(kBlue)
    
    Hmet.Scale(scale)

    Hmet.SetTitle("")
    Hmet.GetXaxis().SetTitle("MET (GeV)")
    Hmet.GetYaxis().SetTitle("A.U.")
    Hmet.GetXaxis().SetRangeUser(0,1000)

    leg = TLegend(0.55,0.70,0.89,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.038)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)
    leg.AddEntry(HmetR,"MET with R^2>0.035","p")
    leg.AddEntry(Hmet,"MET","p")

    c1.SetLogy()

    Hmet.Draw("L")
    HmetR.Draw("Lsame")
    leg.Draw("same")

    c1.SaveAs("razorvariable.png")

    #output = TFile.Open("./ctau"+ctau1+"andctau"+ctau2+"lambda"+lamb+"/output"+str(phot)+".root","recreate")

    #output.Close()


def main():
    function()

if __name__ == "__main__":
    main()

