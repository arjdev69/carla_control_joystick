#!/bin/sh
mkdir CARLA
git clone https://cimatecvr@bitbucket.org/cimatecvr/kamino.git
cd kamino
mv CARLA_0.8.4.tar.gz ../CARLA
cd ../CARLA
tar xvzf CARLA_0.8.4.tar.gz

