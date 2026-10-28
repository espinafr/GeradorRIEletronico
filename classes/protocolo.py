import datetime

from classes.endereco import Endereco
from classes.pessoa import Pessoa

class Protocolo:
    def __init__(self, outorgante: Pessoa = None, outorgado: Pessoa = None, apresentante: Pessoa = None, dataTitulo: str = "", natureza: str = "", imovel: Endereco = None, tipo: str = "Prenotação"):
        self.outorgante = outorgante
        self.outorgado = outorgado
        self.apresentante = apresentante
        self.dataTitulo = dataTitulo
        self.natureza = natureza
        self.imovel = imovel
        self.tipo = tipo

    def _criar_participantes(self):
        self.outorgante = Pessoa()
        self.outorgado = Pessoa()
        self.apresentante = self.outorgado

        self.outorgante.gerarTudo()
        self.outorgado.gerarTudo()

    def _gerar_imovel(self):
        self.imovel = Endereco()
        self.imovel.gerarEndereco()

    def _definir_dados_do_titulo(self):
        self.dataTitulo = datetime.datetime.now().strftime("%d/%m/%Y")
        self.natureza = "Abertura de Matrícula"

    def gerar(self):
        self._criar_participantes()
        self._gerar_imovel()
        self._definir_dados_do_titulo()
        return self
