# Early_Screening_CVD
Capstone Project -Early Screening for Cardiovascular Disorders 


Listening via Stethoscope is primary way by which method, being used by physicians for distinguishing
normally and abnormal cardiac systems.

Built a lowcost, portable device using Raspi-Zero as primary micro-controller to record heartbeat sounds using stethoscope ,this audio is then send to prepossessing pipeline consisting of a filters such as of Low-Pass Filter and (STFT)Short time Fourier Transform algorithm to output Spectral Images of Sound .

These images serve as input to our Convolutional Neural Network deployed on Google Cloud AI Platform, to serve predictions in few seconds as normal or abnormal heart-sounds.

Accuracy - 93% , False Negative - 5.47%  False Positives - 2.3%

This project is done under patial fulfilment of B.tech Degree from Symbiosis .
