# Archivo con funciones útiles

from Clases import Usuario, Clave, Gestor

# Función para validar strings.
def strValido(mensaje : str) -> str :
    cadena = input(mensaje)
    while cadena == "" :
        print("¡Debe escribir un valor válido!")
        cadena = input(mensaje)
    return cadena

# Función para crear un usuario.
def crearUsuario(nombre : str, claveMaestra : str) -> Usuario :
    usuario = Usuario(nombre, claveMaestra)
    return usuario

# Función para crear una contraseña.
def crearClave(clave : str, nombreApp : str, usuarioApp : str, url : str) -> Clave :
    nuevaClave = Clave(clave, nombreApp, usuarioApp, url)
    print()
    print("¡Contraseña agregada con éxito!")
    return nuevaClave

# Función para validar una contraseña.
# Tiene que tener entre 8 y 16 caracteres.
# No puede tener espacios.
# Puede contener letras y números.
# Devuelve True si es válida, y si no, devuelve False.
def validarClave(clave : str) -> bool :
    tamaño = 7 < len(clave) < 17
    hayEspacios = " " in clave
    soloLetrasYNumeros = True
    for cha in clave :
        if not ((48 <= ord(cha) <= 57) or (65 <= ord(cha) <= 90) or (97 <= ord(cha) <= 122)) :
            soloLetrasYNumeros = False
            break
    if not tamaño :
        print("La contraseña debe tener entre 8 y 16 caracteres.")
        return False
    elif hayEspacios :
        print("La contraseña no puede contener espacios.")
        return False
    elif not soloLetrasYNumeros :
        print("La contraseña solo puede contener letras y números.")
        return False
    else :
        return True

# Función para cargar los usuarios existentes contenidos en el archivo de texto, al gestor.
def cargarUsuariosAlGestor(gestor : Gestor, documento) -> None :
    for usuario in documento :
        datos = usuario.split(",")
        # datos = ["Nombre usuario: facu98", " Clave maestra: 12345678"]
        nombre = datos[0][16:]
        # nombre = "facu98"
        clave = datos[1][16:]
        # clave = "12345678"
        gestor.agregarUsuario(crearUsuario(nombre, clave))

# Función para saber si un usuario existe en el archivo de texto.
def existeUsuarioText(documento, nombreUsuario) -> bool :
    for usuario in documento :
        datos = usuario.split(", ")
        nombre = datos[0][16:]
        if nombre == nombreUsuario :
            return True
    return False

# Función para cargar los usuarios existentes contenidos en el gestor, al archivo de texto.
def cargarUsuariosAlText(gestor : Gestor, documento) -> None :
    for usuario in gestor.usuarios :
        if not existeUsuarioText(documento, usuario.nombre) :
            documento.write(f"{usuario.__str__()},\n")

# Función para cargar las claves existentes de cada usuario contenidos en el gestor, al archivo de texto.
''' def cargarClavesAlText(gestor : Gestor, documento) :
    for usuario in gestor.usuarios :
        for clave in usuario.claves :
            documento.write(f"{usuario.nombre},")'''
