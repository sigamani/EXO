EXO-DisplacedPhotons
====================

Displaced photons package 

scramv1 project -n CMSSW_7_1_0_DP CMSSW CMSSW_7_1_0

cd CMSSW_7_1_0_DP/src/ 

git clone https://github.com/sigamani/EXO

git fetch https://github.com/sigamani/EXO rel7:rel7

cd EXO

tar -xvf RecoMET.tar 

scramv1 b clean ; scramv1 b

The next step should be to run over some AOD files, but that doesn't quite work yet.
