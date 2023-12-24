import unittest

class Usuario:

    def __init__(self, nombre, email="indefinido"):
        self.nombre = nombre
        self.email = email

    def obtener_nombre(self):
        return self.nombre

    def obtener_email(self):
        return self.email

class TestUsuario(unittest.TestCase):

    def test_obtener_email_con_email_definido(self):
        user = Usuario("Carlos", "carlos@email.com")
        email = user.obtener_email()
        self.assertEqual(email, "carlos@email.com", "Prueba fallida")

    def test_obtener_email_con_email_indefinido(self):
        user = Usuario("Juan")
        email = user.obtener_email()
        self.assertEqual(email, "indefinido", "Prueba fallida")

    def test_obtener_nombre_con_nombre_definido(self):
        user = Usuario("Ana")
        nombre = user.obtener_nombre()
        self.assertEqual(nombre, "Ana", "Prueba fallida")

    def test_obtener_nombre_con_otro_nombre_definido(self):
        user = Usuario("Luis")
        nombre = user.obtener_nombre()
        self.assertEqual(nombre, "Luis", "Prueba fallida")

if __name__ == '__main__':
    unittest.main()
