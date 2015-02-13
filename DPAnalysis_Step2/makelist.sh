#!/bin/env

set maindir=$1

eos ls $maindir >! datasets.txt

echo "Making lists...."
        foreach i (`cat datasets.txt`)
        touch list/$i.list
        eos ls   $maindir/$i  | sed 's#[a-z]*#&root://eoscms/'$maindir'/'$i'/#' > & ! list2/$i.list  
        end

rm datasets.txt
echo "Done"
