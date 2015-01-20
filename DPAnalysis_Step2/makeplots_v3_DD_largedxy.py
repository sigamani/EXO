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
            dxytemp = []
            for i in range(len(event.dxyConv)):
                if (event.ConvChi2[i] > 0.01):
                    dxytemp.append(fabs(event.dxyConv[i]))
            dxytemp = sorted(dxytemp)

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
#            if (event.MET < 30):
#                continue
            if(flag == 0):
                lum = 19280.
                vechisto[0].Fill( event.ptPhot[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors) )
                if(len(dxytemp) > 0):
                    vechisto[4].Fill( dxytemp[-1], (event.CrossSectionWeight*lum)/(event.EfficiencyScaleFactors))                
                    
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
                
            if (flag == 1):
                vechisto[0].Fill( event.ptPhot[0], 1./event.EfficiencyScaleFactors )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], 1./event.EfficiencyScaleFactors )

                if(len(dxytemp) > 0):
                    vechisto[4].Fill( dxytemp[-1], 1./event.EfficiencyScaleFactors)
                            
                vechisto[5].Fill( event.MET, 1./event.EfficiencyScaleFactors )
                vechisto[6].Fill( event.nJet, 1./event.EfficiencyScaleFactors )
                vechisto[7].Fill( event.nPhot, 1./event.EfficiencyScaleFactors )
                vechisto[8].Fill( event.nGoodVtx, 1./event.EfficiencyScaleFactors )
                vechisto[9].Fill( event.sMajPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[10].Fill( event.sMinPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[11].Fill( event.sigmaIetaPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[12].Fill( event.etaPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[13].Fill( event.chadiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[14].Fill( event.nhadiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[15].Fill( event.photiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[16].Fill( event.phohovere[0], 1./(event.EfficiencyScaleFactors))
                    
            if (flag == 2):
                vechisto[0].Fill( event.ptPhot[0], 1./event.EfficiencyScaleFactors )
                if (event.ptPhot.size() > phot):
                    vechisto[1].Fill( event.ptPhot[1], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 0):
                    vechisto[2].Fill( event.ptJet[0], 1./event.EfficiencyScaleFactors )
                if(event.ptJet.size() > 2):
                    vechisto[3].Fill( event.ptJet[1], 1./event.EfficiencyScaleFactors )
                    
                if(len(dxytemp) > 0):
                    vechisto[4].Fill( dxytemp[-1], 1./event.EfficiencyScaleFactors)

                vechisto[5].Fill( event.MET, 1./event.EfficiencyScaleFactors )
                vechisto[6].Fill( event.nJet, 1./event.EfficiencyScaleFactors )
                vechisto[7].Fill( event.nPhot, 1./event.EfficiencyScaleFactors )
                vechisto[8].Fill( event.nGoodVtx, 1./event.EfficiencyScaleFactors )
                vechisto[9].Fill( event.sMajPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[10].Fill( event.sMinPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[11].Fill( event.sigmaIetaPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[12].Fill( event.etaPhot[0], 1./event.EfficiencyScaleFactors )
                vechisto[13].Fill( event.chadiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[14].Fill( event.nhadiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[15].Fill( event.photiso[0], 1./(event.EfficiencyScaleFactors))
                vechisto[16].Fill( event.phohovere[0], 1./(event.EfficiencyScaleFactors))
                
    return vechisto

def function (lamb,ctau1,ctau2,phot):

    listttjets = ["./v21/TTJets.root"]
    listsig1 = ["./v22/GMSB_L"+lamb+"-CTAU"+ctau1+".root"]
    listsig2 = ["./v22/GMSB_L"+lamb+"-CTAU"+ctau2+".root"]
    listdata = ["./v21/Run2012A.root","./v21/Run2012B.root","./v21/Run2012C_1.root","./v21/Run2012C_2.root","./v21/Run2012C_3.root","./v21/Run2012D_1.root","./v21/Run2012D_2.root","./v21/Run2012D_3.root"]
    listdataisolow = ["./v21/Run2012Aisolow.root","./v21/Run2012Bisolow.root","./v21/Run2012C_1isolow.root","./v21/Run2012C_2isolow.root","./v21/Run2012C_3isolow.root","./v21/Run2012D_1isolow.root","./v21/Run2012D_2isolow.root","./v21/Run2012D_3isolow.root"]
    listfakehigh = ["./v21/Run2012Afakehigh.root","./v21/Run2012Bfakehigh.root","./v21/Run2012C_1fakehigh.root","./v21/Run2012C_2fakehigh.root","./v21/Run2012C_3fakehigh.root","./v21/Run2012D_1fakehigh.root","./v21/Run2012D_2fakehigh.root","./v21/Run2012D_3fakehigh.root"]
    listfakelow = ["./v21/Run2012Afakelow.root","./v21/Run2012Bfakelow.root","./v21/Run2012C_1fakelow.root","./v21/Run2012C_2fakelow.root","./v21/Run2012C_3fakelow.root","./v21/Run2012D_1fakelow.root","./v21/Run2012D_2fakelow.root","./v21/Run2012D_3fakelow.root"]
    

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
    vecfilessig1 = []
    for item in listsig1:
        temp = TFile.Open(item)
        vecfilessig1.append(temp)
    vecfilessig2 = []
    for item in listsig2:
        temp = TFile.Open(item)
        vecfilessig2.append(temp)

    #xbins = array('d',[0.,0.1,0.3, 1., 3., 6.])
    xbins = array('d',[0.,0.3, 1., 3., 6.])

    ptpholeadttjet = TH1D("PtPhotonleadingTTJet","",24,0,500)
    ptphosubleadttjet = TH1D("PtPhotonsubleadingTTJet","",12,0,500)
    ptjetleadttjet = TH1D("PtJetleadingTTJet","",12,0,500)
    ptjetsubleadttjet = TH1D("PtJetsubleadingTTJet","",12,0,500)
    dxyttjet = TH1D("DxyTTJet","",4,xbins)
    metttjet = TH1D("METTTJet","",50,0,1000)
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
    phohoverettjet = TH1D("phoHoverETTJet","",50,0,5)
    vechisttjet = [ptpholeadttjet,ptphosubleadttjet,ptjetleadttjet,ptjetsubleadttjet,dxyttjet,metttjet,njetsttjet,nphotttjet,nvertttjet,smajttjet,sminttjet,sigietattjet,etattjet,chadisottjet,nhadisottjet,photisottjet,phohoverettjet]
    
    for each in vechisttjet:
        each.Sumw2()

    vechisttjet = loop(vecfilesttjets, vechisttjet, 0, phot)


    ptpholeadsig1 = TH1D("PtPhotonleadingSignal1","",24,0,500)
    ptphosubleadsig1 = TH1D("PtPhotonsubleadingSignal1","",12,0,500)
    ptjetleadsig1 = TH1D("PtJetleadingSignal1","",12,0,500)
    ptjetsubleadsig1 = TH1D("PtJetsubleadingSignal1","",12,0,500)
    dxysig1 = TH1D("DxySignal1","",4,xbins)
    metsig1 = TH1D("METSignal1","",50,0,1000)
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
    phohoveresig1 = TH1D("phoHoverESignal1","",50,0,5)
    vechissig1 = [ptpholeadsig1,ptphosubleadsig1,ptjetleadsig1,ptjetsubleadsig1,dxysig1,metsig1,njetssig1,nphotsig1,nvertsig1,smajsig1,sminsig1,sigietasig1,etasig1,chadisosig1,nhadisosig1,photisosig1,phohoveresig1]
    
    for each in vechissig1:
        each.Sumw2()

    vechissig1 = loop(vecfilessig1, vechissig1, 0, phot)

    ptpholeadsig2 = TH1D("PtPhotonleadingSignal2","",24,0,500)
    ptphosubleadsig2 = TH1D("PtPhotonsubleadingSignal2","",12,0,500)
    ptjetleadsig2 = TH1D("PtJetleadingSignal2","",12,0,500)
    ptjetsubleadsig2 = TH1D("PtJetsubleadingSignal2","",12,0,500)
    dxysig2 = TH1D("DxySignal2","",4,xbins)
    metsig2 = TH1D("METSignal2","",50,0,1000)
    njetssig2 = TH1D("nJetsSignal2","",15,0,15)
    nphotsig2 = TH1D("nPhotSignal2","",15,0,15)
    nvertsig2 = TH1D("nVertSignal2","",8,0,40)
    smajsig2 = TH1D("sMajSignal2","",20,0,3)
    sminsig2 = TH1D("sMinSignal2","",20,0,0.5)
    sigietasig2 = TH1D("SigmaIetaSignal2","",50,0,0.03)
    etasig2 = TH1D("EtaSignal2","",50,0,2)
    chadisosig2 = TH1D("cHadIsoSignal2","",50,0,5)
    nhadisosig2 = TH1D("nHadIsoSignal2","",50,0,5)
    photisosig2 = TH1D("photIsoSignal2","",50,0,5)
    phohoveresig2 = TH1D("phoHoverESignal2","",50,0,5)
    vechissig2 = [ptpholeadsig2,ptphosubleadsig2,ptjetleadsig2,ptjetsubleadsig2,dxysig2,metsig2,njetssig2,nphotsig2,nvertsig2,smajsig2,sminsig2,sigietasig2,etasig2,chadisosig2,nhadisosig2,photisosig2,phohoveresig2]
    
    for each in vechissig2:
        each.Sumw2()

    vechissig2 = loop(vecfilessig2, vechissig2, 0, phot)


    ptpholead = TH1D("PtPhotonleading","",24,0,500)
    ptphosublead = TH1D("PtPhotonsubleading","",12,0,500)
    ptjetlead = TH1D("PtJetleading","",12,0,500)
    ptjetsublead = TH1D("PtJetsubleading","",12,0,500)
    dxy = TH1D("Dxy","",4,xbins)
    met = TH1D("MET","",50,0,1000)
    njets = TH1D("nJets","",15,0,15)
    nphot = TH1D("nPhot","",15,0,15)
    nvert = TH1D("nVert","",8,0,40)
    smaj = TH1D("sMaj","",20,0,3)
    smin = TH1D("sMin","",20,0,0.5)
    sigieta = TH1D("SigmaIeta","",50,0,0.03)
    eta = TH1D("Eta","",50,0,2)
    chadiso = TH1D("cHadIso","",50,0,5)
    nhadiso = TH1D("nHadIso","",50,0,5)
    photiso = TH1D("photIso","",50,0,5)
    phohovere = TH1D("phoHoverE","",50,0,5)
    vechis = [ptpholead,ptphosublead,ptjetlead,ptjetsublead,dxy,met,njets,nphot,nvert,smaj,smin,sigieta,eta,chadiso,nhadiso,photiso,phohovere]
    
    for each in vechis:
        each.Sumw2()

    vechis = loop(vecfilesdata, vechis, 1, phot)


    ptpholeadisolow = TH1D("PtPhotonleadingisolow","",24,0,500)
    ptphosubleadisolow = TH1D("PtPhotonsubleadingisolow","",12,0,500)
    ptjetleadisolow = TH1D("PtJetleadingisolow","",12,0,500)
    ptjetsubleadisolow = TH1D("PtJetsubleadingisolow","",12,0,500)
    dxyisolow = TH1D("Dxyisolow","",4,xbins)
    metisolow = TH1D("METisolow","",50,0,1000)
    njetsisolow = TH1D("nJetsisolow","",15,0,15)
    nphotisolow = TH1D("nPhotisolow","",15,0,15)
    nvertisolow = TH1D("nVertisolow","",8,0,40)
    smajisolow = TH1D("sMajisolow","",20,0,3)
    sminisolow = TH1D("sMinisolow","",20,0,0.5)
    sigietaisolow = TH1D("SigmaIetaisolow","",50,0,0.03)
    etaisolow = TH1D("Etaisolow","",50,0,2)
    chadisoisolow = TH1D("cHadIsoisolow","",50,0,5)
    nhadisoisolow = TH1D("nHadIsoisolow","",50,0,5)
    photisoisolow = TH1D("photIsoisolow","",50,0,5)
    phohovereisolow = TH1D("phoHoverEisolow","",50,0,5)
    vechisisolow= [ptpholeadisolow,ptphosubleadisolow,ptjetleadisolow,ptjetsubleadisolow,dxyisolow,metisolow,njetsisolow,nphotisolow,nvertisolow,smajisolow,sminisolow,sigietaisolow,etaisolow,chadisoisolow,nhadisoisolow,photisoisolow,phohovereisolow]

    for each in vechisisolow:
        each.Sumw2()

    vechisisolow = loop(vecfilesdataisolow, vechisisolow, 2, phot)

    
    ptpholeadfakehigh = TH1D("PtPhotonleadingfakehigh","",24,0,500)
    ptphosubleadfakehigh = TH1D("PtPhotonsubleadingfakehigh","",12,0,500)
    ptjetleadfakehigh = TH1D("PtJetleadingfakehigh","",12,0,500)
    ptjetsubleadfakehigh = TH1D("PtJetsubleadingfakehigh","",12,0,500)
    dxyfakehigh = TH1D("Dxyfakehigh","",4,xbins)
    metfakehigh = TH1D("METfakehigh","",50,0,1000)
    njetsfakehigh = TH1D("nJetsfakehigh","",15,0,15)
    nphotfakehigh = TH1D("nPhotfakehigh","",15,0,15)
    nvertfakehigh = TH1D("nVertfakehigh","",8,0,40)
    smajfakehigh = TH1D("sMajfakehigh","",20,0,3)
    sminfakehigh = TH1D("sMinfakehigh","",20,0,0.5)
    sigietafakehigh = TH1D("SigmaIetafakehigh","",50,0,0.03)
    etafakehigh = TH1D("Etafakehigh","",50,0,2)
    chadisofakehigh = TH1D("cHadIsofakehigh","",50,0,5)
    nhadisofakehigh = TH1D("nHadIsofakehigh","",50,0,5)
    photisofakehigh = TH1D("photIsofakehigh","",50,0,5)
    phohoverefakehigh = TH1D("phoHoverEfakehigh","",50,0,5)
    vechisfakehigh = [ptpholeadfakehigh,ptphosubleadfakehigh,ptjetleadfakehigh,ptjetsubleadfakehigh,dxyfakehigh,metfakehigh,njetsfakehigh,nphotfakehigh,nvertfakehigh,smajfakehigh,sminfakehigh,sigietafakehigh,etafakehigh,chadisofakehigh,nhadisofakehigh,photisofakehigh,phohoverefakehigh]

    for each in vechisfakehigh:
        each.Sumw2()

    vechisfakehigh = loop(vecfilesfakehigh, vechisfakehigh, 1, phot)

    
    ptpholeadfakelow = TH1D("PtPhotonleadingfakelow","",24,0,500)
    ptphosubleadfakelow = TH1D("PtPhotonsubleadingfakelow","",12,0,500)
    ptjetleadfakelow = TH1D("PtJetleadingfakelow","",12,0,500)
    ptjetsubleadfakelow = TH1D("PtJetsubleadingfakelow","",12,0,500)
    dxyfakelow = TH1D("Dxyfakelow","",4,xbins)
    metfakelow = TH1D("METfakelow","",50,0,1000)
    njetsfakelow = TH1D("nJetsfakelow","",15,0,15)
    nphotfakelow = TH1D("nPhotfakelow","",15,0,15)
    nvertfakelow = TH1D("nVertfakelow","",8,0,40)
    smajfakelow = TH1D("sMajfakelow","",20,0,3)
    sminfakelow = TH1D("sMinfakelow","",20,0,0.5)
    sigietafakelow = TH1D("SigmaIetafakelow","",50,0,0.03)
    etafakelow = TH1D("Etafakelow","",50,0,2)
    chadisofakelow = TH1D("cHadIsofakelow","",50,0,5)
    nhadisofakelow = TH1D("nHadIsofakelow","",50,0,5)
    photisofakelow = TH1D("photIsofakelow","",50,0,5)
    phohoverefakelow = TH1D("phoHoverEfakelow","",50,0,5)
    vechisfakelow = [ptpholeadfakelow,ptphosubleadfakelow,ptjetleadfakelow,ptjetsubleadfakelow,dxyfakelow,metfakelow,njetsfakelow,nphotfakelow,nvertfakelow,smajfakelow,sminfakelow,sigietafakelow,etafakelow,chadisofakelow,nhadisofakelow,photisofakelow,phohoverefakelow]

    for each in vechisfakelow:
        each.Sumw2()

    vechisfakelow = loop(vecfilesfakelow, vechisfakelow, 1, phot)
    

    #dxy.SetBinContent(25,dxy.GetBinContent(26))
    #dxysig.SetBinContent(25,dxysig.GetBinContent(26))
    #dxyttjet.SetBinContent(25,dxyttjet.GetBinContent(26))
    #dxyisolow.SetBinContent(25,dxyisolow.GetBinContent(26))

    
    for i in range(len(vechis)):
        datatotal = vechis[i].Integral()
        ttjettotal = vechisttjet[i].Integral()
        isolowtotal = vechisisolow[i].Integral()
        fakehightotal = vechisfakehigh[i].Integral()
        fakelowtotal = vechisfakelow[i].Integral()
        newisolowtotal = datatotal - ttjettotal
        #print "oldtotal: " + str(isolowtotal) + ", newtotal: " + str(newisolowtotal)

        if(isolowtotal != 0):
            ratio = newisolowtotal/isolowtotal
            ratiofakelow = newisolowtotal/fakelowtotal
            ratiofakehigh = newisolowtotal/fakehightotal
        else:
            ratio = 1.
            ratiofakelow = 1.
            ratiofakehigh = 1.
        vechisisolow[i].Scale(ratio)
        vechisfakelow[i].Scale(ratiofakelow)
        vechisfakehigh[i].Scale(ratiofakehigh)

       #print "old: " + str(isolowtotal) + ", new: " + str(vechisisolow[i].Integral())

    
    datatotal = vechis[4].GetBinContent(1)
    ttjettotal = vechisttjet[4].GetBinContent(1)
    isolowtotal = vechisisolow[4].GetBinContent(1)
    fakehightotal = vechisfakehigh[4].GetBinContent(1)
    fakelowtotal = vechisfakelow[4].GetBinContent(1)
    newisolowtotal = datatotal - ttjettotal

    if(isolowtotal != 0):
        ratio = newisolowtotal/isolowtotal
        ratiofakelow = newisolowtotal/fakelowtotal
        ratiofakehigh = newisolowtotal/fakehightotal
    else:
        ratio = 1.
        ratiofakelow = 1.
        ratiofakehigh = 1.
    vechisisolow[4].Scale(ratio)
    vechisfakelow[4].Scale(ratiofakelow)
    vechisfakehigh[4].Scale(ratiofakehigh)

    
    vechis[4].SetBinContent(3,0.)
    vechis[4].SetBinContent(2,0.)
    """
    vechissig[4].SetBinContent(1,0.)
    vechissig[4].SetBinContent(2,0.)
    vechisttjet[4].SetBinContent(1,0.)
    vechisttjet[4].SetBinContent(2,0.)
    vechisisolow[4].SetBinContent(1,0.)
    vechisisolow[4].SetBinContent(2,0.)
    """

    output = TFile.Open("./ctau"+ctau1+"andctau"+ctau2+"lambda"+lamb+"/output"+str(phot)+".root","recreate")

    for it in vechis:
        it.Write()
    for it in vechisttjet:
        it.Write()
    for it in vechissig1:
        it.Write()
    for it in vechissig2:
        it.Write()
    for it in vechisisolow:
        it.Write()
    for it in vechisfakehigh:
        it.Write()
    for it in vechisfakelow:
        it.Write()

    #ptpho.Write()
    #ptphomc.Write()    
    #ptphosig.Write()    

    output.Close()


def main():
    #function("180","500","500",2)
    #function("180","250","500",2)
    #function("180","50","500",2)
    function("180","10","500",2)

    #function("160","500","500",2)
    #function("160","100","500",2)
    #function("160","50","500",2)
    #function("160","10","500",2)

if __name__ == "__main__":
    main()

