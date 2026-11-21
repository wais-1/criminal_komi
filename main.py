import sys

import dbconnect
from translate import translations

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QVBoxLayout, QSizePolicy, QMessageBox
from PySide6.QtWidgets import QLabel, QInputDialog
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QStandardItemModel, QStandardItem

import os
import requests
from dotenv import load_dotenv
import pyotp
import secrets
from password_utils import hash_password

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
from UI.CrimeLocationWindow import Ui_MainWindow as CrimeLocationWindow
from UI.AdminAccount import Ui_MainWindow as AdminAccount
from UI.TotpSetup import Ui_MainWindow as TotpSetup
from UI.UserAccount import Ui_MainWindow as UserAccount
from UI.UserAccount import Ui_MainWindow as UserAccount
from UI.InvAccount import Ui_MainWindow as InvAccount
from UI.AuthWindow import Ui_Dialog as AuthWindow
from UI.ChooseRole import Ui_Dialog as ChooseRole
from PySide6.QtCore import QDate

from typing import Optional, Tuple
import logging

from password_utils import verify_password
from totp_auth import create_totp, verify_totp
from recover_codes import generate_recovery_codes

admin_ui = None
user_ui = None
investigator_ui = None

current_language = "ru"

load_dotenv()

#получение апи ключей дадата
DADATA_API_KEY = os.getenv("DADATA_API_KEY")
DADATA_SECRET_KEY = os.getenv("DADATA_SECRET_KEY")

logger = logging.getLogger("dadata")

#добавление в файл логов при добавлении новых координат в бд
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("dadata")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    "logs/dadata_api.log",
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#получение коордитнат для корректного отображения на карте
def get_coordinates(address: str) -> Tuple[Optional[float], Optional[float]]:
    print("ok")
    if not address or not address.strip():
        return None, None

    url = "https://cleaner.dadata.ru/api/v1/clean/address"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {DADATA_API_KEY}",
        "X-Secret": DADATA_SECRET_KEY
    }

    try:
        logger.info(f"DaData запрос: {address}")
        response = requests.post(
            url,
            headers=headers,
            json=[address.strip()],
            timeout=10
        )
        logger.info(f"DaData ответ: status={response.status_code}")

        #превышение лимита заросов
        if response.status_code == 429:
            logger.warning("DaData: превышен лимит запросов")
            return None, None

        response.raise_for_status()

        result = response.json()

        if not result:
            logger.warning(f"DaData: адрес не найден: {address}")
            return None, None

        data = result[0]

        latitude = data.get("geo_lat")
        longitude = data.get("geo_lon")

        if not latitude or not longitude:
            return None, None

        return float(latitude), float(longitude)

    except requests.Timeout:
        logger.error("DaData: превышено время ожидания")

    except requests.RequestException as error:
        logger.error(f"DaData: ошибка запроса: {error}")
    return None, None

#обновление координат (ручная синхронизация)
def sync_coordinates(crime_id):
    crime_location = dbconnect.get_crime_location_by_id(crime_id)
    if not crime_location:
        return
    address = crime_location[2]

    if not address:
        show_toast(crime_location_ui.centralwidget, "адрес отсутсвует")
        return

    latitude, longitude = get_coordinates(address)

    if latitude is None or longitude is None:
        show_toast(crime_location_ui.centralwidget, "не удалось получить координаты")
        return

    coordinates = f"{latitude},{longitude}"

    dbconnect.update_coordinates(crime_location[0], coordinates)

    load_crime_location_window(crime_id)

    show_toast(crime_location_ui.centralwidget, "координаты успешно обновлены")

