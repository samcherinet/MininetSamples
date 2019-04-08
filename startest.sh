#!/bin/bash

sudo mn -c;
python dumbbelltopology.py 21ms reno 1000;
sudo mn -c;
python dumbbelltopology.py 81ms reno 1000;
sudo mn -c;
python dumbbelltopology.py 162ms reno 1000;

sudo mn -c;
python dumbbelltopology.py 21ms bic 1000;
sudo mn -c;
python dumbbelltopology.py 81ms bic 1000;
sudo mn -c;
python dumbbelltopology.py 162ms bic 1000;

sudo mn -c;
python dumbbelltopology.py 21ms vegas 1000;
sudo mn -c;
python dumbbelltopology.py 81ms vegas 1000;
sudo mn -c;
python dumbbelltopology.py 162ms vegas 1000;

sudo mn -c;
python dumbbelltopology.py 21ms scalable 1000;
sudo mn -c;
python dumbbelltopology.py 81ms scalable 1000;
sudo mn -c;
python dumbbelltopology.py 162ms scalable 1000;

git pull;
git add .
git commit -m 'automaically uploading'
git push;


