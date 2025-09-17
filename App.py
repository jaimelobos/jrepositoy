import tkinter as tk
from tkinter import ttk

def simplificar_tema(texto):
    """
    Simula la simplificación de un tema complejo.
    En una app real, aquí podrías usar IA o procesamiento de lenguaje natural.
    """
    if not texto.strip():
        return "Por favor, ingresa un tema complejo."
    # Simulación básica: resume y simplifica
    return f"Explicación sencilla:\n\n{texto[:120]}...\n\n(Piensa en este tema como algo cotidiano y fácil de entender)"

def generar_explicacion():
    tema = entrada_tema.get("1.0", tk.END)
    explicacion = simplificar_tema(tema)
    texto_explicacion.config(state=tk.NORMAL)
    texto_explicacion.delete("1.0", tk.END)
    texto_explicacion.insert(tk.END, explicacion)
    texto_explicacion.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Explicador de Temas Complejos")
root.geometry("500x350")
root.resizable(True, True)

# Estilo minimalista
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Segoe UI', 12), padding=8)
style.configure('TLabel', font=('Segoe UI', 12))

frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

label_tema = ttk.Label(frame, text="Escribe un tema complejo:")
label_tema.pack(anchor=tk.W, pady=(0,5))

entrada_tema = tk.Text(frame, height=4, font=('Segoe UI', 11))
entrada_tema.pack(fill=tk.X, pady=(0,10))

btn_explicar = ttk.Button(frame, text="Generar Explicación", command=generar_explicacion)
btn_explicar.pack(pady=(0,10))

label_explicacion = ttk.Label(frame, text="Explicación sencilla:")
label_explicacion.pack(anchor=tk.W)

texto_explicacion = tk.Text(frame, height=7, font=('Segoe UI', 11), state=tk.DISABLED, bg="#f7f7f7")
texto_explicacion.pack(fill=tk.BOTH, expand=True, pady=(0,5))

root.mainloop()