#тост-уведомление
def show_toast(parent, message):
    toast = QLabel(message, parent)

    toast.setStyleSheet("""
        background-color: #323232;
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        font-size: 14px;
    """)

    toast.setAlignment(Qt.AlignCenter)
    toast.adjustSize()

    toast.move((parent.width() - toast.width()) // 2, parent.height() - toast.height() - 40)

    toast.show()
    toast.raise_()

    QTimer.singleShot(5000, toast.deleteLater)

def tr(key):
    return translations[current_language].get(key, key)

#для кликабельности лейблов
class ClickableLabel(QLabel):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.window = AdminWindow()
            self.window.show()

        super().mousePressEvent(event)

def open_cart_window():
    global cart_window, cart_ui
    
    cart_window = QMainWindow()
    cart_ui = CartWindow()
    cart_ui.setupUi(cart_window)

    load_crime_card_in_trash(cart_ui, "cart")

    cart_window.show()

def open_choose_role():
    global choose_role_window, choose_role_ui
    global current_user_id
        
    choose_role_window = QMainWindow()
    choose_role_ui = ChooseRole()
    choose_role_ui.setupUi(choose_role_window)

    choose_role_ui.pushButton.clicked.connect(
        send_role_request
    )

    roles = dbconnect.get_user_role()
    choose_role_ui.comboBox.clear()

    #отображение данных вместо id в комбобоксах
    for i in roles:
        role_id = i[0]
        role_name = i[1]

        choose_role_ui.comboBox.addItem(
            role_name,
            role_id
        )

    choose_role_window.show()

def open_admin_acc():
    global admin_acc_window, admin_acc_ui
        
    admin_acc_window = QMainWindow()
    admin_acc_ui = AdminAccount()
    admin_acc_ui.setupUi(admin_acc_window)

    admin_acc_ui.pushButton_3.clicked.connect(lambda: open_totp_window(current_user_id))
    admin_acc_ui.pushButton_2.clicked.connect(lambda: admin_acc_window.close())
    load_reset_requests()
    load_roles_requests()
    load_all_users()

    admin_acc_window.show()

def load_reset_requests():

    model = QStandardItemModel()

    model.setHorizontalHeaderLabels(["Логин", "Дата запроса", "Статус", "Действие"])

    admin_acc_ui.tableView.setModel(model)

    requests = dbconnect.get_password_reset_requests()

    for request in requests:

        request_id = request[0]
        login = request[1]
        created_at = request[2]
        status = request[3]
        user_id = request[4]

        row = model.rowCount()
        model.insertRow(row)

        model.setItem(row, 0, QStandardItem(str(login)))

        model.setItem(row, 1, QStandardItem(created_at.strftime("%d.%m.%Y %H:%M")))

        status_text = "Ожидает" if status == "pending" else "Выполнен"

        model.setItem(row, 2, QStandardItem(status_text))

        if status == "pending":
            button = QPushButton("Сбросить")
            button.clicked.connect(lambda checked=False, uid=user_id, rid=request_id: reset_user_password(uid, rid))
            admin_acc_ui.tableView.setIndexWidget(model.index(row, 3), button)

    admin_acc_ui.tableView.resizeColumnsToContents()

def load_roles_requests():
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Логин", "Дата запроса", "Статус", "Роль", "Действие"])
    admin_acc_ui.tableView_2.setModel(model)
    requests = dbconnect.get_set_role_requests()

    for request in requests:

        request_id = request[0]
        login = request[1]
        created_at = request[2]
        status = request[3]
        user_id = request[4]
        role_id = request[5]

        row = model.rowCount()
        model.insertRow(row)

        model.setItem(row, 0, QStandardItem(str(login)))
        model.setItem(row, 3, QStandardItem(str(role_id)))

        model.setItem(row, 1, QStandardItem(created_at.strftime("%d.%m.%Y %H:%M")))

        status_text = "Ожидает" if status == "pending" else "Выполнен"
        model.setItem(row, 2, QStandardItem(status_text))

        if status == "pending":
            button = QPushButton("Назначить")
            button.clicked.connect(lambda checked=False, uid=user_id, rid=request_id, role_id=role_id: approve_role(uid, rid, role_id))
            admin_acc_ui.tableView_2.setIndexWidget(model.index(row, 4), button)

    admin_acc_ui.tableView.resizeColumnsToContents()

def load_all_users():
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Логин", "Роль", "Действие", "Действие"])
    admin_acc_ui.tableView_3.setModel(model)
    requests = dbconnect.get_all_users()

    for request in requests:
        user_id = request[0]
        login = request[1]
        role = request[2]

        row = model.rowCount()
        model.insertRow(row)

        model.setItem(row, 0, QStandardItem(str(login)))
        model.setItem(row, 1, QStandardItem(str(role)))

        button = QPushButton("Заблокировать")
        button.clicked.connect(lambda checked=False, uid=user_id: block_user(uid))
        admin_acc_ui.tableView_3.setIndexWidget(model.index(row, 2), button)

        button_2 = QPushButton("Разблокировать")
        button_2.clicked.connect(lambda checked=False, uid=user_id: unblock_user(uid))
        admin_acc_ui.tableView_3.setIndexWidget(model.index(row, 3), button_2)

    admin_acc_ui.tableView_3.resizeColumnsToContents()

def block_user(user_id):
    try:
        conn = dbconnect.get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE user
                SET is_blocked = 1
                WHERE id = %s
            """, (user_id))
            conn.commit()
            return True
    except Exception as e:
        print("error:", e)
        return False
    finally:
        if conn:
            conn.close()

def unblock_user(user_id):
    try:
        conn = dbconnect.get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE user
                SET is_blocked = 0
                WHERE id = %s
            """, (user_id))
            conn.commit()
            return True
    except Exception as e:
        print("error:", e)
        return False
    finally:
        if conn:
            conn.close()

