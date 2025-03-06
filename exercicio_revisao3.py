import tkinter as tk
def cadastrar_funcionario():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    salario_base = float(salario_entry.get())
    tipo = tipo_entry.get().lower()
    adicional = float(adicional_entry.get())

    if tipo == "administrativo":
        funcionario = Administrativo(nome, cpf, salario_base, adicional)
    elif tipo == "professor":
        funcionario = Professor(nome, cpf, salario_base, float(valor_aula_entry.get()),int(adicional))
    elif tipo == "tecnico":
        funcionario = Tecnico(nome, cpf, salario_base, adicional)
    else:
        resultado_text.insert(tk.END, "Tipo inválido\n")
        return

    resultado_text.insert(tk.END, f"{funcionario.nome} cadastrado, Salário: {funcionario.calcular_salario()}\n")

root = tk.Tk()
root.title("Cadastro de Funcionários")

tk.Label(root, text="Nome:").grid(row=0, column=0)
nome_entry = tk.Entry(root)
nome_entry.grid(row=0, column=1)

tk.Label(root, text="CPF:").grid(row=1, column=0)
cpf_entry = tk.Entry(root)
cpf_entry.grid(row=1, column=1)

tk.Label(root, text="Salário Base:").grid(row=2, column=0)
salario_entry = tk.Entry(root)
salario_entry.grid(row=2, column=1)

tk.Label(root, text="Tipo (Administrativo, Professor, Técnico):").grid(row=3, column=0)
tipo_entry = tk.Entry(root)
tipo_entry.grid(row=3, column=1)

tk.Label(root, text="Valor(Adicional/Aulas/Bonus):").grid(row=4, column=0)
adicional_entry = tk.Entry(root)
adicional_entry.grid(row=4, column=1)

tk.Label(root, text="Numero de Aulas (apenas p/ professor):").grid(row=5, column=0)
valor_aula_entry = tk.Entry(root)
valor_aula_entry.grid(row=5, column=1)

tk.Button(root, text="Cadastrar", command=cadastrar_funcionario).grid(row=6, columnspan=2)

resultado_text = tk.Text(root, height=10, width=50)
resultado_text.grid(row=7, columnspan=2)

class Funcionario:
    def __init__(self, nome, cpf, salario_base):
        self.nome = nome
        self.cpf = cpf
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class Administrativo(Funcionario):
    def __init__(self, nome, cpf, salario_base, adicional):
        super().__init__(nome, cpf, salario_base)
        self.adicional = adicional

    def calcular_salario(self):
        return self.salario_base + self.adicional

class Professor(Funcionario):
    def __init__(self, nome, cpf, salario_base, aulas, valor_aula):
        super().__init__(nome, cpf, salario_base)
        self.aulas = aulas
        self.valor_aula = valor_aula

    def calcular_salario(self):
        return self.salario_base + (self.aulas * self.valor_aula)

class Tecnico(Funcionario):
    def __init__(self, nome, cpf, salario_base, bonus):
        super().__init__(nome, cpf, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus

root.mainloop()
