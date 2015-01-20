from ROOT import *
from array import array
from math import fabs, sqrt

def function (lamb.ctau):

    rootfile = TFile.Open("./v22/GMSB_L"+lamb+"-CTAU"+ctau1+"_lowmet.root")
    
    dxy = gROOT.FindObject("....")
    
    return [dxy.Integral(),lamb,ctau]

def main():
    
    dxy = [None]*8
    
    dxy[0] = function("180","10")
    dxy[1] = function("180","50")
    dxy[2] = function("180","250")
    dxy[3] = function("180","500")

    dxy[4] = function("160","10")
    dxy[5] = function("160","50")
    dxy[6] = function("160","100")
    dxy[7] = function("160","500")

    f = open("signalinlowmetregion.txt","w")

    for i in dxy:
        f.write("Events for lambda " + i[1] + " and ctau " + i[2] + ": " + str(i[0]) + "\n")
    f.close()

if __name__ == "__main__":
    main()

