#!/bin/bash

sudo mn -c;
python dumbbelltopology.py 21ms reno 500;
sudo mn -c;
python dumbbelltopology.py 81ms reno 500;
sudo mn -c;
python dumbbelltopology.py 162ms reno 500;

sudo mn -c;
python dumbbelltopology.py 21ms vegas 500;
sudo mn -c;
python dumbbelltopology.py 81ms vegas 500;
sudo mn -c;
python dumbbelltopology.py 162ms vegas 500;


git pull;
git add .
git commit -m 'automaically uploading'
git push;


