import argparse

from classes.protocolo import Protocolo
from classes.tabela import Tabela


def exibir_dados(protocolo):
    Tabela("Outorgante", ["Nome", "CPF", "Gênero", "Endereço"], [[protocolo.outorgante.nome, protocolo.outorgante.cpf, protocolo.outorgante.genero, str(protocolo.outorgante.endereco)]]).exibir()
    Tabela("Outorgado", ["Nome", "CPF", "Gênero", "Endereço"], [[protocolo.outorgado.nome, protocolo.outorgado.cpf, protocolo.outorgado.genero, str(protocolo.outorgado.endereco)]]).exibir()
    Tabela(
        "Apresentante (outorgado)",
        ["Nome", "CPF", "Endereço"],
        [[protocolo.apresentante.nome, protocolo.apresentante.cpf, str(protocolo.apresentante.endereco)]]
    ).exibir()
    Tabela(
        "Responsável financeiro (outorgado)",
        ["Email", "CPF", "Nome", "Banco", "Agencia", "Conta", "Chave PIX"],
        [[
            protocolo.outorgado.email,
            protocolo.outorgado.cpf,
            protocolo.outorgado.nome,
            protocolo.outorgado.banco,
            protocolo.outorgado.agencia,
            protocolo.outorgado.conta,
            protocolo.outorgado.chavePix,
        ]]
    ).exibir()
    Tabela(
        "Imóvel",
        ["Rua", "Número", "Cidade", "Estado", "CEP", "Tipo"],
        [[
            protocolo.imovel.rua,
            protocolo.imovel.numero,
            protocolo.imovel.cidade,
            protocolo.imovel.estado,
            protocolo.imovel.cep,
            protocolo.imovel.tipo,
        ]]
    ).exibir()
    input("Pressione Enter para sair...")

def main():
    parser = argparse.ArgumentParser(description="Gerador de informações mock para RIEletrônico.")
    parser.parse_args()

    protocolo = Protocolo().gerar()
    exibir_dados(protocolo)


if __name__ == "__main__":
    main()