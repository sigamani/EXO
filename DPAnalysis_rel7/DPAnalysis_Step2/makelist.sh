#!/bin/env

set maindir=$1

/bin/ls $maindir >! datasets.txt

echo "Making lists...."
        foreach i (`cat datasets.txt`)
        touch list/$i.list
        /bin/ls   $maindir/$i  | sed 's#[a-z]*#&dcap://maite.iihe.ac.be/'$maindir'/'$i'/#' > & ! list/$i.list  
        end

rm datasets.txt
echo "Done"
