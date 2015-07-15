#step1
#mkdir $1
#cd $1
#cp ../../../../gridpacks/$1_tarball.tar.xz .
#tar xavf $1_tarball.tar.xz
#cd ..
#step2
#cd $1
#./runcmsgrid.sh 5000 1 1
#cd ..
#step3
#echo $1
#cp /afs/cern.ch/work/e/eusai/public/tests/CMSSW_7_1_14/src/$1/cmsgrid_final.lhe $1.lhe
#step4
#cmsRun gen.py $1 &
#step5
python create-dbs.py /nfs/dust/cms/user/usaiem/gen/ZpVLQ/ $1.root
