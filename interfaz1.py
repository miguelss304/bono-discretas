import tkinter as tk
from tkinter import messagebox
import pyglet
import os

from matematicas import (
    factorial_iterativo,
    factorial_recursivo,
    calcular_permutacion,
    comparar_factoriales,
    casos_de_ejemplo_1,
    calcular_combinacion,
    verificar_identidad,
    generar_triangulo_pascal,
    casos_de_ejemplo_2
)

# ============================================================
# CONFIGURACION DE FUENTE Y TEMA
# ============================================================

pyglet.font.add_file("pixelplay.ttf")
FUENTE_TITULO  = ("Pixelplay", 30, "bold")
FUENTE_NORMAL  = ("Pixelplay", 18)
FUENTE_MONO    = ("Courier New", 12)

COLOR_FONDO     = "#1e1e2e"
COLOR_ACENTO    = "#89b4fa"
COLOR_BOTON     = "#313244"
COLOR_TEXTO     = "#cdd6f4"
COLOR_GRIS      = "#585b70"
COLOR_RESULTADO = "#181825"
COLOR_TAB_ACT   = "#313244"
COLOR_TAB_INA   = "#1e1e2e"



# ============================================================
# CALCULOS PROBLEMA 1
# ============================================================

def calcular_p1():
    text_res_p1.config(state="normal")
    text_res_p1.delete("1.0", tk.END)

    try:
        n = int(entry_n_p1.get())
        r = int(entry_r_p1.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo numeros enteros.")
        return
    if n < 0 or r < 0:
        messagebox.showerror("Error", "n y r deben ser >= 0.")
        return
    if r > n:
        messagebox.showerror("Error", f"r no puede ser mayor que n.\nr={r}, n={n}.")
        return

    resultado   = calcular_permutacion(n, r)
    comparacion = comparar_factoriales(n)
    ejemplos    = casos_de_ejemplo_1()

    texto = (
        f"P({n}, {r})  =  {n}! / ({n}-{r})!\n"
        f"         =  {factorial_iterativo(n)} / {factorial_iterativo(n-r)}\n"
        f"         =  {resultado}\n\n"
        f"-- Comparacion de {n}! --\n"
        f"Iterativo  :  {comparacion['iterativo']}\n"
        f"Recursivo  :  {comparacion['recursivo']}\n"
        f"Iguales?   :  {comparacion['son_iguales']}\n\n"
        f"-- Casos de ejemplo --\n"
    )
    for a, b, p in ejemplos:
        texto += f"P({a:>2}, {b:>2})  =  {p}\n"

    text_res_p1.insert("1.0", texto)
    text_res_p1.config(state="disabled")


# ============================================================
# CALCULOS PROBLEMA 2
# ============================================================

def calcular_p2():
    text_res_p2.config(state="normal")
    text_res_p2.delete("1.0", tk.END)

    try:
        n = int(entry_n_p2.get())
        r = int(entry_r_p2.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo numeros enteros.")
        return
    if n < 0 or r < 0:
        messagebox.showerror("Error", "n y r deben ser >= 0.")
        return
    if r > n:
        messagebox.showerror("Error", f"r no puede ser mayor que n.\nr={r}, n={n}.")
        return

    resultado = calcular_combinacion(n, r)
    identidad = verificar_identidad(n, r)
    triangulo = generar_triangulo_pascal(n)
    ejemplos  = casos_de_ejemplo_2()

    # Triangulo centrado
    filas_texto = []
    ancho_max = len("  ".join(str(x) for x in triangulo[-1])) + 4
    for fila in triangulo:
        fila_str = "  ".join(str(x) for x in fila)
        filas_texto.append(fila_str.center(ancho_max))
    texto_triangulo = "\n".join(filas_texto)

    texto = (
        f"C({n}, {r})  =  {n}! / ({r}! * {n-r}!)\n"
        f"         =  {factorial_iterativo(n)} / ({factorial_iterativo(r)} * {factorial_iterativo(n-r)})\n"
        f"         =  {resultado}\n\n"
        f"-- Identidad C(n,r) = C(n,n-r) --\n"
        f"C({n},{r})    =  {identidad['C(n,r)']}\n"
        f"C({n},{n-r})  =  {identidad['C(n,n-r)']}\n"
        f"Iguales?  =  {identidad['son_iguales']}\n\n"
        f"-- Triangulo de Pascal hasta fila {n} --\n\n"
        f"{texto_triangulo}\n\n"
        f"-- Ejemplos de uso --\n"
    )
    for a, b, c in ejemplos:
        texto += f"C({a:>2}, {b:>2})  =  {c}\n"

    text_res_p2.insert("1.0", texto)
    text_res_p2.config(state="disabled")


# ============================================================
# CONSTRUCCION DE LA VENTANA
# ============================================================

ventana = tk.Tk()
ventana.title("Combinatoria — Discretas I")
ventana.configure(bg=COLOR_FONDO)
ventana.resizable(True, True)

if os.path.exists("icon.ico"):
    ventana.iconbitmap("icon.ico")

# Centrar en pantalla
ventana.update_idletasks()
ancho, alto = 900, 620
x = (ventana.winfo_screenwidth()  // 2) - (ancho // 2)
y = (ventana.winfo_screenheight() // 2) - (alto  // 2)
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


tk.Label(
    ventana,
    text="Calculadora Combinatoria",
    font=FUENTE_TITULO,
    bg=COLOR_FONDO,
    fg=COLOR_ACENTO
).pack(pady=(18, 0))


frame_tabs = tk.Frame(ventana, bg=COLOR_FONDO)
frame_tabs.pack(fill="x", padx=20, pady=(10, 0))

btn_tab1 = tk.Button(
    frame_tabs, text="Permutaciones  P(n,r)",
    font=FUENTE_NORMAL, bg=COLOR_TAB_ACT, fg=COLOR_ACENTO,
    relief="flat", cursor="hand2", padx=15, pady=8,
    command=lambda: mostrar_tab(1)
)
btn_tab1.pack(side="left")

btn_tab2 = tk.Button(
    frame_tabs, text="Combinaciones  C(n,r)",
    font=FUENTE_NORMAL, bg=COLOR_TAB_INA, fg=COLOR_GRIS,
    relief="flat", cursor="hand2", padx=15, pady=8,
    command=lambda: mostrar_tab(2)
)
btn_tab2.pack(side="left")

tk.Frame(ventana, bg=COLOR_ACENTO, height=2).pack(fill="x", padx=20)


# ============================================================
# CONTENEDOR PRINCIPAL 
# ============================================================

frame_main = tk.Frame(ventana, bg=COLOR_FONDO)
frame_main.pack(fill="both", expand=True, padx=20, pady=10)

# Columna izquierda — controles
frame_izq = tk.Frame(frame_main, bg=COLOR_FONDO, width=220)
frame_izq.pack(side="left", fill="y", padx=(0, 15))
frame_izq.pack_propagate(False)

# Separador vertical
tk.Frame(frame_main, bg=COLOR_GRIS, width=1).pack(side="left", fill="y")

# Columna derecha — resultados
frame_der = tk.Frame(frame_main, bg=COLOR_FONDO)
frame_der.pack(side="left", fill="both", expand=True, padx=(15, 0))


# ============================================================
# PROBLEMA 1 — izquierda
# ============================================================

frame_p1 = tk.Frame(frame_izq, bg=COLOR_FONDO)

tk.Label(frame_p1, text="P(n,r) = n! / (n-r)!",
         font=FUENTE_NORMAL, bg=COLOR_FONDO, fg=COLOR_GRIS).pack(pady=(15, 20))

frame_in_p1 = tk.Frame(frame_p1, bg=COLOR_FONDO)
frame_in_p1.pack()

tk.Label(frame_in_p1, text="n :", font=FUENTE_NORMAL, bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry_n_p1 = tk.Entry(frame_in_p1, font=FUENTE_NORMAL, width=8, bg=COLOR_BOTON,
                       fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, relief="flat", justify="center")
entry_n_p1.grid(row=0, column=1, pady=8)

tk.Label(frame_in_p1, text="r :", font=FUENTE_NORMAL, bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=1, column=0, padx=8, pady=8, sticky="e")
entry_r_p1 = tk.Entry(frame_in_p1, font=FUENTE_NORMAL, width=8, bg=COLOR_BOTON,
                       fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, relief="flat", justify="center")
entry_r_p1.grid(row=1, column=1, pady=8)

tk.Button(frame_p1, text="Calcular", font=FUENTE_NORMAL, command=calcular_p1,
          bg=COLOR_ACENTO, fg=COLOR_FONDO, relief="flat", cursor="hand2",
          activebackground=COLOR_GRIS, padx=20, pady=6).pack(pady=20)
entry_n_p1.bind("<Return>", lambda event: calcular_p1())
entry_r_p1.bind("<Return>", lambda event: calcular_p1())

# ============================================================
# PROBLEMA 2 — izquierda
# ============================================================

frame_p2 = tk.Frame(frame_izq, bg=COLOR_FONDO)

tk.Label(frame_p2, text="C(n,r) = n! / (r!(n-r)!)",
         font=FUENTE_NORMAL, bg=COLOR_FONDO, fg=COLOR_GRIS).pack(pady=(15, 20))

frame_in_p2 = tk.Frame(frame_p2, bg=COLOR_FONDO)
frame_in_p2.pack()

tk.Label(frame_in_p2, text="n :", font=FUENTE_NORMAL, bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry_n_p2 = tk.Entry(frame_in_p2, font=FUENTE_NORMAL, width=8, bg=COLOR_BOTON,
                       fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, relief="flat", justify="center")
entry_n_p2.grid(row=0, column=1, pady=8)

tk.Label(frame_in_p2, text="r :", font=FUENTE_NORMAL, bg=COLOR_FONDO, fg=COLOR_TEXTO).grid(row=1, column=0, padx=8, pady=8, sticky="e")
entry_r_p2 = tk.Entry(frame_in_p2, font=FUENTE_NORMAL, width=8, bg=COLOR_BOTON,
                       fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO, relief="flat", justify="center")
entry_r_p2.grid(row=1, column=1, pady=8)

tk.Button(frame_p2, text="Calcular", font=FUENTE_NORMAL, command=calcular_p2,
          bg=COLOR_ACENTO, fg=COLOR_FONDO, relief="flat", cursor="hand2",
          activebackground=COLOR_GRIS, padx=20, pady=6).pack(pady=20)
entry_n_p2.bind("<Return>", lambda event: calcular_p2())
entry_r_p2.bind("<Return>", lambda event: calcular_p2())

# ============================================================
# AREA DE RESULTADOS — derecha 
# ============================================================

# Problema 1 resultado
frame_res_p1 = tk.Frame(frame_der, bg=COLOR_FONDO)
frame_res_p1.pack(fill="both", expand=True)

text_res_p1 = tk.Text(
    frame_res_p1,
    font=FUENTE_MONO,
    bg=COLOR_RESULTADO,
    fg=COLOR_TEXTO,
    relief="flat",
    padx=15, pady=15,
    wrap="none",
    state="disabled"
)
scroll_y_p1 = tk.Scrollbar(frame_res_p1, orient="vertical", command=text_res_p1.yview)
scroll_x_p1 = tk.Scrollbar(frame_res_p1, orient="horizontal", command=text_res_p1.xview)
text_res_p1.configure(yscrollcommand=scroll_y_p1.set, xscrollcommand=scroll_x_p1.set)

scroll_y_p1.pack(side="right", fill="y")
scroll_x_p1.pack(side="bottom", fill="x")
text_res_p1.pack(fill="both", expand=True)

# Problema 2 resultado
frame_res_p2 = tk.Frame(frame_der, bg=COLOR_FONDO)

text_res_p2 = tk.Text(
    frame_res_p2,
    font=FUENTE_MONO,
    bg=COLOR_RESULTADO,
    fg=COLOR_TEXTO,
    relief="flat",
    padx=15, pady=15,
    wrap="none",
    state="disabled"
)
scroll_y_p2 = tk.Scrollbar(frame_res_p2, orient="vertical", command=text_res_p2.yview)
scroll_x_p2 = tk.Scrollbar(frame_res_p2, orient="horizontal", command=text_res_p2.xview)
text_res_p2.configure(yscrollcommand=scroll_y_p2.set, xscrollcommand=scroll_x_p2.set)

scroll_y_p2.pack(side="right", fill="y")
scroll_x_p2.pack(side="bottom", fill="x")
text_res_p2.pack(fill="both", expand=True)


# ============================================================
# LOGICA DE PESTANAS
# ============================================================

def mostrar_tab(tab):
    frame_p1.pack_forget()
    frame_p2.pack_forget()
    frame_res_p1.pack_forget()
    frame_res_p2.pack_forget()

    if tab == 1:
        frame_p1.pack(fill="both", expand=True)
        frame_res_p1.pack(fill="both", expand=True)
        btn_tab1.config(bg=COLOR_TAB_ACT, fg=COLOR_ACENTO)
        btn_tab2.config(bg=COLOR_TAB_INA, fg=COLOR_GRIS)
    else:
        frame_p2.pack(fill="both", expand=True)
        frame_res_p2.pack(fill="both", expand=True)
        btn_tab1.config(bg=COLOR_TAB_INA, fg=COLOR_GRIS)
        btn_tab2.config(bg=COLOR_TAB_ACT, fg=COLOR_ACENTO)


mostrar_tab(1)
ventana.mainloop()