import tkinter as tk
from tkinter import messagebox
import sqlite3


con = sqlite3.connect("pessoas3.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    cep INTEGER NOT NULL
)
""")
con.commit()

def salvar_nome():
    nome = entrada_nome.get().strip()
    endereco = entrada_endereco.get().strip()
    cep = entrada_cep.get().strip()

    if nome == "":
        messagebox.showwarning("Atenção", "Digite um nome antes de salvar!")
        return

    if endereco == "":
        messagebox.showwarning("Atenção", "Digite um endereco antes de salvar!")
        return
    
    if cep == "":
        messagebox.showwarning("Atenção", "Digite um cep antes de salvar!")
        return
    cur.execute(
        "INSERT INTO pessoas (nome, endereco, cep) VALUES (?, ?, ?)",
        (nome, endereco, cep)
    )
    con.commit()
    messagebox.showinfo("Sucesso", f"Nome: '{nome}'- Endereco: '{endereco}' - CEP: {cep} salvo com sucesso!")
    entrada_nome.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_cep.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Nomes")
janela.geometry("300x300")


rotulo = tk.Label(janela, text="Digite o nome:")
rotulo.pack(pady=10)

entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(pady=5)


rotulo = tk.Label(janela, text="Digite o endreco:")
rotulo.pack(pady=10)

entrada_endereco = tk.Entry(janela, width=30)
entrada_endereco.pack(pady=5)


rotulo = tk.Label(janela, text="Digite o cep:")
rotulo.pack(pady=10)

entrada_cep = tk.Entry(janela, width=30)
entrada_cep.pack(pady=5)

botao_salvar = tk.Button(janela, text="Salvar", command=salvar_nome)
botao_salvar.pack(pady=10)

botao_sair = tk.Button(janela, text="Fechar", command=janela.destroy)
botao_sair.pack(pady=5)

janela.mainloop()

con.close()