def send_role_request():
    global current_user_id
    role_id = choose_role_ui.comboBox.currentData()

    if role_id is None:
        QMessageBox.warning(
            choose_role_window,
            "Ошибка",
            "Выберите роль."
        )
        return

    if dbconnect.request_role(current_user_id, role_id):

        QMessageBox.information(
            choose_role_window,
            "Готово",
            "Заявка на назначение роли отправлена администратору."
        )

        choose_role_window.close()

    else:

        QMessageBox.warning(
            choose_role_window,
            "Ошибка",
            "Не удалось отправить заявку."
        )

def reset_user_password(user_id, request_id):

    temporary_password = secrets.token_urlsafe(8)
    password_hash = hash_password(temporary_password)

    if dbconnect.reset_user_password(user_id, request_id,password_hash):
        QMessageBox.information(admin_window, "Пароль сброшен", f"Временный пароль пользователя:\n\n" f"{temporary_password}\n\n"f"Передайте его пользователю.")
        load_reset_requests()
    else:
        QMessageBox.warning(admin_window, "Ошибка", "Не удалось сбросить пароль.")

def approve_role(user_id, request_id, role_id):

    if dbconnect.approve_role_request(user_id, request_id, role_id):
        QMessageBox.information(admin_window, "Успех", f"Роль пользователя назначена")
        load_roles_requests()
    else:
        QMessageBox.warning(admin_window, "Ошибка", "Не удалось назначить роль")

def open_user_acc():
    global user_acc_window, user_acc_ui
        
    user_acc_window = QMainWindow()
    user_acc_ui = UserAccount()
    user_acc_ui.setupUi(user_acc_window)

    user_acc_ui.pushButton_3.clicked.connect(lambda: open_totp_window(current_user_id))
    user_acc_ui.pushButton_2.clicked.connect(lambda: user_acc_window.close())
    user_acc_ui.pushButton_4.clicked.connect(open_choose_role)

    user_acc_window.show()

