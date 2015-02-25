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

            dxytemp = []

            for i in range(len(event.dxyConv)):
                if (event.ConvChi2[i] > 0.01):
                    dxytemp.append(fabs(event.dxyConv[i]))
            dxytemp = sorted(dxytemp)

            #if (event.Rsqrd < 0.035):
            #    continue
            if (event.nPhot < 2):
                continue
            if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                continue
            if (event.ptJet[0] < 30): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                continue
            if (event.sigmaIetaPhot[0] > 0.012):
                continue
            if (event.ptPhot[0] < 85):
                continue
            #if (event.sMajPhot[0] > 1.35):
            #    continue

            #fakehigh
            if(flag == 0):
                if(event.MET < 60):
                    continue
                if (event.ptJet[0] < 35): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    continue
                if(len(dxytemp) > 0):
                    vechisto.Fill( dxytemp[-1], 1./event.EfficiencyScaleFactors )
            #fakelow
            if(flag == 1):
                if(len(dxytemp) > 0):
                    vechisto.Fill( dxytemp[-1], 1./event.EfficiencyScaleFactors )
            #isolow
            if(flag == 2):
                if (event.ptJet[0] < 35): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    continue
                if(len(dxytemp) > 0):
                    vechisto.Fill( dxytemp[-1], 1./event.EfficiencyScaleFactors )

    return vechisto


