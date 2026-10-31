import sys

import dbconnect

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QScrollArea, QWidget, QVBoxLayout, QLabel, QSizePolicy, QMessageBox

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
from UI.AddVictim import Ui_Dialog as AddVictim
from UI.AddWitness import Ui_Dialog as AddWitness
from UI.AddSuspectCrime import Ui_Dialog as AddSuspectCrime
from UI.CartWindow import Ui_MainWindow as CartWindow
from UI.GuestWindow import Ui_MainWindow as GuestWindow
from PySide6.QtCore import QDate

admin_ui = None
user_ui = None
investigator_ui = None

def open_cart_window():
    global cart_window, cart_ui
    
    cart_window = QMainWindow()
    cart_ui = CartWindow()
    cart_ui.setupUi(cart_window)

    load_crime_card_in_trash(cart_ui, "cart")

    cart_window.show()

#открытие окна админа
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
    admin_ui.pushButton_11.clicked.connect(open_add_victim)
    admin_ui.pushButton_12.clicked.connect(open_add_witness)
    admin_ui.pushButton_13.clicked.connect(open_suspect_crime)
    admin_ui.btn_cart.clicked.connect(open_cart_window)
    admin_ui.btn_exit.clicked.connect(lambda:(admin_window.close(), open_guest_window()))
    admin_ui.lineEdit.textChanged.connect(lambda text: live_search(admin_ui, "admin", text))

    load_crime_card(admin_ui, "admin")
    admin_window.show()

#открытие окна пользователя
def open_user_window():
    global user_window, user_ui

    user_window = QMainWindow()
    user_ui = UserWindow()
    user_ui.setupUi(user_window)

    user_ui.btn_filters.clicked.connect(open_filters_dialog)
    user_ui.btn_exit.clicked.connect(lambda:(user_window.close(), open_guest_window()))
    user_ui.line_search.textChanged.connect(lambda text: live_search(user_ui, "user", text))

    load_crime_card(user_ui, "user")
    user_window.show()

#открытие окна следака
def open_investigator_window():
    global investigator_window, investigator_ui
    
    investigator_window = QMainWindow()
    investigator_ui = InvestigatorWindow()
    investigator_ui.setupUi(investigator_window)

    investigator_ui.btn_filters.clicked.connect(open_filters_dialog)
    investigator_ui.btn_add_crime.clicked.connect(open_add_crime)
    investigator_ui.btn_add_criminal_case.clicked.connect(open_add_case)
    investigator_ui.btn_add_protocol.clicked.connect(open_add_record)
    investigator_ui.btn_add_murder.clicked.connect(open_add_suspect)
    investigator_ui.btn_add_clue.clicked.connect(open_add_clue)
    investigator_ui.pushButton_10.clicked.connect(open_add_location)
    investigator_ui.pushButton_11.clicked.connect(open_add_victim)
    investigator_ui.pushButton_12.clicked.connect(open_add_witness)
    investigator_ui.pushButton_13.clicked.connect(open_suspect_crime)
    investigator_ui.btn_exit.clicked.connect(lambda:(investigator_window.close(), open_guest_window()))
    investigator_ui.search.textChanged.connect(lambda text: live_search(investigator_ui, "investigator", text))

    load_crime_card(investigator_ui, "investigator")
    investigator_window.show()