def open_inv_acc():
    global inv_acc_window, inv_acc_ui
        
    inv_acc_window = QMainWindow()
    inv_acc_ui = InvAccount()
    inv_acc_ui.setupUi(inv_acc_window)

    inv_acc_ui.pushButton_3.clicked.connect(lambda: open_totp_window(current_user_id))
    inv_acc_ui.pushButton_2.clicked.connect(lambda: inv_acc_window.close())
    inv_acc_ui.pushButton_4.clicked.connect(open_choose_role)

    inv_acc_window.show()

def confirm_totp(user_id):
    code = totp_ui.lineEdit.text().strip()

    if verify_totp(secret, code):
        dbconnect.save_totp_secret(user_id, secret)

        QMessageBox.information(
            totp_window,
            "Успех",
            "2FA подключена!"
        )
        totp_window.close()
    else:
        totp_ui.label_7.setVisible(True)

    recovery_codes = generate_recovery_codes()

    dbconnect.save_recovery_codes(
        user_id,
        recovery_codes
    )
    QMessageBox.information(
        totp_window,
        "Резервные коды",
        "Сохраните эти коды в безопасном месте:\n\n" +
        "\n".join(recovery_codes)
    )

def enter_recovery_code(user_id, username, role):
    code, ok = QInputDialog.getText(
        auth_window,
        "Резервный код",
        "Введите резервный код:"
    )

    if ok and code:
        if dbconnect.verify_recovery_code_db(user_id, code):
            auth_window.close()
            open_user_by_role(user_id, username, role)
        else:
            QMessageBox.warning(
                auth_window,
                "Ошибка",
                "Неверный или уже использованный резервный код"
            )

def open_totp_window(user_id):
    global totp_window, totp_ui, secret
            
    totp_window = QMainWindow()
    totp_ui = TotpSetup()
    totp_ui.setupUi(totp_window)

    totp_ui.label_7.setVisible(False)

    secret, pixmap = create_totp("criminal11_user")
    totp_ui.label.setPixmap(pixmap)
    totp_ui.label.setScaledContents(True)
    totp_ui.pushButton.clicked.connect(lambda: confirm_totp(user_id))

    totp_window.show()

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
    admin_ui.label_5.mousePressEvent = lambda event: open_admin_acc()

    admin_ui.cb_lang.clear()
    admin_ui.cb_lang.addItem("ru", "ru")
    admin_ui.cb_lang.addItem("en", "en")
    admin_ui.cb_lang.setCurrentIndex(0)

    admin_ui.cb_lang.currentIndexChanged.connect(
        lambda index: change_lang(index, admin_ui)
    )  

    load_crime_card(admin_ui, "admin")
    admin_window.show()

def change_lang(index, window):
    global current_language

    current_language = window.cb_lang.currentData()

    update_interface()

def update_interface():
    if admin_ui is not None:
        admin_ui.pushButton_7.setText(tr("filters"))
        admin_ui.lineEdit.setPlaceholderText(tr("search"))
        admin_ui.btn_cart.setText(tr("cart"))
        admin_ui.btn_exit.setText(tr("exit"))
        admin_ui.pushButton_2.setText(tr("add_crime"))
        admin_ui.pushButton_3.setText(tr("add_case"))
        admin_ui.pushButton_4.setText(tr("add_record"))
        admin_ui.pushButton_5.setText(tr("add_suspect"))
        admin_ui.pushButton_6.setText(tr("add_clue"))
        admin_ui.pushButton_10.setText(tr("add_location"))
        admin_ui.pushButton_11.setText(tr("add_victim"))
        admin_ui.pushButton_12.setText(tr("add_witness"))
        admin_ui.pushButton_13.setText(tr("add_suspect_crime"))

        load_crime_card(admin_ui, "admin")

    if user_ui is not None:
        user_ui.line_search.setPlaceholderText(tr("search"))
        user_ui.pushButton_7.setText(tr("filters"))
        user_ui.btn_exit.setText(tr("exit"))
        load_crime_card(user_ui, "user")

    if investigator_ui is not None:
        investigator_ui.search.setPlaceholderText(tr("search"))
        investigator_ui.btn_add_crime.setText(tr("add_crime"))
        investigator_ui.btn_add_criminal_case.setText(tr("add_case"))
        investigator_ui.btn_add_protocol.setText(tr("add_record"))
        investigator_ui.btn_add_murder.setText(tr("add_suspect"))
        investigator_ui.btn_add_clue.setText(tr("add_clue"))
        investigator_ui.pushButton_10.setText(tr("add_location"))
        investigator_ui.pushButton_11.setText(tr("add_victim"))
        investigator_ui.pushButton_12.setText(tr("add_witness"))
        investigator_ui.pushButton_13.setText(tr("add_suspect_crime"))
        investigator_ui.btn_exit.setText(tr("exit"))
        investigator_ui.pushButton_7.setText(tr("filters"))
        load_crime_card(investigator_ui, "investigator")


