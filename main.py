# TAREA DIAGRAMA DE CINE DILAN GONZÁLEZ

# Archivo main que ejecuta el models
# Primero importa las clases del models EN ESTE CASO AÑADIMOS "*" PARA QUE SE IMPORTE TODO
from datetime import date
from models import * 

print("--- REGISTRO MANUAL DE INVENTARIO CINETFLIX (10 OBJETOS) ---")

# 1. Creación de Objetos de Inventario (Snacks y Productos)
inv1 = Producto(101, "Palomitas Mantequilla XL", 95.0, "Snacks")
inv2 = Producto(102, "Refresco Cinetflix 1L", 55.0, "Bebidas")
inv3 = Producto(103, "Baguette de Pollo", 85.0, "Comida")
inv4 = Producto(104, "Nachos con Extra Queso", 75.0, "Snacks")
inv5 = Producto(105, "Dulces M&M Gigante", 40.0, "Dulces")
inv6 = Producto(106, "Té Helado Durazno", 35.0, "Bebidas")
inv7 = Producto(107, "Combo Cinetflix Pro", 250.0, "Combos")
inv8 = Producto(108, "Ticket Platinum 2D", 90.0, "Boletos")
inv9 = Producto(109, "Ticket Gold 3D", 110.0, "Boletos")
inv10 = Producto(110, "Vaso Coleccionable", 180.0, "Promos")

# Impresión de detalles para la bitácora
productos_inventario = [inv1, inv2, inv3, inv4, inv5, inv6, inv7, inv8, inv9, inv10]
for p in productos_inventario:
    print(p.mostrar_detalle())


print("\n--- VALIDACIÓN DE DATOS FINALIZADA EN CINETFLIX ---")

# --- INSTANCIACIÓN DE LOS 10 OBJETOS POR CATEGORÍA ---

# 10 Usuarios (Inspirados en tu banda y otros nombres nuevos)
u1 = Usuario("Dilan González", 1, "dilan@cinetflix.com", "222001", 1000, 500)
u2 = Usuario("Eduardo González", 2, "edu@mail.com", "222002", 450, 120)
u3 = Usuario("Gerry Bajista", 3, "gerry@rock.com", "222003", 600, 300)
u4 = Usuario("Richy Guitar", 4, "richy@rock.com", "222004", 150, 45)
u5 = Usuario("Pato Drummer", 5, "pato@rock.com", "222005", 800, 200)
u6 = Usuario("Elizabeth Amador", 6, "elyzama@mail.com", "222006", 300, 80)
u7 = Usuario("Oscar Téllez", 7, "oscar@mail.com", "222007", 500, 150)
u8 = Usuario("Sofía Galindo", 8, "sofix@mail.com", "222008", 200, 30)
u9 = Usuario("Andrés G.", 9, "andres@mail.com", "222009", 750, 400)
u10 = Usuario("Alejandra Rivera", 10, "ale@mail.com", "222010", 400, 90)
usuarios = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]

# 10 Empleados (Mezcla de Administradores y Staff)
e1 = Administrador("Andrés González", 11, "director@cinetflix.com", "555101", "admin", "Control Total")
e2 = Empleado("Juan Pérez", 12, "juan@cinetflix.com", "555102", "taquillero")
e3 = Empleado("Marco Polo", 13, "marco@cinetflix.com", "555103", "limpieza")
e4 = Empleado("Luis Lopez Tello", 14, "Ranscellot@cinetflix.com", "555104", "taquillero")
e5 = Administrador("Dilan G. Admin", 15, "dilan_admin@cinetflix.com", "555105", "admin", "Gestión Pro")
e6 = Empleado("Fabiola Solís", 16, "fabi@cinetflix.com", "555106", "limpieza")
e7 = Empleado("Roberto Carlos", 17, "rober@cinetflix.com", "555107", "taquillero")
e8 = Administrador("Ignacio S. Redfield.", 18, "NACHCRICKO@cinetflix.com", "555108", "admin", "Soporte Técnico")
e9 = Empleado("Saúl Gorgonio.", 19, "saul@cinetflix.com", "555109", "limpieza")
e10 = Empleado("Marlene V.", 20, "marlenene@cinetflix.com", "555110", "taquillero")
empleados = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

# 10 Salas Cinetflix
s1 = Sala("Sala Premium 1", "IMAX", 150, True)
s2 = Sala("Sala 2", "3D", 80, False)
s3 = Sala("Sala 3", "2D", 120, False)
s4 = Sala("Sala 4 DX", "4DX", 60, True)
s5 = Sala("Sala 5", "3D", 50, False)
s6 = Sala("Sala 6 Kidz", "2D", 100, False)
s7 = Sala("Sala 7", "2D", 90, False)
s8 = Sala("Sala VIP 8", "IMAX", 40, True)
s9 = Sala("Sala 9", "3D", 55, False)
s10 = Sala("Sala 10 Lounge", "2D", 30, True)
salas = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

# 10 Zonas de Comida
c1 = Comida("Lobby Central", 100, ["Palomitas", "Refresco"])
c2 = Comida("Zona Express", 50, ["Hot Dog", "Nachos"])
c3 = Comida("Coffee Corner", 30, ["Café", "Donas"])
c4 = Comida("Cinetflix Bar", 20, ["Cocteles", "Botanas"])
c5 = Comida("Dulcería 2", 80, ["Gomitas", "Chocolates"])
c6 = Comida("Pizza Point", 40, ["Pizza", "Refresco"])
c7 = Comida("Ice Cream Shop", 25, ["Helado", "Malteada"])
c8 = Comida("VIP Lounge Snacks", 15, ["Canapés", "Vino"])
c9 = Comida("Kiosko Norte", 60, ["Papas", "Agua"])
c10 = Comida("Snack Estelar", 70, ["Palomitas", "Jugos"])
zonas = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

