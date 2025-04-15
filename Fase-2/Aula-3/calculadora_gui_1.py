import tkinter as tk
from tkinter import ttk, messagebox

operacao: dict[str, str] = {
    'a': 'Acréscimo',
    'd': 'Desconto',
    'p': 'Percentual'
}

def calcular_valor(valor: float, percentual: float, tipo: str) -> float:
    def fator(tipo: str, percentual: float) -> float:
        match tipo:
            case 'a':
                return 1 + percentual / 100
            case 'd':
                return 1 - percentual / 100
            case 'p':
                return percentual / 100
    return valor * fator(tipo, percentual)

def executar_calculo():
    try:
        valor = float(entrada_valor.get())
        percentual = float(entrada_percentual.get())
        tipo = tipo_var.get()

        resultado = calcular_valor(valor, percentual, tipo)
        oper = operacao.get(tipo, "Operação desconhecida")

        resultado_label.config(text=f"{oper} de {percentual:.1f}% sobre {valor:.2f} é: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Percentual")
janela.geometry("400x250")
janela.resizable(False, False)

# Widgets
tk.Label(janela, text="Valor:").pack()
entrada_valor = tk.Entry(janela)
entrada_valor.pack()

tk.Label(janela, text="Percentual (%):").pack()
entrada_percentual = tk.Entry(janela)
entrada_percentual.pack()

tk.Label(janela, text="Tipo de cálculo:").pack()
tipo_var = tk.StringVar()
tipo_combo = ttk.Combobox(janela, textvariable=tipo_var, state="readonly")
tipo_combo['values'] = ['a', 'd', 'p']
tipo_combo.pack()

tk.Button(janela, text="Calcular", command=executar_calculo).pack(pady=10)

resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack()

# Loop da janela
janela.mainloop()
