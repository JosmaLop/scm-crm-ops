import mysql.connector
import pandas as pd
from conexion import conectar

def mostrar_menu():
    print("\n" + "="*30)
    print("   CRM IMPORTACIONES BOLIVIA")
    print("="*30)
    print("1. Ver Clientes")
    print("2. Ver Proveedores")
    print("3. REGISTRAR NUEVO CLIENTE")
    print("4. Salir")
    return input("\nSelecciona una opción: ")

def consultar_tabla(tabla):
    db = conectar()
    if db:
        try:
            query = f"SELECT * FROM {tabla}"
            df = pd.read_sql(query, db)
            print(f"\n--- LISTADO DE {tabla.upper()} ---")
            if df.empty:
                print("No hay registros aún.")
            else:
                print(df.to_string(index=False))
        except Exception as e:
            print(f"Error al leer: {e}")
        finally:
            db.close()

def registrar_cliente():
    nombre = input("Nombre completo del cliente: ")
    telef = input("Teléfono: ")
    email = input("Email: ")
    perfil = input("Perfil (Gaming/Diseño/Oficina): ")
    
    db = conectar()
    if db:
        cursor = db.cursor()
        sql = "INSERT INTO clientes (nombre_completo, telefono, email, perfil_uso) VALUES (%s, %s, %s, %s)"
        valores = (nombre, telef, email, perfil)
        try:
            cursor.execute(sql, valores)
            db.commit() # ¡Esto guarda los cambios!
            print(f"\n✅ ¡Cliente '{nombre}' registrado con éxito!")
        except Exception as e:
            print(f"❌ Error al registrar: {e}")
        finally:
            db.close()

def registrar_cotizacion():
    # 1. Primero mostramos los clientes para saber a quién cotizar
    print("\n--- SELECCIONA EL ID DEL CLIENTE ---")
    consultar_tabla("clientes")
    cliente_id = input("\nIntroduce el ID del cliente: ")
    
    # 2. Pedimos los datos del equipo
    descripcion = input("Descripción del equipo (ej: Laptop RTX 4060, Monitor 4K): ")
    precio = input("Precio estimado en USD: ")
    estado = "Pendiente" # Por defecto
    
    db = conectar()
    if db:
        cursor = db.cursor()
        sql = "INSERT INTO cotizaciones (cliente_id, descripcion_equipo, estado, precio_estimado) VALUES (%s, %s, %s, %s)"
        valores = (cliente_id, descripcion, estado, precio)
        try:
            cursor.execute(sql, valores)
            db.commit()
            print(f"\n✅ Cotización registrada para el cliente ID {cliente_id}!")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            db.close()

def calculadora_precios():
    print("\n--- CALCULADORA DE IMPORTACIÓN (USD -> BOB) ---")
    precio_fob = float(input("Precio del equipo en USA (USD): "))
    tasa_cambio = 6.96  # Puedes ajustarla según el mercado
    
    # Supongamos un 15% de gastos (envío + aduana + tu ganancia)
    comision_porcentaje = 0.15 
    precio_final_usd = precio_fob * (1 + comision_porcentaje)
    precio_final_bob = precio_final_usd * tasa_cambio
    
    print(f"\n> Precio con comisión (USD): ${precio_final_usd:.2f}")
    print(f"> PRECIO DE VENTA EN BOLIVIA: {precio_final_bob:.2f} Bs.")

def buscar_por_perfil():
    perfil = input("\n¿Qué perfil buscas? (Gaming/Diseño/Oficina): ")
    db = conectar()
    if db:
        query = f"SELECT nombre_completo, telefono, email FROM clientes WHERE perfil_uso = '{perfil}'"
        df = pd.read_sql(query, db)
        print(f"\n--- CLIENTES INTERESADOS EN {perfil.upper()} ---")
        if df.empty:
            print("No hay clientes con ese perfil.")
        else:
            print(df.to_string(index=False))
        db.close()
def exportar_reporte_excel():
    db = conectar()
    if db:
        try:
            # Traemos las cotizaciones junto con el nombre del cliente (un JOIN de SQL)
            query = """
                SELECT c.nombre_completo, co.descripcion_equipo, co.precio_estimado, co.estado
                FROM cotizaciones co
                JOIN clientes c ON co.cliente_id = c.id
            """
            df = pd.read_sql(query, db)
            
            nombre_archivo = "Reporte_Importaciones_Ventas.xlsx"
            df.to_excel(nombre_archivo, index=False)
            
            print(f"\n✅ ¡ÉXITO! Se ha generado el archivo: {nombre_archivo}")
            print("Ya puedes abrirlo con Excel para tu reporte.")
        except Exception as e:
            print(f"❌ Error al exportar: {e}")
        finally:
            db.close()

# Bucle principal del CRM
# Actualiza el menú
def mostrar_menu():
    print("\n" + "X"*30)
    print("   SISTEMA DE ENTREGAS CRM")
    print("X"*30)
    print("1. Ver Clientes")
    print("2. Ver Proveedores")
    print("3. REGISTRAR CLIENTE")
    print("4. CREAR COTIZACIÓN")
    print("5. VER COTIZACIONES")
    print("6. CALCULADORA USD/BOB")
    print("7. BUSCAR POR PERFIL")
    print("8. EXPORTAR REPORTE A EXCEL")
    print("9. Salir")
    return input("\nAcción a realizar: ")
# Actualiza el bucle
while True:
    opcion = mostrar_menu()
    if opcion == "1":
        consultar_tabla("clientes")
    elif opcion == "2":
        consultar_tabla("proveedores")
    elif opcion == "3":
        registrar_cliente()
    elif opcion == "4":
        registrar_cotizacion()
    elif opcion == "5":
        consultar_tabla("cotizaciones")
    elif opcion == "6":
        calculadora_precios()
    elif opcion == "7":
        buscar_por_perfil()
    elif opcion == "8":
        exportar_reporte_excel()
    elif opcion == "9":
        print("Guardando sesión... Programa finalizado.")
        break