def function():
    listhigh = ["./v24/Run2012Afakehigh.root","./v24/Run2012B_1fakehigh.root","./v24/Run2012B_2fakehigh.root","./v24/Run2012B_3fakehigh.root","./v24/Run2012B_4fakehigh.root","./v24/Run2012C_1fakehigh.root","./v24/Run2012C_2fakehigh.root","./v24/Run2012C_3fakehigh.root","./v24/Run2012C_4fakehigh.root","./v24/Run2012C_5fakehigh.root","./v24/Run2012D_1fakehigh.root","./v24/Run2012D_2fakehigh.root","./v24/Run2012D_3fakehigh.root","./v24/Run2012D_4fakehigh.root","./v24/Run2012D_5fakehigh.root"]
    listlow = ["./v24/Run2012Afakelow.root","./v24/Run2012B_1fakelow.root","./v24/Run2012B_2fakelow.root","./v24/Run2012B_3fakelow.root","./v24/Run2012B_4fakelow.root","./v24/Run2012C_1fakelow.root","./v24/Run2012C_2fakelow.root","./v24/Run2012C_3fakelow.root","./v24/Run2012C_4fakelow.root","./v24/Run2012C_5fakelow.root","./v24/Run2012D_1fakelow.root","./v24/Run2012D_2fakelow.root","./v24/Run2012D_3fakelow.root","./v24/Run2012D_4fakelow.root","./v24/Run2012D_5fakelow.root"]
    listiso = ["./v24/Run2012Aisolow.root","./v24/Run2012B_1isolow.root","./v24/Run2012B_2isolow.root","./v24/Run2012B_3isolow.root","./v24/Run2012B_4isolow.root","./v24/Run2012C_1isolow.root","./v24/Run2012C_2isolow.root","./v24/Run2012C_3isolow.root","./v24/Run2012C_4isolow.root","./v24/Run2012C_5isolow.root","./v24/Run2012D_1isolow.root","./v24/Run2012D_2isolow.root","./v24/Run2012D_3isolow.root","./v24/Run2012D_4isolow.root","./v24/Run2012D_5isolow.root"]

    vecfileshigh = []
    for item in listhigh:
        temp = TFile.Open(item)
        vecfileshigh.append(temp)
    vecfileslow = []
    for item in listlow:
        temp = TFile.Open(item)
        vecfileslow.append(temp)
    vecfilesiso = []
    for item in listiso:
        temp = TFile.Open(item)
        vecfilesiso.append(temp)

    #xbins = array('d',[0.,0.3, 1., 3., 6.])
    xbins = array('d',[0., 0.2, 1.5, 3., 6.])
    #xbins = array('d',[0., 0.2, 1.5, 6.])

    #xbins = array('d',[0.,0.1,0.2,0.3,0.4, 0.5, 1., 1.5, 2.,3.,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11])

    nxbins = len(xbins) - 1


    dxyhigh = TH1D("dXYhigh","",nxbins,xbins)
    dxylow = TH1D("dXYlow","",nxbins,xbins)
    dxyiso = TH1D("dXYiso","",nxbins,xbins)

    #dxyhigh = TH1D("dXYhigh","",25,0,2.5)
    #dxylow = TH1D("dXYlow","",25,0,2.5)
    #dxyiso = TH1D("dXYiso","",25,0,2.5)

    dxyhigh = loop(vecfileshigh,dxyhigh,0)
    dxylow = loop(vecfileslow,dxylow,1)
    dxyiso = loop(vecfilesiso,dxyiso,2)
    
    dxyhigh.SetBinContent(dxyhigh.GetNbinsX(),(dxyhigh.GetBinContent(dxyhigh.GetNbinsX())+dxyhigh.GetBinContent(dxyhigh.GetNbinsX()+1)))
    dxylow.SetBinContent(dxylow.GetNbinsX(),(dxylow.GetBinContent(dxylow.GetNbinsX())+dxylow.GetBinContent(dxylow.GetNbinsX()+1)))
    dxyiso.SetBinContent(dxyiso.GetNbinsX(),(dxyiso.GetBinContent(dxyiso.GetNbinsX())+dxyiso.GetBinContent(dxyiso.GetNbinsX()+1)))

    dxyhigh.SetBinError(dxyhigh.GetNbinsX(),(dxyhigh.GetBinError(dxyhigh.GetNbinsX())+dxyhigh.GetBinError(dxyhigh.GetNbinsX()+1)))
    dxylow.SetBinError(dxylow.GetNbinsX(),(dxylow.GetBinError(dxylow.GetNbinsX())+dxylow.GetBinError(dxylow.GetNbinsX()+1)))
    dxyiso.SetBinError(dxyiso.GetNbinsX(),(dxyiso.GetBinError(dxyiso.GetNbinsX())+dxyiso.GetBinError(dxyiso.GetNbinsX()+1)))

    for i in range(nxbins):
        print "fakehigh: bin " + str(i+1) + " : " + str(dxyhigh.GetBinContent(i+1))
        print "fakelow: bin " + str(i+1) + " : " + str(dxylow.GetBinContent(i+1))
        print "iso: bin " + str(i+1) + " : " + str(dxyiso.GetBinContent(i+1))


    """
    ratiolow = dxyhigh.Integral()/dxylow.Integral()
    ratioiso = dxyhigh.Integral()/dxyiso.Integral()
    """

    ratiolow = dxyiso.GetBinContent(1)/dxylow.GetBinContent(1)
    ratiohigh = dxyiso.GetBinContent(1)/dxyhigh.GetBinContent(1)
    
    dxylow.Scale(ratiolow)
    dxyhigh.Scale(ratiohigh)

    dxy = [dxyhigh,dxylow,dxyiso]

    return dxy

