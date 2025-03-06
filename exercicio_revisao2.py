import tkinter as tk
from tkinter import ttk

def cadastrar_medico():
    nome = entry_medico.get()
    if nome:
        medicos.append(nome)
        combo_medico["values"] = medicos
        entry_medico.delete(0, tk.END)

def cadastrar_paciente():
    nome = entry_paciente.get()
    if nome:
        pacientes.append(nome)
        combo_paciente["values"] = pacientes
        entry_paciente.delete(0, tk.END)

def agendar_consulta():
    medico = combo_medico.get()
    paciente = combo_paciente.get()
    if medico and paciente:
        consultas.append(f"{medico} atenderá {paciente}")

def ver_consultas():
    if consultas:
        consulta_texto.set("\n".join(consultas))
    else:
        consulta_texto.set("Nenhuma consulta agendada.")

root = tk.Tk()
root.title("Clínica Médica")
root.geometry("400x300")

medicos = []
pacientes = []
consultas = []
consulta_texto = tk.StringVar()

ttk.Label(root, text="Nome do Médico:").pack()
entry_medico = ttk.Entry(root)
entry_medico.pack()
ttk.Button(root, text="Cadastrar Médico", command=cadastrar_medico).pack()

ttk.Label(root, text="Nome do Paciente:").pack()
entry_paciente = ttk.Entry(root)
entry_paciente.pack()
ttk.Button(root, text="Cadastrar Paciente", command=cadastrar_paciente).pack()

ttk.Label(root, text="Agendar Consulta:").pack()
combo_medico = ttk.Combobox(root, state="readonly")
combo_paciente = ttk.Combobox(root, state="readonly")
combo_medico.pack()
combo_paciente.pack()
ttk.Button(root, text="Agendar", command=agendar_consulta).pack()

ttk.Button(root, text="Ver Consultas", command=ver_consultas).pack()
ttk.Label(root, textvariable=consulta_texto).pack()

root.mainloop()

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Medico(Pessoa):
    def __init__(self, nome, cpf , crm, especialidade):
        super().__init__(nome, cpf, crm, especialidade)
        self.crm = crm
        self.especialidade = especialidade

class Paciente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

class Consulta:
    def __init__(self, medico, paciente, data):
        self.medico = medico
        self.paciente = paciente
        self.data = data
    
    def __str__(self):
        return f"{self.data}: {self.medico.nome} atenderá {self.paciente.nome}"

class Clinica:
    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.consultas = []
    
    def cadastrar_medico(self, nome, especialidade):
        medico = Medico(nome, especialidade)
        self.medicos.append(medico)
    
    def cadastrar_paciente(self, nome):
        paciente = Paciente(nome)
        self.pacientes.append(paciente)
    
    def agendar_consulta(self, medico_nome, paciente_nome, data):
        medico = next((m for m in self.medicos if m.nome == medico_nome), None)
        paciente = next((p for p in self.pacientes if p.nome == paciente_nome), None)
        if medico and paciente:
            consulta = Consulta(medico, paciente, data)
            self.consultas.append(consulta)
    
    def listar_consultas(self):
        return [str(consulta) for consulta in self.consultas]
