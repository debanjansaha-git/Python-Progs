"""
@Author: Debanjan
@Date: 18 Nov, 2021
@Description: Indigenous Python based browser
"""
import os
import sys
import xml.etree.ElementTree as ET
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from urllib.parse import urlparse

class MainWindow(QMainWindow):

    def __init__(self, *arg, **kwargs):
        super(MainWindow, self).__init__(*arg, **kwargs)
        self.setWindowTitle("My Browser")
        self.setWindowIcon(QIcon('./assets/web_logo.png'))
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # create a keyword suggestion model
        self._model = SuggestionModel(self)
        completer = Completer(self, caseSensitivity=Qt.CaseInsensitive)
        completer.setModel(self._model)
    
        # navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        QTimer.singleShot(0, lambda : self.setMinimumHeight(64))

        # add back button function
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # add forward button function
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # add reload button function
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # add home button function
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # edit URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setCompleter(completer)
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)

        # update URL on change
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))

    def navigate_url(self):
        url = self.url_bar.text()
        if not self.is_url(url).netloc:
            url = "https://www.google.com/search?q=" + url
        self.browser.setUrl(QUrl(url))
        
    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def is_url(self, url):
        return urlparse(url)
        

class SuggestionModel(QStandardItemModel):
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, parent=None):
        super(SuggestionModel, self).__init__(parent)
        self._manager = QNetworkAccessManager(self)
        self._reply = None

    @pyqtSlot(str)
    def search(self, text):
        self.clear()
        if self._reply is not None:
            self._reply.abort()
        if text:
            r = self.create_request(text)
            self._reply = self._manager.get(r)
            self._reply.finished.connect(self.on_finished)
        loop = QEventLoop()
        self.finished.connect(loop.quit)
        loop.exec_()

    def create_request(self, text):
        url = QUrl("http://toolbarqueries.google.com/complete/search")
        query = QUrlQuery()
        query.addQueryItem("q", text)
        query.addQueryItem("output", "toolbar")
        query.addQueryItem("hl", "en")
        url.setQuery(query)
        request = QNetworkRequest(url)
        return request

    @pyqtSlot()
    def on_finished(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            content = reply.readAll().data()
            suggestions = ET.fromstring(content)
            for data in suggestions.iter("suggestion"):
                suggestion = data.attrib["data"]
                self.appendRow(QStandardItem(suggestion))
            self.error.emit("")
        elif reply.error() != QNetworkReply.OperationCanceledError:
            self.error.emit(reply.errorString())
        else:
            self.error.emit("")
        self.finished.emit()
        reply.deleteLater()
        self._reply = None


class Completer(QCompleter):
    def splitPath(self, path):
        self.model().search(path)
        return super(Completer, self).splitPath(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('My Browser')
    window = MainWindow()
    app.exec_()