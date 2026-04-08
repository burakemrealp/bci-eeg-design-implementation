import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import pandas as pd

file = 'C:\\Users\\burak\\Documents\\BYB\\BYB_Recording_2022-06-03_19.04.27.wav'
fs, data = waves.read(file)

length_data = np.shape(data)
length_new = length_data[0] * 0.05
ld_int = int(length_new)

from scipy import signal
data_new = signal.resample(data, ld_int)

plt.figure('Spectrogram')
d, f, t, im = plt.specgram(data_new, NFFT=256, Fs=500, noverlap=250)
plt.ylim(0, 90)
plt.colorbar(label="Power/Frequency")
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.savefig("Spectrogram.jpeg")
plt.show()

matrixf = np.array(f).T
df = pd.DataFrame(matrixf, columns=['Frequencies'])
df.to_csv("Frequencies.csv", index=False)

position_vector = []
length_f = np.shape(f)
l_row_f = length_f[0]

for i in range(0, l_row_f):
    if f[i] >= 7 and f[i] <= 12:
        position_vector.append(i)

length_d = np.shape(d)
l_col_d = length_d[1]
AlphaRange = []

for i in range(0, l_col_d):
    AlphaRange.append(np.mean(d[position_vector[0]:max(position_vector)+1, i]))

def smoothTriangle(data, degree):
    triangle = np.concatenate((np.arange(degree + 1), np.arange(degree)[::-1]))
    smoothed = []
    for i in range(degree, len(data) - degree * 2):
        point = data[i:i + len(triangle)] * triangle
        smoothed.append(np.sum(point) / np.sum(triangle))
    smoothed = [smoothed[0]] * int(degree + degree/2) + smoothed
    while len(smoothed) < len(data):
        smoothed.append(smoothed[-1])
    return smoothed

plt.figure('AlphaRange')
y = smoothTriangle(AlphaRange, 100)
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.xlim(0, max(t))

datosy = np.asarray(y)
datosyt1 = pd.DataFrame(datosy, columns=["Power"])
datosyt2 = pd.DataFrame(t, columns=["Time"])
datosyt = pd.concat([datosyt1, datosyt2], axis=1)
datosyt.to_csv("datosyt.csv", index=False)

tg = np.array([
    4.2552, 14.9426, 23.2801, 36.0951, 45.4738,
    59.3751, 72.0337, 85.0831, max(t) + 1
])

length_t = np.shape(t)
l_row_t = length_t[0]

eyesclosed = []
eyesopen = []

j = 0
l = 0

for i in range(0, l_row_t):
    if t[i] >= tg[j]:
        if j % 2 == 0:
            eyesopen.append(np.mean(datosy[l:i]))
        if j % 2 == 1:
            eyesclosed.append(np.mean(datosy[l:i]))
        l = i
        j = j + 1

plt.figure('DataAnalysis')
plt.boxplot([eyesopen, eyesclosed], sym='ko', whis=1.5)
plt.xticks([1, 2], ['Eyes open', 'Eyes closed'], size='small', color='k')
plt.ylabel('AlphaPower')

meanopen = np.mean(eyesopen)
meanclosed = np.mean(eyesclosed)
sdopen = np.std(eyesopen)
sdclosed = np.std(eyesclosed)

eyes = np.array([eyesopen, eyesclosed])

from scipy import stats
result = stats.ttest_ind(eyesopen, eyesclosed, equal_var=False)
print(result)