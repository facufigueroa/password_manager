# Importamos clases y funciones necesarias.
from Clases import Gestor
from Utils import *

gestor = Gestor()

# Cargamos los usuarios existentes contenidos en el archivo de texto.
# Si no existe el archivo, lo creamos.
try :
    leerUsuarios = open("Usuarios.txt", "r", encoding = "utf-8")
    cargarUsuariosAlGestor(gestor, leerUsuarios)
    leerUsuarios.close()
except :
    usuariosText = open("Usuarios.txt", "x", encoding = "utf-8")
    usuariosText.close()

opcion = -1

print("¡Bienvenido al gestor de contraseñas!")

while opcion != 0 :
    # Menu principal.
    print()
    print("Menu principal")
    print("1) Iniciar sesión")
    print("2) Registrarse")
    print("0) Salir")

    opcion = input("Elija una opción: ")
    
    while opcion != "1" and opcion != "2" and opcion != "0" :
        print("Debe ingresar una opción valida!")
        opcion = input("Elija una opción: ")
    
    opcion = int(opcion)
    
    # Cerrar programa.
    if opcion == 0 :
        print("¡Hasta la próxima!")
        break

    # Inicio de sesión.
    elif opcion == 1 :
        nombreUsuario = strValido("Ingrese su nombre de usuario: ")
        if gestor.existeUsuario(nombreUsuario) :
            claveUsuario = strValido("Ingrese su contraseña maestra: ")
            while not gestor.claveCorrecta(nombreUsuario, claveUsuario) :
                claveUsuario = strValido("Contraseña incorrecta. Pruebe de nuevo: ")
        else :
            print("Usuario no encontrado.")
            continue

    # Registro de usuario.
    elif opcion == 2 :
        nombreUsuario = strValido("Ingrese el nombre de usuario: ")
        while gestor.existeUsuario(nombreUsuario) :
            nombreUsuario = strValido("El nombre de usuario ingresado está ocupado. Ingrese otro: ")

        claveUsuario = strValido("Ingrese una contraseña, esta será su contraseña maestra: ")
        while not validarClave(claveUsuario) :
            claveUsuario = strValido("Ingrese otra contraseña: ")

        nuevoUsuario = crearUsuario(nombreUsuario, claveUsuario)
        print(f"¡Usuario creado con éxito! -> {nuevoUsuario.__str__()}")
        gestor.agregarUsuario(nuevoUsuario)

    usuario = gestor.buscarUsuario(nombreUsuario)

    # Menu de usuario.
    print()
    print(f"¡Bienvenido {nombreUsuario}!")
    
    sesion = -1
    
    while sesion != 0 :
        print()
        print("Menu usuario")
        print("1) Agregar contraseña")
        print("2) Ver contraseñas")
        print("3) Editar contraseña")
        print("4) Eliminar contraseña")
        print("0) Cerrar sesión")

        sesion = input("¿Qué deseas hacer? ")

        while sesion != "1" and sesion != "2" and sesion != "3" and sesion != "4" and sesion != "0" :
            print()
            print("¡Debe ingresar una opción valida!")
            sesion = input("¿Qué deseas hacer? ")
        
        sesion = int(sesion)
        print()
        
        # Cerrar sesión.
        if sesion == 0 :
            break
        
        # Agregar contraseña.
        elif sesion == 1 :
            nombreApp = strValido("Ingrese el nombre de la aplicación: ")
            usuarioApp = strValido("Ingrese su nombre de usuario de la aplicación: ")
            claveApp = strValido("Ingrese la contraseña de la aplicación: ")
            urlApp = strValido("Ingrese la url de la aplicación: ")
            usuario.agregarClave(crearClave(claveApp, nombreApp, usuarioApp, urlApp))
        
        # Ver contraseñas.
        elif sesion == 2 :
            usuario.verClaves()
        
        # Editar contraseña.
        elif sesion == 3 :
            nombreApp = strValido("Ingrese el nombre de la aplicación que desea cambiar la contraseña: ")
            usuarioApp = strValido("Ingrese el nombre de usuario de la aplicación que desea cambiar la contraseña: ")
            claveNueva = strValido("Ingrese la nueva contraseña: ")
            usuario.editarClave(nombreApp, usuarioApp, claveNueva)
        
        # Eliminar contraseña.
        elif sesion == 4 :
            nombreApp = strValido("Ingrese el nombre de la aplicación que desea borrar la contraseña: ")
            usuarioApp = strValido("Ingrese el nombre de usuario de la aplicación: ")
            print("¿Está seguro de eliminar la contraseña? Este proceso es irreversible.")
            confirmacion = strValido("Ingrese 'si' si desea continuar. De lo contrario ingrese 'no': ")
            if confirmacion == "si" :
                usuario.eliminarClave(nombreApp, usuarioApp)
            else :
                print("Proceso abortado")

agregarUsuarios = open("Usuarios.txt", "r+", encoding = "utf-8")
cargarUsuariosAlText(gestor, agregarUsuarios)
agregarUsuarios.close()