from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QCalendarWidget
from PyQt6 import uic
import sys
from PyQt6.QtWidgets import QDialog, QListWidget, QListWidgetItem
from db import db_work
from config import db_name


class Dialog_taskmaker(QDialog):
    def __init__(self, parent_class, dates=[]):
        super().__init__()
        uic.loadUi('UI_files/taskmaker.ui', self)

        self.cancel_pushButton.clicked.connect(self.closing)
        self.commit_pushButton.clicked.connect(self.commiting)

        self.year_lineEdit.setText(str(dates[0]))
        self.month_lineEdit.setText(str(dates[1]))
        self.day_lineEdit.setText(str(dates[2]))
        self.task_name_lineEdit.setText("Your task")

        self.db_workk = db_work(db_name)

    def closing(self):
        self.close()

    def commiting(self):
        print(self.day_lineEdit.text())
        print(self.timeEdit.time().hour(), self.timeEdit.time().minute())
        times = f"{self.timeEdit.time().hour()}:{self.timeEdit.time().minute()}"
        self.db_workk = db_work(db_name)
        dates = f"{self.day_lineEdit.text()}.{self.month_lineEdit.text()}.{self.year_lineEdit.text()}"
        labell = self.task_name_lineEdit.text()
        self.db_workk.insert_task(dates, times, labell)
        self.close()

class tasks_list_Dialog(QDialog):
    def __init__(self, parent_class, dates=[]):
        super().__init__()
        uic.loadUi('UI_files/tasks_list_dialog.ui', self)
        
        self.db_workk = db_work(db_name)
        quers = self.db_workk.get_tasks()
        #print(quers)
        for row in quers:
            # print(row)
            values = "   ".join(map(str, row))
            # print("___".join(row))
            self.tasksList_listWidget.addItem(values)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_files/MW_qwolendar.ui', self)  # Загружаем дизайн
        self.button_add.clicked.connect(self.adding_task)
        self.checkDay_pushButton.clicked.connect(self.check_day_tasks)
        self.deleting_pushButton.clicked.connect(self.deleting)
        self.button_showList.clicked.connect(self.open_tasks_list)

    def adding_task(self):
        # print(52)
        date_object = self.calendarWidget.selectedDate()
        # print(self.calendarWidget.selectedDate().toString()) # toStdSysDays()
        # print(self.calendarWidget.selectedDate().day())
        # print(date_object.year(), date_object.month(), date_object.day())
        dil = Dialog_taskmaker(self, [date_object.year(), date_object.month(), date_object.day()])
        dil.exec()
        # self.label.setText("OK")

    def check_day_tasks(self):
        date_object = self.calendarWidget.selectedDate()
        dates = [date_object.year(), date_object.month(), date_object.day()]
        self.chosenDay_lineEdit.setText(f"{dates[2]}.{dates[1]}.{dates[0]}")

        self.db_workk = db_work(db_name)
        quers = self.db_workk.get_day_tasks(f"{dates[2]}.{dates[1]}.{dates[0]}")
        #print(quers)
        self.listWidget.clear()
        for row in quers:
            # print(row)
            values = "   ".join(map(str, row))
            # print("___".join(row))
            self.listWidget.addItem(values)

    def deleting(self):
        # print("deleting")

        # print(self.listWidget.currentItem().text())
        # print(self.listWidget.currentItem().text().split()[0])
        if self.listWidget.currentItem().text().split()[0]:
            id = self.listWidget.currentItem().text().split()[0]
            self.db_workk = db_work(db_name)
        # dates = f"{self.day_lineEdit.text()}.{self.month_lineEdit.text()}.{self.year_lineEdit.text()}"
        # labell = self.task_name_lineEdit.text()
            self.db_workk.delete_task(id)
            quers = self.db_workk.get_day_tasks(f"{self.listWidget.currentItem().text().split()[1]}")
        #print(quers)
            self.listWidget.clear()
            for row in quers:
                # print(row)
                values = "   ".join(map(str, row))
                # print("___".join(row))
                self.listWidget.addItem(values)

    def open_tasks_list(self):
        # print("tasks_list")
        dil = tasks_list_Dialog(self)
        dil.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
