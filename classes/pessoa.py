import os
import random

from classes.endereco import Endereco
from modulos.carregarcsv import CSV

# Depois adicionar formas de casar uma pessoa com outra...
class Pessoa:
    def __init__(self, nome: str = "", cpf: str = "", email: str = "", genero: str = random.choice(["Masculino", "Feminino"])):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.genero = genero

    def gerarFinanceiro(self):
        # Banco do Brasil, Itaú, Bradesco, Caixa, Nubank
        bancos = ["001", "341", "237", "104", "260"]

        self.banco = random.choice(bancos)
        self.agencia = f"{random.randint(1, 9999):04d}"
        self.conta = f"{random.randint(1, 99999):05d}-{random.randint(0, 9)}"
        self.chavePix = f"{self.nome.split()[0].lower()}.{random.randint(100, 999999)}@pix"

    def gerarCPF(self):
        # Os 8 primeiros dígitos aleatórios + o 9º dígito fixo igual a 8 (SP)
        nove_digitos = [random.randint(0, 9) for _ in range(8)] + [8]

        # Cálculo do 10º dígito (primeiro dígito verificador)
        soma_1 = sum(v * (10 - i) for i, v in enumerate(nove_digitos))
        resto_1 = soma_1 % 11
        digito_1 = 0 if resto_1 < 2 else 11 - resto_1
        nove_digitos.append(digito_1)

        # Cálculo do 11º dígito (segundo dígito verificador)
        soma_2 = sum(v * (11 - i) for i, v in enumerate(nove_digitos))
        resto_2 = soma_2 % 11
        digito_2 = 0 if resto_2 < 2 else 11 - resto_2
        nove_digitos.append(digito_2)

        # Formata o CPF no padrão XXX.XXX.XXX-XX
        c = "".join(map(str, nove_digitos))
        self.cpf = f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"

    def gerarNome(self):
        arquivo_nome = os.path.join("public", f"nomes{self.genero.lower()[:3]}.csv")
        self.nome = CSV(arquivo_nome).valorAleatorio()
        csvSobrenomes = CSV(os.path.join("public", "sobrenomes.csv"))

        for _ in range(random.randint(1, 2)):
            sobrenome = csvSobrenomes.valorAleatorio()
            self.nome += " " + sobrenome

    def gerarEmail(self):
        if self.nome == "":
            raise ValueError("O nome deve ser gerado antes de gerar o email.")

        self.email = f"{self.nome.split()[0].lower()}{random.randint(1, 999)}@exemplo.com"

    def gerarEndereco(self):
        self.endereco = Endereco()
        self.endereco.gerarEndereco()

    def gerarNumeroTelefone(self):
        self.numeroTelefone = f"({random.randint(11, 99)}) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

    def gerarTudo(self):
        self.gerarNome()
        self.gerarCPF()
        self.gerarEmail()
        self.gerarEndereco()
        self.gerarFinanceiro()
        self.gerarNumeroTelefone()

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Gênero: {self.genero}"

    def __repr__(self):
        saida = {"nome": self.nome, "cpf": self.cpf, "email": self.email, "genero": self.genero}

        if hasattr(self, 'banco'):
            saida.update({"banco": self.banco, "agencia": self.agencia, "conta": self.conta})

        if hasattr(self, 'chavePix'):
            saida.update({"chavePix": self.chavePix})

        return saida