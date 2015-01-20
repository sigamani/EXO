from ROOT import *
from array import array
from math import fabs, sqrt

def loop(vec, dxy, flag, phot):
  
    for i in vec:
        tree = i.Get("anaTree")
        entr = tree.GetEntries()
        j=0
        print 'total events ' + str(entr)
        for event in tree:
            #if (event.nPhot < phot):
                #continue
            if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                continue
            if (event.ptJet[0] < 35):
                continue
            if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
                continue
            if (event.ptPhot[0] < 85):
                continue
            if (event.sMajPhot[0] > 1.35):
                continue
            
            if(flag == 0):
                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        dxy.Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                    
            if (flag == 1):
                for i in range(len(event.dxyConv)):
                    #if (abs(event.dxyConv[i]) < 0.1 and event.ConvChi2[i] > 0.01):
                    if (abs(event.ConvChi2[i] > 0.01)):
                        dxy.Fill( fabs(event.dxyConv[i]), 1./event.EfficiencyScaleFactors )
                       
            if (flag == 2):
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        dxy.Fill( fabs(event.dxyConv[i]), 1./event.EfficiencyScaleFactors )        
    return dxy

def function (lamb,ctau,phot):

    listttjets = ["./v21_2phot/TTJets.root"]
    listsig = ["./v21_2phot/GMSB_L"+lamb+"-CTAU"+ctau+".root"]
    listdata = ["./v21_2phot/Run2012A.root","./v21_2phot/Run2012B.root","./v21_2phot/Run2012C_1.root","./v21_2phot/Run2012C_2.root","./v21_2phot/Run2012C_3.root","./v21_2phot/Run2012D_1.root","./v21_2phot/Run2012D_2.root","./v21_2phot/Run2012D_3.root"]
    listdataisolow = ["./v21_2phot/Run2012Aisolow.root","./v21_2phot/Run2012Bisolow.root","./v21_2phot/Run2012C_1isolow.root","./v21_2phot/Run2012C_2isolow.root","./v21_2phot/Run2012C_3isolow.root","./v21_2phot/Run2012D_1isolow.root","./v21_2phot/Run2012D_2isolow.root","./v21_2phot/Run2012D_3isolow.root"]
    
    vecfilesttjets = []
    for item in listttjets:
        temp = TFile.Open(item)
        vecfilesttjets.append(temp)
    vecfilesdata = []
    for item in listdata:
        temp = TFile.Open(item)
        vecfilesdata.append(temp)
    vecfilesdataisolow = []
    for item in listdataisolow:
        temp = TFile.Open(item)
        vecfilesdataisolow.append(temp)
    vecfilessig = []
    for item in listsig:
        temp = TFile.Open(item)
        vecfilessig.append(temp)
    

    xbins = array('d',[0.,0.3, 1., 3., 6.])

    ttjet = TH1F("TTJet","",4,xbins)
    ttjet = loop(vecfilesttjets,ttjet,0,phot)

    signal = TH1F("signal","",4,xbins)
    signal = loop(vecfilessig, signal, 0, phot)
    signal_sigmaUp = signal.Clone("signal_sigmaUp")
    signal_sigmaDown = signal.Clone("signal_sigmaDown")

    data_obs = TH1F("data_obs","",4,xbins)
    data_obs = loop(vecfilesdata, data_obs, 1, phot)

    background = TH1F("background","",4,xbins)
    background = loop(vecfilesdataisolow, background, 2, phot)
    background_alphaUp = background.Clone("background_alphaUp")
    background_alphaDown = background.Clone("background_alphaDown")
    
    datatotal = data_obs.GetBinContent(1)
    ttjettotal = ttjet.GetBinContent(1)
    isolowtotal = background.GetBinContent(1)
    newisolowtotal = datatotal - ttjettotal

    if(isolowtotal != 0):
        ratio = newisolowtotal/isolowtotal
    else:
        ratio = 1.
    background.Scale(ratio)

    """
    signal.SetBinContent(1,0.)
    signal.SetBinContent(2,0.)
    signal_sigmaUp.SetBinContent(1,0.)
    signal_sigmaUp.SetBinContent(2,0.)
    signal_sigmaDown.SetBinContent(1,0.)
    signal_sigmaDown.SetBinContent(2,0.)
    data_obs.SetBinContent(1,0.)
    data_obs.SetBinContent(2,0.)
    background.SetBinContent(1,0.)
    background.SetBinContent(2,0.)
    background_alphaUp.SetBinContent(1,0.)
    background_alphaUp.SetBinContent(2,0.)
    background_alphaDown.SetBinContent(1,0.)
    background_alphaDown.SetBinContent(2,0.)
    """
    
    output = TFile.Open("simple-shapes-TH1_2photL"+lamb+"CT"+ctau+".root","recreate")

    ttjet.Write()
    signal.Write()
    signal_sigmaUp.Write()
    signal_sigmaDown.Write()
    data_obs.Write()
    background.Write()
    background_alphaUp.Write()
    background_alphaDown.Write()
    

    output.Close()


def main():
    #function("160","100",1)
    function("180","10",2)
    function("180","50",2)
    function("180","250",2)
    function("180","500",2)

if __name__ == "__main__":
    main()

