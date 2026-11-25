 # PROYECTO FINAL: SISTEMA CRUD CON TKINTER
# Nombre del sistema: CUYO TICKETS
# Integrantes: Vanessa Fernández T03077100 Sofia Gonzalez T07275629

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import os


# ============================================================
#  CONFIGURACIÓN (Día 1)
# ============================================================
NOMBRE_SISTEMA = "CUYO TICKETS"
INTEGRANTES = "Vanessa Fernández T03077100 · Sofia Gonzalez (T07275629)"

FONDO = "white"
FONDO_GRIS = "#F2F2F2"
COLOR_TEXTO = "#833B86"
COLOR_BOTON = "#A36FE6"
COLOR_BOTON_MOUSE = "#3F8FD1"
COLOR_TEXTO_BOTON = "white"
COLOR_TITULOS = "#A01F77"

LETRA_TITULO = ("Lora", 26, "bold")
LETRA_SUBTITULO = ("DM Sans", 15, "bold")
LETRA_BOTON = ("DM Sans", 13, "bold")
LETRA_NORMAL = ("Source Sans 3", 11)

# Logo: archivo logo.png de 90 x 90 pixeles en la misma carpeta que este programa
ARCHIVO_LOGO = "logo.png"


# ============================================================
#  DATOS (Día 1)
#  Cada registro: [clave, nombre, categoría, precio, cantidad]
# ============================================================
CLAVE = "UWU210"
NOMBRE = 1
CATEGORIA = 2
PRECIO = 3
CANTIDAD = 4

PREFIJO_CLAVE = "UWU"

registros = [
    ["UWU210", "Concierto de Olivida Rodrigo", "Concierto de música Pop", 3000, 25000],
    ["UWU210", "Concierto de ENHYPEN", "Concierto de música Kpop", 2500, 20000],
    ["UWU210", "Concierto de Bad Bunny", "Concierto de música Reguetón", 2033, 14000],
    ["UWU210", "Concierto de Coldaplay", "Concierto de música Pop Rock", 2564, 58368],
    ["UWU210", "Concierto de The Weeknd", "Concierto de música Pop", 2927, 47745],
    ["UWU210", "Concierto de Bruno Mars", "Concierto de música Pop", 8538, 5301],
    ["UWU210", "Concierto de Shakira", "Concierto de música Pop latino", 2478, 38689],
    ["UWU210", "Concierto de Beyoncé", "Concierto de música Pop", 4894, 49880],
    ["UWU210", "Concierto de Stray Kids", "Concierto de música Kpop", 2897, 40823],
    ["UWU210", "Concierto de Imagine Dragons", "Concierto de música Pop rock", 2183, 44680],
]


# ============================================================
#  FUNCIONES DE APOYO (ya están listas)
# ============================================================

def mostrar(texto):
    area_resultados.config(state="normal")
    area_resultados.delete("1.0", tk.END)
    area_resultados.insert(tk.END, texto)
    area_resultados.config(state="disabled")


def generar_clave():
    numero_mayor = 0
    for registro in registros:
        numero = int(registro[CLAVE][len(PREFIJO_CLAVE):])
        if numero > numero_mayor:
            numero_mayor = numero
    return PREFIJO_CLAVE + str(numero_mayor + 1).zfill(3)


def buscar_posicion(clave_buscada):
    for posicion in range(len(registros)):
        if registros[posicion][CLAVE] == clave_buscada.upper():
            return posicion
    return -1


def etiqueta(contenedor, texto, fila):
    tk.Label(contenedor, text=texto, font=LETRA_NORMAL, bg=FONDO_GRIS, fg=COLOR_TEXTO).grid(row=fila, column=0, sticky="e", pady=4)


def caja_texto(contenedor, fila, ancho=25):
    caja = tk.Entry(contenedor, font=LETRA_NORMAL, width=ancho, bg="white", fg=COLOR_TEXTO,
                    insertbackground=COLOR_TEXTO, relief="solid", bd=1)
    caja.grid(row=fila, column=1, pady=4, padx=(6, 0))
    return caja


