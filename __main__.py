import argparse

from classes.protocolo import Protocolo
from classes.tabela import Tabela

def _dados_pessoa(pessoa):
    return [
        pessoa.cpf,
        pessoa.genero,
        "RG",
        pessoa.cpf,
        "SSP",
        "SP",
        pessoa.nome,
        "brasileiro",
        "solteiro",
        str(pessoa.endereco),
    ]

def exibir_dados(protocolo):
    Tabela("Outorgante", ["Nome"], [[protocolo.outorgante.nome]]).exibir()
    Tabela("Outorgado", ["Nome", "CPF", "Endereço"], [[protocolo.outorgado.nome, protocolo.outorgado.cpf, str(protocolo.outorgado.endereco)]]).exibir()
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
        ]],
        vertical=True
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
    headers_pessoa = [
        "CPF",
        "Gênero",
        "Tipo de doc",
        "Doc Identificação",
        "Emissor Doc",
        "UF Doc.",
        "Nome",
        "Nacionalidade",
        "Estado Civil",
        "Endereço",
    ]
    Tabela("Outorgante (Info pessoa)", headers_pessoa, [_dados_pessoa(protocolo.outorgante)], vertical=True).exibir()
    Tabela("Outorgado (Info pessoa)", headers_pessoa, [_dados_pessoa(protocolo.outorgado)], vertical=True).exibir()
    input("Pressione Enter para sair...")

def main():
    parser = argparse.ArgumentParser(description="Gerador de informações mock para RIEletrônico.")
    parser.parse_args()

    protocolo = Protocolo().gerar()
    exibir_dados(protocolo)


if __name__ == "__main__":
    main()