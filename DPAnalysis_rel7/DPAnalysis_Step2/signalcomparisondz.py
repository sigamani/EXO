from ROOT import *
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
        headlabel.AddText("CMS = 15.3 fb^{-1}")
    if (quadrant == 2):
        headlabel.AddText("#sqrt{s} = 8 TeV")

    headlabel.SetFillColor(kWhite)
    headlabel.SetTextSize(0.04)
    headlabel.SetTextFont(42)
    headlabel.SetBorderSize(0)
    headlabel.SetShadowColor(kWhite)

    return headlabel

def loop(vec,vechist):
    for i in range(len(vec)):
        tree = vec[i].Get("anaTree")
        entr = tree.GetEntries()
        print 'total events ' + str(entr)
        for event in tree:
            lum = 1. #!!!!!!!!!!!!!!!! doet er toch niet toe
            for each in event.dzPhot:
                vechist[i].Fill( each )

    return vechist

def function():

    files = ["./v18/GMSB_L180-CTAU10.root","./v18/GMSB_L180-CTAU50.root","./v18/GMSB_L180-CTAU250.root","./v18/GMSB_L180-CTAU500.root"]
    vecfiles = []
    
    for item in files:
        temp = TFile.Open(item)
        vecfiles.append(temp)

    dxy10 = TH1D("Dxy10","",50,-150,150)
    dxy50 = TH1D("Dxy50","",50,-150,150)
    dxy250 = TH1D("Dxy250","",50,-150,150)
    dxy500 = TH1D("Dxy500","",50,-150,150)

    dxy = [dxy10,dxy50,dxy250,dxy500]

    dxy = loop(vecfiles,dxy)

    return dxy

def plot(dxy,cmslabel,sqrtlabel):
    dxy[0].SetLineWidth(2)
    dxy[1].SetLineWidth(2)
    dxy[2].SetLineWidth(2)
    dxy[3].SetLineWidth(2)
    dxy[0].SetLineColor(kRed)
    dxy[1].SetLineColor(kGreen)
    dxy[2].SetLineColor(kOrange)
    dxy[3].SetLineColor(kBlue)

    c1 = TCanvas("c1","c1",600,500)
    c1.SetLogy()
    leg = TLegend(0.65,0.75,0.89,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.03)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)
    leg.AddEntry(dxy[0], "GMSB (180,10)","l")
    leg.AddEntry(dxy[1], "GMSB (180,50)","l")
    leg.AddEntry(dxy[2], "GMSB (180,250)","l")
    leg.AddEntry(dxy[3], "GMSB (180,500)","l")
    
    
    dxy[0].GetXaxis().SetTitle("d_{Z}")
    dxy[0].GetYaxis().SetTitle("Events")

    dxy[0].Draw()
    dxy[1].Draw("same")
    dxy[2].Draw("same")
    dxy[3].Draw("same")
    cmslabel.Draw("same")
    sqrtlabel.Draw("same")
    leg.Draw("same")
    
    c1.SaveAs("dzcomparisonsignal.png")
    c1.Close()

def main():
    dxy = function()
    cmslabel = label(1)
    sqrtlabel = label(2)
    plot(dxy,cmslabel,sqrtlabel)

if __name__ == "__main__":
    main()

