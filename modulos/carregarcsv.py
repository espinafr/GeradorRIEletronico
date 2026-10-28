import csv
import os
import random
import sys
from pathlib import Path


class CSV:
    def __init__(self, filepath):
        self.filepath = self._resolver_caminho(filepath)

    def _resolver_caminho(self, filepath):
        if os.path.isabs(filepath):
            return filepath

        caminhos = []

        caminhos.append(Path.cwd() / filepath)
        caminhos.append(Path.cwd() / "public" / Path(filepath).name)

        if getattr(sys, "_MEIPASS", None):
            caminhos.append(Path(sys.executable).resolve().parent / filepath)
            caminhos.append(Path(sys.executable).resolve().parent / "public" / Path(filepath).name)

        caminhos.append(Path(__file__).resolve().parent.parent / filepath)
        caminhos.append(Path(__file__).resolve().parent.parent / "public" / Path(filepath).name)

        caminho_diretorio = os.environ.get("RICRIARINFO_DATA_DIR")
        if caminho_diretorio:
            caminhos.append(Path(caminho_diretorio) / filepath)
            caminhos.append(Path(caminho_diretorio) / "public" / Path(filepath).name)

        for candidato in caminhos:
            if candidato.exists():
                return str(candidato)

        return str(Path(__file__).resolve().parent.parent / filepath)

    def fileDefinido(self):
        return os.path.exists(self.filepath)

    def valorAleatorio(self):
        if not self.fileDefinido():
            raise ValueError(f"Arquivo CSV não definido: {self.filepath}")

        linha_escolhida = None

        with open(self.filepath, mode='r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)

            for i, linha in enumerate(reader, start=1):
                if random.randrange(i) == 0:
                    linha_escolhida = linha

        if linha_escolhida is None:
            raise ValueError(f"Arquivo CSV vazio: {self.filepath}")

        return linha_escolhida[0] if isinstance(linha_escolhida, list) and len(linha_escolhida) == 1 else linha_escolhida

    def fechar(self):
        if hasattr(self, 'file') and self.file is not None:
            self.file.close()