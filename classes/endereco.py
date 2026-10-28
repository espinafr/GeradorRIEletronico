import random

class Endereco():
    def __init__(self):
        self.rua = ""
        self.bairro = ""
        self.numero = ""
        self.cidade = ""
        self.estado = ""
        self.cep = ""
        self.tipo = ""

    def setarEndereco(self, rua: str, numero: str, cidade: str, estado: str, cep: str, tipo: str, bairro: str = ""):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.tipo = tipo
        self.bairro = bairro

    def gerarEndereco(self): # função para gerar endereço aleatório (depois modificar para gerar endereço realista)
        self.rua = "Rua " + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[random.randint(0, 25)]
        self.bairro = random.choice([
            "Jardim", "Vila", "Parque", "Morro", "Granja", "Colina",
            "Alto de", "Baixada", "Barra", "Balneário", "Centro",
        ]) + " " + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.numero = str(random.randint(1, 1000))
        self.cidade = "Cidade " + str(random.randint(1, 100))
        self.estado = "SP"
        self.cep = f"{random.randint(0, 20999):05d}-{random.randint(0, 999):03d}"
        self.tipo = random.choice(["Apartamento", "Casa", "Chácara", "Lote", "Fazenda"])

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro} - {self.cidade}/{self.estado} | CEP: {self.cep}"

    def __repr__(self):
        return {
            "rua": self.rua,
            "bairro": self.bairro,
            "numero": self.numero,
            "cidade": self.cidade,
            "estado": self.estado,
            "cep": self.cep,
        }