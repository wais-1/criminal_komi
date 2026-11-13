import folium
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView


class CrimeMap(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

    def show_location(self, latitude, longitude, address="Место преступления"):

        crime_map = folium.Map(
            location=[latitude, longitude],
            zoom_start=16,
            tiles="OpenStreetMap"
        )

        folium.Marker(
            location=[latitude, longitude],
            popup=address,
            tooltip="Место преступления",
            icon=folium.Icon(color="red")
        ).add_to(crime_map)

        self.web_view.setHtml(crime_map.get_root().render())