#открытие окна фильтров
def open_filters_dialog():
    global filters_window, filters_ui

    filters_window = QMainWindow()
    filters_ui = FiltersDialog()
    filters_ui.setupUi(filters_window)

    filters_ui.pushButton.clicked.connect(apply_filters)
    filters_ui.pushButton_2.clicked.connect(reset_filters)

    crime_type = dbconnect.get_crime_type()
    filters_ui.cb_crime_type.clear()
    filters_ui.cb_crime_type.addItem("Все типы", None)

    #отображение enum в комбобоксах
    for i in crime_type:
        filters_ui.cb_crime_type.addItem(i[1], i[1])

    status = dbconnect.get_crime_status()
    filters_ui.cb_status_case.clear()
    filters_ui.cb_status_case.addItem("Все статусы", None)

    #отображение enum в комбобоксах
    for i in status:
        filters_ui.cb_status_case.addItem(i[1], i[1])

    suspect_status = dbconnect.get_suspect_status()
    filters_ui.cb_criminal_status.clear()
    filters_ui.cb_criminal_status.addItem("Все статусы", None)

    #отображение enum в комбобоксах
    for i in suspect_status:
        filters_ui.cb_criminal_status.addItem(i[1], i[1])

    suspects = dbconnect.get_suspects()
    filters_ui.cb_criminal.clear()
    filters_ui.cb_criminal.addItem("Все преступники", None)

    #отображение данных вместо id в комбобоксах
    for i in suspects:
        suspect_id = i[0]
        suspect_name = i[1]

        filters_ui.cb_criminal.addItem(
            suspect_name,
            suspect_id
        )

    investigators = dbconnect.get_investigator()
    filters_ui.cb_investigator.clear()
    filters_ui.cb_investigator.addItem("Все следователи", None)

    #отображение данных вместо id в комбобоксах
    for i in investigators:
        investigator_id = i[0]
        investigator_name = i[1]

        filters_ui.cb_investigator.addItem(
            investigator_name,
            investigator_id
        )

    filters_window.show()

#применение фильтров
def apply_filters():
    date_from = filters_ui.dateEdit.date().toString("yyyy-MM-dd")
    date_to = filters_ui.dateEdit_2.date().toString("yyyy-MM-dd")
    crime_type = filters_ui.cb_crime_type.currentData()
    district = filters_ui.line_district.text().strip()
    investigator_id = filters_ui.cb_investigator.currentData()
    crime_status = filters_ui.cb_status_case.currentData()
    suspect_name = filters_ui.cb_criminal.currentData()
    suspect_status = filters_ui.cb_criminal_status.currentData()

    crimes = dbconnect.filtered_data(date_from, date_to, crime_type, district, investigator_id, crime_status, suspect_name, suspect_status)

    if admin_ui is not None:
        load_crime_card(admin_ui, "admin", crimes)

    if user_ui is not None:
        load_crime_card(user_ui, "user", crimes)

    if investigator_ui is not None:
        load_crime_card(investigator_ui, "investigator", crimes)

    if crimes:
        filters_window.close()
    else:
        QMessageBox.information(
            filters_window,
            "Результат фильтрации",
            "По выбранным критериям преступления не найдены."
        )

def live_search(window, role, search_text):
    crimes = dbconnect.live_search(search_text)
    load_crime_card(window, role, crimes)

def reset_filters():
    # Сбрасываем даты
    filters_ui.dateEdit.setDate(QDate(2020, 1, 1))
    filters_ui.dateEdit_2.setDate(QDate(2026, 12, 31))

    # Сбрасываем ComboBox
    filters_ui.cb_crime_type.setCurrentIndex(0)
    filters_ui.cb_investigator.setCurrentIndex(0)
    filters_ui.cb_status_case.setCurrentIndex(0)
    filters_ui.cb_criminal.setCurrentIndex(0)
    filters_ui.cb_criminal_status.setCurrentIndex(0)

    # Очищаем район
    filters_ui.line_district.clear()

    crimes = dbconnect.get_crime_card()

    if admin_ui is not None:
        load_crime_card(admin_ui, "admin", crimes)

    if user_ui is not None:
        load_crime_card(user_ui, "user", crimes)

    if investigator_ui is not None:
        load_crime_card(investigator_ui, "investigator", crimes)

def open_suspect_crime():
    global suspect_crime_window, suspect_crime_ui
        
    suspect_crime_window = QDialog()
    suspect_crime_ui = AddSuspectCrime()
    suspect_crime_ui.setupUi(suspect_crime_window)

    suspect_crime_ui.buttonBox.rejected.connect(suspect_crime_window.close)
    suspect_crime_ui.buttonBox.accepted.connect(add_suspect_crime)

    suspects = dbconnect.get_suspects()
    suspect_crime_ui.comboBox.clear()

    #отображение данных вместо id в комбобоксах
    for i in suspects:
        suspect_id = i[0]
        suspect_name = i[1]

        suspect_crime_ui.comboBox.addItem(
            suspect_name,
            suspect_id
        )

    crimes = dbconnect.get_crimes()
    suspect_crime_ui.comboBox_2.clear()

    for i in crimes:
            crime_id = i[0]
            crime_name = i[1]
    
            suspect_crime_ui.comboBox_2.addItem(
                crime_name,
                crime_id
            )

    suspect_crime_window.show()

