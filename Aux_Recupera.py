# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaAcceso.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import VentanaRecupera
import VentanaBloques
#Import Aux_Recupera

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic
import webbrowser
import sqlite3

class VentanaAccesoModulo(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, VentanaAcceso):
        VentanaAcceso.setObjectName("VentanaAcceso")
        VentanaAcceso.resize(599, 600)
        self.centralwidget = QtWidgets.QWidget(VentanaAcceso)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(40, 40, 301, 481))
        self.verticalFrame.setStyleSheet("background-color: rgb(170, 0, 0);\n"
                                             "border-radius: 10px;\n"
                                             "")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_2.setGeometry(QtCore.QRect(340, 80, 231, 401))
        self.verticalFrame_2.setStyleSheet("\n"
                                               "border-radius: 10px;\n"
                                               "background-color: rgb(0, 0, 0);\n"
                                               "")
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CboIdioma = QtWidgets.QComboBox(self.centralwidget)
        self.CboIdioma.setGeometry(QtCore.QRect(180, 70, 131, 21))
        self.CboIdioma.setObjectName("CboIdioma")
        self.CboIdioma.addItem("")
        self.CboIdioma.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 230, 211, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Desktop/Qt/ucacue-logo-centro-mediacion.png"))
        self.label_2.setObjectName("label_2")
        self.LblIngreso = QtWidgets.QLabel(self.centralwidget)
        self.LblIngreso.setGeometry(QtCore.QRect(50, 110, 61, 21))
        self.LblIngreso.setObjectName("LblIngreso")
        self.LblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.LblUsuario.setGeometry(QtCore.QRect(60, 130, 81, 31))
        self.LblUsuario.setObjectName("LblUsuario")
        self.TxtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.TxtUsuario.setGeometry(QtCore.QRect(90, 160, 141, 20))
        self.TxtUsuario.setObjectName("TxtUsuario")
        self.LblContrasena = QtWidgets.QLabel(self.centralwidget)
        self.LblContrasena.setGeometry(QtCore.QRect(60, 190, 111, 31))
        self.LblContrasena.setObjectName("LblContrasena")
        self.TxtContrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.TxtContrasena.setEchoMode(QLineEdit.Password)  # Configuración para ocultar el texto
        self.TxtContrasena.setGeometry(QtCore.QRect(90, 220, 141, 20))
        self.TxtContrasena.setObjectName("TxtContrasena")
        self.CmdRecuperarContra = QtWidgets.QPushButton(self.centralwidget)
        self.CmdRecuperarContra.setGeometry(QtCore.QRect(110, 300, 131, 23))
        self.CmdRecuperarContra.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CmdRecuperarContra.setObjectName("CmdRecuperarContra")
        self.CmdAcceder = QtWidgets.QPushButton(self.centralwidget)
        self.CmdAcceder.setGeometry(QtCore.QRect(150, 260, 61, 23))
        self.CmdAcceder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CmdAcceder.setObjectName("CmdAcceder")
        self.CmdFacebook = QtWidgets.QPushButton(self.centralwidget)
        self.CmdFacebook.setGeometry(QtCore.QRect(60, 400, 61, 41))
        self.CmdFacebook.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CmdFacebook.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("descarga (6).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CmdFacebook.setIcon(icon)
        self.CmdFacebook.setIconSize(QtCore.QSize(59, 55))
        self.CmdFacebook.setObjectName("CmdFacebook")
        self.CmdErp = QtWidgets.QPushButton(self.centralwidget)
        self.CmdErp.setGeometry(QtCore.QRect(150, 400, 61, 41))
        self.CmdErp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CmdErp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("descarga.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CmdErp.setIcon(icon1)
        self.CmdErp.setIconSize(QtCore.QSize(59, 55))
        self.CmdErp.setObjectName("CmdErp")
        self.CmdInstagram = QtWidgets.QPushButton(self.centralwidget)
        self.CmdInstagram.setGeometry(QtCore.QRect(240, 400, 61, 41))
        self.CmdInstagram.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CmdInstagram.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("descarga (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CmdInstagram.setIcon(icon2)
        self.CmdInstagram.setIconSize(QtCore.QSize(59, 55))
        self.CmdInstagram.setObjectName("CmdInstagram")
        self.CmdSalir = QtWidgets.QPushButton(self.centralwidget)
        self.CmdSalir.setGeometry(QtCore.QRect(140, 470, 75, 23))
        self.CmdSalir.setObjectName("CmdSalir")
        VentanaAcceso.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaAcceso)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        VentanaAcceso.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaAcceso)
        self.statusbar.setObjectName("statusbar")
        VentanaAcceso.setStatusBar(self.statusbar)

        self.CboIdioma.currentIndexChanged.connect(self.SeleccionaIdioma)
        self.CmdRecuperarContra.setCheckable(True)
        self.CmdRecuperarContra.clicked.connect(self.MostrarDialogo)
        self.CmdFacebook.setCheckable(True)
        self.CmdFacebook.clicked.connect(self.abrir_facebook)
        self.CmdErp.clicked.connect(self.abrir_erp)
        self.CmdInstagram.clicked.connect(self.abrir_instagram)
        self.CmdAcceder.clicked.connect(self.acceder)
        self.CmdSalir.clicked.connect(self.salirtodo)

        self.retranslateUi(VentanaAcceso)
        QtCore.QMetaObject.connectSlotsByName(VentanaAcceso)

        self.retranslateUi(VentanaAcceso)
        QtCore.QMetaObject.connectSlotsByName(VentanaAcceso)

    def retranslateUi(self, VentanaAcceso):
        _translate = QtCore.QCoreApplication.translate
        VentanaAcceso.setWindowTitle(_translate("VentanaAcceso", "VentanaAcceso"))
        self.CboIdioma.setItemText(0, _translate("VentanaAcceso", "Español"))
        self.CboIdioma.setItemText(1, _translate("VentanaAcceso", "English"))
        self.label.setText(_translate("VentanaAcceso", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Seleccionar Idioma</span></p></body></html>"))
        self.LblIngreso.setText(_translate("VentanaAcceso", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Acceso</span></p></body></html>"))
        self.LblUsuario.setText(_translate("VentanaAcceso", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">USUARIO</span></p></body></html>"))
        self.LblContrasena.setText(_translate("VentanaAcceso", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">CONTRASEÑA</span></p><p><br/></p></body></html>"))
        self.CmdRecuperarContra.setText(_translate("VentanaAcceso", "Recuperar Contraseña"))
        self.CmdAcceder.setText(_translate("VentanaAcceso", "Acceder"))
        self.CmdSalir.setText(_translate("VentanaAcceso", "Salir"))

    def SeleccionaIdioma(self):
        IdiomaSeleccionado = self.CboIdioma.currentIndex()
        if IdiomaSeleccionado == 0:
            self.LblIngreso.setText('<span style="font-size: 15px;"><b>ACCESO</b>')
            self.LblUsuario.setText('<span style="font-size: 15px;"><b>USUARIO</b>')
            self.LblContrasena.setText('<span style="font-size: 15px;"><b>CONTRASEÑA</b>')
        else:
            self.LblIngreso.setText('<span style="font-size: 15px;"><b>LOG IN</b>')
            self.LblUsuario.setText('<span style="font-size: 15px;"><b>USER</b>')

            self.LblContrasena.setText('<span style="font-size: 15px;"><b>PASSWORD</b>')

    def abrir_facebook(self):
        # URL de la página de Facebook
        url_facebook = 'https://www.facebook.com/universidadcatolicacuenca'

        # Abrir la URL en el navegador web predeterminado
        webbrowser.open(url_facebook)


    def abrir_erp(self):
        # URL de la página de Facebook
        url_erp = 'erpuniversity.ucacue.edu.ec'

        # Abrir la URL en el navegador web predeterminado
        webbrowser.open(url_erp)

    def abrir_instagram(self):
        # URL de la página de Facebook
        url_instagram = 'https://www.instagram.com/ucatolicacuenca'

        # Abrir la URL en el navegador web predeterminado
        webbrowser.open(url_instagram)



    def MostrarDialogo(self):
        try:

            self.close()  # Cierra la ventana actual
            self.VentRecu = VentanaRecupera.DlgRecupera1()
            self.VentRecu.show()
        except Exception as e:
            print(f"Error al cargar la ventana: {e}")

    def acceder(self):

        cedulatexto = self.TxtUsuario.text()
        # Conectar a la base de datos (creará una nueva si no existe)
        conexion = sqlite3.connect('BaseContrasena.db')

        # Crear un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Consultar datos
        cursor.execute("SELECT * FROM usuarios WHERE Cedula=?", (cedulatexto,))
        resultado = cursor.fetchone()  # Obtiene el primer registro que cumple con la condición

        if resultado:
            # Si el resultado no es None y contiene datos
            usuarioreg = resultado[1]
            contrasenareg = resultado[2]
            #print (contrasenareg)
            #print (usuarioreg)

            if usuarioreg == self.TxtUsuario.text():
                if contrasenareg==self.TxtContrasena.text():
                    try:
                        self.close()  # Cierra la ventana actual
                        #self.ventana_principal = VentanaAccesoModulo()  # Crea una nueva instancia de VentanaPrincipal
                        #self.ventana_principal.show()  # Muestra la nueva ventana principal
                        self.VentRecu1 = VentanaBloques.VentanaBloquesClass()

                        # with open('VentanaRecupera.py', 'r') as file:
                        #    codigo_ventana = file.read()

                        # exec(codigo_ventana)
                        self.VentRecu1.show()
                    except Exception as e:
                        print(f"Error al cargar la ventana acceder: {e}")
                    conexion.close()
                else:
                    self.mostrar_dialogo_prin("Mensaje", "Contraseña incorrecta")
                    self.TxtUsuario.setText("")
                    self.TxtContrasena.setText("")

            else:
                print ("el usuario es diferente")
            conexion.close()

        else:
            self.mostrar_dialogo_prin("Mensaje", "Datos incorrectos. Verificar")
            self.TxtUsuario.setText("")
            self.TxtContrasena.setText("")
            conexion.close()
    def mostrar_dialogo_prin(self, titulo, mensaje):
        mensaje_box = QMessageBox()
        mensaje_box.setWindowTitle(titulo)
        mensaje_box.setText(mensaje)
        mensaje_box.setIcon(QMessageBox.Information)
        mensaje_box.setStandardButtons(QMessageBox.Ok)

        mensaje_box.exec_()

    def salirtodo(self):
        sys.exit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaAccesoModulo()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
