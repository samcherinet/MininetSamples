#!/bin/bash

sudo mn -c;
python dumbbelltopology.py 21ms bic 100;
sudo mn -c;
python dumbbelltopology.py 81ms bic 100;
sudo mn -c;
python dumbbelltopology.py 162ms bic 100;

sudo mn -c;
python dumbbelltopology.py 21ms scalable 100;
sudo mn -c;
python dumbbelltopology.py 81ms scalable 100;
sudo mn -c;
python dumbbelltopology.py 162ms scalable 100;

git pull;
git add .
git commit -m 'automaically uploading'
git push;


