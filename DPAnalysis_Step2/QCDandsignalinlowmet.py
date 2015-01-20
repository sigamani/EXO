from ROOT import *
from array import array
from math import fabs, sqrt

def loop(vec, vechisto, flag, phot, statmet, statptphot):

    for i in vec:
        tree = i.Get("anaTree")
        entr = tree.GetEntries()
        j=0
        print 'total events ' + str(entr)        

        if (flag == 0):
            for event in tree:
                if (event.nPhot < phot):
                    continue
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
                
                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))

    return vechisto

def function (lamb,ctau,phot,statmet,statptphot):

    listQCDlowmet = ["./v21/QCD_Pt-80to120_lowmet.root", "./v21/QCD_Pt-120to170_lowmet.root","./v21/QCD_Pt-170to300_lowmet.root","./v21/QCD_Pt-300to470_lowmet.root","./v21/QCD_Pt-470to600_lowmet.root","./v21/QCD_Pt-600to800_lowmet.root","./v21/QCD_Pt-800to1000_lowmet.root","./v21/QCD_Pt-1000to1400_lowmet.root"]
    listsiglowmet = ["./v22/GMSB_L"+lamb+"-CTAU"+ctau+"_lowmet.root"]
    listdataisolow = ["./v21/Run2012Aisolow.root","./v21/Run2012Bisolow.root","./v21/Run2012C_1isolow.root","./v21/Run2012C_2isolow.root","./v21/Run2012C_3isolow.root","./v21/Run2012D_1isolow.root","./v21/Run2012D_2isolow.root","./v21/Run2012D_3isolow.root"]
    listQCD = ["./v21/QCD_Pt-80to120.root","./v21/QCD_Pt-120to170.root","./v21/QCD_Pt-170to300.root","./v21/QCD_Pt-300to470.root","./v21/QCD_Pt-470to600.root","./v21/QCD_Pt-600to800.root","./v21/QCD_Pt-800to1000.root","./v21/QCD_Pt-1000to1400.root"]
    listsig = ["./v22/GMSB_L"+lamb+"-CTAU"+ctau+".root"]


    vecfilessig = []
    for item in listsig:
        temp = TFile.Open(item)
        vecfilessig.append(temp)

    vecfilesQCD = []
    for item in listQCD:
        temp = TFile.Open(item)
        vecfilesQCD.append(temp)

    vecfilessiglowmet = []
    for item in listsiglowmet:
        temp = TFile.Open(item)
        vecfilessiglowmet.append(temp)

    vecfilesQCDlowmet = []
    for item in listQCDlowmet:
        temp = TFile.Open(item)
        vecfilesQCDlowmet.append(temp)

    vecfilesdataisolow = []
    for item in listdataisolow:
        temp = TFile.Open(item)
        vecfilesdataisolow.append(temp)

    #xbins = array('d',[0.,0.1,0.3, 1., 3., 6.])
    xbins = array('d',[0.,0.3, 1., 3., 6.])

    dxysig = TH1D("DxySignal","",4,xbins)
    dxysig.Sumw2()
    vechissig = [dxysig]
    vechissig = loop(vecfilessig, vechissig, 0, phot, statmet, statptphot)

    dxyQCD = TH1D("DxyQCD","",4,xbins)
    dxyQCD.Sumw2()
    vechisQCD = [dxyQCD]
    vechisQCD = loop(vecfilesQCD, vechisQCD, 0, phot, statmet, statptphot)

    dxysiglowmet = TH1D("DxySignallowmet","",4,xbins)
    dxysiglowmet.Sumw2()
    vechissiglowmet = [dxysiglowmet]
    vechissiglowmet = loop(vecfilessiglowmet, vechissiglowmet, 0, phot, statmet, statptphot)

    dxyQCDlowmet = TH1D("DxyQCDlowmet","",4,xbins)
    dxyQCDlowmet.Sumw2()
    vechisQCDlowmet = [dxyQCDlowmet]
    vechisQCDlowmet = loop(vecfilesQCDlowmet, vechisQCDlowmet, 0, phot, statmet, statptphot)

    dxyisolow = TH1D("Dxyisolow","",4,xbins)
    dxyisolow.Sumw2()
    vechisisolow = [dxyisolow]
    vechisisolow = loop(vecfilesdataisolow, vechisisolow, 0, phot, statmet, statptphot)

    f = open("QCDandGMSBL"+lamb+"CT"+ctau+"_lowmet.txt","w")

    f.write("QCD: " + str(vechisQCD[0].Integral()) + "\n")
    f.write("Sig: " + str(vechissig[0].Integral()) + "\n")
    f.write("QCDlowmet: " + str(vechisQCDlowmet[0].Integral()) + "\n")
    f.write("Siglowmet: " + str(vechissiglowmet[0].Integral()) + "\n")
    f.write("BKG: " + str(vechisisolow[0].Integral()) + "\n")
    f.write("QCD/BKG: " + str(vechisQCD[0].Integral()/vechisisolow[0].Integral()) + "\n")
    f.write("Sig/BKG: " + str(vechissig[0].Integral()/vechisisolow[0].Integral()) + "\n")
    #f.write("QCDlowmet/QCD: " + str(vechisQCDlowmet[0].Integral()/vechisQCD[0].Integral()) + "\n")
    f.write("Siglowmet/Sig: " + str(vechissiglowmet[0].Integral()/vechissig[0].Integral()) + "\n")

    f.close()

def main():

    # function("180","500","500",2,27,85)
    function("180","500",2,30,85)
    # function("180","500","500",2,33,85)
    # function("180","500","500",2,30,82)
    # function("180","500","500",2,30,88)

    # function("180","250","500",2,27,85)
    function("180","250",2,30,85)
    # function("180","250","500",2,33,85)
    # function("180","250","500",2,30,82)
    # function("180","250","500",2,30,88)

    # function("180","50","500",2,27,85)
    function("180","50",2,30,85)
    # function("180","50","500",2,33,85)
    # function("180","50","500",2,30,82)
    # function("180","50","500",2,30,88)

    # function("180","10","500",2,27,85)
    function("180","10",2,30,85)
    # function("180","10","500",2,33,85)
    # function("180","10","500",2,30,82)
    # function("180","10","500",2,30,88)

    # function("160","500","500",2,27,85)
    function("160","500",2,30,85)
    # function("160","500","500",2,33,85)
    # function("160","500","500",2,30,82)
    # function("160","500","500",2,30,88)

    # function("160","250","500",2,27,85)
    #function("160","250",2,30,85)
    # function("160","250","500",2,33,85)
    # function("160","250","500",2,30,82)
    # function("160","250","500",2,30,88)

    # function("160","100","500",2,27,85)
    function("160","100",2,30,85)
    # function("160","100","500",2,33,85)
    # function("160","100","500",2,30,82)
    # function("160","100","500",2,30,88)

    # function("160","50","500",2,27,85)
    function("160","50",2,30,85)
    # function("160","50","500",2,33,85)
    # function("160","50","500",2,30,82)
    # function("160","50","500",2,30,88)

    # function("160","10","500",2,27,85)
    function("160","10",2,30,85)
    # function("160","10","500",2,33,85)
    # function("160","10","500",2,30,82)
    # function("160","10","500",2,30,88)

if __name__ == "__main__":
    main()

