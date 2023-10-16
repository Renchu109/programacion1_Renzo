import math
import pytest
from funciones import *

#Función ejemplo
@pytest.mark.parametrize("a, b, res",[
    (2,3,5)
])
def test_suma(a,b,res):
    assert suma(a,b) == 5

#Funcion ej 1: validación DNI

@pytest.mark.parametrize("dni",[
    str(44986473)
])
def test_dni_Validation(dni):
    assert dni_Validation(dni) == True

#Funcion ej 4: número múltiplo del otro

@pytest.mark.parametrize("a,b",[
    (4,8)
])
def test_multiplo(a,b):
    assert multiplo(a,b) == False

#Funcion ej 5: temperatura media

@pytest.mark.parametrize("a,b",[
    (23,58)
])
def test_media_Temp(a,b):
    assert media_Temp != math.pi

#Funcion ej 7.1: valor maximo de una lista

@pytest.mark.parametrize("cad",[
    ([3,5,4,7,8,7,4,5,2,3,1,5,9,8,45])
]) 
def test_the_Max(cad):
    assert the_Max(cad) == 45

#Funcion ej 7.2: valor minimo de una lista

@pytest.mark.parametrize("cad",[
    ([3,5,4,7,8,7,4,5,2,3,1,5,9,8,45])
]) 
def test_the_Min(cad):
    assert the_Min(cad) == 1

#Funcion ej 8.1: area de una circunferencia

@pytest.mark.parametrize("a",[
    (20)
])
def test_calculate_Area(a):
    assert calculate_Area(a) ==  math.pi*a*a

#Funcion ej 8.2: perímetro de una circunferencia

@pytest.mark.parametrize("a",[
    (20)
])
def test_calculate_Per(a):
    assert calculate_Per(a) == math.pi*20*2