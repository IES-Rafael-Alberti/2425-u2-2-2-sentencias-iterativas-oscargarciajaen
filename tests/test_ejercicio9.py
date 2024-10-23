from src.ejercicio9 import comprobación_de_contraseña
def test_comprobacion_de_contraseña():
    assert comprobación_de_contraseña('contraseña') == "Has introducido la contraseña correcta"