
from ROOT import *
from array import array
from math import fabs, sqrt
from tdrStyle import *

setTDRStyle()

def label(quadrant):
    if (quadrant!=1 and quadrant !=2):
        print "This quadrant is not defined, choose a value of 1 or 2!"
    else:
        if (quadrant == 1):
            x1 = 0.1
            x2 = 0.28
            y1 = 0.95
            y2 = 1.0
        if (quadrant == 2):
            x1 = 0.75
            x2 = 0.93
            y1 = 0.95
            y2 = 1.0
            
    headlabel = TPaveText( x1, y1, x2, y2, "brNDC" )
    if (quadrant == 1):
        headlabel.AddText("CMS = 6.58 fb^{-1}")
    if (quadrant == 2):
        headlabel.AddText("#sqrt{s} = 8 TeV")

    headlabel.SetFillColor(kWhite)
    headlabel.SetTextSize(0.04)
    headlabel.SetTextFont(42)
    headlabel.SetBorderSize(0)
    headlabel.SetShadowColor(kWhite)
    
    return headlabel


def loop(vec,vechisto,flag):
    for i in vec:
        tree = i.Get("anaTree")
        entr = tree.GetEntries()
        print 'total events ' + str(entr)
        for event in tree:
            if(flag == 0):
                lum = 6578.
                if(event.dxyPhot.size() > 0):
                    vechisto.Fill(event.dxyPhot[0],(event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
            else:
                if(event.dxyPhot.size() > 0):
                    vechisto.Fill(event.dxyPhot[0], 1./event.EfficiencyScaleFactors )

    return vechisto


def function(lamb,ctau):
    listhigh = ["./v18/Run2012Cfakehigh.root"]
    listlow = ["./v18/Run2012Cfakelow.root"]

    vecfileshigh = []
    for item in listhigh:
        temp = TFile.Open(item)
        vecfileshigh.append(temp)
    vecfileslow = []
    for item in listlow:
        temp = TFile.Open(item)
        vecfileslow.append(temp)

    dxyhigh = TH1D("dXYhigh","",50,0,2.5)
    dxylow = TH1D("dXYlow","",50,0,2.5)

    dxyhigh = loop(vecfileshigh,dxyhigh,1)
    dxylow = loop(vecfileslow,dxylow,1)

    dxyhigh.SetBinContent(50,dxyhigh.GetBinContent(51))
    dxylow.SetBinContent(50,dxylow.GetBinContent(51))
    ratio = dxyhigh.Integral()/dxylow.Integral()
    dxylow.Scale(ratio)

    dxy = [dxyhigh,dxylow]

    return dxy

def plot(dxy,cmslabel,sqrtlabel):
    dxy[0].SetLineWidth(2)
    dxy[1].SetMarkerStyle(20)
    dxy[1].SetMarkerSize(0.8)
    dxy[1].SetMarkerColor(kRed)

    c1 = TCanvas("c1","c1",600,500)
    c1.SetLogy()
    leg = TLegend(0.65,0.75,0.89,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.03)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)
    leg.AddEntry(dxy[0], "Fake, E^{miss}_{T} > 30 GeV","l")
    leg.AddEntry(dxy[1], "Fake, E^{miss}_{T} < 20 GeV","pe")

    dxy[1].GetXaxis().SetTitle("d_{XY}")
    dxy[1].GetYaxis().SetTitle("Events")
    dxy[1].GetXaxis().SetTitleSize(0.05)
    dxy[1].GetYaxis().SetTitleSize(0.05)
    
    dxy[1].Draw("PE")
    dxy[0].Draw("same")
    cmslabel.Draw("same")
    sqrtlabel.Draw("same")
    leg.Draw("same")

    c1.SaveAs("dxycomparisonfakehighfakelow.png")
    c1.Close()
    
def main():
    dxy = function("180","500")
    cmslabel = label(1)
    sqrtlabel = label(2)
    plot(dxy,cmslabel,sqrtlabel)

if __name__ == "__main__":
    main()
