class Empresa():
    def __init__(self):
        self.empleados=[]
    def agregar_empleado(self,empleado):
        self.empleados.append(empleado)
    def buscar_empleado(self,identificador):
        for empleado in self.empleados:
            if empleado.identificador == identificador:
                return empleado
            return None
    def mostar_empleados(self):
        for empleado in self.empleados:
            print (empleado.info())
class Empleado():
    def __init__(self,nombre,identificador,salario):
        self.nombre=nombre
        self.identificador=identificador
        self.salario=salario
    def aumentar_salario(self,aumento):
        self.salario+=aumento
        return self.salario
    def info(self):
        return f"Nombre: {self.nombre} identificador: {self.identificador} Salario: {self.salario}"
    
empleado1=Empleado("Juan", 12345, 200)
empleado1.aumentar_salario(200)
print(empleado1.info())
empleado2=Empleado("Maria", 23456, 500)
empresa=Empresa()
empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(empleado2)
empresa.mostar_empleados()
buscar=empresa.buscar_empleado(123456)
if buscar:
    print(buscar.info())
else:
    print("No existe")
