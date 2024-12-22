import sys
import sqlite3
import wave
import pyaudio
from PyQt5.QtWidgets import QApplication, QDialog
from voiceRecorderDialog import Ui_voiceRecorderDialog
from PyQt5.QtCore import QTimer



class VoiceRecorder(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_voiceRecorderDialog()
        self.ui.setupUi(self)
        
        # Bağlantıları ayarlama
        self.ui.pushButtonDialogRecordVoice.clicked.connect(self.toggle_recording)

        # Kayıt durumu ve ses parametreleri
        self.is_recording = False
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []

        # SQLite veri tabanı bağlantısı
        self.conn = sqlite3.connect("veritabani.db")
        self.cursor = self.conn.cursor()
        self.create_table()

         # QTimer tanımlaması
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.record_audio)  # Timer her çalıştığında ses kaydedecek

    def create_table(self):
        # Eğer yoksa tabloyu oluştur
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS voice(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,   \
                 Language TEXT NOT NULL,                       \
                 Gender TEXT NOT NULL,                         \
                 Name TEXT NOT NULL,                      \
                 Commend TEXT NOT NULL,                          \
                 Url TEXT NOT NULL UNIQUE,                             \
                 Status BOOLEAN NOT NULL )''')
        self.conn.commit()

    def toggle_recording(self):
        
        if not self.is_recording:
            self.is_recording = True
            self.frames = []
            
            self.stream = self.audio.open(format=pyaudio.paInt16,
                                           channels=1,
                                           rate=44100,
                                           input=True,
                                           frames_per_buffer=1024)
            self.ui.pushButtonDialogRecordVoice.setText("Kaydı Durdur")
            self.timer.start(1)# Her 100ms'de bir ses kaydedilecek
            print("Kayıt başladı...")
            
        else:
            # Kayıt durdur
            self.is_recording = False
            self.timer.stop()
            self.stream.stop_stream()
            self.stream.close()
            self.ui.pushButtonDialogRecordVoice.setText("Başla/Bitir")
            print("Kayıt durduruldu.")
            self.save_recording()
    
    def record_audio(self):
        #Her 100ms'de bir ses kaydedecek
        data = self.stream.read(1024)
        self.frames.append(data)        

    def save_recording(self):
        name = self.ui.lineEditDialog.text()
        commend = self.ui.lineEditDialog_2.text()
        english_selected_record = self.ui.radioButtonDialogLanguageEnglish.isChecked()
        turkish_selected_record = self.ui.radioButtonDialogLanguageTurkish.isChecked()

        # Cinsiyet kontrolleri
        male_selected_record = self.ui.radioButtonDialogGenderMale.isChecked()
    
        female_selected_record = self.ui.radioButtonDialogGenderFemale.isChecked()

        # Seçilen dillerin listesini oluştur

        if turkish_selected_record:
            languages="tr"
        if english_selected_record:
            languages="en"

        # Seçilen cinsiyetlerin listesini oluştur
        
        if male_selected_record:
          genders = "male"
        if female_selected_record:
         genders= "female"    
        
        file_path = f"voices\{name.replace(' ', '_')+"-"+genders.replace(' ', '_')+"-"+commend.replace(' ', '_')+"-"+languages.replace(' ', '_')}.wav"
        file_path2 = f"{name.replace(' ', '_')+"-"+genders.replace(' ', '_')+"-"+commend.replace(' ', '_')+"-"+languages.replace(' ', '_')}.wav"
        status=0

        # Ses kaydını dosyaya yaz
        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))
            print("wav dosyasına dönüştürüldü.")

        # Veriyi veri tabanına ekle
        self.cursor.execute("""
            INSERT INTO voice (Language, Gender, Name, Commend, Url, Status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (languages, genders, name, commend, file_path2, status))
        self.conn.commit()
        

        print(f"Kayıt başarıyla kaydedildi: {file_path}")

    def closeEvent(self, event):
        # Program kapandığında kaynakları temizle
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()
        self.conn.close()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    recorder = VoiceRecorder()
    recorder.show()
    sys.exit(app.exec_())
    
