#!/bin/bash
 
cd /dev/ ; sudo chmod og+rwx gpio*

cd /home/ubuntu/Rasberry-pi-light-control
screen -S light -dm bash -c "python3 main.py"

