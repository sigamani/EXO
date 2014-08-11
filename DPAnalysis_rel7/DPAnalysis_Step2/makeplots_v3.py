
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
#            if (event.MET < 30.):
#                continue
#            if (event.ptJet.size() < 2):
#                continue
#            if (event.ptJet[1] < 30):
#                continue
            if(flag == 0):
                lum = 8430.
                vechisto[0].Fill( event.ptPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                for each in event.dxyConv:
                    vechisto[4].Fill( abs(each), (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
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
                for each in event.dxyConv:
                    vechisto[4].Fill( abs(each), 1./event.EfficiencyScaleFactors )
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

    listgpt = ["./v21/G_Pt-50to80.root","./v21/G_Pt-80to120.root","./v21/G_Pt-120to170.root","./v21/G_Pt-170to300.root","./v21/G_Pt-300to470.root","./v21/G_Pt-470to800.root"]
    listqcd = ["./v21/QCD_Pt-80to120.root","./v21/QCD_Pt-120to170.root","./v21/QCD_Pt-170to300.root","./v21/QCD_Pt-470to600.root","./v21/QCD_Pt-600to800.root","./v21/QCD_Pt-800to1000.root"]
    listttjets = ["./v21/TTJets.root"]
    listsig = ["./v21/GMSB_L"+lamb+"-CTAU"+ctau+".root"]
    listdata = ["./v21/Run2012C.root","./v21/Run2012D.root"]
    
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
    vecfilesdata = []
    for item in listdata:
        temp = TFile.Open(item)
        vecfilesdata.append(temp)        
    vecfilessig = []
    for item in listsig:
        temp = TFile.Open(item)
        vecfilessig.append(temp)

    ptpholeadgpt = TH1D("PtPhotonleadingGPT","",12,0,500)
    ptphosubleadgpt = TH1D("PtPhotonsubleadingGPT","",12,0,500)
    ptjetleadgpt = TH1D("PtJetleadingGPT","",12,0,500)
    ptjetsubleadgpt = TH1D("PtJetsubleadingGPT","",12,0,500)
    dxygpt = TH1D("DxyGPT","",25,0,2.5)
    metgpt = TH1D("METGPT","",50,0,1000)
    njetsgpt = TH1D("nJetsGPT","",15,0,15)
    nphotgpt = TH1D("nPhotGPT","",15,0,15)
    nvertgpt = TH1D("nVertGPT","",8,0,40)
    smajgpt = TH1D("sMajGPT","",20,0,3)
    smingpt = TH1D("sMinGPT","",20,0,0.5)
    sigietagpt = TH1D("SigmaIetaGPT","",50,0,0.03)
    etagpt = TH1D("EtaGPT","",50,0,2)
    vechisgpt = [ptpholeadgpt,ptphosubleadgpt,ptjetleadgpt,ptjetsubleadgpt,dxygpt,metgpt,njetsgpt,nphotgpt,nvertgpt,smajgpt,smingpt,sigietagpt,etagpt]
    vechisgpt = loop(vecfilesgpt, vechisgpt, 0, phot)

    ptpholeadqcd = TH1D("PtPhotonleadingQCD","",12,0,500)
    ptphosubleadqcd = TH1D("PtPhotonsubleadingQCD","",12,0,500)
    ptjetleadqcd = TH1D("PtJetleadingQCD","",12,0,500)
    ptjetsubleadqcd = TH1D("PtJetsubleadingQCD","",12,0,500)
    dxyqcd = TH1D("DxyQCD","",25,0,2.5)
    metqcd = TH1D("METQCD","",50,0,1000)
    njetsqcd = TH1D("nJetsQCD","",15,0,15)
    nphotqcd = TH1D("nPhotQCD","",15,0,15)
    nvertqcd = TH1D("nVertQCD","",8,0,40)
    smajqcd = TH1D("sMajQCD","",20,0,3)
    sminqcd = TH1D("sMinQCD","",20,0,0.5)
    sigietaqcd = TH1D("SigmaIetaQCD","",50,0,0.03)
    etaqcd = TH1D("EtaQCD","",50,0,2)
    vechisqcd = [ptpholeadqcd,ptphosubleadqcd,ptjetleadqcd,ptjetsubleadqcd,dxyqcd,metqcd,njetsqcd,nphotqcd,nvertqcd,smajqcd,sminqcd,sigietaqcd,etaqcd]
    vechisqcd = loop(vecfilesqcd, vechisqcd, 0, phot)

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
            
    output = TFile.Open("./ctau"+ctau+"lambda"+lamb+"/output"+str(phot)+".root","recreate")

    for it in vechis:
        it.Write()
    for it in vechisgpt:
        it.Write()
    for it in vechisqcd:
        it.Write()
    for it in vechisttjet:
        it.Write()
    for it in vechissig:
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

