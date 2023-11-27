#VENTANA RECUPERA

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaRecupera.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from PyQt5.QtWidgets import QApplication, QMessageBox
import Aux_Recupera # Importa la clase de la ventana principal


class DlgRecupera1(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, DlgRecupera):
        DlgRecupera.setObjectName("DlgRecupera")
        DlgRecupera.resize(443, 288)
        DlgRecupera.setStyleSheet("")
        self.label = QtWidgets.QLabel(DlgRecupera)
        self.label.setGeometry(QtCore.QRect(140, 30, 251, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DlgRecupera)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 151, 61))
        self.label_2.setObjectName("label_2")
        self.TxtRecupera = QtWidgets.QLineEdit(DlgRecupera)
        self.TxtRecupera.setGeometry(QtCore.QRect(170, 150, 171, 20))
        self.TxtRecupera.setObjectName("TxtRecupera")
        self.CmdRecupera = QtWidgets.QPushButton(DlgRecupera)
        self.CmdRecupera.setGeometry(QtCore.QRect(220, 210, 75, 23))
        self.CmdRecupera.setObjectName("CmdRecupera")
        self.label_3 = QtWidgets.QLabel(DlgRecupera)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 151, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("logo_tamaño_web_vertical.png"))
        self.label_3.setObjectName("label_3")
        self.CmdCancelar = QtWidgets.QPushButton(DlgRecupera)
        self.CmdCancelar.setGeometry(QtCore.QRect(30, 230, 75, 23))
        self.CmdCancelar.setObjectName("CmdCancelar")
        self.CmdRecupera.clicked.connect(self.cedulaing)
        self.CmdCancelar.clicked.connect(self.Cancelar)
        self.retranslateUi(DlgRecupera)
        QtCore.QMetaObject.connectSlotsByName(DlgRecupera)

    def retranslateUi(self, DlgRecupera):
        _translate = QtCore.QCoreApplication.translate
        DlgRecupera.setWindowTitle(_translate("DlgRecupera", "VentanaRecupera"))
        self.label.setText(_translate("DlgRecupera", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Recuperacion de la contraseña</span></p></body></html>"))
        self.label_2.setText(_translate("DlgRecupera", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Ingresa tu numero</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">de cedula</span></p></body></html>"))
        self.CmdRecupera.setText(_translate("DlgRecupera", "Enviar"))
        self.CmdCancelar.setText(_translate("DlgRecupera", "Cancelar"))

    def mostrar_dialogo(self, titulo, mensaje):
        mensaje_box = QMessageBox()
        mensaje_box.setWindowTitle(titulo)
        mensaje_box.setText(mensaje)
        mensaje_box.setIcon(QMessageBox.Information)
        mensaje_box.setStandardButtons(QMessageBox.Ok)

        mensaje_box.exec_()

    def cedulaing(self):
        cedulatexto = self.TxtRecupera.text()
        # Conectar a la base de datos (creará una nueva si no existe)
        conexion = sqlite3.connect('BaseContrasena.db')

        # Crear un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Consultar datos
        cursor.execute("SELECT * FROM usuarios WHERE Cedula=?", (cedulatexto,))
        resultado = cursor.fetchone()  # Obtiene el primer registro que cumple con la condición

        if resultado:
            # Si el resultado no es None y contiene datos
            correo_electronico = resultado[3]
            contrasena = resultado[2]
            #print (contrasena)
            #print (correo_electronico)

            if correo_electronico:
                # Si el correo electrónico existe en la fila obtenida
                # Datos del remitente y destinatario
                remitente = 'marypenafiel@hotmail.com'
                destinatario = correo_electronico
                contrasena_p = '@Juanjose2'

                # Crear el mensaje
                mensajeC = MIMEMultipart()
                mensajeC['From'] = remitente
                mensajeC['To'] = destinatario
                mensajeC['Subject'] = 'Envío de contraseña'

                cuerpo_mensaje = 'Hola, tu contraseña es:'
                mensajeC.attach(MIMEText(cuerpo_mensaje, 'plain'))
                #print ("se generó mensaje")

                try:
                    # Establecer la conexión con el servidor SMTP
                    #print ("ingresa a try")

                    servidor_smtp = smtplib.SMTP('smtp.office365.com', 587)
                    #print ("ingresó a hotmail")
                    #print ('contrasena')
                    servidor_smtp.starttls()
                    servidor_smtp.login(remitente, contrasena_p)

                    # Enviar el correo
                    servidor_smtp.sendmail(remitente, destinatario, mensajeC.as_string())
                    #print ("verificó correo")
                    # Cerrar la conexión
                    servidor_smtp.quit()
                    #print ("Todo listo para imprimir mensaje")
                    self.mostrar_dialogo("Mensaje", "Correo electrónico enviado con éxito")
                    #print ("Cuadro de texto expuesto")

                    # Cerrar la ventana actual y abrir una nueva instancia de VentanaPrincipal
                    self.close()  # Cierra la ventana actual
                    self.ventana_principal = Aux_Recupera.VentanaAccesoModulo()  # Crea una nueva instancia de VentanaPrincipal
                    self.ventana_principal.show()  # Muestra la nueva ventana principal

                except Exception as e:
                    #print ("Todo listo para el mensaje de error")
                    self.mostrar_dialogo("Mensaje", f"Error al enviar el correo electrónico: {e}")

            else:
                # Si no se encuentra el correo electrónico en la fila obtenida
                self.mostrar_dialogo("Mensaje", "No existe el correo electrónico para ese usuario")
        else:
            # Si no se encuentra ninguna fila con esa cédula
            self.mostrar_dialogo("Mensaje", "No existe usuario con esa cédula")

        conexion.close()

    def Cancelar(self):
        self.close()  # Cierra la ventana actual
        self.ventana_principal = Aux_Recupera.VentanaAccesoModulo()  # Crea una nueva instancia de VentanaPrincipal
        self.ventana_principal.show()  # Muestra la nueva ventana principal

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = DlgRecupera1()
    ventana.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()