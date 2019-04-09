#!/bin/bash

sudo mn -c;
python dumbbelltopology.py 21ms westwood 1000;
sudo mn -c;
python dumbbelltopology.py 81ms westwood 1000;
sudo mn -c;
python dumbbelltopology.py 162ms westwood 1000;

sudo mn -c;
python dumbbelltopology.py 21ms htcp 1000;
sudo mn -c;
python dumbbelltopology.py 81ms htcp 1000;
sudo mn -c;
python dumbbelltopology.py 162ms htcp 1000;

git pull;
git add .
git commit -m 'automaically uploading'
git push;


