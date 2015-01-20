from ROOT import *
from array import array
from math import fabs, sqrt

def loop(vec, vechisto, flag, phot, statmet, statptphot):

    for i in vec:

        jetptward = []
        jetptupward = []
                            
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
                if (event.MET < 30):
                    continue
                
                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))

        if (flag == 1):

            for event in tree:

                if (event.nPhot < phot):
                    continue
                if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                    continue
                if ((event.ptJet[0]*1.05) < 35):
                    continue
                if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
                    continue
                if (event.ptPhot[0] < 85):
                    continue
                if (event.sMajPhot[0] > 1.35):
                    continue
                if (event.MET < 30):
                    continue

                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))

        if (flag == 2):

            for event in tree:

                if (event.nPhot < phot):
                    continue
                if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                    continue
                if ((event.ptJet[0] * 0.95) < 35):
                    continue
                if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
                    continue
                if (event.ptPhot[0] < 85):
                    continue
                if (event.sMajPhot[0] > 1.35):
                    continue
                if (event.MET < 30):
                    continue

                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))


        # if (flag == 1):

        #     for event in tree:

        #         if (event.nPhot < phot):
        #             continue
        #         if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
        #             continue
        #         if (event.ptJetUp.size() < 2):
        #             continue
        #         if (event.ptJetUp[0] < 35):
        #             continue
        #         if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
        #             continue
        #         if (event.ptPhot[0] < 85):
        #             continue
        #         if (event.sMajPhot[0] > 1.35):
        #             continue
        #         if (event.MET < 30):
        #                 continue
        #         lum = 19280.
        #         for i in range(len(event.dxyConv)):
        #             if (event.ConvChi2[i] > 0.01):
        #                 vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))

        # if (flag == 2):

        #     for event in tree:

        #         if (event.nPhot < phot):
        #             continue
        #         if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
        #             continue
        #         if (event.ptJetDown.size() < 2):
        #             continue
        #         if (event.ptJetDown[0] < 35):
        #             continue
        #         if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
        #             continue
        #         if (event.ptPhot[0] < 85):
        #             continue
        #         if (event.sMajPhot[0] > 1.35):
        #             continue
        #         if (event.MET < 30):
        #                 continue
        #         lum = 19280.
        #         for i in range(len(event.dxyConv)):
        #             if (event.ConvChi2[i] > 0.01):
        #                 vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))

        if (flag == 3):

            for event in tree:

                if (event.nPhot < phot):
                    continue
                if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                    continue
                if (event.ptJet[0] < 35):
                    continue
                if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
                    continue
                if ((event.ptPhot[0] * 1.036) < 85):
                    continue
                if (event.sMajPhot[0] > 1.35):
                    continue
                if (event.MET < 30):
                    continue

                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))

        if (flag == 4):

            for event in tree:

                if (event.nPhot < phot):
                    continue
                if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                    continue
                if (event.ptJet[0] < 35):
                    continue
                if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
                    continue
                if ((event.ptPhot[0] * 0.964) < 85):
                    continue
                if (event.sMajPhot[0] > 1.35):
                    continue
                if (event.MET < 30):
                    continue

                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))

        if (flag == 5):

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
                if ((event.MET * 1.01)< 30):
                    continue

                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))

        if (flag == 6):

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
                if ((event.MET * 0.99)< 30):
                    continue

                lum = 19280.
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[0].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                
    return vechisto

