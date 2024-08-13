class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return True
        return False
    def informacion(self):
        estado = "" 
        if self.disponible:
            estado="disponible"
        else:
            estado="no disponible"
        return f"Título: {self.titulo}, Estado: {estado}"
class Biblioteca:
        def __init__(self):
            self.libros=[]
        def agregar_libro(self,libro):
            self.libros.append(libro)
        def buscar_libro(self,titulo):
            for libro in self.libros:
             if libro.titulo == titulo:
                return libro
            return None
        def mostar_libros(self):
            for libro in self.libros:
                print (libro.informacion())

libro1=Libro("Mi planta naranja lima")
libro2=Libro("Codigo Limpio")
libro3=Libro("Java")
libro2.prestar()
biblioteca=Biblioteca()
libro3.prestar()
libro3.devolver()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
libroBusca="Java"
busqueda=biblioteca.buscar_libro(libroBusca)
if busqueda:
    print("Libro Encotrado  ",busqueda.informacion())
else:
    print("No existe el libro")
biblioteca.mostar_libros()
libroBusca="Donde esta mi queso"
busqueda=biblioteca.buscar_libro(libroBusca)
if busqueda:
    print("Libro Encotrado  ",busqueda.informacion())
else:
    print("No existe el libro",libroBusca)





