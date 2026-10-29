import tkinter as tk
from tkinter import messagebox

def resolver_n_reinas(n):

    tablero = [[0] * n for _ in range(n)]

    def es_seguro(fila, col):

        for i in range(col):
            if tablero[fila][i] == 1:
                return False

        for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
            if tablero[i][j] == 1:
                return False

        for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
            if tablero[i][j] == 1:
                return False
        return True

    def resolver(col):
        if col >= n:
            return True
        
        for i in range(n):
            if es_seguro(i, col):
                tablero[i][col] = 1 
                
                if resolver(col + 1): 
                    return True
                    
                tablero[i][col] = 0 
        
        return False


    if resolver(0):
        return tablero
    return None

def mostrar_interfaz():
    def dibujar():
        try:
            n = int(entrada_n.get())
            if n < 4:
                messagebox.showwarning("Aviso", "Para el problema clásico, N debe ser 4 o mayor.")
                return
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número entero válido.")
            return

        solucion = resolver_n_reinas(n)
        canvas.delete("all")
        
        if not solucion:
            messagebox.showinfo("Sin solución", f"No se encontró solución para N={n}")
            return

        tamano_celda = 400 // n
        for i in range(n):
            for j in range(n):
                # Crear patrón de colores de tablero de ajedrez
                color = "#DDBB99" if (i + j) % 2 == 0 else "#8B5A2B"
                x1, y1 = j * tamano_celda, i * tamano_celda
                x2, y2 = x1 + tamano_celda, y1 + tamano_celda
                canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                
                # Dibujar la reina si hay un 1 en la matriz
                if solucion[i][j] == 1:
                    canvas.create_text(x1 + tamano_celda//2, y1 + tamano_celda//2, 
                                    text="♛", font=("Arial", tamano_celda//2), fill="black")

    ventana = tk.Tk()
    ventana.title("Práctica: Algoritmo N-Reinas")

    tk.Label(ventana, text="Introduce el número de reinas (N):", font=("Arial", 10)).pack(pady=5)
    entrada_n = tk.Entry(ventana, justify="center", font=("Arial", 12))
    entrada_n.insert(0, "4")
    entrada_n.pack(pady=5)
    
    tk.Button(ventana, text="Resolver y Dibujar", command=dibujar, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

    canvas = tk.Canvas(ventana, width=400, height=400, bg="white")
    canvas.pack(pady=10)

    ventana.mainloop()


mostrar_interfaz()