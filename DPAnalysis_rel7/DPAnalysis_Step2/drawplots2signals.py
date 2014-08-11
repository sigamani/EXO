from ROOT import *
from tdrStyle import *

setTDRStyle()

#label function
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
        headlabel.AddText("CMS = 1.375 fb^{-1}")
    if (quadrant == 2):
        headlabel.AddText("#sqrt{s} = 8 TeV")
                    
    headlabel.SetFillColor(kWhite)
    headlabel.SetTextSize(0.04)
    headlabel.SetTextFont(42)
    headlabel.SetBorderSize(0)
    headlabel.SetShadowColor(kWhite)
        
    return headlabel
                
def Draw(text,vec,cmslabel,sqrtlabel):
    vec[1].SetFillColor(kOrange)
    vec[2].SetFillColor(kGreen)
    vec[3].SetFillColor(kBlue)
    vec[4].SetLineColor(kRed)
    vec[4].SetLineWidth(2)
    vec[5].SetLineColor(kViolet)
    vec[5].SetLineWidth(2)
    stack = THStack("stack","")
    stack.Add(vec[3])
    stack.Add(vec[2])
    stack.Add(vec[1])
    vec[0].SetMarkerStyle(20)
    vec[0].SetMarkerSize(0.5)
    vec[0].SetMarkerColor(kBlack)
    ratio = vec[0].Clone()
    ratio.SetMarkerStyle(20)
    ratio.SetMarkerSize(0.5)
    ratio.SetMarkerColor(kBlack)
    total = vec[1].Clone()
    total.Add(vec[2],vec[3])
    ratio.Divide(total)

    c1 = TCanvas("c1","c1",600,500)
    pad1 = TPad("pad1", "pad1",0.01,0.27,0.99,0.99);
    pad1.SetTopMargin(0.1);
    pad1.SetBottomMargin(0.01);
    pad1.SetRightMargin(0.1);
    pad1.SetLogy()
    pad1.Draw()
    pad1.cd()
    leg = TLegend(0.55,0.70,0.89,0.89)
    leg.SetFillColor(kWhite)
    leg.SetTextSize(0.038)
    leg.SetTextFont(42)
    leg.SetBorderSize(0)
    leg.AddEntry(vec[0], "DATA","pe")
    leg.AddEntry(vec[1], "G_Pt","f")
    leg.AddEntry(vec[2], "QCD","f")
    leg.AddEntry(vec[3], "TTJet","f")
    leg.AddEntry(vec[4], "GMSB(180,1)", "l")
    leg.AddEntry(vec[5], "GMSB(180,100)", "l")
    vec[0].Draw("PE")
    vec[0].GetYaxis().SetTitle("Number of Events")
    vec[0].GetYaxis().SetRangeUser(0.001,1000)
    stack.Draw("same")
    vec[4].Draw("same")
    vec[5].Draw("same")
    vec[0].Draw("PEsame")
    leg.Draw("same")
    cmslabel.Draw("same")
    sqrtlabel.Draw("same")
    c1.cd()

    pad2 = TPad("pad2", "pad2",0.01,0.02,0.99,0.26)
    pad2.SetGrid()
    pad2.SetTopMargin(0.01)
    pad2.SetBottomMargin(0.3)
    pad2.SetRightMargin(0.1)
    pad2.Draw()
    pad2.cd()
    ratio.GetYaxis().SetTitle("Data/Bkg.")
    ratio.GetXaxis().SetTitle(text)
    ratio.GetYaxis().SetTitleSize(0.18)
    ratio.GetYaxis().SetTitleOffset(0.38)
    ratio.GetYaxis().SetLabelSize(0.1)
    ratio.GetXaxis().SetTitleSize(0.19)
    ratio.GetXaxis().SetLabelSize(0.12)
    ratio.GetXaxis().SetTitleOffset(0.55)
    ratio.GetYaxis().SetRangeUser(0.,5.)
    ratio.Draw("PE")
    c1.cd()
    
    c1.SaveAs(text+".png")
    c1.Close()

def writeto(veclist):
    all = 0
    preselection = 0
    goodvtx = 0
    met = 0
    nphot  = 0
    ptphot = 0
    njet = 0
    ptjet0 = 0
    ptjet1 = 0
    
    for each in veclist:
        hist = each.Get("Entries")
        tree = each.Get("anaTree")
        for event in tree:
            weight = event.CrossSectionWeight*1375.
        all += hist[1]*weight
        preselection += hist[2]*weight
        goodvtx += hist[3]*weight
        met += hist[4]*weight
        nphot += hist[5]*weight
        ptphot += hist[6]*weight
        njet += hist[7]*weight
        ptjet0 += hist[8]*weight
        ptjet1 += hist[9]*weight

    list = [all,preselection,goodvtx,met,nphot,ptphot,njet,ptjet0,ptjet1]
    return list
    
