#! /usr/bin/env python
import os
import sys
import re
import time


pwd = os.environ['PWD']

decay_mode 		= ['S180-N10'] 
#decay_mode 	= ['T2bw025'] 

outputdir = pwd
output = "datacard-"+str(decay_mode[0])
outputname = outputdir+"/"+output+".src"

outputfile = open(outputname,'w')
outputfile.write('#!/bin/bash\n')
outputfile.write('export SCRAM_ARCH=slc6_amd64_gcc472\n')
outputfile.write('cd '+outputdir+'; eval `scramv1 runtime -sh`; \n')
#outputfile.write('cd /tmp/sigamani; \n')
#outputfile.write('cp /afs/cern.ch/work/s/sigamani/public/CMSSW_6_1_1/bin/slc5_amd64_gcc472/combine .; \n')
#outputfile.write('cp /afs/cern.ch/work/s/sigamani/public/CMSSW_6_1_1/src/HiggsAnalysis/CombinedLimit/limit_V2 .; \n')
#outputfile.write('cp '+outputdir+'/'+output+'.txt . ; \n')
outputfile.write('./limit_V2 '+output+'.txt ; \n') 
outputfile.write('hadd -f '+outputdir+'/FULL_CLS_RESULT_'+str(decay_mode[0])+'.root higgsCombineTest.HybridNew.mH120.* ; \n') 
outputfile.write('cp higgsCombineTest.Asymptotic.mH120.root '+outputdir+'/ASYMPTOTIC_CLS_RESULT_S'+str(decay_mode[0])+'.root; \n')
outputfile.write('rm higgsCombineTest.HybridNew.mH120.* ; \n') 
outputfile.write('cp datacard-'+str(decay_mode[0])+'.txt.result.txt '+outputdir+'/RESULT_S'+str(decay_mode[0])+'.txt; \n')
outputfile.write('rm higgsCombine*root; \n')
outputfile.close
os.system("echo bsub -q 1nd -o "+outputdir+"/"+output+".log source "+outputname)
os.system("bsub -q 1nd -o "+outputdir+"/"+output+".log source "+outputname)
