from ROOT import *
from array import array
from math import fabs, sqrt
import CMS_lumi, tdrstyle

#set the tdr style
tdrstyle.setTDRStyle()

def loop(vec,vechisto,flag):
    for i in vec:
        tree = i.Get("anaTree")
        entr = tree.GetEntries()
        print 'total events ' + str(entr)
        for event in tree:
            if (event.nPhot < 2):
                continue
            if (event.nJet < 2):
                continue
            if(flag == 0):
                lum = 19300.
                for i in range(len(event.dxyConv)):
                    vechisto.Fill(abs(event.dxyConv[i]),(event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
            else:
                for i in range(len(event.dxyConv)):
                    vechisto.Fill(abs(event.dxyConv[i]), 1./event.EfficiencyScaleFactors )

    return vechisto


def function():
    listgjet = ["./v21/G_Pt-50to80loose.root","./v21/G_Pt-80to120loose.root","./v21/G_Pt-120to170loose.root","./v21/G_Pt-170to300loose.root","./v21/G_Pt-300to470loose.root","./v21/G_Pt-470to800loose.root"]
    listgjetlowmet = ["./v21/G_Pt-50to80_lowmet.root","./v21/G_Pt-80to120_lowmet.root","./v21/G_Pt-120to170_lowmet.root","./v21/G_Pt-170to300_lowmet.root","./v21/G_Pt-300to470_lowmet.root","./v21/G_Pt-470to800_lowmet.root"]

    vecfilesgjet = []
    for item in listgjet:
        temp = TFile.Open(item)
        vecfilesgjet.append(temp)
    vecfilesgjetlowmet = []
    for item in listgjetlowmet:
        temp = TFile.Open(item)
        vecfilesgjetlowmet.append(temp)

    #xbins = array('d',[0.,0.1,0.2,0.6,2.5])
    #xbins = array('d',[0.,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,2.5])
    xbins = array('d',[0.,0.3, 1., 3., 6.])

    dxygjet = TH1D("dXYgjet","",4,xbins)
    dxygjetlowmet = TH1D("dXYgjetlowmet","",4,xbins)
    #dxygjet = TH1D("dXYgjet","",25,0,2.5)
    #dxygjetlowmet = TH1D("dXYgjetlowmet","",25,0,2.5)
    dxygjet.Sumw2()
    dxygjetlowmet.Sumw2()

    dxygjet = loop(vecfilesgjet,dxygjet,0)
    dxygjetlowmet = loop(vecfilesgjetlowmet,dxygjetlowmet,0)

    dxygjet.SetBinContent(50,dxygjet.GetBinContent(51))
    dxygjetlowmet.SetBinContent(50,dxygjetlowmet.GetBinContent(51))

    #ratiogjet = dxyiso.GetBinContent(1)/dxygjet.GetBinContent(1)
    ratiogjetlowmet = dxygjet.GetBinContent(1)/dxygjetlowmet.GetBinContent(1)
    
    dxygjetlowmet.Scale(ratiogjetlowmet)
    
    dxy = [dxygjet,dxygjetlowmet]

    return dxy

def plot(dxy):
 
    dxy[1].SetFillStyle(3001)
    dxy[0].SetLineWidth(2)
    dxy[0].SetLineColor(kRed)
    dxy[1].SetFillColor(kOrange)
    dxy[0].SetMarkerColor(kRed)

    n = dxy[1].GetNbinsX()
    x = array('d',[])
    y = array('d',[])
    ex = array('d',[])
    ey = array('d',[])

    for km in range(n):
        conte = dxy[1].GetBinError(km)
        x.append(float(dxy[1].GetBinCenter(km)))
        y.append(float(dxy[1].GetBinContent(km)))
        ex.append(float(dxy[1].GetBinWidth(km)/2))
        ey.append(float(conte))

    errhist = TGraphErrors(n,x,y,ex,ey,)
    errhist.SetFillColor(1)
    errhist.SetLineWidth(3)
    errhist.SetFillStyle(3005)

    dxy[1].GetXaxis().SetTitle("Conversion d_{XY} (cm)")
    dxy[1].GetYaxis().SetTitle("Events")
    dxy[1].GetYaxis().SetRangeUser(1,15)
    dxy[1].GetYaxis().SetTitleSize(0.06)
    dxy[1].GetXaxis().SetTitleSize(0.06)

    leg = TLegend(0.55,0.75,0.89,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.03)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)
    leg.AddEntry(dxy[1], "#gamma + jets (CR 1 Selection)","f")
    leg.AddEntry(dxy[0], "#gamma + jets (Signal Region Selection)","l")


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

    dxy[1].Draw("HIST")
    dxy[0].Draw("EsameHIST")
    errhist.Draw("2 sames")
    leg.Draw("same")  

    #draw the lumi text on the canvas
    CMS_lumi.CMS_lumi(canvas, 2, iPos)

    canvas.cd()
    canvas.Update()
    canvas.RedrawAxis()
    frame = canvas.GetFrame()
    frame.Draw()

    canvas.SaveAs("dxycomparisongjet.png")
    #canvas.Close()
    
def main():
    dxy = function()
    plot(dxy)
   
if __name__ == "__main__":
    main()
