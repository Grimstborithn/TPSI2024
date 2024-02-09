from contacto import Contacto, Morada
from utils import DataError, divZero








contacto1 = Contacto("João", "123456789", "Rua A", "01/01/1990")
contacto1.adicionar_telefone("987654321")
print(contacto1)