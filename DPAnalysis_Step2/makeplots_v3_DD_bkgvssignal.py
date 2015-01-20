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
            #if (event.nPhot < phot):
            #    continue
            #if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
            #    continue
            #if (event.ptJet[0] < 35):
            #    continue
            #if (event.sigmaIetaPhot[0] < 0.006 or event.sigmaIetaPhot[0] > 0.012):
            #    continue
            #if (event.ptPhot[0] < 85):
            #    continue
            #if (event.sMajPhot[0] > 1.35):
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
                    #if (event.ConvChi2[i] > 0.01):
                    vechisto[4].Fill( fabs(event.dxyConv[i]), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                
                vechisto[5].Fill( event.MET, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                vechisto[6].Fill( event.nJet, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[7].Fill( event.nPhot, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[8].Fill( event.nGoodVtx, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[9].Fill( event.sMajPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[10].Fill( event.sMinPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[11].Fill( event.sigmaIetaPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[12].Fill( event.etaPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                for i in event.deltaRward:
                    vechisto[13].Fill( i, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                                        
            if (flag == 1):
                #if (event.ptPhot[0] < 250):
                vechisto[0].Fill( event.ptPhot[0], 1./event.EfficiencyScaleFactors )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], 1./event.EfficiencyScaleFactors )

                for i in range(len(event.dxyConv)):
                    #if (abs(event.dxyConv[i]) < 0.1 and event.ConvChi2[i] > 0.01):
                    #if (abs(event.ConvChi2[i] > 0.01)):
                    vechisto[4].Fill( fabs(event.dxyConv[i]), 1./event.EfficiencyScaleFactors )
                            
                vechisto[5].Fill( event.MET, 1./event.EfficiencyScaleFactors )
                vechisto[6].Fill( event.nJet, 1./event.EfficiencyScaleFactors )
                vechisto[7].Fill( event.nPhot, 1./event.EfficiencyScaleFactors )
                vechisto[8].Fill( event.nGoodVtx, 1./event.EfficiencyScaleFactors )
                vechisto[9].Fill( event.sMajPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[10].Fill( event.sMinPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[11].Fill( event.sigmaIetaPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[12].Fill( event.etaPhot[0], 1./event.EfficiencyScaleFactors )
                for i in event.deltaRward:
                    vechisto[13].Fill( i, 1./event.EfficiencyScaleFactors )
                    
            if (flag == 2):
                vechisto[0].Fill( event.ptPhot[0], 1./event.EfficiencyScaleFactors )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], 1./event.EfficiencyScaleFactors )
                    
                for i in range(len(event.dxyConv)):
                    #if (event.ConvChi2[i] > 0.01):
                    vechisto[4].Fill( fabs(event.dxyConv[i]), 1./event.EfficiencyScaleFactors )

                vechisto[5].Fill( event.MET, 1./event.EfficiencyScaleFactors )
                vechisto[6].Fill( event.nJet, 1./event.EfficiencyScaleFactors )
                vechisto[7].Fill( event.nPhot, 1./event.EfficiencyScaleFactors )
                vechisto[8].Fill( event.nGoodVtx, 1./event.EfficiencyScaleFactors )
                vechisto[9].Fill( event.sMajPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[10].Fill( event.sMinPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[11].Fill( event.sigmaIetaPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[12].Fill( event.etaPhot[0], 1./event.EfficiencyScaleFactors )
                for i in event.deltaRward:
                    vechisto[13].Fill( i, 1./event.EfficiencyScaleFactors )
        
    return vechisto

def function (lamb,ctau,phot):

    listttjets = ["./v21/TTJets.root"]
    listsig = ["./v21/GMSB_L"+lamb+"-CTAU"+ctau+".root"]
    listdata = ["./v21/Run2012A.root","./v21/Run2012B.root","./v21/Run2012C_1.root","./v21/Run2012C_2.root","./v21/Run2012C_3.root","./v21/Run2012D_1.root","./v21/Run2012D_2.root","./v21/Run2012D_3.root"]
    listdataisolow = ["./v21/Run2012Aisolow.root","./v21/Run2012Bisolow.root","./v21/Run2012C_1isolow.root","./v21/Run2012C_2isolow.root","./v21/Run2012C_3isolow.root","./v21/Run2012D_1isolow.root","./v21/Run2012D_2isolow.root","./v21/Run2012D_3isolow.root"]
    
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
    

    xbins = array('d',[0.,0.1,0.3, 1., 3., 6.])

    ptpholeadttjet = TH1D("PtPhotonleadingTTJet","",24,0,500)
    ptphosubleadttjet = TH1D("PtPhotonsubleadingTTJet","",12,0,500)
    ptjetleadttjet = TH1D("PtJetleadingTTJet","",12,0,500)
    ptjetsubleadttjet = TH1D("PtJetsubleadingTTJet","",12,0,500)
    dxyttjet = TH1D("DxyTTJet","",50,0,3)
    metttjet = TH1D("METTTJet","",50,0,1000)
    njetsttjet = TH1D("nJetsTTJet","",15,0,15)
    nphotttjet = TH1D("nPhotTTJet","",15,0,15)
    nvertttjet = TH1D("nVertTTJet","",8,0,40)
    smajttjet = TH1D("sMajTTJet","",20,0,3)
    sminttjet = TH1D("sMinTTJet","",20,0,0.5)
    sigietattjet = TH1D("SigmaIetaTTJet","",50,0,0.03)
    etattjet = TH1D("EtaTTJet","",50,0,2)
    deltaRttjet = TH1D("DeltaRTTJet","",50,0,15)
    vechisttjet = [ptpholeadttjet,ptphosubleadttjet,ptjetleadttjet,ptjetsubleadttjet,dxyttjet,metttjet,njetsttjet,nphotttjet,nvertttjet,smajttjet,sminttjet,sigietattjet,etattjet,deltaRttjet]
    vechisttjet = loop(vecfilesttjets, vechisttjet, 0, phot)

    ptpholeadsig = TH1D("PtPhotonleadingSignal","",24,0,500)
    ptphosubleadsig = TH1D("PtPhotonsubleadingSignal","",12,0,500)
    ptjetleadsig = TH1D("PtJetleadingSignal","",12,0,500)
    ptjetsubleadsig = TH1D("PtJetsubleadingSignal","",12,0,500)
    dxysig = TH1D("DxySignal","",50,0,3)
    metsig = TH1D("METSignal","",50,0,1000)
    njetssig = TH1D("nJetsSignal","",15,0,15)
    nphotsig = TH1D("nPhotSignal","",15,0,15)
    nvertsig = TH1D("nVertSignal","",8,0,40)
    smajsig = TH1D("sMajSignal","",20,0,3)
    sminsig = TH1D("sMinSignal","",20,0,0.5)
    sigietasig = TH1D("SigmaIetaSignal","",50,0,0.03)
    etasig = TH1D("EtaSignal","",50,0,2)
    deltaRsig = TH1D("DeltaRSignal","",50,0,15)
    vechissig = [ptpholeadsig,ptphosubleadsig,ptjetleadsig,ptjetsubleadsig,dxysig,metsig,njetssig,nphotsig,nvertsig,smajsig,sminsig,sigietasig,etasig,deltaRsig]
    vechissig = loop(vecfilessig, vechissig, 0, phot)

    ptpholead = TH1D("PtPhotonleading","",24,0,500)
    ptphosublead = TH1D("PtPhotonsubleading","",12,0,500)
    ptjetlead = TH1D("PtJetleading","",12,0,500)
    ptjetsublead = TH1D("PtJetsubleading","",12,0,500)
    dxy = TH1D("Dxy","",50,0,3)
    met = TH1D("MET","",50,0,1000)
    njets = TH1D("nJets","",15,0,15)
    nphot = TH1D("nPhot","",15,0,15)
    nvert = TH1D("nVert","",8,0,40)
    smaj = TH1D("sMaj","",20,0,3)
    smin = TH1D("sMin","",20,0,0.5)
    sigieta = TH1D("SigmaIeta","",50,0,0.03)
    eta = TH1D("Eta","",50,0,2)
    deltaR = TH1D("DeltaR","",50,0,15)
    vechis = [ptpholead,ptphosublead,ptjetlead,ptjetsublead,dxy,met,njets,nphot,nvert,smaj,smin,sigieta,eta, deltaR]
    vechis = loop(vecfilesdata, vechis, 1, phot)

    ptpholeadisolow = TH1D("PtPhotonleadingisolow","",24,0,500)
    ptphosubleadisolow = TH1D("PtPhotonsubleadingisolow","",12,0,500)
    ptjetleadisolow = TH1D("PtJetleadingisolow","",12,0,500)
    ptjetsubleadisolow = TH1D("PtJetsubleadingisolow","",12,0,500)
    dxyisolow = TH1D("Dxyisolow","",50,0,3)
    metisolow = TH1D("METisolow","",50,0,1000)
    njetsisolow = TH1D("nJetsisolow","",15,0,15)
    nphotisolow = TH1D("nPhotisolow","",15,0,15)
    nvertisolow = TH1D("nVertisolow","",8,0,40)
    smajisolow = TH1D("sMajisolow","",20,0,3)
    sminisolow = TH1D("sMinisolow","",20,0,0.5)
    sigietaisolow = TH1D("SigmaIetaisolow","",50,0,0.03)
    etaisolow = TH1D("Etaisolow","",50,0,2)
    deltaRisolow = TH1D("DeltaRisolow","",50,0,15)
    vechisisolow= [ptpholeadisolow,ptphosubleadisolow,ptjetleadisolow,ptjetsubleadisolow,dxyisolow,metisolow,njetsisolow,nphotisolow,nvertisolow,smajisolow,sminisolow,sigietaisolow,etaisolow, deltaRisolow]
    vechisisolow = loop(vecfilesdataisolow, vechisisolow, 2, phot)

    dxy.SetBinContent(25,dxy.GetBinContent(26))
    dxysig.SetBinContent(25,dxysig.GetBinContent(26))
    dxyttjet.SetBinContent(25,dxyttjet.GetBinContent(26))
    dxyisolow.SetBinContent(25,dxyisolow.GetBinContent(26))

    
    for i in range(len(vechis)):
        datatotal = vechis[i].Integral()
        ttjettotal = vechisttjet[i].Integral()
        isolowtotal = vechisisolow[i].Integral()
        newisolowtotal = datatotal - ttjettotal
        #print "oldtotal: " + str(isolowtotal) + ", newtotal: " + str(newisolowtotal)

        if(isolowtotal != 0):
            ratio = newisolowtotal/isolowtotal
        else:
            ratio = 1.
        vechisisolow[i].Scale(ratio)

       #print "old: " + str(isolowtotal) + ", new: " + str(vechisisolow[i].Integral())

    
    datatotal = vechis[4].GetBinContent(1)
    ttjettotal = vechisttjet[4].GetBinContent(1)
    isolowtotal = vechisisolow[4].GetBinContent(1)
    newisolowtotal = datatotal - ttjettotal

    if(isolowtotal != 0):
        ratio = newisolowtotal/isolowtotal
    else:
        ratio = 1.
    vechisisolow[4].Scale(ratio)

    """
    vechis[4].SetBinContent(1,0.)
    vechis[4].SetBinContent(2,0.)
    vechissig[4].SetBinContent(1,0.)
    vechissig[4].SetBinContent(2,0.)
    vechisttjet[4].SetBinContent(1,0.)
    vechisttjet[4].SetBinContent(2,0.)
    vechisisolow[4].SetBinContent(1,0.)
    vechisisolow[4].SetBinContent(2,0.)
    """
    output = TFile.Open("./ctau"+ctau+"lambda"+lamb+"/output"+str(phot)+".root","recreate")

    for it in vechis:
        it.Write()
    for it in vechisttjet:
        it.Write()
    for it in vechissig:
        it.Write()
    for it in vechisisolow:
        it.Write()

    #ptpho.Write()
    #ptphomc.Write()    
    #ptphosig.Write()    

    output.Close()


def main():
    function("180","500",1)
    function("180","500",2)

if __name__ == "__main__":
    main()

