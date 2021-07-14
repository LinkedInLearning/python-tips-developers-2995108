import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
def on_btn1_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()
def on_btn2_clicked():
    lbl.setText("Hallo")
def on_btn3_clicked():
    sys.exit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Einfaches Fenster")
    layout = QVBoxLayout()
    btn1 = QPushButton('Klick')
    btn2 = QPushButton('Ausgabe Text')
    btn3 = QPushButton('Ende')
    lbl = QLabel('')

    btn1.clicked.connect(on_btn1_clicked)
    btn2.clicked.connect(on_btn2_clicked)
    btn3.clicked.connect(on_btn3_clicked)
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(lbl)
    layout.addWidget(btn3)
    w.setLayout(layout)
    w.show()
    app.exec_()