def function (lamb,ctau1,phot,statmet,statptphot):

    listsig1 = ["./v21/GMSB_L"+lamb+"-CTAU"+ctau1+"_old.root"]

    vecfilessig1 = []
    for item in listsig1:
        temp = TFile.Open(item)
        vecfilessig1.append(temp)

    #xbins = array('d',[0.,0.1,0.3, 1., 3., 6.])
    xbins = array('d',[0.,0.3, 1., 3., 6.])

    dxysig1 = TH1D("DxySignal1","",4,xbins)
    vechissig1 = [dxysig1]
    vechissig1 = loop(vecfilessig1, vechissig1, 0, phot, statmet, statptphot)

    dxysig1ptup = TH1D("DxySignal1PtUp","",4,xbins)
    vechissig1ptup = [dxysig1ptup]
    vechissig1ptup = loop(vecfilessig1, vechissig1ptup, 1, phot, statmet, statptphot)

    dxysig1ptdown = TH1D("DxySignal1PtDown","",4,xbins)
    vechissig1ptdown = [dxysig1ptdown]
    vechissig1ptdown = loop(vecfilessig1, vechissig1ptdown, 2, phot, statmet, statptphot)

    dxysig1phoup = TH1D("DxySignal1PhoUp","",4,xbins)
    vechissig1phoup = [dxysig1phoup]
    vechissig1phoup = loop(vecfilessig1, vechissig1phoup, 3, phot, statmet, statptphot)

    dxysig1phodown = TH1D("DxySignal1PhoDown","",4,xbins)
    vechissig1phodown = [dxysig1phodown]
    vechissig1phodown = loop(vecfilessig1, vechissig1phodown, 4, phot, statmet, statptphot)

    dxysig1metup = TH1D("DxySignal1MetUp","",4,xbins)
    vechissig1metup = [dxysig1metup]
    vechissig1metup = loop(vecfilessig1, vechissig1metup, 5, phot, statmet, statptphot)

    dxysig1metdown = TH1D("DxySignal1MetDown","",4,xbins)
    vechissig1metdown = [dxysig1metdown]
    vechissig1metdown = loop(vecfilessig1, vechissig1metdown, 6, phot, statmet, statptphot)

    output = TFile.Open("./ctau"+ctau1+"lambda"+lamb+"/output"+str(phot)+"MET"+str(statmet)+"PtPhot"+str(statptphot)+".root","recreate")

    for it in vechissig1:
        it.Write()
    for it in vechissig1ptup:
        it.Write()
    for it in vechissig1ptdown:
        it.Write()
    for it in vechissig1phoup:
        it.Write()
    for it in vechissig1phodown:
        it.Write()
    for it in vechissig1metup:
        it.Write()
    for it in vechissig1metdown:
        it.Write()
    output.Close()


def main():
    #function("180","10","500",1)

    # function("180","500","500",2,27,85)
    function("180","500",2,30,85)
    # function("180","500","500",2,33,85)
    # function("180","500","500",2,30,82)
    # function("180","500","500",2,30,88)

    # function("180","250","500",2,27,85)
    # function("180","250",2,30,85)
    # function("180","250","500",2,33,85)
    # function("180","250","500",2,30,82)
    # function("180","250","500",2,30,88)

    # function("180","50","500",2,27,85)
    # function("180","50",2,30,85)
    # function("180","50","500",2,33,85)
    # function("180","50","500",2,30,82)
    # function("180","50","500",2,30,88)

    # function("180","10","500",2,27,85)
    # function("180","10",2,30,85)
    # function("180","10","500",2,33,85)
    # function("180","10","500",2,30,82)
    # function("180","10","500",2,30,88)

    # function("160","500","500",2,27,85)
    # function("160","500",2,30,85)
    # function("160","500","500",2,33,85)
    # function("160","500","500",2,30,82)
    # function("160","500","500",2,30,88)

    # function("160","250","500",2,27,85)
    # function("160","250","500",2,30,85)
    # function("160","250","500",2,33,85)
    # function("160","250","500",2,30,82)
    # function("160","250","500",2,30,88)

    # function("160","100","500",2,27,85)
    # function("160","100",2,30,85)
    # function("160","100","500",2,33,85)
    # function("160","100","500",2,30,82)
    # function("160","100","500",2,30,88)

    # function("160","50","500",2,27,85)
    # function("160","50",2,30,85)
    # function("160","50","500",2,33,85)
    # function("160","50","500",2,30,82)
    # function("160","50","500",2,30,88)

    # function("160","10","500",2,27,85)
    # function("160","10",2,30,85)
    # function("160","10","500",2,33,85)
    # function("160","10","500",2,30,82)
    # function("160","10","500",2,30,88)

if __name__ == "__main__":
    main()

