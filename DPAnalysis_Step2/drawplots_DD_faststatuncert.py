from ROOT import *
from tdrStyle import *
from array import *
    
statismet = 30
statisptphot = 85

def function(pho,ctau,statmet,statptphot,lamb):
    input = TFile.Open("./ctau"+ctau+"lambda"+str(lamb)+"/output"+str(pho)+"MET"+str(statmet)+"PtPhot"+str(statptphot)+".root")
    
    vecdxy = [input.Get("DxySignal1"),input.Get("DxySignal1PtUp"),input.Get("DxySignal1PtDown"),input.Get("DxySignal1PhoUp"),input.Get("DxySignal1PhoDown"),input.Get("DxySignal1MetUp"),input.Get("DxySignal1MetDown")]

    #vecdxy = [input.Get("DxySignal1")]
       
    sig = []

    
    for each in vecdxy:
        sig.append(each.Integral())

    return sig


#function(2,"250",30,85,180)

output = open("./cutflowMET"+str(30)+"PtPhot"+str(85)+".tex","w")


output.write(str(function(2,"250",30,85,180)[0]) + '\n')
output.write(str(function(2,"250",30,85,180)[1]) + '\n')
output.write(str(function(2,"250",30,85,180)[2]) + '\n')
output.write(str(function(2,"250",30,85,180)[3]) + '\n')
output.write(str(function(2,"250",30,85,180)[4]) + '\n')
output.write(str(function(2,"250",30,85,180)[5]) + '\n')
output.write(str(function(2,"250",30,85,180)[6]) + '\n')

output.close()