def add_suspect_crime():
    suspect_id = suspect_crime_ui.comboBox.currentData()
    crime_id = suspect_crime_ui.comboBox_2.currentData()

    if suspect_id is not None and crime_id is not None:
        success = dbconnect.set_suspect_crime(suspect_id, crime_id)

    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно добавили информацию")
        crime_add_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при добавлении информации")

#окно добавления преступления
def open_add_crime():
    global crime_add_window, crime_add_ui
    
    crime_add_window = QMainWindow()
    crime_add_ui = AddEditCrime()
    crime_add_ui.setupUi(crime_add_window)

    crime_add_ui.buttonBox.rejected.connect(crime_add_window.close)
    crime_add_ui.buttonBox.accepted.connect(add_crime)
    crime_add_ui.label_11.setVisible(False)
    crime_add_ui.pushButton.clicked.connect(edit_crime)

    status = dbconnect.get_crime_status()
    crime_add_ui.comboBox.clear()

    #отображение enum в комбобоксах
    for i in status:
        crime_add_ui.comboBox.addItem(i[1], i[0])

    crime_type = dbconnect.get_crime_type()
    crime_add_ui.comboBox_2.clear()

    for i in crime_type:
        crime_add_ui.comboBox_2.addItem(i[1], i[0])

    security = dbconnect.get_crime_security()
    crime_add_ui.comboBox_3.clear()

    for i in security:
        crime_add_ui.comboBox_3.addItem(i[1], i[0])

    crime_add_window.show()


#добавление преступления
def add_crime():
    name = crime_add_ui.lineEdit.text()
    mini_description = crime_add_ui.lineEdit_2.text()
    description = crime_add_ui.lineEdit_3.text()
    date = crime_add_ui.dateEdit.date().toString("yyyy-MM-dd")
    id_location_text = crime_add_ui.lineEdit_5.text().strip()
    if id_location_text:
        id_location = int(id_location_text)
    else:
        id_location = None
    status = crime_add_ui.comboBox.currentText()
    crime_type = crime_add_ui.comboBox_2.currentText()
    security = crime_add_ui.comboBox_3.currentText()
    

    success = dbconnect.set_crime(name, mini_description, description, date, status, crime_type, security, id_location)

    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно добавили информацию")
        crime_add_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при добавлении информации")

#редактирование преступления
def edit_crime():
    crime_id_text = crime_add_ui.lineEdit_7.text().strip()

    if not crime_id_text:
        crime_add_ui.label_11.setVisible(True)
        return

    crime_id = int(crime_id_text)

    name = crime_add_ui.lineEdit.text()
    mini_description = crime_add_ui.lineEdit_2.text()
    description = crime_add_ui.lineEdit_3.text()
    date = crime_add_ui.dateEdit.date().toString("yyyy-MM-dd")
    id_location_text = crime_add_ui.lineEdit_5.text().strip()
    if id_location_text:
        id_location = int(id_location_text)
    else:
        id_location = None
    status = crime_add_ui.comboBox.currentText()
    crime_type = crime_add_ui.comboBox_2.currentText()
    security = crime_add_ui.comboBox_3.currentText()

    success = dbconnect.update_crime(crime_id, name, mini_description, description, date, status, crime_type, security, id_location)
    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно обновили информацию")
        crime_add_ui.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при обновлении информации")

#окно добавления УД
def open_add_case():
    global case_window, case_ui
    
    case_window = QMainWindow()
    case_ui = AddEditCriminalCase()
    case_ui.setupUi(case_window)

    case_ui.buttonBox.rejected.connect(case_window.close)
    case_ui.buttonBox.accepted.connect(add_case)
    case_ui.label_10.setVisible(False)
    case_ui.pushButton.clicked.connect(edit_case)

    case_window.show()