def function():
    input1 = TFile.Open("./ctau10lambda180/output1.root")
    input2 = TFile.Open("./ctau1000lambda180/output1.root")
    vecdxy = [input1.Get("Dxy"),input1.Get("DxyGPT"),input1.Get("DxyQCD"),input1.Get("DxyTTJet"),input1.Get("DxySignal"),input2.Get("DxySignal")]
    vecphotlead = [input1.Get("PtPhotonleading"),input1.Get("PtPhotonleadingGPT"),input1.Get("PtPhotonleadingQCD"),input1.Get("PtPhotonleadingTTJet"),input1.Get("PtPhotonleadingSignal"),input2.Get("PtPhotonleadingSignal")]
    vecphotsublead = [input1.Get("PtPhotonsubleading"),input1.Get("PtPhotonsubleadingGPT"),input1.Get("PtPhotonsubleadingQCD"),input1.Get("PtPhotonsubleadingTTJet"),input1.Get("PtPhotonsubleadingSignal"),input2.Get("PtPhotonsubleadingSignal")]
    vecjetlead = [input1.Get("PtJetleading"),input1.Get("PtJetleadingGPT"),input1.Get("PtJetleadingQCD"),input1.Get("PtJetleadingTTJet"),input1.Get("PtJetleadingSignal"),input2.Get("PtJetleadingSignal")]
    vecjetsublead = [input1.Get("PtJetsubleading"),input1.Get("PtJetsubleadingGPT"),input1.Get("PtJetsubleadingQCD"),input1.Get("PtJetsubleadingTTJet"),input1.Get("PtJetsubleadingSignal"),input2.Get("PtJetsubleadingSignal")]
    vecmet = [input1.Get("MET"),input1.Get("METGPT"),input1.Get("METQCD"),input1.Get("METTTJet"),input1.Get("METSignal"),input2.Get("METSignal")]
    vecnphot = [input1.Get("nPhot"),input1.Get("nPhotGPT"),input1.Get("nPhotQCD"),input1.Get("nPhotTTJet"),input1.Get("nPhotSignal"),input2.Get("nPhotSignal")]
    vecnjet = [input1.Get("nJets"),input1.Get("nJetsGPT"),input1.Get("nJetsQCD"),input1.Get("nJetsTTJet"),input1.Get("nJetsSignal"),input2.Get("nJetsSignal")]
    vecnvert = [input1.Get("nVert"),input1.Get("nVertGPT"),input1.Get("nVertQCD"),input1.Get("nVertTTJet"),input1.Get("nVertSignal"),input2.Get("nVertSignal")]
    vecsmaj = [input1.Get("sMaj"),input1.Get("sMajGPT"),input1.Get("sMajQCD"),input1.Get("sMajTTJet"),input1.Get("sMajSignal"),input2.Get("sMajSignal")]
    vecsmin = [input1.Get("sMin"),input1.Get("sMinGPT"),input1.Get("sMinQCD"),input1.Get("sMinTTJet"),input1.Get("sMinSignal"),input2.Get("sMinSignal")]
    vecsigmaieta = [input1.Get("SigmaIeta"), input1.Get("SigmaIetaGPT"), input1.Get("SigmaIetaQCD"), input1.Get("SigmaIetaTTJet"),input1.Get("SigmaIetaSignal"), input2.Get("SigmaIetaSignal")]

    cmslabel = label(1)
    sqrtlabel = label(2)

    
    Draw("dXY (cm)",vecdxy,cmslabel,sqrtlabel)
    Draw("MET",vecmet,cmslabel,sqrtlabel)
    Draw("PhotPtleading",vecphotlead,cmslabel,sqrtlabel)
    Draw("PhotPtsubleading",vecphotsublead,cmslabel,sqrtlabel)
    Draw("JetPtleading",vecjetlead,cmslabel,sqrtlabel)
    Draw("JetPtsubleading",vecjetsublead,cmslabel,sqrtlabel)
    Draw("nJet",vecnjet,cmslabel,sqrtlabel)
    Draw("nPhot",vecnphot,cmslabel,sqrtlabel)
    Draw("nVert",vecnvert,cmslabel,sqrtlabel)
    Draw("sMaj",vecsmaj,cmslabel,sqrtlabel)
    Draw("sMin",vecsmin,cmslabel,sqrtlabel)
    Draw("SigmaIeta",vecsigmaieta,cmslabel,sqrtlabel)

     
function()