def plot(dxy):
    dxy[2].SetFillStyle(3001)
    dxy[0].SetMarkerStyle(22)
    dxy[1].SetMarkerStyle(21)
    dxy[0].SetMarkerColor(kBlack)
    dxy[1].SetMarkerColor(kRed)
    dxy[0].SetMarkerSize(1.5)
    dxy[1].SetMarkerSize(1.5)
    dxy[0].SetLineWidth(2)
    dxy[1].SetLineWidth(2)
    dxy[0].SetLineColor(kBlack)
    dxy[1].SetLineColor(kRed)
    dxy[2].SetFillColor(kOrange)

    print dxy[2].Integral()

    n = dxy[0].GetNbinsX()
    x0 = array('d',[])
    y0 = array('d',[])
    ex0 = array('d',[])
    ey0 = array('d',[])

    x1 = array('d',[])
    y1 = array('d',[])
    ex1 = array('d',[])
    ey1 = array('d',[])

    x2 = array('d',[])
    y2 = array('d',[])
    ex2 = array('d',[])
    ey2 = array('d',[])

    for km in range(n):
        conte0 = sqrt(dxy[0].GetBinContent(km+1))
        conte1 = sqrt(dxy[1].GetBinContent(km+1))
        conte2 = sqrt(dxy[2].GetBinContent(km+1))

        x0.append(float(dxy[0].GetBinCenter(km+1)))
        y0.append(float(dxy[0].GetBinContent(km+1)))
        ex0.append(float(dxy[0].GetBinWidth(km+1)/2))
        ey0.append(float(conte0))

        x1.append(float(dxy[1].GetBinCenter(km+1)))
        y1.append(float(dxy[1].GetBinContent(km+1)))
        ex1.append(float(dxy[1].GetBinWidth(km+1)/2))
        ey1.append(float(conte1))
        
        x2.append(float(dxy[2].GetBinCenter(km+1)))
        y2.append(float(dxy[2].GetBinContent(km+1)))
        ex2.append(float(dxy[2].GetBinWidth(km+1)/2))
        ey2.append(float(conte2))

    errhist0 = TGraphErrors(n,x0,y0,ex0,ey0)
    errhist0.SetFillColor(kBlack)
    errhist0.SetLineWidth(3)
    errhist0.SetFillStyle(3005)

    errhist1 = TGraphErrors(n,x1,y1,ex1,ey1)
    errhist1.SetFillColor(kRed)
    errhist1.SetLineWidth(3)
    errhist1.SetFillStyle(3005)

    errhist2 = TGraphErrors(n,x2,y2,ex2,ey2)
    errhist2.SetFillColor(kBlack)
    errhist2.SetLineWidth(3)
    errhist2.SetFillStyle(3005)
    
    leg = TLegend(0.65,0.75,0.89,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.03)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)
    leg.AddEntry(dxy[2], "Control region 1","f")
    leg.AddEntry(dxy[1], "Control region 2","l")
    leg.AddEntry(dxy[0], "Control region 3","l")

    dxy[1].GetXaxis().SetTitle("Conversion d_{XY} (cm)")
    dxy[1].GetYaxis().SetTitle("Events / bin")
    dxy[1].GetYaxis().SetRangeUser(0.01,1000)
    dxy[1].GetYaxis().SetTitleSize(0.05)
    dxy[1].GetXaxis().SetTitleSize(0.05)

    gStyle.SetOptStat(0)

    #change the CMS_lumi variables (see CMS_lumi.py)

    CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
    CMS_lumi.lumi_8TeV = "19.7 fb^{-1}"
    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = ""

    iPos = 11
    if( iPos==0 ): CMS_lumi.relPosX = 0.12

    H_ref = 600;
    W_ref = 800;
    W = W_ref
    H  = H_ref

    #
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

    dxy[1].Draw("eHIST")
    dxy[0].Draw("eHISTsame")
    dxy[2].Draw("eHISTsame")
    dxy[1].Draw("eHISTsame")
    dxy[0].Draw("eHISTsame")
    leg.Draw("same")
    #errhist0.Draw("2 sames")
    #errhist1.Draw("2 sames")
    errhist2.Draw("2 sames")

    #draw the lumi text on the canvas
    CMS_lumi.CMS_lumi(canvas, 2, iPos)

    canvas.cd()
    canvas.Update()
    canvas.RedrawAxis()
    frame = canvas.GetFrame()
    frame.Draw()
    
    canvas.SaveAs("dxycomparisonfakehighfakelowisolow.png")
    canvas.Close()
    
def main():
    dxy = function()
    plot(dxy)

if __name__ == "__main__":
    main()
