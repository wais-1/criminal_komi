import sys

import dbconnect

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QScrollArea, QWidget, QVBoxLayout, QLabel, QSizePolicy

from PySide6.QtCore import Qt

from UI.LogInDialog import Ui_Dialog as Login
from UI.AdminMainWindow import Ui_MainWindow as AdminWindow
from UI.SignInDialog import Ui_Dialog as Signin
from UI.UserMainWindow import Ui_MainWindow as UserWindow
from UI.InvestigatorMainWindow import Ui_MainWindow as InvestigatorWindow
from UI.DialogFilters import Ui_Dialog as FiltersDialog
from UI.AddEditClue import Ui_Dialog as AddEditClue
from UI.AddEditCrime import Ui_Dialog as AddEditCrime
from UI.AddEditCriminalCase import Ui_Dialog as AddEditCriminalCase
from UI.AddEditLocation import Ui_Dialog as AddEditLocation
from UI.AddEditRecord import Ui_Dialog as AddEditRecord
from UI.AddEditSuspect import Ui_Dialog as AddEditSuspect
from UI.CrimeCard import Ui_Form as CrimeCard
from UI.CrimeWindow import Ui_MainWindow as CrimeWindow
from UI.ProtocolWindow import Ui_MainWindow as ProtocolWindow


def open_admin_window():
    global admin_window, admin_ui

    admin_window = QMainWindow()
    admin_ui = AdminWindow()
    admin_ui.setupUi(admin_window)

    admin_ui.pushButton_7.clicked.connect(open_filters_dialog)
    admin_ui.pushButton_2.clicked.connect(open_add_crime)
    admin_ui.pushButton_3.clicked.connect(open_add_case)
    admin_ui.pushButton_4.clicked.connect(open_add_record)
    admin_ui.pushButton_5.clicked.connect(open_add_suspect)
    admin_ui.pushButton_6.clicked.connect(open_add_clue)
    admin_ui.pushButton_10.clicked.connect(open_add_location)

    load_crime_card(admin_ui, "admin")
    admin_window.show()

def open_user_window():
    global user_window, user_ui

    user_window = QMainWindow()
    user_ui = UserWindow()
    user_ui.setupUi(user_window)

    user_ui.btn_filters.clicked.connect(open_filters_dialog)
    load_crime_card(user_ui, "user")
    user_window.show()

def open_investigator_window():
    global investigator_window, investigator_ui
    
    investigator_window = QMainWindow()
    investigator_ui = InvestigatorWindow()
    investigator_ui.setupUi(investigator_window)

    investigator_ui.btn_filters.clicked.connect(open_filters_dialog)
    load_crime_card(investigator_ui, "investigator")
    investigator_window.show()

def open_filters_dialog():
    global filters_window, filters_ui

    filters_window = QMainWindow()
    filters_ui = FiltersDialog()
    filters_ui.setupUi(filters_window)

    filters_window.show()

def open_add_crime():
    global crime_add_window, crime_add_ui
    
    crime_add_window = QMainWindow()
    crime_add_ui = AddEditCrime()
    crime_add_ui.setupUi(crime_add_window)

    crime_window.show()

def open_add_case():
    global case_window, case_ui
    
    case_window = QMainWindow()
    case_ui = AddEditCriminalCase()
    case_ui.setupUi(case_window)

    case_window.show()

def open_add_record():
    global record_window, record_ui
    
    record_window = QMainWindow()
    record_ui = AddEditRecord()
    record_ui.setupUi(record_window)

    record_window.show()

def open_add_clue():
    global clue_window, clue_ui
    
    clue_window = QMainWindow()
    clue_ui = AddEditClue()
    clue_ui.setupUi(clue_window)

    clue_window.show()

def open_add_suspect():
    global suspect_window, suspect_ui
    
    suspect_window = QMainWindow()
    suspect_ui = AddEditSuspect()
    suspect_ui.setupUi(suspect_window)

    suspect_window.show()

def open_add_location():
    global location_window, location_ui
    
    location_window = QMainWindow()
    location_ui = AddEditLocation()
    location_ui.setupUi(location_window)

    location_window.show()

def open_crime_window(crime_id):
    global crime_window, crime_ui
        
    crime_window = QMainWindow()
    crime_ui = CrimeWindow()
    crime_ui.setupUi(crime_window)

    crime_ui.btn_read_protocol.clicked.connect(open_protocol_window)
    load_crime_window(crime_id)
    crime_window.show()

def open_protocol_window():
    global protocol_window, protocol_ui
        
    protocol_window = QMainWindow()
    protocol_ui = ProtocolWindow()
    protocol_ui.setupUi(protocol_window)

    protocol_window.show()