#добавление УД
def add_case():
    case_number = case_ui.lineEdit.text()
    opening_date = case_ui.dateEdit.date().toString("yyyy-MM-dd")
    closing_date = case_ui.dateEdit_2.date().toString("yyyy-MM-dd")
    article = case_ui.lineEdit_2.text()
    id_record_text = case_ui.lineEdit_4.text().strip()
    if id_record_text:
        id_record = int(id_record_text)
    else:
        id_record = None
    id_investigator_text = case_ui.lineEdit_5.text().strip()
    if id_investigator_text:
        id_investigator = int(id_investigator_text)
    else:
        id_investigator = None
    id_crime_text = case_ui.lineEdit_6.text().strip()
    if id_crime_text:
        id_crime = int(id_crime_text)
    else:
        id_crime = None
    

    success = dbconnect.set_criminal_case(case_number, opening_date, closing_date, article, id_record, id_investigator, id_crime)

    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно добавили информацию")
        case_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при добавлении информации")

#редактирование УД
def edit_case():
    case_id_text = case_ui.lineEdit_7.text().strip()

    if not case_id_text:
        case_ui.label_10.setVisible(True)
        return

    case_id = int(case_id_text)

    case_number = case_ui.lineEdit.text()
    opening_date = case_ui.dateEdit.date().toString("yyyy-MM-dd")
    closing_date = case_ui.dateEdit_2.date().toString("yyyy-MM-dd")
    article = case_ui.lineEdit_2.text()
    id_record_text = case_ui.lineEdit_4.text().strip()
    if id_record_text:
        id_record = int(id_record_text)
    else:
        id_record = None
    id_investigator_text = case_ui.lineEdit_5.text().strip()
    if id_investigator_text:
        id_investigator = int(id_investigator_text)
    else:
        id_investigator = None
    id_crime_text = case_ui.lineEdit_6.text().strip()
    if id_crime_text:
        id_crime = int(id_crime_text)
    else:
        id_crime = None

    success = dbconnect.update_criminal_case(case_id, case_number, opening_date, closing_date, article, id_record, id_investigator, id_crime)
    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно обновили информацию")
        case_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при обновлении информации")

#окно добавления протокола допроса
def open_add_record():
    global record_window, record_ui
    
    record_window = QMainWindow()
    record_ui = AddEditRecord()
    record_ui.setupUi(record_window)

    record_ui.buttonBox.rejected.connect(record_window.close)

    record_window.show()

#окно добавления улики
def open_add_clue():
    global clue_window, clue_ui
    
    clue_window = QMainWindow()
    clue_ui = AddEditClue()
    clue_ui.setupUi(clue_window)

    clue_ui.buttonBox.rejected.connect(clue_window.close)
    clue_ui.buttonBox.accepted.connect(add_clue)
    clue_ui.label_11.setVisible(False)
    clue_ui.pushButton.clicked.connect(edit_clue)

    status = dbconnect.get_clue_type()
    clue_ui.comboBox.clear()

    for i in status:
        clue_ui.comboBox.addItem(i[1], i[0])

    clue_window.show()

#добавление улики
def add_clue():
    name = clue_ui.lineEdit.text()
    date = clue_ui.dateEdit.date().toString("yyyy-MM-dd")
    description = clue_ui.lineEdit_2.text()
    clue_type = clue_ui.comboBox.currentText()
    id_clue_text = clue_ui.lineEdit_3.text().strip()
    if id_clue_text:
        id_clue = int(id_clue_text)
    else:
        id_clue = None
    

    success = dbconnect.set_clue(name, date, clue_type, description, id_clue)

    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно добавили информацию")
        clue_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при добавлении информации")

#редактирование улики
def edit_clue():
    clue_id_text = clue_ui.lineEdit_7.text().strip()

    if not clue_id_text:
        clue_ui.label_11.setVisible(True)
        return

    clue_id = int(clue_id_text)

    name = clue_ui.lineEdit.text()
    date = clue_ui.dateEdit.date().toString("yyyy-MM-dd")
    description = clue_ui.lineEdit_2.text()
    clue_type = clue_ui.comboBox.currentText()
    id_crime_text = case_ui.lineEdit_4.text().strip()
    if id_crime_text:
        id_crime = int(id_crime_text)
    else:
        id_crime = None

    success = dbconnect.update_clue(clue_id, name, date, clue_type, description, id_crime)
    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно обновили информацию")
        clue_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при обновлении информации")

