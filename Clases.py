# Archivo con las clases definidas (Clave, Usuario, Gestor)

class Clave :
    def __init__(self, clave : str, nombreApp : str, usuarioApp : str, url : str) -> None :
        self.clave = clave
        self.nombreApp = nombreApp
        self.usuarioApp = usuarioApp
        self.url = url
        self.vulnerada = False

    def __str__(self) -> str :
        return f"App: {self.nombreApp}, Clave: {self.clave}, Usuario: {self.usuarioApp}, Url: {self.url}, Vulnerada?: {self.vulnerada}"

class Usuario :
    def __init__(self, nombre : str, claveMaestra : str) -> None :
        self.nombre = nombre
        self.claveMaestra = claveMaestra
        self.claves = []

    # Método para agregar una contraseña.
    def agregarClave(self, clave : Clave) :
        self.claves.append(clave)

    # Método para ver las contraseñas de un usuario.
    def verClaves(self) :
        if len(self.claves) == 0 :
            print("No tiene contraseñas guardadas.")
        else :
            for clave in self.claves :
                print(clave)

    # Método para editar una contraseña.
    def editarClave(self, nombreApp : str, usuarioApp : str, claveNueva : str) -> None:
        claveActualizada = False
        for clave in self.claves :
            if clave.nombreApp == nombreApp :
                if clave.usuarioApp == usuarioApp :
                    clave.clave = claveNueva
                    claveActualizada = True
                    break
        print()
        if claveActualizada :
            print("¡Contraseña actualizada con éxito!")
        else :
            print("No tiene contraseñas con los datos brindados.")

    # Método para eliminar una contraseña.
    def eliminarClave(self, nombreApp : str, usuarioApp : str) -> None :
        indice = -1
        for i in range(len(self.claves)) :
            if self.claves[i].nombreApp == nombreApp and self.claves[i].usuarioApp == usuarioApp :
                indice = i
                continue
        if indice >= 0 :
            self.claves.pop(indice)
            print("¡Contraseña eliminada con éxito!")
        else :
            print("No se pudo encontrar una contraseña con los datos brindados.")

    def __str__(self) -> str :
        return f"Nombre usuario: {self.nombre}, Clave maestra: {self.claveMaestra}"

class Gestor :
    def __init__(self) -> None :
        self.usuarios : list[Usuario] = []

    # Método para agregar usuarios al gestor.
    def agregarUsuario(self, usuario : Usuario) -> None :
        self.usuarios.append(usuario)

    # Método para comprobar si el usuario existe en el gestor.
    def existeUsuario(self, nombreUsuario : str) -> bool :
        for usuario in self.usuarios :
            if usuario.nombre == nombreUsuario :
                return True
        return False

    # Método para buscar un usuario.
    def buscarUsuario(self, nombreUsuario : str) :
        for usuario in self.usuarios :
            if usuario.nombre == nombreUsuario :
                return usuario
        print("Usuario no encontrado.")

    # Método para ver por consola los usuarios existentes en el gestor.
    def verUsuarios(self) -> None :
        if len(self.usuarios) == 0 :
            print("No hay usuarios cargados.")
        else :
            for usuario in self.usuarios :
                print(usuario)

    # Método para comparar la contraseña de un usuario cuando inicia sesión.
    def claveCorrecta(self, nombreUsuario : str, claveMaestra : str) -> bool :
        for usuario in self.usuarios :
            if usuario.nombre == nombreUsuario and usuario.claveMaestra == claveMaestra :
                return True
        return False

    def __str__(self) -> str :
        return f"Usuarios: {self.usuarios}"