#открытие окна пользователя
def open_user_window():
    global user_window, user_ui

    user_window = QMainWindow()
    user_ui = UserWindow()
    user_ui.setupUi(user_window)

    user_ui.pushButton_7.clicked.connect(open_filters_dialog)
    user_ui.btn_exit.clicked.connect(lambda:(user_window.close(), open_guest_window()))
    user_ui.line_search.textChanged.connect(lambda text: live_search(user_ui, "user", text))
    user_ui.lbl_username.mousePressEvent = lambda event: open_user_acc()

    user_ui.cb_lang.clear()
    user_ui.cb_lang.addItem("ru", "ru")
    user_ui.cb_lang.addItem("en", "en")
    user_ui.cb_lang.setCurrentIndex(0)

    user_ui.cb_lang.currentIndexChanged.connect(
        lambda index: change_lang(index, user_ui)
    )  
    
    load_crime_card(user_ui, "user")
    user_window.show()

#открытие окна следака
def open_investigator_window():
    global investigator_window, investigator_ui
    
    investigator_window = QMainWindow()
    investigator_ui = InvestigatorWindow()
    investigator_ui.setupUi(investigator_window)

    investigator_ui.pushButton_7.clicked.connect(open_filters_dialog)
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
    investigator_ui.lbl_username.mousePressEvent = lambda event: open_inv_acc()

    investigator_ui.cb_lang.clear()
    investigator_ui.cb_lang.addItem("ru", "ru")
    investigator_ui.cb_lang.addItem("en", "en")
    investigator_ui.cb_lang.setCurrentIndex(0)

    investigator_ui.cb_lang.currentIndexChanged.connect(
        lambda index: change_lang(index, investigator_ui)
    )      

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
    crime_ui.btn_read_protocol_2.clicked.connect(lambda: open_crime_location_window(crime_id))
    load_crime_window(crime_id)
    crime_window.show()

#окно места преступления
def open_crime_location_window(crime_id):
    global crime_location_window, crime_location_ui
        
    crime_location_window = QMainWindow()
    crime_location_ui = CrimeLocationWindow()
    crime_location_ui.setupUi(crime_location_window)

    crime_location_ui.pushButton.clicked.connect(lambda: sync_coordinates(crime_id))

    load_crime_location_window(crime_id)

    crime_location_window.show()

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
        QMessageBox.information(admin_window, "Удаление", "Преступление успешно удалено.")
        load_crime_card(admin_ui, "admin")
    else:
        QMessageBox.critical(admin_window, "Ошибка", "Не удалось удалить преступление и связанные данные.")

def restore_crime_card(crime_id):
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
        QMessageBox.information(admin_window, "восстановление", "Преступление успешно восстановлено.")
        load_crime_card(admin_ui, "admin")
    else:
        QMessageBox.critical(admin_window, "Ошибка", "Не удалось восстановить преступление и связанные данные.")


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

        crime_card_ui.btn_read.setText(tr("read"))
        crime_card_ui.btn_delete.setText(tr("delete"))
        crime_card_ui.btn_delete_2.setText(tr("restore"))
        crime_card_ui.btn_delete_3.setText(tr("permanent_delete"))

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
        
        crime_card_ui.btn_delete_2.setText(tr("restore"))
        crime_card_ui.btn_delete_3.setText(tr("permanent_delete"))

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