def boton(contenedor, texto, funcion, fila, columna):
    ttk.Button(contenedor, text=texto, style="Sistema.TButton", command=funcion).grid(row=fila, column=columna, pady=12, padx=6)


def nueva_ventanita(titulo):
    ventanita = tk.Toplevel(ventana)
    ventanita.title(titulo)
    ventanita.config(bg=FONDO_GRIS, padx=20, pady=20)
    ventanita.resizable(False, False)
    ventanita.grab_set()
    tk.Label(ventanita, text=titulo, font=LETRA_SUBTITULO, bg=FONDO_GRIS, fg=COLOR_TITULOS).grid(row=0, column=0, columnspan=2, pady=(0, 12))
    return ventanita


# ============================================================
#  REGLAS DEL SISTEMA
# ============================================================

def es_numero_valido(texto):
    # Día 2: RS02
    return True


def texto_alerta(cantidad):
    # Día 1: RS08
    return ""


def cumple_regla_propia(registro):
    # Día 3: RS10
    return False


# ============================================================
#  BIENVENIDA
# ============================================================

def bienvenida():
    area_resultados.config(state="normal")
    area_resultados.delete("1.0", tk.END)
    area_resultados.tag_configure("titulo", font=("Trebuchet MS", 24, "bold"), foreground=COLOR_TITULOS, justify="center")
    area_resultados.tag_configure("centro", font=LETRA_NORMAL, foreground=COLOR_TEXTO, justify="center")
    area_resultados.insert(tk.END, "\nBienvenidos a " + NOMBRE_SISTEMA + "\n\n", "titulo")
    area_resultados.insert(tk.END, "Usa el menú de la izquierda para administrar los registros.\n", "centro")
    area_resultados.config(state="disabled")


# ============================================================
#  IMPRIMIR (Día 1)
# ============================================================

def imprimir():
    # Día 1: RS07 y RS08
    mostrar("Día 1: aquí se muestra la tabla de registros.")


# ============================================================
#  ALTAS (Día 2)
# ============================================================

def abrir_altas():
    ventanita = nueva_ventanita("Altas")

    clave_nueva = generar_clave()
    etiqueta(ventanita, "Clave:", 1)
    tk.Label(ventanita, text=clave_nueva, font=LETRA_NORMAL, bg=FONDO_GRIS, fg=COLOR_TEXTO).grid(row=1, column=1, sticky="w", pady=4, padx=(6, 0))

    etiqueta(ventanita, "Nombre:", 2)
    caja_nombre = caja_texto(ventanita, 2)

    etiqueta(ventanita, "Precio:", 3)
    caja_precio = caja_texto(ventanita, 3)

    def guardar():
        # Día 2: RS01, RS02 y RS03
        mostrar("Día 2: aquí se guarda el registro.")
        ventanita.destroy()

    boton(ventanita, "Guardar", guardar, 10, 0)
    boton(ventanita, "Cancelar", ventanita.destroy, 10, 1)


# ============================================================
#  CONSULTAS (Día 2)
# ============================================================

def abrir_consultas():
    ventanita = nueva_ventanita("Consultas")

    etiqueta(ventanita, "Buscar:", 1)
    caja_busqueda = caja_texto(ventanita, 1)

    def buscar():
        # Día 2: RS06
        mostrar("Día 2: aquí se muestran los resultados.")
        ventanita.destroy()

    boton(ventanita, "Buscar", buscar, 2, 0)
    boton(ventanita, "Cancelar", ventanita.destroy, 2, 1)


# ============================================================
#  BAJAS (Día 3)
# ============================================================

def abrir_bajas():
    ventanita = nueva_ventanita("Bajas")

    etiqueta(ventanita, "Clave:", 1)
    caja_clave = caja_texto(ventanita, 1, 20)

    def eliminar():
        # Día 3: RS04
        mostrar("Día 3: aquí se elimina el registro.")
        ventanita.destroy()

    boton(ventanita, "Eliminar", eliminar, 2, 0)
    boton(ventanita, "Cancelar", ventanita.destroy, 2, 1)


