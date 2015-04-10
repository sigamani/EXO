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
            dxytemp = []

            for i in range(len(event.dxyConv)):
                if (event.ConvChi2[i] > 0.01):
                    dxytemp.append(fabs(event.dxyConv[i]))
            dxytemp = sorted(dxytemp)

            #if (event.Rsqrd < 0.035):
            #    continue
            if (event.nPhot < phot):
                continue
            if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                continue
            if (event.ptJet[0] < 30): #!!!!!!!!!!!!!!!!!!!!!
                continue
            if (event.sigmaIetaPhot[0] > 0.012):
                continue
            if (event.ptPhot[0] < 85):
                continue
            #if (event.sMajPhot[0] > 1.35):
            #    continue

            #MC
            if(flag == 0):
                lum = 19280.
                if (event.ptJet[0] < 35): #!!!!!!!!!!!!!!!!!!!!!
                    continue
                if(event.MET < 60):
                    continue
                if(len(dxytemp) > 0):
                    #dxy.Fill( dxytemp[-1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                    dxy.Fill( dxytemp[-1], (event.r2ScalingFactor*event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
            #data
            if (flag == 1):
                if (event.ptJet[0] < 35): #!!!!!!!!!!!!!!!!!!!!!
                    continue
                if(event.MET < 60):
                    continue
                if(len(dxytemp) > 0):
                    dxy.Fill( dxytemp[-1], 1./event.EfficiencyScaleFactors)
            #bkg
            if (flag == 2):
                if(len(dxytemp) > 0):
                    dxy.Fill( dxytemp[-1], 1./event.EfficiencyScaleFactors)
    return dxy

