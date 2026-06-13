from argon2 import PasswordHasher
import re

ph = PasswordHasher()

def hash_password(password_plain):
    return ph.hash(password_plain)

def validar_complejidad_contraseña(password):
    """Validar complejidad de contraseña."""
    if len(password) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres"
    if not re.search(r'[A-Z]', password):
        return False, "La contraseña debe contener al menos una letra mayúscula"
    if not re.search(r'[a-z]', password):
        return False, "La contraseña debe contener al menos una letra minúscula"
    if not re.search(r'\d', password):
        return False, "La contraseña debe contener al menos un número"
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        return False, "La contraseña debe contener al menos un carácter especial"
    return True, "Contraseña válida"
