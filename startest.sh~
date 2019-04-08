#!/bin/bash

sudo mn -c;
python dumbbelltopology.py 21ms reno 100;
sudo mn -c;
python dumbbelltopology.py 81ms reno 100;
sudo mn -c;
python dumbbelltopology.py 162ms reno 100;

sudo mn -c;
python dumbbelltopology.py 21ms bic 100;
sudo mn -c;
python dumbbelltopology.py 81ms bic 100;
sudo mn -c;
python dumbbelltopology.py 162ms bic 100;

sudo mn -c;
python dumbbelltopology.py 21ms vegas 100;
sudo mn -c;
python dumbbelltopology.py 81ms vegas 100;
sudo mn -c;
python dumbbelltopology.py 162ms vegas 100;

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