#окно добавления преступника
def open_add_suspect():
    global suspect_window, suspect_ui
    
    suspect_window = QMainWindow()
    suspect_ui = AddEditSuspect()
    suspect_ui.setupUi(suspect_window)

    suspect_ui.buttonBox.rejected.connect(suspect_window.close)
    suspect_ui.buttonBox.accepted.connect(add_suspect)
    suspect_ui.label_11.setVisible(False)
    suspect_ui.pushButton.clicked.connect(edit_suspect)

    status = dbconnect.get_suspect_status()
    suspect_ui.comboBox.clear()

    for i in status:
        suspect_ui.comboBox.addItem(i[1], i[0])

    suspect_window.show()

#добавление преступника
def add_suspect():
    full_name = suspect_ui.lineEdit.text()
    birth_date = suspect_ui.dateEdit.date().toString("yyyy-MM-dd")
    img_url = suspect_ui.lineEdit_3.text()
    marks = suspect_ui.lineEdit_2.text()
    status = suspect_ui.comboBox.currentText()
    
    success = dbconnect.set_suspect(full_name, img_url, birth_date, marks, status)

    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно добавили информацию")
        suspect_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при добавлении информации")

#редактирование преступника
def edit_suspect():
    suspect_id_text = suspect_ui.lineEdit_7.text().strip()

    if not suspect_id_text:
        suspect_ui.label_11.setVisible(True)
        return

    suspect_id = int(suspect_id_text)

    full_name = suspect_ui.lineEdit.text()
    birth_date = suspect_ui.dateEdit.date().toString("yyyy-MM-dd")
    img_url = suspect_ui.lineEdit_3.text()
    marks = suspect_ui.lineEdit_2.text()
    status = suspect_ui.comboBox.currentText()

    success = dbconnect.update_suspect(suspect_id, full_name, img_url, birth_date, marks, status)
    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно обновили информацию")
        suspect_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при обновлении информации")

#окно добавления места преступления
def open_add_location():
    global location_window, location_ui
    
    location_window = QMainWindow()
    location_ui = AddEditLocation()
    location_ui.setupUi(location_window)

    location_ui.buttonBox.rejected.connect(location_window.close)
    location_ui.buttonBox.accepted.connect(add_location)
    location_ui.pushButton.clicked.connect(edit_location)
    location_ui.label_11.setVisible(False)
    
    status = dbconnect.get_location_type()
    location_ui.comboBox.clear()

    for i in status:
        location_ui.comboBox.addItem(i[1], i[0])

    location_window.show()

#добавление свидетеля
def add_location():
    coordinates = location_ui.lineEdit.text()
    address = location_ui.lineEdit_2.text()
    district = location_ui.lineEdit_3.text()
    object_type = location_ui.comboBox.currentText()
    
    success = dbconnect.set_location(coordinates, address, district, object_type)

    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно добавили информацию")
        location_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при добавлении информации")

#редактирование свидетеля
def edit_location():
    location_id_text = location_ui.lineEdit_7.text().strip()

    if not location_id_text:
        witness_ui.label_11.setVisible(True)
        return

    location_id = int(location_id_text)

    coordinates = location_ui.lineEdit.text()
    address = location_ui.lineEdit_2.text()
    district = location_ui.lineEdit_3.text()
    object_type = location_ui.comboBox.currentText()

    success = dbconnect.update_location(location_id, coordinates, address, district, object_type)
    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно обновили информацию")
        location_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при обновлении информации")

#окно добавления потерпевшего
def open_add_victim():
    global victim_window, victim_ui
    
    victim_window = QMainWindow()
    victim_ui = AddVictim()
    victim_ui.setupUi(victim_window)

    victim_ui.buttonBox.rejected.connect(victim_window.close)
    victim_ui.buttonBox.accepted.connect(add_victim)
    victim_ui.pushButton.clicked.connect(edit_victim)
    victim_ui.label_11.setVisible(False)
        
    status = dbconnect.get_victim_status()
    victim_ui.comboBox.clear()

    for i in status:
        victim_ui.comboBox.addItem(i[1], i[0])

    victim_window.show()

#добавление потерпевшего
def add_victim():
    full_name = victim_ui.lineEdit.text()
    birth_date = victim_ui.dateEdit.date().toString("yyyy-MM-dd")
    severity = victim_ui.lineEdit_2.text()
    status = victim_ui.comboBox.currentText()
    
    success = dbconnect.set_victim(full_name, birth_date, severity, status)

    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно добавили информацию")
        suspect_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при добавлении информации")

