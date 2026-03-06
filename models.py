# TAREA DIAGRAMA DE CINE DILAN GONZÁLEZ
#CINETFLIX.COM!


from datetime import date

#SÁBADO 28 DE FEBRERO //////

#Definimos las clases persona y usuario que contiene la herencia de persona:

class Persona:
    def __init__(self, name, id, mail, telefono):
        self.name = name
        self.id = id
        self.mail = mail
        self.telefono = telefono

class Usuario(Persona):
    def __init__(self, name, id, mail, telefono, dinero, puntos):
        super().__init__(name, id, mail, telefono)
        self.dinero = dinero
        self.puntos = puntos
        self.historial_reservas = []

#Definimos los MÉTODOS 

    def login(self):
        print(f"\n[LOGIN] Hola {self.name}, bienvenido a CINETLFIX!.")
        print(f"Tienes un crédito disponible de: ${self.dinero}")

    def logout(self):
        print(f"[LOGOUT] Nos vemos pronto {self.name}, gracias por visitarnos.")

    def deposito(self, monto):
        self.dinero += monto
        print(f"Depósito exitoso. Nuevo saldo: ${self.dinero}")

    def crear_reserva(self, reserva):
        self.historial_reservas.append(reserva)

#DOMINGO 01 DE MARZO ####

# AHORA CLASES DE EMPLEASO (ADMIN) QUE HEREDA ATRIBUTOS DE LA CLASE PERSONA

class Empleado(Persona):
    def __init__(self, name, id, mail, telefono, trabajo):
        super().__init__(name, id, mail, telefono)
        self.trabajo = trabajo

## 04 DE MARZO CORRECCIÓN: me había faltado la clase ADMINISTRADOR DEL DIAGRAMA:
class Administrador(Empleado):
    def __init__(self, name, id, mail, telefono, trabajo, permisos):
        super().__init__(name, id, mail, telefono, trabajo)
        self.tipodepermisos = permisos




    def marcar_entrada(self):
        print(f"[NOMINA] {self.name} ha marcado su entrada.")

    def gestionar_funciones(self):
        if self.trabajo == "admin":
            print(f"[ADMIN] {self.name} está gestionando las funciones.")
        else:
            print("[!] Acceso denegado: Se requiere rol de admin.")

# MARZO 03 ################

#CLASES DE ESPACIO (osea las habitaciones del cine)

class Espacio:
    def __init__(self, lugar):
        self.lugar = lugar

    def limpiar(self):
        print(f"[LIMPIEZA] Limpiando espacio en {self.lugar}")

class Sala(Espacio):
    def __init__(self, lugar, tipo, capacidad, vip):
        super().__init__(lugar)
        self.tipo = tipo
        self.capacidad = capacidad
        self.vip = vip
        self.asientos_ocupados = []

    def que_sala_es(self):
        print(f"Sala: {self.lugar} | Tipo: {self.tipo} | Capacidad: {self.capacidad}")

    def asiento_libre(self, asiento):
        return asiento not in self.asientos_ocupados

class Pelicula:
    def __init__(self, titulo, duracion, genero, clasificacion):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.clasificacion = clasificacion

    def reseña(self):
        print(f"Película: {self.titulo} ({self.clasificacion}) - {self.genero}")


class Producto():
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio} | Categoría: {self.categoria}"



class Promocion:
    def __init__(self, codigo, descripcion, descuento, fecha_fin):
        self.codigo = codigo
        self.descripcion = descripcion
        self.descuento = descuento
        self.fecha_fin = fecha_fin

    def es_valida(self):
        # Comparamos la fecha de vencimiento con el día de hoy
        if self.fecha_fin >= date.today():
            print(f"La promoción {self.codigo} es válida.")
            return True # Retornamos True para usarlo en la lógica de pago
        else:
            print(f"La promoción {self.codigo} ha vencido.")
            return False # Retornamos False para usarlo en la lógica de pago

class Comida:    
    def __init__(self, lugar, capacidad, productos):
        self.lugar = lugar
        self.capacidad = capacidad
        self.productos = productos

    def disponibilidad(self):
        print(f"Zona: {self.lugar} | Capacidad: {self.capacidad} personas.")



class Funcion:
    def __init__(self, pelicula, sala, horario, precio):
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario
        self.precio = precio

    def detalles_funcion(self):
        self.pelicula.reseña()
        print(f"Horario: {self.horario} | Precio: ${self.precio}")

class Reserva:
    contador = 1
    def __init__(self, usuario, funcion, asientos):
        self.id = Reserva.contador
        Reserva.contador += 1
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = []
        self.estado = "Pendiente"
        
        for a in asientos:
            if self.funcion.sala.asiento_libre(a):
                self.asientos.append(a)
                self.funcion.sala.asientos_ocupados.append(a)
        
        self.total = len(self.asientos) * self.funcion.precio

    def confirmar_pago(self):
        if self.usuario.dinero >= self.total:
            self.usuario.dinero -= self.total
            self.usuario.puntos += int(self.total // 10)
            self.estado = "Confirmada"
            self.usuario.crear_reserva(self)
            print(f"Pago exitoso. Total: ${self.total}")
        else:
            print("Saldo insuficiente.")

    def generar_ticket(self):
        if self.estado == "Confirmada":
            print(f"\n--- TICKET #{self.id} ---")
            print(f"Cine CINETFLIX")
            print(f"Fecha: {date.today()}")
            print(f"Usuario: {self.usuario.name}")
            print(f"Película: {self.funcion.pelicula.titulo}")
            print(f"Horario: {self.funcion.horario}")
            print(f"Asientos: {', '.join(self.asientos)}")
            print(f"Total: ${self.total}")
        else:
            print("La reserva no ha sido confirmada.", {self.funcion.pelicula.titulo})


    def mostrar_detalle(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Categoría: {self.categoria}"