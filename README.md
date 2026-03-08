# Cadastro simples com Python, Tkinter e SQLite

Este repositório contém um trabalho desenvolvido para a faculdade como atividade final da disciplina.
O projeto consiste em uma aplicação simples com **interface gráfica em Python (Tkinter)** integrada a um **banco de dados SQLite**.

O banco possui uma tabela com três campos:

* Nome
* Endereço
* CEP

Durante o desenvolvimento foram criadas três versões do sistema, mostrando a evolução da aplicação.

## Arquivos do projeto

**`tk.py`**
Primeira versão do sistema. Foi usada para aprender a criar uma interface básica com **Tkinter** e fazer a conexão com **SQLite3**.
Nessa versão o programa apenas insere registros no banco de dados utilizando o comando **INSERT**.

**`tk2.py`**
Segunda versão do projeto. Mantém os três campos de cadastro e adiciona um **Treeview**, que permite visualizar os registros da tabela diretamente na interface.

**`tk3.py`**
Versão final da aplicação. Implementa as operações principais do banco de dados:

* INSERT
* UPDATE
* DELETE

Além disso, o **Treeview** exibe os registros e é atualizado conforme as alterações são feitas.

## Tecnologias utilizadas

* Python
* Tkinter
* SQLite3

Projeto desenvolvido apenas para **fins acadêmicos e de aprendizado**.
