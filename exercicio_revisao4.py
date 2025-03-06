import tkinter as tk

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

class Biblioteca:
    def __init__(self, status_label):
        self.livros = []
        self.membros = []
        self.status_label = status_label

    def atualizar_status(self, mensagem):
        self.status_label.config(text=mensagem)

    def adicionar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))
        self.atualizar_status("Livro cadastrado com sucesso!")

    def adicionar_membro(self, nome):
        self.membros.append(Membro(nome))
        self.atualizar_status("Membro cadastrado com sucesso!")

    def emprestar_livro(self, nome_membro, titulo_livro):
        membro = next((m for m in self.membros if m.nome == nome_membro), None)
        livro = next((l for l in self.livros if l.titulo == titulo_livro and l.disponivel), None)
        
        if membro and livro:
            livro.disponivel = False
            membro.emprestimos.append(livro)
            self.atualizar_status("Livro emprestado com sucesso!")
        else:
            self.atualizar_status("Erro: Livro não disponível ou membro não encontrado!")

    def devolver_livro(self, nome_membro, titulo_livro):
        membro = next((m for m in self.membros if m.nome == nome_membro), None)
        if membro:
            livro = next((l for l in membro.emprestimos if l.titulo == titulo_livro), None)
            if livro:
                livro.disponivel = True
                membro.emprestimos.remove(livro)
                self.atualizar_status("Livro devolvido com sucesso!")
            else:
                self.atualizar_status("Erro: Este membro não possui esse livro!")
        else:
            self.atualizar_status("Erro: Membro não encontrado!")

    def visualizar_emprestimos(self):
        emprestimos = "\n".join([f"{m.nome}: {[l.titulo for l in m.emprestimos]}" for m in self.membros if m.emprestimos])
        self.atualizar_status(emprestimos if emprestimos else "Nenhum empréstimo registrado.")

root = tk.Tk()
root.title("Sistema de Biblioteca")

status_label = tk.Label(root, text="Bem-vindo ao sistema de biblioteca!", fg="blue")
status_label.pack()

biblioteca = Biblioteca(status_label)

tk.Label(root, text="Título do Livro:").pack()
entrada_titulo = tk.Entry(root)
entrada_titulo.pack()

tk.Label(root, text="Autor do Livro:").pack()
entrada_autor = tk.Entry(root)
entrada_autor.pack()

tk.Button(root, text="Adicionar Livro", command=lambda: biblioteca.adicionar_livro(entrada_titulo.get(), entrada_autor.get())).pack()

tk.Label(root, text="Nome do Membro:").pack()
entrada_membro = tk.Entry(root)
entrada_membro.pack()

tk.Button(root, text="Adicionar Membro", command=lambda: biblioteca.adicionar_membro(entrada_membro.get())).pack()

tk.Label(root, text="Membro:").pack()
entrada_membro_emprestimo = tk.Entry(root)
entrada_membro_emprestimo.pack()

tk.Label(root, text="Livro:").pack()
entrada_livro_emprestimo = tk.Entry(root)
entrada_livro_emprestimo.pack()

tk.Button(root, text="Emprestar Livro", command=lambda: biblioteca.emprestar_livro(entrada_membro_emprestimo.get(), entrada_livro_emprestimo.get())).pack()

tk.Button(root, text="Devolver Livro", command=lambda: biblioteca.devolver_livro(entrada_membro_emprestimo.get(), entrada_livro_emprestimo.get())).pack()

tk.Button(root, text="Visualizar Empréstimos", command=biblioteca.visualizar_emprestimos).pack()

root.mainloop()
