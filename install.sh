#!/bin/bash
pip3 install -r requirements.txt 
sudo cp $(readlink -f argus.py) ${PATH%%:*}/argus
