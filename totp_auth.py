import pyotp
import qrcode
from io import BytesIO
from PySide6.QtGui import QPixmap


def create_totp(login):
    secret = pyotp.random_base32()

    totp = pyotp.TOTP(secret)

    uri = totp.provisioning_uri(name=login, issuer_name="criminal11")

    qr = qrcode.make(uri)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    pixmap = QPixmap()
    pixmap.loadFromData(buffer.getvalue())

    return secret, pixmap


def verify_totp(secret, code):
    if not code or not code.isdigit() or len(code) != 6:
        return False

    return pyotp.TOTP(secret).verify(code, valid_window=1)