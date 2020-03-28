import re

string_validar = input("Ingrese la contraseña:")

objeto = re.match('[A-Z][0-9]{3}[a-z]{1,}\W{3}',string_validar)

if(bool(objeto)):
    print("La contraseña es valida.")
else:
    print("La contraseña no es valida.")
