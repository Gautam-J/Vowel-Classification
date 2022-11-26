import pickle
import librosa
import numpy as np
import tensorflow as tf
import sounddevice as sd
from scipy.io.wavfile import write


def extract_mfcc(file_name, pad_len=40, n_mfcc=15):
    """Function used to extract MFCCs from audio data.

    Computes MEL Coefficients for an audio file.

    Args:
        file_name (str): Path to the audio file along with extension.
        pad_len (int): Number of samples to use.
            Default: 40 (approx. 4 seconds)
        n_mfcc (int): Number of MEL coefficients to compute.

    Returns:
        mfccs (np.array): 2D array of shape (n_mfcc, pad_len)
    """

    signal, sr = librosa.load(file_name, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=n_mfcc)

    if mfccs.shape[1] > pad_len:
        mfccs = mfccs[:, :pad_len]
    else:
        pad_width = pad_len - mfccs.shape[1]
        mfccs = np.pad(mfccs, ((0, 0), (0, pad_width)), mode='constant')

    return mfccs


def class_to_category(c):
    if c == 0:
        return 'a'
    if c == 1:
        return 'i'
    if c == 2:
        return 'u'


model = tf.keras.models.load_model('./models/best.h5')

with open('./models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

freq = 44100  # Sampling frequency
duration = 3  # Recording duration

recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=1)

print('Speak now...')
sd.wait()
print('Processing...')
write("./recordings/recording0.wav", freq, recording)

x = extract_mfcc('./recordings/recording0.wav')
x = np.mean(x, axis=1)
x = x.reshape(1, -1)
x = scaler.transform(x)
pred_prob = model.predict(x)[0]
c = np.argmax(pred_prob)
confidence_score = pred_prob[c]
prediction = class_to_category(c)

print('Prediction:', prediction)
print(pred_prob)
