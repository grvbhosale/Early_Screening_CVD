# Early_Screening_CVD
Capstone Project -Early Screening for Cardiovascular Disorders 


Listening via Stethoscope is primary way by which method, being used by physicians for distinguishing
normally and abnormal cardiac systems.

Built a lowcost, portable device using Raspi-Zero as primary micro-controller to record heartbeat sounds using stethoscope ,this audio is then send to prepossessing pipeline consisting of a filters such as of Low-Pass Filter and (STFT)Short time Fourier Transform algorithm to output Spectral Images of Sound .

These images serve as input to our Convolutional Neural Network deployed on Google Cloud AI Platform, to serve predictions in few seconds as normal or abnormal heart-sounds.

Accuracy - 93% , False Negative - 5.47%  False Positives - 2.3%

This project is done under patial fulfilment of B.tech Degree from Symbiosis.
Please refer to the report for detailed understanding and implementation of hardware and software.

This Project titled Early Screening for Cardiovascular Disorders aims to provide a low-cost
solution to mitigate the severe lack of medical and healthcare workers in the rural parts of the
country. The WHO states that heart-related diseases are the number one cause of death globally,
with three-quarters occurring in developing countries. In India, the doctor-patient ratio is less
than the WHO-prescribed limit of 1:1000 with rural areas bearing the maximum brunt. The
solution proposed by us aims to assist any worker or volunteer with no prior experience or skill
in the medical industry to detect murmurs or arrhythmia in the heart sounds of the test subject,
which could be symptoms for heart complications typically detected by experienced doctors. The
Project aims to equip the frontline workers with a tool that can effectively and quickly conduct a
primary screening on hundreds of possible patients and deliver the result in real-time. This is
possible with a mobile device consisting of a microcontroller and a sensor with connectivity. The
microcontroller is a Raspberry Pi unit with a sound card, specialized microphone, and chest piece
of the stethoscope. The heart sound is stored into Raspberry Pi and then uploaded onto cloud
storage for further processing and storage. We use Low Pass filters and Short Time Fourier
Transform as preprocessing techniques to the neural network deployed on the Cloud, the data is
sent onto Cloud, and Convolutional Neural Network provides the response to the user in a short
interval of time. The network is trained on Pascal and PhysioNet datasets with data collected
from digital stethoscopes. Since the training data used was measured with the digital stethoscope,
we build our own to deliver the same data while mimicking the actual input. The classification
accuracy of the model is 92%, which is achieved with the current model. However, as per the
various literature, it can be further improved with an increase in the amount of training data. The
system can be used for preliminary screening of CVD and can be integrated to support doctors so
they can work on further diagnosis and testing.
