#-------------------- KÜTÜPHANE --------------------
import sys
import os
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from voiceCommandDatabase import *
from voice_record_page import VoiceRecorder
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
import numpy as np
from pydub import AudioSegment
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import shutil
import sys
import sqlite3
import wave
import pyaudio
from PyQt5.QtWidgets import QApplication, QDialog
from voiceRecorderDialog import Ui_voiceRecorderDialog  # Sizin UI dosyanız
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QRadioButton, QVBoxLayout, QWidget
from PyQt5.uic import loadUi


#-------------------- Ses Dalgası --------------------
class AudioWaveformWidget(QGraphicsView):
    def __init__(self, file_path, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.file_path = file_path
        self.load_waveform()

    def load_waveform(self):
        # Ses dosyasını yükle
        try:
            audio = AudioSegment.from_file(self.file_path)
            samples = np.array(audio.get_array_of_samples())

            # Normalize et
            samples = samples / np.max(np.abs(samples))

            # Dalga formunu çiz
            pen = QPen(Qt.blue)
            pen.setWidth(1)

            width = 200  # Dalga formu genişliği
            height = 200  # Dalga formu yüksekliği
            self.setFixedSize(width, height)

            #half_height = height // 2
            step = max(1, len(samples) // width)  # Ekran genişliğine göre örnekleme

            for i in range(0, len(samples), step):
                x = i // step
                y = int(height * samples[i])  # Genliği ölçekle
                self.scene.addLine(x, height, x, height - y, pen)

        except Exception as e:
            print(f"Error loading waveform: {e}")


#---------------- ÖZEL WIDGET TANIMI ---------------
class CustomWidget(QtWidgets.QWidget):
    def __init__(self, name, language, gender, commend, file_name):
        super().__init__()

        self.name = name
        self.language = language
        self.gender = gender
        self.commend = commend
        self.file_name = file_name

        layout = QtWidgets.QHBoxLayout(self)

        # Border'ı ayarla
        self.setStyleSheet(
            "border-style: solid;"
            "border-width: 3px;"
            "border-color: #4d4018;"
        )

        # Media Player
        self.player = QMediaPlayer()
        self.player.setVolume(100)

        # Play Butonu
        self.pushButtonCardExamplePlay = QPushButton('Play')
        self.pushButtonCardExamplePlay.setStyleSheet(
            "QPushButton {"
            "border-style: solid;"
            "border-width: 3px;"
            "background-color: #ff6d49;"
            "border-color: #4d4018;"
            "color: black;"
            "}"
            "QPushButton:hover {"
            "background-color: red;"
            "}"
        )
        layout.addWidget(self.pushButtonCardExamplePlay)

        # Play Button'a tıklayınca sesi çalma
        voices_folder = os.path.join(os.path.dirname(__file__), 'voices')
        file_path = os.path.join(voices_folder, file_name)
        self.pushButtonCardExamplePlay.clicked.connect(lambda: self.play_sound(file_path))

        # Language Label
        self.labelCardExampleLanguage = QLabel(language)
        self.labelCardExampleLanguage.setStyleSheet(
            "background-color: #ff9b0f;"
            "color: black;"
            "border-color: #4d4018;"
        )
        self.labelCardExampleLanguage.setFixedSize(50, 30)
        layout.addWidget(self.labelCardExampleLanguage)

        # Gender Label
        self.labelCardExampleGender = QLabel(gender)
        self.labelCardExampleGender.setStyleSheet(
            "background-color: #ff9b0f;"
            "color: black;"
            "border-color: #4d4018;"
        ),
        self.labelCardExampleGender.setFixedSize(50, 30)
        layout.addWidget(self.labelCardExampleGender)

        # Name Label
        self.labelCardExampleName = QLabel(name)
        self.labelCardExampleName.setStyleSheet(
            "background-color: #ff9b0f;"
            "color: black;"
            "border-color: #4d4018;"
        )
        self.labelCardExampleName.setFixedSize(70, 30)
        layout.addWidget(self.labelCardExampleName)

        # Voice Command Label
        self.labelCardExampleCommend = QLabel(commend)
        self.labelCardExampleCommend.setStyleSheet(
            "background-color: #ff9b0f;"
            "color: black;"
            "border-color: #4d4018;"
        )
        self.labelCardExampleCommend.setFixedSize(70, 30)
        layout.addWidget(self.labelCardExampleCommend)

        # Düzenle Butonu
        self.pushButtonEdit = QPushButton('Edit')
        self.pushButtonEdit.setStyleSheet(
            "QPushButton {"
            "border-style: solid;"
            "border-width: 3px;"
            "background-color: #add8e6;"
            "border-color: #4d4018;"
            "color: black;"
            "}"
            "QPushButton:hover {"
            "background-color: #87ceeb;"
            "}"
        )
        self.pushButtonEdit.clicked.connect(self.edit_properties)
        layout.addWidget(self.pushButtonEdit)

        # Sil Butonu
        self.pushButtonDelete = QPushButton('Delete')
        self.pushButtonDelete.setStyleSheet(
            "QPushButton {"
            "border-style: solid;"
            "border-width: 3px;"
            "background-color: #ff6d49;"
            "border-color: #4d4018;"
            "color: black;"
            "}"
            "QPushButton:hover {"
            "background-color: red;"
            "}"
        )
        layout.addWidget(self.pushButtonDelete)

        # Download Butonu
        self.pushButtonDownload = QPushButton('Download')
        self.pushButtonDownload.setStyleSheet(
            "QPushButton {"
            "border-style: solid;"
            "border-width: 3px;"
            "background-color: #ff6d49;"
            "border-color: #4d4018;"
            "color: black;"
            "}"
            "QPushButton:hover {"
            "background-color: red;"
            "}"
        )
        layout.addWidget(self.pushButtonDownload)


        # Ses Dalga Formu Widget'ını ekle
        self.audio_waveform_widget = AudioWaveformWidget(file_path)
        layout.addWidget(self.audio_waveform_widget)

    # Ses Çalma Fonksiyonu
    def play_sound(self, file_path):
        if os.path.exists(file_path):  # Dosyanın mevcut olup olmadığını kontrol et
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            self.player.play()
        else:
            print(f"Ses dosyası bulunamadı: {file_path}")

    # Özellikleri Düzenleme Fonksiyonu
    def edit_properties(self):
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Edit Properties")

        layout = QtWidgets.QFormLayout(dialog)

        # QLabel'lar ekle ve stil uygula
        name_label = QtWidgets.QLabel("Name:")
        name_label.setStyleSheet(
            "color: red;"
            "font-weight: bold;"
            "font-size: 12px;"
            
            "padding: 2px;"
            "border: 1px solid #4d4018;"
            "border-radius: 3px;"
        )
        language_label = QtWidgets.QLabel("Language:")
        language_label.setStyleSheet(
            "color: red;"
            "font-style: italic;"
            "font-size: 12px;"
            
            "padding: 2px;"
            "border: 1px solid #4d4018;"
            "border-radius: 3px;"
        )
        gender_label = QtWidgets.QLabel("Gender:")
        gender_label.setStyleSheet(
            "color: red;"
            "font-size: 12px;"
            
            "padding: 2px;"
            "border: 1px solid #4d4018;"
            "border-radius: 3px;"
        )
        commend_label = QtWidgets.QLabel("Commend:")
        commend_label.setStyleSheet(
            "color: red;"
            "font-weight: bold;"
            "font-size: 12px;"
            
            "padding: 2px;"
            "border: 1px solid #4d4018;"
            "border-radius: 3px;"
        )

        name_input = QtWidgets.QLineEdit(self.name)
        name_input.setStyleSheet(
            "background-color: #f0f0f0;"
            "border: 1px solid #4d4018;"
            "color: black;"

        )
        language_input = QtWidgets.QLineEdit(self.language)
        language_input.setStyleSheet(
            "background-color: #f0f0f0;"
            "border: 1px solid #4d4018;"
            "color: black;"
        )
        gender_input = QtWidgets.QLineEdit(self.gender)
        gender_input.setStyleSheet(
            "background-color: #f0f0f0;"
            "border: 1px solid #4d4018;"
            "color: black;"
        )
        commend_input = QtWidgets.QLineEdit(self.commend)
        commend_input.setStyleSheet(
            "background-color: #f0f0f0;"
            "border: 1px solid #4d4018;"
            "color: black;"
        )

        layout.addRow(name_label, name_input)
        layout.addRow(language_label, language_input)
        layout.addRow(gender_label, gender_input)
        layout.addRow(commend_label, commend_input)

        save_button = QtWidgets.QPushButton("Save")
        save_button.setStyleSheet(
            "background-color: #00FF00;"
            "border: 1px solid #4d4018;"
            "color: black;"
        )
        save_button.clicked.connect(lambda: self.save_properties(dialog, name_input, language_input, gender_input, commend_input))
        layout.addWidget(save_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def save_properties(self, dialog, name_input, language_input, gender_input, commend_input):
        name = name_input.text().strip()
        language = language_input.text().strip()
        gender = gender_input.text().strip()
        commend = commend_input.text().strip()

        # Doğrulama
        if not name or not language or not gender or not commend:
            QtWidgets.QMessageBox.warning(dialog, "Validation Error", "All fields must be filled!")
            return

        if language not in ["en", "tr"]:
            QtWidgets.QMessageBox.warning(dialog, "Validation Error", "Language must be 'en' or 'tr'!")
            return

        if gender not in ["male", "female"]:
            QtWidgets.QMessageBox.warning(dialog, "Validation Error", "Gender must be 'male' or 'female'!")
            return

        # Değerleri güncelle
        self.name = name
        self.language = language
        self.gender = gender
        self.commend = commend

        # Widget üzerindeki etiketleri güncelle
        self.labelCardExampleName.setText(self.name)
        self.labelCardExampleLanguage.setText(self.language)
        self.labelCardExampleGender.setText(self.gender)
        self.labelCardExampleCommend.setText(self.commend)

        dialog.accept()


#---------------- UYGULAMA OLUŞTURMA ---------------

global last_query
last_query = None

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)


#--------------- VERİTABANI OLUŞTURMA --------------
global curs
global conn
conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()
queryCreTblVoice = (
    "CREATE TABLE IF NOT EXISTS voice(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,   \
                 Language TEXT NOT NULL,                       \
                 Gender TEXT NOT NULL,                         \
                 Name TEXT NOT NULL,                      \
                 Commend TEXT NOT NULL,                          \
                 Url TEXT NOT NULL UNIQUE,                             \
                 Status BOOLEAN NOT NULL )"
)
curs.execute(queryCreTblVoice)
conn.commit()
#--------------- VERİTABANINDAN İSİMLERİ VE COMMANDLARI ÇEKME --------------


def load_names_from_database(force_update=False):
        if not force_update:
            return 
        connection = sqlite3.connect("veritabani.db")
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT Name FROM voice")
        names = cursor.fetchall()
        # ComboBox'ı temizle
        ui.comboBoxFilterName.clear()
        ui.comboBoxFilterName.addItem("All")
        for name in names:
            ui.comboBoxFilterName.addItem(name[0]) 
        connection.close()
load_names_from_database(force_update=True)


def load_command_from_database(force_update=False):
        if not force_update:
            return
        connection = sqlite3.connect("veritabani.db")  
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT Commend FROM voice")  
        command = cursor.fetchall()
        ui.comboBoxFilterCommend.clear()
        ui.comboBoxFilterCommend.addItem("All")
        for commend in command:
            ui.comboBoxFilterCommend.addItem(commend[0])  
        connection.close()
load_command_from_database(force_update=True)

def first_row_count():
        
        connection = sqlite3.connect("veritabani.db")
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM voice")
        first_row_count = cursor.fetchone()[0]  # Toplam satır sayısını al
        connection.close()
        return first_row_count


first_count_global = first_row_count()

def get_row_count():
        
        connection = sqlite3.connect("veritabani.db")
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM voice")
        row_count = cursor.fetchone()[0]  # Toplam satır sayısını al
        connection.close()
        return row_count


def check_for_changes(first_count):
        current_count = get_row_count()
        if current_count != first_count :
            print("Değişiklik tespit edildi! Veriler güncelleniyor...")
            load_names_from_database(force_update=True)
            load_command_from_database(force_update=True)
            global first_count_global 
            first_count_global = current_count  
            return print("first_count return kısmında:",first_count_global)
        else:
            print("Değişiklik yok.")
            return first_count_global

timer = QTimer()
timer.timeout.connect(lambda:check_for_changes(first_count_global))
timer.start(3000)



#--------------- VERİTABANINDAN VERİ ÇEKME --------------
def LISTALLDATA():
    global last_query
    scrollAreaWidgetContents_2 = ui.scrollAreaWidgetContents_2
    if scrollAreaWidgetContents_2.layout() is None:
        verticalLayout = QVBoxLayout(scrollAreaWidgetContents_2)
        scrollAreaWidgetContents_2.setLayout(verticalLayout)
        print("Yeni layout oluşturuldu.")
    else:
        verticalLayout = scrollAreaWidgetContents_2.layout()
        print("Mevcut layout bulundu.")

    for i in reversed(range(verticalLayout.count())):
        widget_to_remove = verticalLayout.itemAt(i).widget()
        if widget_to_remove is not None:
            widget_to_remove.deleteLater()

    queryAllData = "SELECT * FROM voice"
    curs.execute(queryAllData)

    # last_query'yi güncelle
    last_query = (queryAllData, [])


    # Verileri kullanarak CustomWidget oluştur
    for satirVeri in curs:
        data = {
            "Language": satirVeri[1],
            "Gender": satirVeri[2],
            "Name": satirVeri[3],
            "Commend": satirVeri[4],
            "Url": satirVeri[5]
        }
        custom_widget = CustomWidget(data["Name"], data["Language"], data["Gender"], data["Commend"], data["Url"])
        verticalLayout.addWidget(custom_widget)
        print(f"Widget eklendi: {data['Name']}")
    curs.execute("SELECT COUNT(*) FROM voice")
    numberVoice = curs.fetchone()
    ui.labelShowedDataNumber.setText(str(numberVoice[0]))


def FILTERDATA():

    global last_query

    # Dil kontrolleri
    english_selected = ui.radioButtonFilterLanguageEnglish.isChecked()
    turkish_selected = ui.radioButtonFilterLanguageTurkish.isChecked()

    # Cinsiyet kontrolleri
    male_selected = ui.radioButtonFilterGenderMale.isChecked()
    
    female_selected = ui.radioButtonFilterGenderFemale.isChecked()

    
    
    
    # Dil kontrolü
    if not (turkish_selected or english_selected):
        QtWidgets.QMessageBox.warning(None, "Uyarı", "Lütfen en az bir dil seçin.")
        return  # Fonksiyonu sonlandır

    # Cinsiyet kontrolü
    if not (male_selected or female_selected):
        QtWidgets.QMessageBox.warning(None, "Uyarı", "Lütfen en az bir cinsiyet seçin.")
        return  # Fonksiyonu sonlandır

    # Seçilen dillerin listesini oluştur
    languages = []
    if turkish_selected:
        languages.append("tr")
    if english_selected:
        languages.append("en")

    # Seçilen cinsiyetlerin listesini oluştur
    genders = []
    if male_selected:
        genders.append("male")
    if female_selected:
        genders.append("female")

    # ComboBox'lardan seçilen değerleri al
    name_selected = ui.comboBoxFilterName.currentText()
    commend_selected = ui.comboBoxFilterCommend.currentText()

    # Sorguyu oluştur
    query = "SELECT * FROM voice WHERE Language IN ({}) AND Gender IN ({})".format(
        ', '.join('?' * len(languages)),
        ', '.join('?' * len(genders))
    )
    params = languages + genders

    # Name koşulunu ekle
    if name_selected != "All":
        query += " AND Name = ?"
        params.append(name_selected)

    # Commend koşulunu ekle
    if commend_selected != "All":
        query += " AND Commend = ?"
        params.append(commend_selected)

    # Filtreleme sorgusu
    curs.execute(query, params)

    last_query = (query, params)

    # Sonuçları işleme
    results = curs.fetchall()

    # ScrollArea'nın layout'unu al
    scrollAreaWidgetContents_2 = ui.scrollAreaWidgetContents_2

    if scrollAreaWidgetContents_2.layout() is None:
        verticalLayout = QVBoxLayout(scrollAreaWidgetContents_2)
        scrollAreaWidgetContents_2.setLayout(verticalLayout)
    else:
        verticalLayout = scrollAreaWidgetContents_2.layout()

    # Mevcut widget'ları temizle
    for i in reversed(range(verticalLayout.count())):
        widget_to_remove = verticalLayout.itemAt(i).widget()
        if widget_to_remove is not None:
            widget_to_remove.deleteLater()

    numberVoice = 0

    # Sonuçları widget'lara ekle
    for satirVeri in results:
        numberVoice += 1
        data = {
            "Language": satirVeri[1],
            "Gender": satirVeri[2],
            "Name": satirVeri[3],
            "Commend": satirVeri[4],
            "Url": satirVeri[5]
        }
        custom_widget = CustomWidget(data["Name"], data["Language"], data["Gender"], data["Commend"], data["Url"])
        verticalLayout.addWidget(custom_widget)

    # Sonuç sayısını göster
    ui.labelShowedDataNumber.setText(str(numberVoice))
def clear_widgets():
    layout = ui.scrollAreaWidgetContents_2.layout()

    if layout is not None:
        # Layout içerisindeki tüm widget'ları sil
        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.deleteLater()
        print("Tüm widget'lar silindi.")
clear_widgets()
def download_data():
    global last_query
    if last_query:
        query, params = last_query  # Sorgu ve parametreleri al
        curs.execute(query, params)  # Parametrelerle sorguyu çalıştır
        data = curs.fetchall()
        columns = [desc[0] for desc in curs.description]  # Sütun adlarını al
        df = pd.DataFrame(data, columns=columns)  # DataFrame oluştur

        # Kullanıcıdan nereye kaydetmek istediğini sormak için QFileDialog kullan
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Save CSV File",
            "data",
            "CSV Files (*.csv);;All Files (*)",
            options=options
        )

        if file_path:
            try:
                df.to_csv(file_path, index=False)
                QMessageBox.information(None, "Success", f"Data saved to {file_path}")
            except Exception as e:
                QMessageBox.warning(None, "Error", f"Failed to save data: {e}")
        else:
            QMessageBox.information(None, "Cancelled", "File save operation was cancelled.")
    else:
        QMessageBox.warning(None, "Error", "No data to download.")


def download_voice():
    global last_query
    if last_query:
        query, params = last_query  # Sorgu ve parametreleri al
        curs.execute(query, params)  # Parametrelerle sorguyu çalıştır
        data = curs.fetchall()
        
        # Sadece `.wav` uzantılı dosyaları filtrele
        filtered_data = [row for row in data if row[5].endswith('.wav')]  # Url sütunu 5. indexte yer alıyor
        
        if not filtered_data:
            QMessageBox.warning(None, "Error", "No .wav files found to download.")
            return

        # Kullanıcıdan nereye kaydetmek istediğini sormak için QFileDialog kullan
        options = QFileDialog.Options()
        target_folder = QFileDialog.getExistingDirectory(
            None,
            "Select Target Folder",
            options=options
        )

        if target_folder:
            try:
                for row in filtered_data:
                    source_path = os.path.join('voices', row[5])  # voices klasöründen dosya yolu oluştur
                    target_path = os.path.join(target_folder, os.path.basename(row[5]))  # Hedef klasöre dosya adıyla kopyala
                    
                    if os.path.exists(source_path):
                        shutil.copy2(source_path, target_path)  # Dosyayı kopyala (tüm metadata dahil)
                        print(f"File copied: {source_path} -> {target_path}")
                    else:
                        print(f"File not found: {source_path}")
                
                QMessageBox.information(None, "Success", "All .wav files have been successfully downloaded.")
            except Exception as e:
                QMessageBox.warning(None, "Error", f"Failed to download files: {e}")
        else:
            QMessageBox.information(None, "Cancelled", "Download operation was cancelled.")
    else:
        QMessageBox.warning(None, "Error", "No data to download.")


#-------------- UYGULAMA OLAYLARI -------------------

ui.pushButtonButtonsShowAllData.clicked.connect(LISTALLDATA)
ui.pushButtonButtonsFilterData.clicked.connect(FILTERDATA)
ui.pushButtonButtonsClearData.clicked.connect(clear_widgets)
ui.pushButtonButtonsDownloadData.clicked.connect(download_data)
ui.pushButtonButtonsDownloadSound.clicked.connect(download_voice)

#--------------- UYGULAMAYI ÇALIŞTIRMA --------------

penAna.show()
sys.exit(Uygulama.exec_())


