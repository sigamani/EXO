from ROOT import *

def function():

    files = ["./v18/GMSB_L180-CTAU10.root","./v18/GMSB_L180-CTAU50.root","./v18/GMSB_L180-CTAU250.root","./v18/GMSB_L180-CTAU500.root"]
    vecfiles = []
    
    for item in files:
        temp = TFile.Open(item)
        vecfiles.append(temp)
    
    
    
def main():
    function()

if __name__ == "__main__":
    main()

