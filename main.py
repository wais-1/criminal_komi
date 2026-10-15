import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from UI.LogInDialog import Ui_Dialog as Login

if __name__ == '__main__':
    app = QApplication(sys.argv)

    global login_window

    login_window = QDialog()
    login_ui = Login()
    login_ui.setupUi(login_window)

    login_window.show()
    sys.exit(app.exec())