from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QCalendarWidget
from PyQt6 import uic
import sys




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_files/MW_qwolendar.ui', self)  # Загружаем дизайн
        self.button_add.clicked.connect(self.adding_task)

    def adding_task(self):
        print(52)
        date_object = self.calendarWidget.selectedDate()
        # print(self.calendarWidget.selectedDate().toString()) # toStdSysDays()
        # print(self.calendarWidget.selectedDate().day())
        print(date_object.year(), date_object.month(), date_object.day())
        # self.label.setText("OK")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
