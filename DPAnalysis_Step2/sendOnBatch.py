#! /usr/bin/env python
import os
import sys
import re
import time


pwd = os.environ['PWD']


dataset_name        = ['Run2012A', 'Run2012B_1', 'Run2012B_2', 'Run2012B_3', 'Run2012B_4', 
					   'Run2012C_1', 'Run2012C_2', 'Run2012C_3', 'Run2012C_4', 'Run2012C_5', 
					   'Run2012D_1', 'Run2012D_2', 'Run2012D_3', 'Run2012D_4', 'Run2012D_5', 
					   'GMSB_Lambda-140_CTau-10','GMSB_Lambda-140_CTau-100','GMSB_Lambda-140_CTau-1000', 'GMSB_Lambda-140_CTau-2000', 'GMSB_Lambda-140_CTau-50', 'GMSB_Lambda-140_CTau-500', 
					   'GMSB_Lambda-160_CTau-10', 'GMSB_Lambda-160_CTau-100', 'GMSB_Lambda-160_CTau-1000', 'GMSB_Lambda-160_CTau-2000', 'GMSB_Lambda-160_CTau-50', 'GMSB_Lambda-160_CTau-500', 
					   'GMSB_Lambda-180_CTau-10', 'GMSB_Lambda-180_CTau-2000', 'GMSB_Lambda-180_CTau-250', 'GMSB_Lambda-180_CTau-50', 'GMSB_Lambda-180_CTau-500', 
					   'G_Pt-120to170', 'G_Pt-170to300', 'G_Pt-300to470', 'G_Pt-470to800', 'G_Pt-50to80', 'G_Pt-80to120',
					   'QCD_Pt-120to170', 'QCD_Pt-170to300','QCD_Pt-300to470','QCD_Pt-470to600', 'QCD_Pt-600to800','QCD_Pt-800to1000', 'QCD_Pt-1000to1400', 
			           'TTJets']

queue              	= "1nh" 
executable         	= "tmp/main" 

for z in range(len(dataset_name)):

    inputlist = "list2/"+dataset_name[z]+".list"
    outputdir = pwd+"/ntuples/"+dataset_name[z] 

    os.system("rm -r "+outputdir)
    os.system("mkdir -p "+outputdir)
    os.system("mkdir -p "+outputdir+"/log/")
    os.system("mkdir -p "+outputdir+"/input/")
    os.system("mkdir -p "+outputdir+"/output/")
    os.system("mkdir -p "+outputdir+"/src/")

    outputname = outputdir+"/src/"+dataset_name[z]+".src"
    outputfile = open(outputname,'w')
    outputfile.write('#!/bin/bash\n')
    outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
    outputfile.write('cd '+pwd+'; eval `scramv1 runtime -sh`; \n')
    outputfile.write("./"+executable+" "+inputlist+" "+dataset_name[z]+";")
    outputfile.write("mv "+dataset_name[z]+".root "+outputdir+"/output/;") 
    outputfile.close
    os.system("echo Submitting "+dataset_name[z]+" to batch queue")
    os.system("bsub -q 1nd -o "+outputdir+"/log/"+dataset_name[z]+".log source "+outputname)