# ============================================================
#  CAMBIOS (Día 3)
# ============================================================

def abrir_cambios():
    ventanita = nueva_ventanita("Cambios")

    etiqueta(ventanita, "Clave:", 1)
    caja_clave = caja_texto(ventanita, 1, 20)

    campo_elegido = tk.IntVar(value=NOMBRE)
    opciones = [("Nombre", NOMBRE), ("Precio", PRECIO)]
    fila = 2
    for texto_opcion, numero_campo in opciones:
        tk.Radiobutton(ventanita, text=texto_opcion, variable=campo_elegido, value=numero_campo,
                       font=LETRA_NORMAL, bg=FONDO_GRIS, fg=COLOR_TEXTO, selectcolor="white",
                       activebackground=FONDO_GRIS).grid(row=fila, column=0, columnspan=2, sticky="w", padx=40)
        fila = fila + 1

    etiqueta(ventanita, "Nuevo valor:", 8)
    caja_nuevo = caja_texto(ventanita, 8, 20)

    def guardar_cambio():
        # Día 3: RS05
        mostrar("Día 3: aquí se guarda el cambio.")
        ventanita.destroy()

    boton(ventanita, "Guardar", guardar_cambio, 9, 0)
    boton(ventanita, "Cancelar", ventanita.destroy, 9, 1)


# ============================================================
#  SALIR (Día 3)
# ============================================================

def salir():
    # Día 3: RS09
    ventana.destroy()


# ============================================================
#  VENTANA PRINCIPAL (ya está lista)
# ============================================================

ventana = tk.Tk()
ventana.title(NOMBRE_SISTEMA)
ventana.geometry("1100x650")
ventana.config(bg=FONDO)

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Sistema.TButton", font=LETRA_BOTON, background=COLOR_BOTON, foreground=COLOR_TEXTO_BOTON,
                 borderwidth=0, focuscolor=COLOR_BOTON, padding=(16, 8))
estilo.map("Sistema.TButton", background=[("active", COLOR_BOTON_MOUSE)])

encabezado = tk.Frame(ventana, bg=FONDO)
encabezado.pack(pady=15)

if os.path.exists(ARCHIVO_LOGO):
    imagen_logo = tk.PhotoImage(file=ARCHIVO_LOGO)
    ventana.iconphoto(False, imagen_logo)
    tk.Label(encabezado, image=imagen_logo, bg=FONDO).pack(side="left", padx=10)

tk.Label(encabezado, text=NOMBRE_SISTEMA, font=LETRA_TITULO, bg=FONDO, fg=COLOR_TITULOS).pack(side="left")

cuerpo = tk.Frame(ventana, bg=FONDO)
cuerpo.pack(fill="both", expand=True, padx=20)

menu = tk.Frame(cuerpo, bg=FONDO_GRIS, padx=15, pady=15)
menu.pack(side="left", fill="y")
tk.Label(menu, text="MENÚ", font=LETRA_SUBTITULO, bg=FONDO_GRIS, fg=COLOR_TITULOS).pack(pady=(0, 10))

botones = [
    ("Altas", abrir_altas),
    ("Bajas", abrir_bajas),
    ("Cambios", abrir_cambios),
    ("Consultas", abrir_consultas),
    ("Imprimir", imprimir),
    ("Salir", salir),
]
for texto_boton, funcion in botones:
    ttk.Button(menu, text=texto_boton, style="Sistema.TButton", width=12, command=funcion).pack(pady=6)

area_resultados = scrolledtext.ScrolledText(cuerpo, font=LETRA_NORMAL, bg=FONDO, fg=COLOR_TEXTO, wrap="none",
                                            tabs=(80, 290, 400, 480, 550, 680), padx=10, pady=10)
area_resultados.pack(side="left", fill="both", expand=True, padx=(15, 0))

tk.Label(ventana, text=INTEGRANTES, font=("Verdana", 10), bg=FONDO, fg="gray").pack(pady=10)

bienvenida()
ventana.mainloop()