# 10 Películas Cinetflix
p1 = Pelicula("Data Science: The Movie", 130, "Documental", "A")
p2 = Pelicula("Mala Idea: El Concierto", 110, "Musical", "A")
p3 = Pelicula("Invasión Python", 145, "Sci-Fi", "B")
p4 = Pelicula("El Código Perdido", 120, "Misterio", "B")
p5 = Pelicula("Algoritmo Mortal", 105, "Terror", "C")
p6 = Pelicula("La Red Social 2", 115, "Drama", "B")
p7 = Pelicula("Cyberpunk 2077: PueblaYork", 160, "Acción", "C")
p8 = Pelicula("El Viaje de la IA", 95, "Animación", "A")
p9 = Pelicula("Base de Datos Sangrienta", 140, "Thriller", "C")
p10 = Pelicula("Pandas al Rescate", 85, "Comedia", "A")
peliculas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# 10 Funciones
f1 = Funcion(p1, s1, "12:00", 150.0)
f2 = Funcion(p2, s8, "15:00", 250.0)
f3 = Funcion(p3, s2, "18:00", 120.0)
f4 = Funcion(p4, s3, "21:00", 90.0)
f5 = Funcion(p5, s4, "23:00", 180.0)
f6 = Funcion(p6, s5, "13:30", 110.0)
f7 = Funcion(p7, s1, "20:00", 150.0)
f8 = Funcion(p8, s6, "11:00", 85.0)
f9 = Funcion(p9, s7, "16:45", 100.0)
f10 = Funcion(p10, s9, "14:20", 95.0)
funciones = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

# 10 Promociones Cinetflix
pr1 = Promocion("NETFLIX10", "10% Descuento Inicial", 10, date(2026, 12, 31))
pr2 = Promocion("PRO_ESTUDIANTE", "25% Descuento Uni", 25, date(2026, 6, 30))
pr3 = Promocion("MALA_IDEA_FAN", "30% Fans de la banda", 30, date(2026, 12, 31))
pr4 = Promocion("CUMPLE_PRO", "50% Cumpleañeros", 50, date(2026, 12, 31))
pr5 = Promocion("LUNES_2X1", "50% Lunes de Locura", 50, date(2026, 5, 20))
pr6 = Promocion("VIP_ACCESS", "15% Zona VIP", 15, date(2026, 12, 31))
pr7 = Promocion("DATA_DS", "20% Futuros Científicos", 20, date(2026, 12, 31))
pr8 = Promocion("NIGHT_OWL", "12% Funciones Nocturnas", 12, date(2026, 8, 15))
pr9 = Promocion("COMBO_MAX", "10% en Dulcería", 10, date(2026, 12, 31))
pr10 = Promocion("EXPIRED", "40% Vencida", 40, date(2024, 1, 1))
promociones = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10]

# --- FUNCIONES DEL MENÚ ---

def mostrar_usuarios():
    print("REGISTRO DE USUARIOS CINETFLIX")
    for u in usuarios:
        u.login()
        print(f"Puntos: {u.puntos} | Saldo: ${u.dinero}\n")

def mostrar_empleados():
    print("PLANTILLA DE EMPLEADOS")
    for e in empleados:
        e.marcar_entrada()
        e.gestionar_funciones()
        print("-" * 15)

def mostrar_salas():
    print("SALAS DISPONIBLES")
    for s in salas:
        s.que_sala_es()
        s.limpiar()

def mostrar_zonas():
    print("ZONAS DE CONSUMO")
    for z in zonas:
        z.disponibilidad()
        print(f"Productos: {z.productos}\n")

def mostrar_peliculas():
    for p in peliculas:
        p.reseña()
        p.clasificacion_edad()

def mostrar_funciones():
    for f in funciones:
        f.detalles_funcion()

def mostrar_promociones():
    for promo in promociones:
        promo.es_valida()

def hacer_reserva():
    print("NUEVA RESERVA CINETFLIX")
    idx_u = int(input("Selecciona ID de Usuario (1-10): ")) - 1
    idx_f = int(input("Selecciona ID de Función (1-10): ")) - 1
    
    u = usuarios[idx_u]
    f = funciones[idx_f]
    
    asientos_str = input("Ingresa asientos (ej: B1,B2): ")
    asientos = [a.strip().upper() for a in asientos_str.split(",")]
    
    res = Reserva(u, f, asientos)
    
    print("\n¿Aplicar código de descuento?")
    for i, p in enumerate(promociones):
        print(f"{i+1}. {p.codigo}")
    
    p_idx = int(input("Selecciona (0 para ninguno): "))
    if p_idx != 0:
        res.aplicar_descuento(promociones[p_idx-1])
        
    res.confirmar_pago()
    res.generar_ticket()

def menu():
    while True:
        print("\n" + "="*40)
        print("         CINETFLIX - SMART CINE         ")
        print("="*40)
        print("1. Ver Usuarios       2. Ver Empleados")
        print("3. Ver Salas          4. Ver Dulcería")
        print("5. Ver Películas      6. Ver Cartelera")
        print("7. Ver Promociones    8. Reservar Ticket")
        print("0. Salir")
        
        op = input("\nSelecciona opción: ")
        if op == "1": mostrar_usuarios()
        elif op == "2": mostrar_empleados()
        elif op == "3": mostrar_salas()
        elif op == "4": mostrar_zonas()
        elif op == "5": mostrar_peliculas()
        elif op == "6": mostrar_funciones()
        elif op == "7": mostrar_promociones()
        elif op == "8": hacer_reserva()
        elif op == "0": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    menu()