import sys
import sympy
from sympy import symbols, factor, gcd

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic
#from VentanaBloque1 import Ui_VentanaBloque1_2

#FACTOR COMUN

x = sympy.symbols('x')
y = sympy.symbols('y')
z = sympy.symbols ('z')
a = sympy.symbols ('a')

#expr = 5*x*y + 4*5*x**2 + 5*2*x*z
expr = 10*a**2-5*a+15*a**2
VAR_Z = 9**2
print (VAR_Z)
factored_expr = sympy.factor(expr)
print ('cuarta')
print (factored_expr)
print ('///fin////')


#BINOMIO CUADRADO PERFECTO

# Definir el símbolo 'x'
x = sympy.symbols('x')

# Expresión del binomio al cuadrado
expr = (x + 3)**2

# Expandir la expresión
expr_expandida = sympy.expand(expr)
print("Expandida:", expr_expandida)

# Intentar factorizarla para verificar si es un cuadrado perfecto
expr_factorizada = sympy.factor(expr_expandida)
print("Factorizada:", expr_factorizada)

#DIFERENCIA DE CUADRADOS

# Definir el símbolo 'x'
x = sympy.symbols('x')

# Expresión de la diferencia de cuadrados
expr = x**2 - 9

# Intentar factorizar la diferencia de cuadrados
expr_factorizada = sympy.factor(expr)
print ('diferencia de cuadrados')
print(expr_factorizada)

#DIFERENCIA DE CUBOS
# Definir el símbolo 'x'
x = sympy.symbols('x')

# Expresión de la diferencia de cubos
expr = x**3 - 8

# Intentar factorizar la diferencia de cubos
expr_factorizada = sympy.factor(expr)
print ('Diferencia de cubos')
print(expr_factorizada)


#TRINOMIO CUADRADO PERFECTO

# Definir el símbolo 'x'
x = sympy.symbols('x')

# Expresión de un trinomio cuadrado perfecto
expr = x**2 + 4*x + 4  # (x + 2)^2

# Intentar expandir la expresión
expr_expandida = sympy.expand(expr)
print("Expandida:", expr_expandida)

# Verificar si coincide con el trinomio original
if expr_expandida == expr:
    print("La expresión es un trinomio cuadrado perfecto:", expr)
else:
    print("La expresión no es un trinomio cuadrado perfecto.")

# SUMA DE CUBOS

# Definir el símbolo 'x'
x = sympy.symbols('x')

# Expresión de suma de cubos
expr = x**3 + 8  # x^3 + 2^3

# Intentar factorizar la suma de cubos
expr_factorizada = sympy.factor(expr)
print(expr_factorizada)



