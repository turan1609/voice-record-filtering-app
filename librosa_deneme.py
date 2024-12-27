import librosa
import librosa.display
import matplotlib.pyplot as plt

# Ses dosyasını yükle
#y, sr = librosa.load('voices/Yusuf-male-Aydınlatmayı-en.wav', sr=None)

# MFCC özelliğini çıkar
#mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# MFCC grafiğini oluştur ve göster
#plt.figure(figsize=(10, 6))
#librosa.display.specshow(mfccs, x_axis='time')
#plt.colorbar(label='MFCC Özellikleri')
#plt.title('MFCC Özellikleri')
#plt.show()


# Ses dosyasını yükle
y, sr = librosa.load('voices/Mekkiye-female-Evet-tr.wav', sr=None)

# Genlik grafiğini oluştur
plt.figure(figsize=(10, 6))
librosa.display.waveshow(y, sr=sr)
plt.title('Sesin Genliği (Amplitude)')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Genlik')
plt.show()