#редактирование потерпевшего
def edit_victim():
    victim_id_text = victim_ui.lineEdit_7.text().strip()

    if not victim_id_text:
        victim_ui.label_11.setVisible(True)
        return

    victim_id = int(victim_id_text)

    full_name = victim_ui.lineEdit.text()
    birth_date = victim_ui.dateEdit.date().toString("yyyy-MM-dd")
    severity = victim_ui.lineEdit_2.text()
    status = victim_ui.comboBox.currentText()

    success = dbconnect.update_victim(victim_id, full_name, birth_date, severity, status)
    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно обновили информацию")
        victim_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при обновлении информации")

#окно добавления свидетеля
def open_add_witness():
    global witness_window, witness_ui
    
    witness_window = QMainWindow()
    witness_ui = AddWitness()
    witness_ui.setupUi(witness_window)

    witness_ui.buttonBox.rejected.connect(witness_window.close)
    witness_ui.label_11.setVisible(False)
    witness_ui.buttonBox.accepted.connect(add_witness)
    witness_ui.pushButton.clicked.connect(edit_witness)

            
    levels = dbconnect.get_witness_levels()
    witness_ui.comboBox_2.clear()

    for i in levels:
        witness_ui.comboBox_2.addItem(i[1], i[0])

    stages = dbconnect.get_witness_stages()
    witness_ui.comboBox.clear()

    for i in stages:
        witness_ui.comboBox.addItem(i[1], i[0])

    witness_window.show()

#добавление свидетеля
def add_witness():
    full_name = witness_ui.lineEdit.text()
    levels = witness_ui.comboBox_2.currentText()
    stages = witness_ui.comboBox.currentText()
    
    success = dbconnect.set_witness(full_name, levels, stages)

    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно добавили информацию")
        witness_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при добавлении информации")

#редактирование свидетеля
def edit_witness():
    witness_id_text = witness_ui.lineEdit_7.text().strip()

    if not witness_id_text:
        witness_ui.label_11.setVisible(True)
        return

    witness_id = int(witness_id_text)

    full_name = witness_ui.lineEdit.text()
    levels = witness_ui.comboBox_2.currentText()
    stages = witness_ui.comboBox.currentText()

    success = dbconnect.update_witness(witness_id, full_name, levels, stages)
    if success:
        QMessageBox.information(None, "Успешно", "Вы успешно обновили информацию")
        witness_window.close()
    else:
        QMessageBox.warning(None, "Ошибка", "Ошибка при обновлении информации")

#окно преступления
def open_crime_window(crime_id):
    global crime_window, crime_ui
        
    crime_window = QMainWindow()
    crime_ui = CrimeWindow()
    crime_ui.setupUi(crime_window)

    crime_ui.btn_read_protocol.clicked.connect(lambda: open_protocol_window(crime_id))
    load_crime_window(crime_id)
    crime_window.show()

#окно протокола допроса
def open_protocol_window(crime_id):
    global protocol_window, protocol_ui
        
    protocol_window = QMainWindow()
    protocol_ui = ProtocolWindow()
    protocol_ui.setupUi(protocol_window)

    load_record_window(crime_id)
    protocol_window.show()

