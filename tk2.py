import tkinter as tk
from tkinter import ttk, messagebox
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

    atualizar_grade()

def atualizar_grade():

    for item in tabela.get_children():
        tabela.delete(item)

    cur.execute("SELECT id, nome, endereco, cep FROM pessoas ORDER BY id DESC")
    for row in cur.fetchall():
        tabela.insert("", tk.END, values=row)

janela = tk.Tk()
janela.title("Cadastro de Nomes")
janela.geometry("400x600")


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

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

botao_salvar = tk.Button(frame_botoes, text="Salvar", command=salvar_nome)
botao_salvar.grid(row=0, column=0, padx=5)

botao_sair = tk.Button(frame_botoes, text="Fechar", command=janela.destroy)
botao_sair.grid(row=0, column=1, padx=5)

tabela = ttk.Treeview(janela, columns=("id", "nome","endereco", "cep"), show="headings", height=15)
tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome")
tabela.heading("endereco", text="Endereco")
tabela.heading("cep", text="CEP")
tabela.column("id", width=80, anchor="center")
tabela.column("nome", width=80)
tabela.column("endereco", width=80)
tabela.column("cep", width=80)
tabela.pack(pady=10)


atualizar_grade()

janela.mainloop()

con.close()