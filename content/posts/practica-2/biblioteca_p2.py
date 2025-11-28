import json
import os
from abc import ABC, abstractmethod

# Clase para ítems
class Item(ABC):
    def __init__(self, id, titulo, autor=None):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._disponible = True
    
    def get_id(self):
        return self._id
    
    def get_titulo(self):
        return self._titulo
    
    def get_autor(self):
        return self._autor
    
    def esta_disponible(self):
        return self._disponible
    
    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True
        return False
    
    def devolver(self):
        self._disponible = True
    
    @abstractmethod
    def mostrar_info(self):
        pass
    
    @abstractmethod
    def to_dict(self):
        pass

# Clase Libro 
class Libro(Item):
    def __init__(self, id, titulo, autor, año_publicacion, genero):
        super().__init__(id, titulo, autor)
        self._año_publicacion = año_publicacion
        self._genero = genero
    
    def get_año_publicacion(self):
        return self._año_publicacion
    
    def get_genero(self):
        return self._genero
    
    def mostrar_info(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"\nID: {self._id}\nTítulo: {self._titulo}\nAutor: {self._autor}\nAño: {self._año_publicacion}\nGénero: {self._genero}\nEstado: {estado}"
    
    def to_dict(self):
        return {
            'tipo': 'libro',
            'id': self._id,
            'titulo': self._titulo,
            'autor': self._autor,
            'año_publicacion': self._año_publicacion,
            'genero': self._genero,
            'disponible': self._disponible
        }
    
    @staticmethod
    def from_dict(data):
        libro = Libro(data['id'], data['titulo'], data['autor'], 
                     data['año_publicacion'], data['genero'])
        libro._disponible = data['disponible']
        return libro

# Clase Revista
class Revista(Item):
    def __init__(self, id, titulo, autor, año, numero_edicion):
        super().__init__(id, titulo, autor)
        self._año = año
        self._numero_edicion = numero_edicion
    
    def get_numero_edicion(self):
        return self._numero_edicion
    
    def mostrar_info(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"\nID: {self._id}\nTítulo: {self._titulo}\nAutor/Editor: {self._autor}\nAño: {self._año}\nEdición: #{self._numero_edicion}\nEstado: {estado}"
    
    def to_dict(self):
        return {
            'tipo': 'revista',
            'id': self._id,
            'titulo': self._titulo,
            'autor': self._autor,
            'año': self._año,
            'numero_edicion': self._numero_edicion,
            'disponible': self._disponible
        }
    
    @staticmethod
    def from_dict(data):
        revista = Revista(data['id'], data['titulo'], data['autor'],
                         data['año'], data['numero_edicion'])
        revista._disponible = data['disponible']
        return revista

# Clase Usuario
class Usuario:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre
        self._items_prestados = []
    
    def get_id(self):
        return self._id
    
    def get_nombre(self):
        return self._nombre
    
    def get_items_prestados(self):
        return self._items_prestados.copy()
    
    def prestar_item(self, item_id):
        self._items_prestados.append(item_id)
    
    def devolver_item(self, item_id):
        if item_id in self._items_prestados:
            self._items_prestados.remove(item_id)
            return True
        return False
    
    def tiene_item(self, item_id):
        return item_id in self._items_prestados
    
    def mostrar_info(self):
        return f"\nID Usuario: {self._id}\nNombre: {self._nombre}\nÍtems prestados: {len(self._items_prestados)}"
    
    def to_dict(self):
        return {
            'id': self._id,
            'nombre': self._nombre,
            'items_prestados': self._items_prestados
        }
    
    @staticmethod
    def from_dict(data):
        usuario = Usuario(data['id'], data['nombre'])
        usuario._items_prestados = data['items_prestados']
        return usuario

# Clase Biblioteca 
class Biblioteca:
    def __init__(self):
        self._items = []
        self._usuarios = []
    
    def agregar_item(self, item):
        if self._buscar_item(item.get_id()):
            print("Error: Ya existe un ítem con ese ID")
            return False
        self._items.append(item)
        print(f"Ítem '{item.get_titulo()}' agregado exitosamente")
        return True
    
    def agregar_usuario(self, usuario):
        if self._buscar_usuario(usuario.get_id()):
            print("Error: Ya existe un usuario con ese ID")
            return False
        self._usuarios.append(usuario)
        print(f"Usuario '{usuario.get_nombre()}' agregado exitosamente")
        return True
    
    def _buscar_item(self, item_id):
        for item in self._items:
            if item.get_id() == item_id:
                return item
        return None
    
    def _buscar_usuario(self, usuario_id):
        for usuario in self._usuarios:
            if usuario.get_id() == usuario_id:
                return usuario
        return None
    
    def prestar_item(self, usuario_id, item_id):
        usuario = self._buscar_usuario(usuario_id)
        item = self._buscar_item(item_id)
        
        if not usuario:
            print("Error: Usuario no encontrado")
            return False
        
        if not item:
            print("Error: Ítem no encontrado")
            return False
        
        if not item.esta_disponible():
            print("Error: El ítem no está disponible")
            return False
        
        item.prestar()
        usuario.prestar_item(item_id)
        print(f"Ítem '{item.get_titulo()}' prestado a {usuario.get_nombre()}")
        return True
    
    def devolver_item(self, usuario_id, item_id):
        usuario = self._buscar_usuario(usuario_id)
        item = self._buscar_item(item_id)
        
        if not usuario:
            print("Error: Usuario no encontrado")
            return False
        
        if not item:
            print("Error: Ítem no encontrado")
            return False
        
        if not usuario.tiene_item(item_id):
            print("Error: El usuario no tiene este ítem prestado")
            return False
        
        item.devolver()
        usuario.devolver_item(item_id)
        print(f"Ítem '{item.get_titulo()}' devuelto por {usuario.get_nombre()}")
        return True
    
    def mostrar_items(self):
        if not self._items:
            print("\nNo hay ítems en la biblioteca")
            return
        
        print("\n=== ÍTEMS EN LA BIBLIOTECA ===")
        for item in self._items:
            print(item.mostrar_info())
    
    def mostrar_usuarios(self):
        if not self._usuarios:
            print("\nNo hay usuarios registrados")
            return
        
        print("\n=== USUARIOS REGISTRADOS ===")
        for usuario in self._usuarios:
            print(usuario.mostrar_info())
            if usuario.get_items_prestados():
                print("Ítems prestados:")
                for item_id in usuario.get_items_prestados():
                    item = self._buscar_item(item_id)
                    if item:
                        print(f"  - {item.get_titulo()}")
    
    def buscar_usuario(self, usuario_id):
        usuario = self._buscar_usuario(usuario_id)
        if usuario:
            print(usuario.mostrar_info())
            if usuario.get_items_prestados():
                print("\nÍtems prestados:")
                for item_id in usuario.get_items_prestados():
                    item = self._buscar_item(item_id)
                    if item:
                        print(item.mostrar_info())
        else:
            print("Usuario no encontrado")
    
    def guardar_datos(self, archivo_items='items.json', archivo_usuarios='usuarios.json'):
        # Guardar ítems
        items_data = [item.to_dict() for item in self._items]
        with open(archivo_items, 'w', encoding='utf-8') as f:
            json.dump(items_data, f, ensure_ascii=False, indent=2)
        
        # Guardar usuarios
        usuarios_data = [usuario.to_dict() for usuario in self._usuarios]
        with open(archivo_usuarios, 'w', encoding='utf-8') as f:
            json.dump(usuarios_data, f, ensure_ascii=False, indent=2)
        
        print("Datos guardados exitosamente")
    
    def cargar_datos(self, archivo_items='items.json', archivo_usuarios='usuarios.json'):
        # Cargar ítems
        if os.path.exists(archivo_items):
            with open(archivo_items, 'r', encoding='utf-8') as f:
                items_data = json.load(f)
                for data in items_data:
                    if data['tipo'] == 'libro':
                        self._items.append(Libro.from_dict(data))
                    elif data['tipo'] == 'revista':
                        self._items.append(Revista.from_dict(data))
            print(f"Cargados {len(self._items)} ítems")
        
        # Cargar usuarios
        if os.path.exists(archivo_usuarios):
            with open(archivo_usuarios, 'r', encoding='utf-8') as f:
                usuarios_data = json.load(f)
                for data in usuarios_data:
                    self._usuarios.append(Usuario.from_dict(data))
            print(f"Cargados {len(self._usuarios)} usuarios")

def mostrar_menu():
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("="*50)
    print("1. Agregar libro")
    print("2. Agregar revista")
    print("3. Mostrar todos los ítems")
    print("4. Agregar usuario")
    print("5. Mostrar usuarios")
    print("6. Prestar ítem")
    print("7. Devolver ítem")
    print("8. Buscar usuario")
    print("9. Guardar y salir")
    print("="*50)

def main():
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una opción: ").strip()
            
            if opcion == '1':
                id = int(input("ID del libro: "))
                titulo = input("Título: ")
                autor = input("Autor: ")
                año = int(input("Año de publicación: "))
                genero = input("Género: ")
                libro = Libro(id, titulo, autor, año, genero)
                biblioteca.agregar_item(libro)
            
            elif opcion == '2':
                id = int(input("ID de la revista: "))
                titulo = input("Título: ")
                autor = input("Editor: ")
                año = int(input("Año: "))
                edicion = int(input("Número de edición: "))
                revista = Revista(id, titulo, autor, año, edicion)
                biblioteca.agregar_item(revista)
            
            elif opcion == '3':
                biblioteca.mostrar_items()
            
            elif opcion == '4':
                id = int(input("ID del usuario: "))
                nombre = input("Nombre: ")
                usuario = Usuario(id, nombre)
                biblioteca.agregar_usuario(usuario)
            
            elif opcion == '5':
                biblioteca.mostrar_usuarios()
            
            elif opcion == '6':
                usuario_id = int(input("ID del usuario: "))
                item_id = int(input("ID del ítem: "))
                biblioteca.prestar_item(usuario_id, item_id)
            
            elif opcion == '7':
                usuario_id = int(input("ID del usuario: "))
                item_id = int(input("ID del ítem: "))
                biblioteca.devolver_item(usuario_id, item_id)
            
            elif opcion == '8':
                usuario_id = int(input("ID del usuario: "))
                biblioteca.buscar_usuario(usuario_id)
            
            elif opcion == '9':
                biblioteca.guardar_datos()
                print("\n¡Hasta pronto!")
                break
            
            else:
                print("Opción no válida")
        
        except ValueError:
            print("Error: Ingresa un valor válido")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido")
            biblioteca.guardar_datos()
            break

if __name__ == "__main__":
    main()
