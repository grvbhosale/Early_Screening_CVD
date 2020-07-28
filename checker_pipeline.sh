#!/bin/bash

while [ true ] 

sleep 10

do

if [ -f /home/pi/FY/audio/*.wav ];

then
cp /home/pi/FY/audio/*.wav /home/pi/rpi-sync
python /home/pi/FY/trial.py
echo "Pushing the audio file onto cloud database"
/home/pi/rclone-push.sh
python /home/pi/FY/pipeline.py
sleep 5
rm /home/pi/FY/audio/*.wav
rm /home/pi/rpi-sync/*.wav
echo “File exists”


else

echo "File does not exists"

fi
done

