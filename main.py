#-------------------- KÜTÜPHANE --------------------
import sys
import os
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from voiceCommandDatabase import *
from PyQt5 import uic
import sqlite3
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl





#---------------- ÖZEL WIDGET TANIMI ---------------
class CustomWidget(QtWidgets.QWidget):
    def __init__(self, name, language, gender, commend, file_name):
        super().__init__()
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

        self.player.positionChanged.connect(self.update_progress)
        self.player.stateChanged.connect(self.on_player_state_changed)

        # Language Label
        self.labelCardExampleLanguage = QLabel(language)
        self.labelCardExampleLanguage.setStyleSheet(
            "background-color: #ff9b0f;"
            "color: black;"
            "border-color: #4d4018;"
        )
        layout.addWidget(self.labelCardExampleLanguage)

        # Gender Label
        self.labelCardExampleGender = QLabel(gender)
        self.labelCardExampleGender.setStyleSheet(
            "background-color: #ff9b0f;"
            "color: black;"
            "border-color: #4d4018;"
        )
        layout.addWidget(self.labelCardExampleGender)

        # Name Label
        self.labelCardExampleName = QLabel(name)
        self.labelCardExampleName.setStyleSheet(
            "background-color: #ff9b0f;"
            "color: black;"
            "border-color: #4d4018;"
        )
        layout.addWidget(self.labelCardExampleName)

        # Voice Command Label
        self.labelCardExampleCommend = QLabel(commend)
        self.labelCardExampleCommend.setStyleSheet(
            "background-color: #ff9b0f;"
            "color: black;"
            "border-color: #4d4018;"
        )
        layout.addWidget(self.labelCardExampleCommend)

        # Progress Bar
        self.progressBarCardExample = QProgressBar()
        self.progressBarCardExample.setStyleSheet(
            "background-color: black;"
            "border-color: #4d4018;"
        )
        self.progressBarCardExample.setValue(0)
        layout.addWidget(self.progressBarCardExample)

    # Ses Çalma Fonksiyonu
    print("1")

    def play_sound(self, file_path):
        print("1")
        if os.path.exists(file_path):  # Dosyanın mevcut olup olmadığını kontrol et
            print("2")
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
            print("3")
            self.player.play()
            print("4")
            print(f"Çalınıyor: {file_path}")
            print("5")
        else:
            print(f"Ses dosyası bulunamadı: {file_path}")

    def update_progress(self, position):
        # İlerleme çubuğunu güncelle
        duration = self.player.duration()
        if duration > 0:
            self.progressBarCardExample.setValue(int((position / duration) * 100))

    def on_player_state_changed(self, state):
        if state == QMediaPlayer.StoppedState:
            self.progressBarCardExample.setValue(0)


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









#-------------- UYGULAMA OLAYLARI -------------------
#-------------- UYGULAMA OLAYLARI -------------------
ui.pushButtonButtonsShowAllData.clicked.connect(LISTALLDATA)
ui.pushButtonButtonsFilterData.clicked.connect(FILTERDATA)
ui.pushButtonButtonsClearData.clicked.connect(clear_widgets)
ui.pushButtonButtonsDownloadData.clicked.connect(download_data)





#--------------- UYGULAMAYI ÇALIŞTIRMA --------------
penAna.show()
sys.exit(Uygulama.exec_())