def load_crime_card(window, role):
    global crime_card_window, card_crime_ui
    crime_card = dbconnect.get_crime_card()

    scroll_area = window.scrollArea

    if scroll_area is None:
        print('скролл не неайден')
        return

    container = window.scrollAreaWidgetContents

    layout = container.layout()
    if layout is None:
        layout = QVBoxLayout(container)

    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(10)
    layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    for crime in crime_card:
        crime_card_window = QWidget()
        crime_card_ui = CrimeCard()
        crime_card_ui.setupUi(crime_card_window)
        crime_id = crime[0]

        crime_card_ui.btn_read.clicked.connect(lambda checked=False, cid=crime_id: open_crime_window(cid))

        crime_card_ui.lbl_name.setText(str(crime[1] or ""))
        crime_card_ui.lbl_mini_descr.setText(str(crime[2] or ""))

        crime_card_window.setMinimumHeight(200)
        crime_card_window.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        layout.addWidget(crime_card_window)

        if role == "admin":
            crime_card_ui.btn_delete.setVisible(True)
            crime_card_ui.btn_edit.setVisible(True)

        elif role == "user":
            crime_card_ui.btn_delete.setVisible(False)
            crime_card_ui.btn_edit.setVisible(False)

        elif role == "investigator":
            crime_card_ui.btn_delete.setVisible(False)
            crime_card_ui.btn_edit.setVisible(True)

    layout.addStretch()
    scroll_area.setWidgetResizable(True)

def load_crime_window(crime_id):
    suspect = dbconnect.get_suspect_by_id(crime_id)
    crimes = dbconnect.get_crime_by_id(crime_id)
    clues = dbconnect.get_clue_by_id(crime_id)
    cases = dbconnect.get_case_by_id(crime_id)

    print("Полученный ID:", crime_id)
    print("Результат запроса:", clues)

    if crimes is None:
        print("преступление не найдено")
        return

    if suspect is None:
        print("преступник не найдено")
        return

    if clues is None:
        print("clue не найдено")
        return

    if cases is None:
        print("case не найдено")
        return

    crime_ui.lbl_fullname.setText(str(suspect[1] or ""))
    crime_ui.lbl_date_birth.setText(str(suspect[2] or ""))
    crime_ui.lbl_signs.setText(str(suspect[3] or ""))
    if suspect:
        crime_ui.lbl_status.setText(str(suspect[4] or "Не указан"))
    else:
        crime_ui.lbl_status.setText("Не указан")

    crime_ui.lbl_article_name.setText(str(crimes[1] or ""))
    crime_ui.lbl_article_date.setText(str(crimes[3] or ""))
    crime_ui.lbl_article_status.setText(str(crimes[4] or ""))
    crime_ui.lbl_type.setText(str(crimes[5] or ""))
    crime_ui.lbl_secret.setText(str(crimes[6] or ""))
    crime_ui.lbl_date_text.setText(str(crimes[2] or "Нет описания"))

    crime_ui.lbl_clue_nomination.setText(str(clues[1] or ""))
    crime_ui.lbl_clue_date.setText(str(clues[2] or ""))
    crime_ui.lbl_clue_descr.setText(str(clues[3] or ""))
    crime_ui.lbl_clue_type.setText(str(clues[4] or ""))

    crime_ui.lbl_case_number.setText(str(cases[1] or ""))
    crime_ui.lbl_case.setText(str(cases[2] or ""))
    crime_ui.lbl_date_open.setText(str(cases[3] or ""))
    crime_ui.lbl_date_close.setText(str(cases[4] or "Не закрыто"))


def authorization():
    login = login_ui.lineEdit.text()
    password = login_ui.lineEdit_2.text()

    role = check_login(login, password)

    if role:
        login_window.close()

        if role[0] == 'Администратор':
            open_admin_window()

        elif role[0] == 'user':
            open_user_window()
        elif role[0] == 'Следователь':
            open_investigator_window()
    else:
        print('no such user')
        login_ui.label_6.setVisible(True)
        login_ui.label_5.setVisible(True)


def check_login(loginValue, passValue):
    conn = dbconnect.get_db_connection()

    with conn.cursor() as cursor:
        cursor.execute("""SELECT role.name FROM user
                            JOIN role on user.id_role = role.id
                            where user.login = %s AND user.password = %s""", (loginValue, passValue))
        role = cursor.fetchone()

        conn.close()
        return role

def open_registration_window():
    global signin_window, signin_ui

    signin_window = QDialog()
    signin_ui = Signin()
    signin_ui.setupUi(signin_window)

    signin_ui.pushButton_2.clicked.connect(lambda: (signin_window.close(), login_window.show()))
    signin_ui.pushButton.clicked.connect(registration)

    signin_window.show()
    login_window.close()

def registration():
    login = signin_ui.lineEdit.text()
    password = signin_ui.lineEdit_2.text()

    success_add = dbconnect.set_user(login, password)

    if success_add:
        signin_window.close()
        open_user_window()
    else:
        print('error')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    global login_window, login_ui

    login_window = QDialog()
    login_ui = Login()
    login_ui.setupUi(login_window)

    login_ui.pushButton.clicked.connect(authorization)
    login_ui.pushButton_2.clicked.connect(open_registration_window)

    login_window.show()

    login_ui.label_5.setVisible(False)
    login_ui.label_6.setVisible(False)
    sys.exit(app.exec())