def soft_delete_card(crime_id):
    answer = QMessageBox.question(
            admin_window,
            "Удаление преступления",
            "Удалить преступление и связанные с ним данные?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
    
    if answer != QMessageBox.StandardButton.Yes:
        return

    if dbconnect.soft_delete(crime_id):
        # card.deleteLater()
        QMessageBox.information(
            admin_window,
            "Удаление",
            "Преступление успешно удалено."
        )
        load_crime_card(admin_ui, "admin")
    else:
        QMessageBox.critical(
            admin_window,
            "Ошибка",
            "Не удалось удалить преступление и связанные данные."
        )

def restore_crime_card(crime_id):
    print("ID для восстановления:", crime_id)
    # print("Результат восстановления:", result)
    answer = QMessageBox.question(
            admin_window,
            "восстановление преступления",
            "восстановить преступление и связанные с ним данные?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
    
    if answer != QMessageBox.StandardButton.Yes:
        return

    if dbconnect.restore_crime_from_trash(crime_id):
        # card.deleteLater()
        QMessageBox.information(
            admin_window,
            "восстановление",
            "Преступление успешно восстановлено."
        )
        load_crime_card(admin_ui, "admin")
    else:
        QMessageBox.critical(
            admin_window,
            "Ошибка",
            "Не удалось восстановить преступление и связанные данные."
        )


#отображение карточки преступления
def load_crime_card(window, role, crime_card=None):
    global crime_card_window, card_crime_ui

    if crime_card is None:
        crime_card = dbconnect.get_crime_card()
    # crime_card = dbconnect.get_crime_card()

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

    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()

        if widget is not None:
            widget.deleteLater()

    for crime in crime_card:
        crime_card_window = QWidget()
        crime_card_ui = CrimeCard()
        crime_card_ui.setupUi(crime_card_window)
        crime_id = crime[0]

        crime_card_ui.btn_delete.clicked.connect(lambda checked=False, cid=crime_id: soft_delete_card(cid))

        crime_card_ui.btn_read.clicked.connect(lambda checked=False, cid=crime_id: open_crime_window(cid))

        crime_card_ui.lbl_name.setText(str(crime[1] or ""))
        crime_card_ui.lbl_mini_descr.setText(str(crime[2] or ""))

        crime_card_window.setMinimumHeight(200)
        crime_card_window.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        layout.addWidget(crime_card_window)
        crime_card_ui.btn_delete.setVisible(False)
        crime_card_ui.btn_delete_2.setVisible(False)
        crime_card_ui.btn_delete_3.setVisible(False)
        crime_card_ui.btn_read.setVisible(True)

        if role == "admin":
            crime_card_ui.btn_delete.setVisible(True)

        elif role == "user":
            pass
        elif role == "guest":
            pass

        elif role == "investigator":
            pass

        elif role == "cart":
            crime_card_ui.btn_delete_2.setVisible(True)
            crime_card_ui.btn_delete_3.setVisible(True)
            crime_card_ui.btn_read.setVisible(False)

            layout.addStretch()
            scroll_area.setWidgetResizable(True)

#отображение карточки в корзине
def load_crime_card_in_trash(window, role):
    # global crime_card_window, card_crime_ui

    crime_card = dbconnect.get_cards_in_trash()

    scroll_area = window.scrollArea

    if scroll_area is None:
        print('скролл не найден')
        return

    container = window.scrollAreaWidgetContents

    layout = container.layout()
    if layout is None:
        layout = QVBoxLayout(container)

    layout.setContentsMargins(10, 10, 10, 10)
    layout.setSpacing(10)
    layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()

        if widget is not None:
            widget.deleteLater()

    for crime in crime_card:
        crime_card_window = QWidget()
        crime_card_ui = CrimeCard()
        crime_card_ui.setupUi(crime_card_window)
        crime_id = crime[0]

        crime_card_ui.btn_delete.setVisible(False)
        crime_card_ui.btn_read.setVisible(False)
    
        if role == "cart":
            crime_card_ui.btn_delete_2.setVisible(True)
            crime_card_ui.btn_delete_3.setVisible(True)
    
        layout.addStretch()
        scroll_area.setWidgetResizable(True)

        crime_card_ui.lbl_name.setText(str(crime[1] or ""))
        crime_card_ui.lbl_mini_descr.setText(str(crime[2] or ""))
        crime_card_ui.btn_delete_3.clicked.connect(lambda checked=False, cid=crime_id, card=crime_card_window: delete_crime(cid, card))
        crime_card_ui.btn_delete_2.clicked.connect(lambda checked=False, cid=crime_id: restore_crime_card(cid))

        crime_card_window.setMinimumHeight(200)
        crime_card_window.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        layout.addWidget(crime_card_window)


#отображение данных в окне преступления
def load_crime_window(crime_id):
    suspect = dbconnect.get_suspect_by_id(crime_id)
    crimes = dbconnect.get_crime_by_id(crime_id)
    clues = dbconnect.get_clue_by_id(crime_id)
    cases = dbconnect.get_case_by_id(crime_id)

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

def load_record_window(crime_id):
    record = dbconnect.get_record_by_crime_id(crime_id)
    print("Полученная запись протокола:", record)
    print("ID преступления:", crime_id)
    if record is not None:
        protocol_ui.lbl_date.setText(str(record[4] or "дата не указана"))
        protocol_ui.lbl_descr.setText(str(record[1] or "текст не указан"))
        # TODO: загружать аудио/видео в лейбл протокола допроса
        # protocol_ui.label_15.setText(str(record[2] or record[3] or "аудио/видео файл не приложен"))
        protocol_ui.lbl_full_name.setText(str(record[8] or "фио не указано"))
        protocol_ui.lbl_status.setText(str(record[11] or "нет статуса"))
        protocol_ui.lbl_date_birth.setText(str(record[9] or "не указана"))
        protocol_ui.lbl_degree.setText(str(record[10] or "не указана"))
        protocol_ui.lbl_witness_name.setText(str(record[5] or "фио не указано"))
        protocol_ui.lbl_level.setText(str(record[6] or "не указан"))
        protocol_ui.lbl_programm.setText(str(record[7] or "не указан"))



#авторизация пользователя
def authorization():
    login = login_ui.lineEdit.text()
    password = login_ui.lineEdit_2.text()

    user = check_login(login, password)

    if user:
        login_window.close()

        user_id = user[0]
        username = user[1]
        role = user[2]

        if role == "Администратор":
            open_admin_window()
            admin_ui.label_5.setText(username)

        elif role == "user":
            open_user_window()
            user_ui.lbl_username.setText(username)

        elif role == "Следователь":
            open_investigator_window()
            investigator_ui.lbl_username.setText(username)

        else:
            QMessageBox.warning(
                None,
                "Ошибка",
                f"Неизвестная роль пользователя: {role}"
            )
            login_window.show()

    else:
        print("no such user")
        login_ui.label_6.setVisible(True)
        login_ui.label_5.setVisible(True)

#проверка на существование пользователя и корректность введенных данных
def check_login(loginValue, passValue):
    conn = dbconnect.get_db_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT user.id, user.login, role.name
                FROM user
                JOIN role ON user.id_role = role.id
                WHERE user.login = %s AND user.password = %s
            """, (loginValue, passValue))

            user = cursor.fetchone()

        if user:
            print("ID:", user[0])
            print("Логин:", user[1])
            print("Роль:", user[2])

            return user

        return None

    except Exception as e:
        print(f"error: {e}")
        return None

    finally:
        if conn:
            conn.close()
    

#окно регистрации пользователя
def open_registration_window():
    global signin_window, signin_ui

    signin_window = QDialog()
    signin_ui = Signin()
    signin_ui.setupUi(signin_window)

    signin_ui.pushButton_2.clicked.connect(lambda: (signin_window.close(), login_window.show()))
    signin_ui.pushButton.clicked.connect(registration)

    signin_window.show()
    login_window.close()

#регистрация
def registration():
    login = signin_ui.lineEdit.text()
    password = signin_ui.lineEdit_2.text()

    success_add = dbconnect.set_user(login, password)

    if success_add:
        signin_window.close()
        open_user_window()
    else:
        print('error')

def delete_crime(crime_id, card):
    answer = QMessageBox.question(
        admin_window,
        "Удаление преступления",
        "Удалить преступление и связанные с ним данные?",
        QMessageBox.StandardButton.Yes |
        QMessageBox.StandardButton.No
    )

    if answer != QMessageBox.StandardButton.Yes:
        return

    if dbconnect.delete_crime(crime_id):
        card.deleteLater()
        QMessageBox.information(
            admin_window,
            "Удаление",
            "Преступление успешно удалено."
        )
    else:
        QMessageBox.critical(
            admin_window,
            "Ошибка",
            "Не удалось удалить преступление и связанные данные."
        )

def open_login_dialog():
    global login_window, login_ui
    
    login_window = QDialog()
    login_ui = Login()
    login_ui.setupUi(login_window)

    login_ui.pushButton.clicked.connect(authorization)
    login_ui.pushButton_2.clicked.connect(open_registration_window)
    login_ui.pushButton_3.clicked.connect(lambda: (login_window.close(), open_guest_window()))
    guest_window.close()
    login_window.show()

    login_ui.label_5.setVisible(False)
    login_ui.label_6.setVisible(False)

def open_guest_window():
    global guest_window, guest_ui
            
    guest_window = QMainWindow()
    guest_ui = GuestWindow()
    guest_ui.setupUi(guest_window)
    load_crime_card(guest_ui, "guest")
    guest_ui.pushButton.clicked.connect(open_login_dialog)

    guest_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    open_guest_window()
    sys.exit(app.exec())