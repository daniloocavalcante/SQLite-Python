# Sistema simples de cadastro com Python, Tkinter e SQLite

Este repositório contém um trabalho desenvolvido para a faculdade como **atividade de conclusão da disciplina**.
O objetivo foi praticar a criação de uma aplicação simples com **interface gráfica em Python**, integrada a um **banco de dados SQLite**.

O banco utilizado possui uma tabela com três campos básicos:

* **Nome**
* **Endereço**
* **CEP**

Ao longo do projeto foram criadas diferentes versões do programa, mostrando a evolução da aplicação.

---

## Estrutura do projeto

### `tk.py`

Primeira versão do projeto.

Esse arquivo foi criado principalmente para aprender a utilizar **interface gráfica com Tkinter** e fazer a integração com o **SQLite3**.

Nesta versão:

* existe um formulário simples com os três campos (nome, endereço e CEP)
* os dados digitados são enviados para o banco de dados
* o programa executa apenas a operação **INSERT** no banco

Ou seja, ele apenas **adiciona novos registros**, sem exibir ou editar os dados.

---

### `tk2.py`

Segunda versão do projeto.

Aqui a aplicação continua permitindo adicionar registros com os mesmos três campos, mas foi adicionada uma melhoria importante na interface.

Nesta versão foi utilizado o **Treeview**, que permite mostrar os dados da tabela diretamente na interface do programa.

Agora o sistema:

* continua inserindo registros no banco
* exibe os dados cadastrados em uma tabela dentro da aplicação

Isso facilita a visualização das informações armazenadas no banco de dados.

---

### `tk3.py`

Versão final do projeto.

Nessa etapa foram implementadas as principais operações de manipulação de dados:

* **INSERT** – adicionar novos registros
* **UPDATE** – atualizar registros existentes
* **DELETE** – remover registros

Além disso, o **Treeview continua sendo utilizado para exibir os dados**, mostrando automaticamente os registros atualizados conforme as operações são realizadas.

Essa versão representa uma aplicação mais completa, permitindo **criar, editar, visualizar e excluir registros diretamente pela interface**.

---

## Tecnologias utilizadas

* **Python**
* **Tkinter** (interface gráfica)
* **SQLite3** (banco de dados)

---

## Objetivo do projeto

O objetivo deste trabalho foi praticar:

* criação de interfaces gráficas em Python
* integração entre aplicação e banco de dados
* operações básicas de SQL
* organização simples de um projeto em Python

Projeto desenvolvido para fins **acadêmicos e de aprendizado**.
