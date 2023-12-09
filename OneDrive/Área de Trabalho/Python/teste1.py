import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class GerenciadorFinancas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Finanças")

        # Conectar ao banco de dados SQLite
        self.conexao = sqlite3.connect("financas.db")
        self.criar_tabela()

        # Variáveis de controle
        self.saldo_atual = tk.DoubleVar()
        self.valor_compra = tk.DoubleVar()
        self.descricao_compra = tk.StringVar()

        # Componentes da interface
        tk.Label(root, text="Saldo Atual:").grid(row=0, column=0, sticky="W", padx=10, pady=5)
        tk.Entry(root, textvariable=self.saldo_atual, state="readonly").grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Valor da Compra:").grid(row=1, column=0, sticky="W", padx=10, pady=5)
        tk.Entry(root, textvariable=self.valor_compra).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Descrição da Compra:").grid(row=2, column=0, sticky="W", padx=10, pady=5)
        tk.Entry(root, textvariable=self.descricao_compra).grid(row=2, column=1, padx=10, pady=5)

        tk.Button(root, text="Registrar Compra", command=self.registrar_compra).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Ver Extrato", command=self.ver_extrato).grid(row=4, column=0, columnspan=2, pady=10)

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS extrato (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_hora TEXT,
                descricao TEXT,
                valor REAL
            )
        ''')
        self.conexao.commit()

    def registrar_compra(self):
        valor_compra = self.valor_compra.get()
        descricao = self.descricao_compra.get()

        if not valor_compra or not descricao:
            messagebox.showwarning("Campos Vazios", "Preencha todos os campos.")
            return

        try:
            valor_compra = float(valor_compra)
        except ValueError:
            messagebox.showwarning("Valor Inválido", "Insira um valor numérico válido.")
            return

        # Atualizar o saldo atual
        self.saldo_atual.set(round(self.saldo_atual.get() - valor_compra, 2))

        # Registrar a compra no banco de dados
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO extrato (data_hora, descricao, valor) VALUES (?, ?, ?)",
                       (data_hora, descricao, valor_compra))
        self.conexao.commit()

        # Limpar os campos
        self.valor_compra.set("")
        self.descricao_compra.set("")

    def ver_extrato(self):
        extrato_window = tk.Toplevel(self.root)
        extrato_window.title("Extrato")

        # Obter dados do extrato do banco de dados
        cursor = self.conexao.cursor()
        cursor.execute("SELECT data_hora, descricao, valor FROM extrato")
        extrato_data = cursor.fetchall()

        # Exibir dados do extrato na nova janela
        tk.Label(extrato_window, text="Data/Hora").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(extrato_window, text="Descrição").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(extrato_window, text="Valor").grid(row=0, column=2, padx=5, pady=5)

        for i, (data_hora, descricao, valor) in enumerate(extrato_data, start=1):
            tk.Label(extrato_window, text=data_hora).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(extrato_window, text=descricao).grid(row=i, column=1, padx=5, pady=5)
            tk.Label(extrato_window, text=valor).grid(row=i, column=2, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorFinancas(root)
    root.mainloop()