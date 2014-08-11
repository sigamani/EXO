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
            if (event.ptPhot.size() < phot):
                continue
            if (event.sMinPhot[0] < 0.15 or event.sMinPhot[0] > 0.3):
                continue
            if (event.ptJet[0] < 30):
                continue
            if (event.sigmaIetaPhot[0] < 0.0085 or event.sigmaIetaPhot[0] > 0.01):
                continue
            if (event.sMajPhot[0] > 1.5):
                continue
            if(flag == 0):
                lum = 19000.
                vechisto[0].Fill( event.ptPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                for i in event.dxyConv:
                    vechisto[4].Fill( fabs(i), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                
                vechisto[5].Fill( event.MET, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                vechisto[6].Fill( event.nJet, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[7].Fill( event.nPhot, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[8].Fill( event.nGoodVtx, (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[9].Fill( event.sMajPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[10].Fill( event.sMinPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[11].Fill( event.sigmaIetaPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
                vechisto[12].Fill( event.etaPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))
            else:
                vechisto[0].Fill( event.ptPhot[0], 1./event.EfficiencyScaleFactors )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], 1./event.EfficiencyScaleFactors )

                for i in event.dxyConv:
                    vechisto[4].Fill( fabs(i), 1./event.EfficiencyScaleFactors )
                            
                vechisto[5].Fill( event.MET, 1./event.EfficiencyScaleFactors )
                vechisto[6].Fill( event.nJet, 1./event.EfficiencyScaleFactors )
                vechisto[7].Fill( event.nPhot, 1./event.EfficiencyScaleFactors )
                vechisto[8].Fill( event.nGoodVtx, 1./event.EfficiencyScaleFactors )
                vechisto[9].Fill( event.sMajPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[10].Fill( event.sMinPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[11].Fill( event.sigmaIetaPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[12].Fill( event.etaPhot[0], 1./event.EfficiencyScaleFactors )
    return vechisto

def function (lamb,ctau,phot):

    listttjets = ["./v21/TTJets.root"]
    listsig = ["./v21/GMSB_L"+lamb+"-CTAU"+ctau+".root"]
    listdata = ["./v21/Run2012A.root","./v21/Run2012B.root","./v21/Run2012C.root","./v21/Run2012D.root"]
    listdataisolow = ["./v21/Run2012Aisolow.root","./v21/Run2012Bisolow.root","./v21/Run2012Cisolow.root","./v21/Run2012Disolow.root"]
    
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
    

    ptpholeadttjet = TH1D("PtPhotonleadingTTJet","",12,0,500)
    ptphosubleadttjet = TH1D("PtPhotonsubleadingTTJet","",12,0,500)
    ptjetleadttjet = TH1D("PtJetleadingTTJet","",12,0,500)
    ptjetsubleadttjet = TH1D("PtJetsubleadingTTJet","",12,0,500)
    dxyttjet = TH1D("DxyTTJet","",25,0,2.5)
    metttjet = TH1D("METTTJet","",50,0,1000)
    njetsttjet = TH1D("nJetsTTJet","",15,0,15)
    nphotttjet = TH1D("nPhotTTJet","",15,0,15)
    nvertttjet = TH1D("nVertTTJet","",8,0,40)
    smajttjet = TH1D("sMajTTJet","",20,0,3)
    sminttjet = TH1D("sMinTTJet","",20,0,0.5)
    sigietattjet = TH1D("SigmaIetaTTJet","",50,0,0.03)
    etattjet = TH1D("EtaTTJet","",50,0,2)
    vechisttjet = [ptpholeadttjet,ptphosubleadttjet,ptjetleadttjet,ptjetsubleadttjet,dxyttjet,metttjet,njetsttjet,nphotttjet,nvertttjet,smajttjet,sminttjet,sigietattjet,etattjet]
    vechisttjet = loop(vecfilesttjets, vechisttjet, 0, phot)

    ptpholeadsig = TH1D("PtPhotonleadingSignal","",12,0,500)
    ptphosubleadsig = TH1D("PtPhotonsubleadingSignal","",12,0,500)
    ptjetleadsig = TH1D("PtJetleadingSignal","",12,0,500)
    ptjetsubleadsig = TH1D("PtJetsubleadingSignal","",12,0,500)
    dxysig = TH1D("DxySignal","",25,0,2.5)
    metsig = TH1D("METSignal","",50,0,1000)
    njetssig = TH1D("nJetsSignal","",15,0,15)
    nphotsig = TH1D("nPhotSignal","",15,0,15)
    nvertsig = TH1D("nVertSignal","",8,0,40)
    smajsig = TH1D("sMajSignal","",20,0,3)
    sminsig = TH1D("sMinSignal","",20,0,0.5)
    sigietasig = TH1D("SigmaIetaSignal","",50,0,0.03)
    etasig = TH1D("EtaSignal","",50,0,2)
    vechissig = [ptpholeadsig,ptphosubleadsig,ptjetleadsig,ptjetsubleadsig,dxysig,metsig,njetssig,nphotsig,nvertsig,smajsig,sminsig,sigietasig,etasig]
    vechissig = loop(vecfilessig, vechissig, 0, phot)

    ptpholead = TH1D("PtPhotonleading","",12,0,500)
    ptphosublead = TH1D("PtPhotonsubleading","",12,0,500)
    ptjetlead = TH1D("PtJetleading","",12,0,500)
    ptjetsublead = TH1D("PtJetsubleading","",12,0,500)
    dxy = TH1D("Dxy","",25,0,2.5)
    met = TH1D("MET","",50,0,1000)
    njets = TH1D("nJets","",15,0,15)
    nphot = TH1D("nPhot","",15,0,15)
    nvert = TH1D("nVert","",8,0,40)
    smaj = TH1D("sMaj","",20,0,3)
    smin = TH1D("sMin","",20,0,0.5)
    sigieta = TH1D("SigmaIeta","",50,0,0.03)
    eta = TH1D("Eta","",50,0,2)
    vechis = [ptpholead,ptphosublead,ptjetlead,ptjetsublead,dxy,met,njets,nphot,nvert,smaj,smin,sigieta,eta]
    vechis = loop(vecfilesdata, vechis, 1, phot)

    ptpholeadisolow = TH1D("PtPhotonleadingisolow","",12,0,500)
    ptphosubleadisolow = TH1D("PtPhotonsubleadingisolow","",12,0,500)
    ptjetleadisolow = TH1D("PtJetleadingisolow","",12,0,500)
    ptjetsubleadisolow = TH1D("PtJetsubleadingisolow","",12,0,500)
    dxyisolow = TH1D("Dxyisolow","",25,0,2.5)
    metisolow = TH1D("METisolow","",50,0,1000)
    njetsisolow = TH1D("nJetsisolow","",15,0,15)
    nphotisolow = TH1D("nPhotisolow","",15,0,15)
    nvertisolow = TH1D("nVertisolow","",8,0,40)
    smajisolow = TH1D("sMajisolow","",20,0,3)
    sminisolow = TH1D("sMinisolow","",20,0,0.5)
    sigietaisolow = TH1D("SigmaIetaisolow","",50,0,0.03)
    etaisolow = TH1D("Etaisolow","",50,0,2)
    vechisisolow = [ptpholeadisolow,ptphosubleadisolow,ptjetleadisolow,ptjetsubleadisolow,dxyisolow,metisolow,njetsisolow,nphotisolow,nvertisolow,smajisolow,sminisolow,sigietaisolow,etaisolow]
    vechisisolow = loop(vecfilesdataisolow, vechisisolow, 1, phot)


    dxy.SetBinContent(25,dxy.GetBinContent(26))
    dxysig.SetBinContent(25,dxy.GetBinContent(26))
    dxyttjet.SetBinContent(25,dxy.GetBinContent(26))
    dxyisolow.SetBinContent(25,dxy.GetBinContent(26))


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

