class Celular:
    def __init__(self,cores,marca,modelo,memoria,numero):
        self.cores = cores
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.__numero = numero

    def get_numero(self):
        return self.__numero
    
    def __str__(self):
        print("INFORMACOES DO CELULAR")
        print(f"cor: {self.cores}")
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"memoria: {self.memoria}G")
        print(f"numero: {self.__numero}")

celular1 = Celular('preto','iphone','iphone11','64','1154748384')
print(str(celular1))
    
