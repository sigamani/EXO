from ROOT import *
from array import array
from math import fabs, sqrt

def loop(vec, vechisto, flag, phot):
    
    for i in vec:
        tree = i.Get("anaTree")
        entr = tree.GetEntries()
        j=0
        print 'total events ' + str(entr)
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
            #if (len(event.ptJet) < 2):
            #    continue
            
            if(flag == 0):
                lum = 19280.
                vechisto[0].Fill( event.ptPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                for i in range(len(event.dxyConv)):
                    if (event.ConvChi2[i] > 0.01):
                        vechisto[4].Fill( abs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                vechisto[5].Fill( event.MET, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                vechisto[6].Fill( event.nJet, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[7].Fill( event.nPhot, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[8].Fill( event.nGoodVtx, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[9].Fill( event.sMajPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[10].Fill( event.sMinPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[11].Fill( event.sigmaIetaPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[12].Fill( event.etaPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[13].Fill( event.chadiso[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[14].Fill( event.nhadiso[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[15].Fill( event.photiso[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[16].Fill( event.phohovere[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
            else:
                vechisto[0].Fill( event.ptPhot[0], 1./event.EfficiencyScaleFactors )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], 1./event.EfficiencyScaleFactors )
                for i in range(len(event.dxyConv)):
                    if (abs(event.ConvChi2[i] > 0.01)):
                        vechisto[4].Fill( abs(event.dxyConv[i]), 1./event.EfficiencyScaleFactors )
                vechisto[5].Fill( event.MET, 1./event.EfficiencyScaleFactors )
                vechisto[6].Fill( event.nJet, 1./event.EfficiencyScaleFactors )
                vechisto[7].Fill( event.nPhot, 1./event.EfficiencyScaleFactors )
                vechisto[8].Fill( event.nGoodVtx, 1./event.EfficiencyScaleFactors )
                vechisto[9].Fill( event.sMajPhot[0], 1./(event.EfficiencyScaleFactors))
                vechisto[10].Fill( event.sMinPhot[0], 1./(event.EfficiencyScaleFactors))
                vechisto[11].Fill( event.sigmaIetaPhot[0], 1./(event.EfficiencyScaleFactors))
                vechisto[12].Fill( event.etaPhot[0], 1./(event.EfficiencyScaleFactors))
                vechisto[13].Fill( event.chadiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[14].Fill( event.nhadiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[15].Fill( event.photiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[16].Fill( event.phohovere[0], 1./(event.EfficiencyScaleFactors))
    return vechisto

def function (lamb,ctau,phot):

    listgpt = ["./v24n-1/G_Pt-50to80.root","./v24n-1/G_Pt-80to120.root","./v24n-1/G_Pt-120to170.root","./v24n-1/G_Pt-170to300.root","./v24n-1/G_Pt-300to470.root","./v24n-1/G_Pt-470to800.root"]
    listqcd = ["./v24n-1/QCD_Pt-80to120.root","./v24n-1/QCD_Pt-120to170.root","./v24n-1/QCD_Pt-170to300.root","./v24n-1/QCD_Pt-470to600.root","./v24n-1/QCD_Pt-600to800.root","./v24n-1/QCD_Pt-800to1000.root","./v24n-1/QCD_Pt-1000to1400.root"]
    listttjets = ["./v24n-1/TTJets.root"]
    listsig = ["./v24n-1/GMSB_L"+lamb+"-CTAU"+ctau+".root"]
    
    vecfilesgpt = []
    for item in listgpt:
        temp = TFile.Open(item)
        vecfilesgpt.append(temp)
    vecfilesqcd = []
    for item in listqcd:
        temp = TFile.Open(item)
        vecfilesqcd.append(temp)
    vecfilesttjets = []
    for item in listttjets:
        temp = TFile.Open(item)
        vecfilesttjets.append(temp)
    vecfilessig1 = []
    for item in listsig:
        temp = TFile.Open(item)
        vecfilessig1.append(temp)
   

    xbins = array('d',[0.,0.3, 1., 3., 6.])

    ptpholeadgpt = TH1D("PtPhotonleadingGPT","",24,0,500)
    ptphosubleadgpt = TH1D("PtPhotonsubleadingGPT","",12,0,500)
    ptjetleadgpt = TH1D("PtJetleadingGPT","",40,0,300)
    ptjetsubleadgpt = TH1D("PtJetsubleadingGPT","",12,0,500)
    dxygpt = TH1D("DxyGPT","",4,xbins)
    metgpt = TH1D("METGPT","",50,0,500)
    njetsgpt = TH1D("nJetsGPT","",15,0,15)
    nphotgpt = TH1D("nPhotGPT","",15,0,15)
    nvertgpt = TH1D("nVertGPT","",8,0,40)
    smajgpt = TH1D("sMajGPT","",20,0,3)
    smingpt = TH1D("sMinGPT","",20,0,0.5)
    sigietagpt = TH1D("SigmaIetaGPT","",50,0,0.03)
    etagpt = TH1D("EtaGPT","",50,0,2)
    chadisogpt = TH1D("cHadIsoGPT","",50,0,5)
    nhadisogpt = TH1D("nHadIsoGPT","",50,0,5)
    photisogpt = TH1D("photIsoGPT","",50,0,5)
    phohoveregpt = TH1D("phoHoverEGPT","",50,0,0.1)
    vechisgpt = [ptpholeadgpt,ptphosubleadgpt,ptjetleadgpt,ptjetsubleadgpt,dxygpt,metgpt,njetsgpt,nphotgpt,nvertgpt,smajgpt,smingpt,sigietagpt,etagpt,chadisogpt,nhadisogpt,photisogpt,phohoveregpt]

    for each in vechisgpt:
        each.Sumw2()

    vechisgpt = loop(vecfilesgpt, vechisgpt, 0, phot)


    ptpholeadqcd = TH1D("PtPhotonleadingQCD","",24,0,500)
    ptphosubleadqcd = TH1D("PtPhotonsubleadingQCD","",12,0,500)
    ptjetleadqcd = TH1D("PtJetleadingQCD","",40,0,300)
    ptjetsubleadqcd = TH1D("PtJetsubleadingQCD","",12,0,500)
    dxyqcd = TH1D("DxyQCD","",4,xbins)
    metqcd = TH1D("METQCD","",50,0,500)
    njetsqcd = TH1D("nJetsQCD","",15,0,15)
    nphotqcd = TH1D("nPhotQCD","",15,0,15)
    nvertqcd = TH1D("nVertQCD","",8,0,40)
    smajqcd = TH1D("sMajQCD","",20,0,3)
    sminqcd = TH1D("sMinQCD","",20,0,0.5)
    sigietaqcd = TH1D("SigmaIetaQCD","",50,0,0.03)
    etaqcd = TH1D("EtaQCD","",50,0,2)
    chadisoqcd = TH1D("cHadIsoQCD","",50,0,5)
    nhadisoqcd = TH1D("nHadIsoQCD","",50,0,5)
    photisoqcd = TH1D("photIsoQCD","",50,0,5)
    phohovereqcd = TH1D("phoHoverEQCD","",50,0,0.1)
    vechisqcd = [ptpholeadqcd,ptphosubleadqcd,ptjetleadqcd,ptjetsubleadqcd,dxyqcd,metqcd,njetsqcd,nphotqcd,nvertqcd,smajqcd,sminqcd,sigietaqcd,etaqcd,chadisoqcd,nhadisoqcd,photisoqcd,phohovereqcd]

    for each in vechisqcd:
        each.Sumw2()

    vechisqcd = loop(vecfilesqcd, vechisqcd, 0, phot)

    ptpholeadttjet = TH1D("PtPhotonleadingTTJet","",24,0,500)
    ptphosubleadttjet = TH1D("PtPhotonsubleadingTTJet","",12,0,500)
    ptjetleadttjet = TH1D("PtJetleadingTTJet","",40,0,300)
    ptjetsubleadttjet = TH1D("PtJetsubleadingTTJet","",12,0,500)
    dxyttjet = TH1D("DxyTTJet","",4,xbins)
    metttjet = TH1D("METTTJet","",50,0,500)
    njetsttjet = TH1D("nJetsTTJet","",15,0,15)
    nphotttjet = TH1D("nPhotTTJet","",15,0,15)
    nvertttjet = TH1D("nVertTTJet","",8,0,40)
    smajttjet = TH1D("sMajTTJet","",20,0,3)
    sminttjet = TH1D("sMinTTJet","",20,0,0.5)
    sigietattjet = TH1D("SigmaIetaTTJet","",50,0,0.03)
    etattjet = TH1D("EtaTTJet","",50,0,2)
    chadisottjet = TH1D("cHadIsoTTJet","",50,0,5)
    nhadisottjet = TH1D("nHadIsoTTJet","",50,0,5)
    photisottjet = TH1D("photIsoTTJet","",50,0,5)
    phohoverettjet = TH1D("phoHoverETTJet","",50,0,0.1)
    vechisttjet = [ptpholeadttjet,ptphosubleadttjet,ptjetleadttjet,ptjetsubleadttjet,dxyttjet,metttjet,njetsttjet,nphotttjet,nvertttjet,smajttjet,sminttjet,sigietattjet,etattjet,chadisottjet,nhadisottjet,photisottjet,phohoverettjet]

    for each in vechisttjet:
        each.Sumw2()

    vechisttjet = loop(vecfilesttjets, vechisttjet, 0, phot)

    ptpholeadsig1 = TH1D("PtPhotonleadingSignal1","",24,0,500)
    ptphosubleadsig1 = TH1D("PtPhotonsubleadingSignal1","",12,0,500)
    ptjetleadsig1 = TH1D("PtJetleadingSignal1","",40,0,300)
    ptjetsubleadsig1 = TH1D("PtJetsubleadingSignal1","",12,0,500)
    dxysig1 = TH1D("DxySignal1","",4,xbins)
    metsig1 = TH1D("METSignal1","",50,0,500)
    njetssig1 = TH1D("nJetsSignal1","",15,0,15)
    nphotsig1 = TH1D("nPhotSignal1","",15,0,15)
    nvertsig1 = TH1D("nVertSignal1","",8,0,40)
    smajsig1 = TH1D("sMajSignal1","",20,0,3)
    sminsig1 = TH1D("sMinSignal1","",20,0,0.5)
    sigietasig1 = TH1D("SigmaIetaSignal1","",50,0,0.03)
    etasig1 = TH1D("EtaSignal1","",50,0,2)
    chadisosig1 = TH1D("cHadIsoSignal1","",50,0,5)
    nhadisosig1 = TH1D("nHadIsoSignal1","",50,0,5)
    photisosig1 = TH1D("photIsoSignal1","",50,0,5)
    phohoveresig1 = TH1D("phoHoverESignal1","",50,0,0.1)
    vechissig1 = [ptpholeadsig1,ptphosubleadsig1,ptjetleadsig1,ptjetsubleadsig1,dxysig1,metsig1,njetssig1,nphotsig1,nvertsig1,smajsig1,sminsig1,sigietasig1,etasig1,chadisosig1,nhadisosig1,photisosig1,phohoveresig1]

    for each in vechissig1:
        each.Sumw2()

    vechissig1 = loop(vecfilessig1, vechissig1, 0, phot)
            
    output = TFile.Open("./ctau"+ctau+"lambda"+lamb+"/output"+str(phot)+".root","recreate")

    # for i in range(len(vechissig1)):
    #     ttjettotal = vechisttjet[i].Integral()
    #     gpttotal = vechisgpt[i].Integral()
    #     qcdtotal = vechisqcd[i].Integral()
    #     sigtotal = vechissig1[i].Integral()

    #     if(ttjettotal != 0):
    #         ratiottjet = 1./ttjettotal
    #     else:
    #         ratiottjet = 1.

    #     if(gpttotal != 0):
    #         ratiogpt = 1./gpttotal
    #     else:
    #         ratiogpt = 1.

    #     if(qcdtotal != 0):
    #         ratioqcd = 1./qcdtotal
    #     else:
    #         ratioqcd = 1.

    #     if(sigtotal != 0):
    #         ratiosig = 1./sigtotal
    #     else:
    #         ratiosig = 1.
            
    #     vechisttjet[i].Scale(ratiottjet)
    #     vechisqcd[i].Scale(ratiogpt)
    #     vechisgpt[i].Scale(ratiogpt)
    #     vechissig1[i].Scale(ratiosig)

    # print vechisttjet[7].Integral()
    
    
    for it in vechisgpt:
        it.Write()
    for it in vechisqcd:
        it.Write()
    for it in vechisttjet:
        it.Write()
    for it in vechissig1:
        it.Write()

    #ptpho.Write()
    #ptphomc.Write()    
    #ptphosig.Write()    

    output.Close()


def main():
    #function("180","50",1)
    function("180","500",2)

if __name__ == "__main__":
    main()

