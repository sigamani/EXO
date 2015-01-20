#! /usr/bin/env python
import os
import sys
import re
import time


pwd = os.environ['PWD']


PDname 		    = sys.argv[1]


dataset_path = PDname 
dataset_name = PDname 
inputlist = "list/"+dataset_name

dir = "ntuples/"+dataset_path
dirout = pwd + "/" + dir



os.system("rm -r "+dir)
os.system("mkdir -p "+dir)
os.system("mkdir -p "+dir+"/log/")
os.system("mkdir -p "+dir+"/input/")
os.system("mkdir -p "+dir+"/output/")
os.system("mkdir -p "+dir+"/src/")


#######################################
input = open(inputlist)
inputfiles = input.readlines()
######################################

ijob=0

while (len(inputfiles) > 0):
    inputfilename = dir+"/input/input_"+str(ijob)
    inputfile = open(inputfilename,'w')
    for line in range(min(1,len(inputfiles))):
        ntpfile = inputfiles.pop()
        if ntpfile != '':
            inputfile.write(ntpfile)

    inputfile.close()

######################################


    outputname = dir+"/src/"+dataset_name+"_"+str(ijob)+".src"
    outputfile = open(outputname,'w')
    #outputfile.write('#!/bin/bash\n')
    #outputfile.write('source $VO_CMS_SW_DIR/cmsset_default.sh\n')
    #outputfile.write('export SCRAM_ARCH=slc5_amd64_gcc462\n')
    outputfile.write('cd '+pwd[0:]+';eval `scramv1 runtime -sh` \n')
    outputfile.write("./tmp/main list/"+dataset_name+" "+dataset_name+";")

    outputfile.close
    os.system('echo bsub -q 8nh "<" '+pwd+'/'+ dir+'/src/'+dataset_name+'_'+str(ijob)+'.src'+' -o ' +dirout[0:]+'/log/'+dataset_name+"_"+str(ijob)+'.out' + ' -e '+dirout[0:]+'/log/'+dataset_name+"_"+str(ijob)+'.stderr ')
    #os.system('echo bsub -q 8nh -o '+dirout[0:]+'/log/'+dataset_name+"_"+str(ijob)+'.out < '+ pwd+'/'+ dir+'/src/'+dataset_name+'_'+str(ijob)+'.src')
    #os.system('qsub -q localgrid@cream02 -o '+dirout[14:]+'/log/'+dataset_name+"_"+str(ijob)+'.stdout -e '+dirout[14:]+'/log/'+dataset_name+"_"+str(ijob)+'.stderr '+dir+'/src/'+dataset_name+'_'+str(ijob)+'.src')
    ijob = ijob+1
    continue
