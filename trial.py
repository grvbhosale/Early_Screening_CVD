
import numpy as np
import matplotlib
matplotlib.use("Pdf") 
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
from numpy.lib import stride_tricks
import glob
import os
os.chdir("/home/pi/FY/plot")

path = "/home/pi/FY/audio"

print("Starting proccessing of Audio to spectrogram!")




""" short time fourier transform of audio signal """
def stft(sig, frameSize, overlapFac=0.5, window=np.hanning):
    win = window(frameSize)
    hopSize = int(frameSize - np.floor(overlapFac * frameSize))

    # zeros at beginning (thus center of 1st window should be for sample nr. 0)
    samples = np.append(np.zeros(int(np.floor(frameSize/2.0))), sig)
    # cols for windowing
    cols = np.ceil( (len(samples) - frameSize) / float(hopSize)) + 1
    # zeros at end (thus samples can be fully covered by frames)
    samples = np.append(samples, np.zeros(frameSize))

    frames = stride_tricks.as_strided(samples, shape=(int(cols), frameSize), strides=(samples.strides[0]*hopSize, samples.strides[0])).copy()
    frames *= win
    print("Applying STFT on audio data!")
    return np.fft.rfft(frames)

""" scale frequency axis logarithmically """
def logscale_spec(spec, sr=44100, factor=0.):
    timebins, freqbins = np.shape(spec)

    scale = np.linspace(0, 1, freqbins) ** factor
    scale *= (freqbins-1)/max(scale)
    scale = np.unique(np.round(scale))

    # create spectrogram with new freq bins
    newspec = np.complex128(np.zeros([timebins, len(scale)]))
    for i in range(0, len(scale)):
        if i == len(scale)-1:
            newspec[:,i] = np.sum(spec[:,int(scale[i]):], axis=1)
        else:
            newspec[:,i] = np.sum(spec[:,int(scale[i]):int(scale[i+1])], axis=1)

    # list center freq of bins
    allfreqs = np.abs(np.fft.fftfreq(freqbins*2, 1./sr)[:freqbins+1])
    freqs = []
    for i in range(0, len(scale)):
        if i == len(scale)-1:
            freqs += [np.mean(allfreqs[int(scale[i]):])]
        else:
            freqs += [np.mean(allfreqs[int(scale[i]):int(scale[i+1])])]

    return newspec, freqs

""" plot spectrogram"""



def plotstft(audiopath, binsize=2**10, plotpath=("C:/Users/grvbh/Desktop/fyp/plt/plt_at_un"), colormap="jet"):
    samplerate, samples = wav.read(filename)
    #print(samples)
    s = stft(samples, binsize)
    #samples=samples/8
    #print(len(samples))
    sshow, freq = logscale_spec(s, factor=1.0, sr=samplerate)

    ims = 20.*np.log10(np.abs(s)/10e-6) # amplitude to decibel
    #print(np.shape(ims))
    timebins, freqbins = np.shape(ims)
    #print(freqbins)
    #print("timebins: ", timebins)
    #print("freqbins: ", freqbins)

    #print(freqbins)


    plt.figure(figsize=(15, 7.5))
    plt.imshow(np.transpose(ims), origin="lower", aspect="auto", cmap=colormap, interpolation="none")
    #plt.colorbar()
    #plt.axis([0, 10, 0, 300])
    #print(ims)

    #plt.xlabel("time (s)")
    #plt.ylabel("frequency (hz)")
    plt.xlim([0, timebins-1])
    #plt.ylim(0,250)

    plt.ylim([0, freqbins])

    xlocs = np.float32(np.linspace(0, timebins-1, 5))
    plt.xticks(xlocs, ["%.02f" % l for l in ((xlocs*len(samples)/timebins)+(0.5*binsize))/samplerate])
    ylocs = np.int16(np.round(np.linspace(0, freqbins-1, 10)))
    plt.yticks(ylocs, ["%.02f" % freq[i] for i in ylocs])
    from pathlib import Path

    #pathforplot="C:/Users/grvbh/Desktop/fyp/plt"

    filenamexd=(Path(filename).resolve().stem)

    plt.savefig(filenamexd+".png", bbox_inches="tight")
    #print(fffy)
    print("Saving STFT spectrogram !")
    plt.close()

    return ims

import os,wave
files=glob.glob(path)
for filename in glob.glob(os.path.join(path, '*.wav')):
    #print(filename)
    ims = plotstft(filename)
    #filename.close()
