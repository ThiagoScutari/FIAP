import tkinter as tk
from tkinter import ttk, messagebox

operacao: dict[str, str] = {
    'Acréscimo': 'a',
    'Desconto': 'd',
    'Percentual': 'p'
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
        tipo_nome = tipo_var.get()
        tipo = operacao.get(tipo_nome)

        resultado = calcular_valor(valor, percentual, tipo)
        resultado_label.config(
            text=f"{tipo_nome} de {percentual:.1f}% sobre {valor:.2f} é: {resultado:.2f}"
        )
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    except TypeError:
        messagebox.showerror("Erro", "Por favor, selecione um tipo de operação.")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Percentual")
janela.geometry("400x220")
janela.resizable(False, False)

# Layout grid
tk.Label(janela, text="Valor:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entrada_valor = tk.Entry(janela, width=20)
entrada_valor.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Percentual (%):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entrada_percentual = tk.Entry(janela, width=20)
entrada_percentual.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Tipo de cálculo:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
tipo_var = tk.StringVar()
tipo_combo = ttk.Combobox(janela, textvariable=tipo_var, state="readonly", width=18)
tipo_combo['values'] = list(operacao.keys())
tipo_combo.grid(row=2, column=1, padx=10, pady=5)

tk.Button(janela, text="Calcular", command=executar_calculo).grid(row=3, column=0, columnspan=2, pady=10)

resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.grid(row=4, column=0, columnspan=2)

# Loop da janela
janela.mainloop()