def load_crime_location_window(crime_id):
    crime_location = dbconnect.get_crime_location_by_id(crime_id)

    crime_location_ui.label_4.setText(str(crime_location[1] or "Не указано"))
    crime_location_ui.label_6.setText(str(crime_location[2] or "Не указано"))
    crime_location_ui.label_8.setText(str(crime_location[3] or "Не указано"))
    crime_location_ui.label_10.setText(str(crime_location[4] or "Не указано"))

    address = crime_location[2]
    coordinates = crime_location[1]

    if coordinates:
        latitude, longitude = map(float, coordinates.split(","))

    elif address:
        latitude, longitude = get_coordinates(address)

        if latitude is not None and longitude is not None:
            # Здесь можно сохранить координаты в БД
            pass

    else:
        latitude, longitude = None, None

    if latitude is not None and longitude is not None:
        crime_location_ui.crime_map.show_location(
            latitude,
            longitude,
            address
        )

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

def open_auth_window(user_id, username, role, secret):
    global auth_window, auth_ui

    auth_window = QMainWindow()
    auth_ui = AuthWindow()
    auth_ui.setupUi(auth_window)

    auth_ui.label_5.setVisible(False)
    auth_ui.pushButton.clicked.connect(lambda: verify_auth_code(user_id, username, role, secret))
    auth_ui.pushButton_2.clicked.connect(lambda: enter_recovery_code(user_id, username, role))

    login_window.close()
    auth_window.show()

def verify_auth_code(user_id, username, role, secret):
    code = auth_ui.lineEdit.text().strip()

    if verify_totp(secret, code):
        auth_window.close()

        open_user_by_role(user_id, username, role)
    else:
        auth_ui.label_5.setVisible(True)

def open_user_by_role(user_id, username, role):
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

#авторизация пользователя
def authorization():
    global current_user_id
    login = login_ui.lineEdit.text()
    password = login_ui.lineEdit_2.text()

    user = check_login(login, password)

    if user:
        if user[5] == 1:
            QMessageBox.warning(login_window,"Доступ запрещён", "Ваш аккаунт заблокирован.")
            return

        current_user_id = user[0]
        login_window.close()
        username = user[1]
        role = user[2]
        totp_enabled = user[3]
        totp_secret = user[4]

        if totp_enabled:
            open_auth_window(current_user_id, username, role, totp_secret)
        else:
            open_user_by_role(current_user_id, username, role)

    else:
        print("no such user")
        print("LOGIN:", login)
        print("USER:", user)
        login_ui.label_6.setVisible(True)
        login_ui.label_5.setVisible(True)

def forgot_password():
    login, ok = QInputDialog.getText(login_window, "Сброс пароля", "Введите логин:")

    if ok and login:
        dbconnect.create_reset_request(login)

        QMessageBox.information(login_window, "Запрос отправлен", "Запрос на сброс пароля отправлен администратору.")

#проверка на существование пользователя и корректность введенных данных
def check_login(loginValue, passValue):
    try:
        conn = dbconnect.get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT user.id, user.login, role.name, user.password, user.totp_enabled, user.totp_secret, user.is_blocked
                FROM `user`
                JOIN role ON user.id_role = role.id
                WHERE user.login = %s
            """, (loginValue,))

            user = cursor.fetchone()

        if user and verify_password(passValue, user[3]):
            return user[0], user[1], user[2], user[4], user[5], user[6]

        return None
    

    except Exception as e:
        print(f"Ошибка авторизации: {e}")
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
    login_ui.pushButton_4.clicked.connect(forgot_password)
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