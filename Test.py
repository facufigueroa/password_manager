# Archivo con pruebas

from Clases import Clave, Usuario, Gestor
from Utils import *

# Pruebo si funciona la clase Gestor.
'''gestor = Gestor()

print(gestor)'''

# Pruebo si funciona la clase Usuario.
'''facu = Usuario("facu98", "123456789")
tiago = Usuario("tiagro", "987654321")

print(facu)
print(tiago)'''

# Pruebo si funciona la clase Clave.
'''clave1 = Clave("Sistemas-2024", "X", "elfachipiola", "x.com")
clave2 = Clave("Verano2024", "Facebook", "Facu Figueroa", "facebook.com")

print(clave1)
print(clave2)'''

# Pruebo si funciona la clase Gestor.
'''gestor = Gestor()

print(gestor)'''

# Pruebo agregar un usuario al gestor y verlo por consola.
'''facu = Usuario("facu98", "123456789")
gestor = Gestor()

gestor.verUsuarios()
gestor.agregarUsuario(facu)
gestor.verUsuarios()'''

# Pruebo si existe un usuario en el gestor.
'''facu = Usuario("facu98", "123456789")
gestor = Gestor()

print(gestor.existeUsuario(facu.nombre))
gestor.agregarUsuario(facu)
print(gestor.existeUsuario(facu.nombre))'''

# Pruebo de buscar un usuario en el gestor.
'''facu = Usuario("facu98", "123456789")
gestor = Gestor()

gestor.buscarUsuario(facu.nombre)
gestor.agregarUsuario(facu)
print(gestor.buscarUsuario(facu.nombre))'''

# Pruebo si los datos ingresados son correctos para iniciar sesión.
'''facu = Usuario("facu98", "123456789")
gestor = Gestor()
gestor.agregarUsuario(facu)

nombreUsuario1 = "facu"
claveMaestra1 = "514646546"
nombreUsuario2 = "facu98"
claveMaestra2 = "123456789"

print(gestor.claveCorrecta(nombreUsuario1, claveMaestra1))
print(gestor.claveCorrecta(nombreUsuario2, claveMaestra2))'''

# Pruebo si funciona la clase Clave.
'''clave = Clave("Verano2024", "Facebook", "Facu Figueroa", "facebook.com")

print(clave)'''

# Pruebo agregar una contraseña a un usuario.
'''facu = Usuario("facu98", "123456789")
gestor = Gestor()
gestor.agregarUsuario(facu)
clave = Clave("Verano2024", "Facebook", "Facu Figueroa", "facebook.com")

gestor.usuarios[0].verClaves()
gestor.usuarios[0].agregarClave(clave)
gestor.usuarios[0].verClaves()'''

# Pruebo editar una contraseña.
'''facu = Usuario("facu98", "123456789")
gestor = Gestor()
gestor.agregarUsuario(facu)
clave = Clave("Verano2024", "Facebook", "Facu Figueroa", "facebook.com")
gestor.usuarios[0].agregarClave(clave)
gestor.usuarios[0].verClaves()
nombreApp = "Facebook"
usuarioApp = "Facu Figueroa"
claveNueva = "Prueba123"
gestor.usuarios[0].editarClave(nombreApp, usuarioApp, claveNueva)
gestor.usuarios[0].verClaves()'''

# Pruebo eliminar una contraseña.
'''facu = Usuario("facu98", "123456789")
gestor = Gestor()
gestor.agregarUsuario(facu)
clave = Clave("Verano2024", "Facebook", "Facu Figueroa", "facebook.com")
gestor.usuarios[0].agregarClave(clave)
gestor.usuarios[0].verClaves()
nombreApp = "Facebook"
usuarioApp = "Facu Figueroa"
gestor.usuarios[0].eliminarClave(nombreApp, usuarioApp)
gestor.usuarios[0].verClaves()'''