def function (lamb,ctau,phot):

    listttjets = ["./v24/TTJets.root"]
    listsig = ["./v24/GMSB_Lambda-"+lamb+"_CTau-"+ctau+".root"]
    listdata = ["./v24/Run2012A.root",
                "./v24/Run2012B_1.root","./v24/Run2012B_2.root","./v24/Run2012B_3.root","./v24/Run2012B_4.root",
                "./v24/Run2012C_1.root","./v24/Run2012C_2.root","./v24/Run2012C_3.root","./v24/Run2012C_4.root","./v24/Run2012C_5.root",
                "./v24/Run2012D_1.root","./v24/Run2012D_2.root","./v24/Run2012D_3.root","./v24/Run2012D_4.root","./v24/Run2012D_5.root"]
    listdataisolow = ["./v24/Run2012Aisolow.root",
                      "./v24/Run2012B_1isolow.root","./v24/Run2012B_2isolow.root","./v24/Run2012B_3isolow.root","./v24/Run2012B_4isolow.root",
                      "./v24/Run2012C_1isolow.root","./v24/Run2012C_2isolow.root","./v24/Run2012C_3isolow.root","./v24/Run2012C_4isolow.root","./v24/Run2012C_5isolow.root",
                      "./v24/Run2012D_1isolow.root","./v24/Run2012D_2isolow.root","./v24/Run2012D_3isolow.root","./v24/Run2012D_4isolow.root","./v24/Run2012D_5isolow.root"]
    listfakehigh = ["./v24/Run2012Afakehigh.root",
                    "./v24/Run2012B_1fakehigh.root","./v24/Run2012B_2fakehigh.root","./v24/Run2012B_3fakehigh.root","./v24/Run2012B_4fakehigh.root",
                    "./v24/Run2012C_1fakehigh.root","./v24/Run2012C_2fakehigh.root","./v24/Run2012C_3fakehigh.root","./v24/Run2012C_4fakehigh.root","./v24/Run2012C_5fakehigh.root",
                    "./v24/Run2012D_1fakehigh.root","./v24/Run2012D_2fakehigh.root","./v24/Run2012D_3fakehigh.root","./v24/Run2012D_4fakehigh.root","./v24/Run2012D_5fakehigh.root"]
    listfakelow = ["./v24/Run2012Afakelow.root",
                   "./v24/Run2012B_1fakelow.root","./v24/Run2012B_2fakelow.root","./v24/Run2012B_3fakelow.root","./v24/Run2012B_4fakelow.root",
                   "./v24/Run2012C_1fakelow.root","./v24/Run2012C_2fakelow.root","./v24/Run2012C_3fakelow.root","./v24/Run2012C_4fakelow.root","./v24/Run2012C_5fakelow.root",
                   "./v24/Run2012D_1fakelow.root","./v24/Run2012D_2fakelow.root","./v24/Run2012D_3fakelow.root","./v24/Run2012D_4fakelow.root","./v24/Run2012D_5fakelow.root"]
    
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
    vecfilesfakehigh = []
    for item in listfakehigh:
        temp = TFile.Open(item)
        vecfilesfakehigh.append(temp)
    vecfilesfakelow = []
    for item in listfakelow:
        temp = TFile.Open(item)
        vecfilesfakelow.append(temp)
    vecfilessig = []
    for item in listsig:
        temp = TFile.Open(item)
        vecfilessig.append(temp)
    

    xbins = array('d',[0., 0.2, 1.5, 3., 6.])
    #xbins = array('d',[0., 0.2, 1.5, 6.])
    
    #dit is v21
    #xbins = array('d',[0.,0.3, 1., 3., 6.])

    nxbins = len(xbins) - 1

    ttjet = TH1F("TTJet","",nxbins,xbins)
    ttjet.Sumw2()
    ttjet = loop(vecfilesttjets,ttjet,0,phot)

    signal = TH1F("signal","",nxbins,xbins)
    signal.Sumw2()
    signal = loop(vecfilessig, signal, 0, phot)
    signal_sigmaUp = signal.Clone("signal_sigmaUp")
    signal_sigmaDown = signal.Clone("signal_sigmaDown")

    data_obs = TH1F("data_obs","",nxbins,xbins)
    data_obs.Sumw2()
    data_obs = loop(vecfilesdata, data_obs, 1, phot)

    background = TH1F("background","",nxbins,xbins)
    background.Sumw2()
    background = loop(vecfilesdataisolow, background, 2, phot)

    background.Add(ttjet)

    background_alphaUp = TH1F("background_alphaUp","",nxbins,xbins)
    #background_alphaUp = loop(vecfilesfakehigh,background_alphaUp, 2, phot)
    
    background_alphaUp = loop(vecfilesfakelow,background_alphaUp, 2, phot)
    
    background_alphaDown = background.Clone("background_alphaDown")
    
    datatotal = data_obs.GetBinContent(1)
    ttjettotal = ttjet.GetBinContent(1)
    isolowtotal = background.GetBinContent(1)
    background_alphaUptotal = background_alphaUp.GetBinContent(1)
    background_alphaDowntotal = background_alphaDown.GetBinContent(1)
    newisolowtotal = datatotal


    if(isolowtotal != 0):
        ratio = newisolowtotal/isolowtotal
        ratio_alphaUp = newisolowtotal/background_alphaUptotal
        ratio_alphaDown = newisolowtotal/background_alphaDowntotal
    else:
        ratio = 1.
        ratio_alphaUp = 1.
        ratio_alphaDown = 1.
    background.Scale(ratio)
    background_alphaUp.Scale(ratio_alphaUp)
    background_alphaDown.Scale(ratio_alphaDown)

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

    ttjet.SetBinContent(ttjet.GetNbinsX(),(ttjet.GetBinContent(ttjet.GetNbinsX())+ttjet.GetBinContent(ttjet.GetNbinsX()+1)))
    signal.SetBinContent(signal.GetNbinsX(),(signal.GetBinContent(signal.GetNbinsX())+signal.GetBinContent(signal.GetNbinsX()+1)))
    data_obs.SetBinContent(data_obs.GetNbinsX(),(data_obs.GetBinContent(data_obs.GetNbinsX())+data_obs.GetBinContent(data_obs.GetNbinsX()+1)))
    background.SetBinContent(background.GetNbinsX(),(background.GetBinContent(background.GetNbinsX())+background.GetBinContent(background.GetNbinsX()+1)))
    background_alphaUp.SetBinContent(background_alphaUp.GetNbinsX(),(background_alphaUp.GetBinContent(background_alphaUp.GetNbinsX())+background_alphaUp.GetBinContent(background_alphaUp.GetNbinsX()+1)))
    background_alphaDown.SetBinContent(background_alphaDown.GetNbinsX(),(background_alphaDown.GetBinContent(background_alphaDown.GetNbinsX())+background_alphaDown.GetBinContent(background_alphaDown.GetNbinsX()+1)))

    ttjet.SetBinError(ttjet.GetNbinsX(),(ttjet.GetBinError(ttjet.GetNbinsX())+ttjet.GetBinError(ttjet.GetNbinsX()+1)))
    signal.SetBinError(signal.GetNbinsX(),(signal.GetBinError(signal.GetNbinsX())+signal.GetBinError(signal.GetNbinsX()+1)))
    data_obs.SetBinError(data_obs.GetNbinsX(),(data_obs.GetBinError(data_obs.GetNbinsX())+data_obs.GetBinError(data_obs.GetNbinsX()+1)))
    background.SetBinError(background.GetNbinsX(),(background.GetBinError(background.GetNbinsX())+background.GetBinError(background.GetNbinsX()+1)))
    background_alphaUp.SetBinError(background_alphaUp.GetNbinsX(),(background_alphaUp.GetBinError(background_alphaUp.GetNbinsX())+background_alphaUp.GetBinError(background_alphaUp.GetNbinsX()+1)))
    background_alphaDown.SetBinError(background_alphaDown.GetNbinsX(),(background_alphaDown.GetBinError(background_alphaDown.GetNbinsX())+background_alphaDown.GetBinError(background_alphaDown.GetNbinsX()+1)))

    signal.SetBinContent(1,0)
    signal_sigmaUp.SetBinContent(1,0)
    signal_sigmaDown.SetBinContent(1,0)
    
    output = TFile.Open("./simpleshapes/histofile_L"+lamb+"CT"+ctau+".root","recreate")

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
    # function("140","1",2)
    # function("140","10",2)
    # function("140","100",2)
    # function("140","500",2)
    # function("140","1000",2)
    # function("140","2000",2)

    # function("160","1",2)
    # function("160","10",2)
    # function("160","100",2)
    # function("160","500",2)
    # function("160","1000",2)
    # function("160","2000",2)

    function("180","1",2)
    function("180","10",2)
    function("180","50",2)
    function("180","250",2)
    function("180","500",2)
    function("180","2000",2)

if __name__ == "__main__":
    main()

