import colorama


class Tabela:
    def __init__(self, titulo, headers, rows, vertical=False):
        self.titulo = titulo
        self.headers = headers
        self.rows = rows
        self.vertical = vertical

    def _larguras(self):
        larguras = [len(str(header)) for header in self.headers]

        for row in self.rows:
            for indice, valor in enumerate(row):
                larguras[indice] = max(larguras[indice], len(str(valor)))

        return larguras

    def _linha_divisoria(self, larguras):
        partes = ["-" * (largura + 2) for largura in larguras]
        return "+" + "+".join(partes) + "+"

    def _linha_dados(self, valores, larguras, colorir_headers=False, indices_coloridos=None):
        partes = []
        for indice, valor in enumerate(valores):
            texto = str(valor).ljust(larguras[indice])
            if colorir_headers and (indices_coloridos is None or indice in indices_coloridos):
                texto = f"{colorama.Fore.WHITE}{colorama.Style.BRIGHT}{texto}{colorama.Style.RESET_ALL}"
            partes.append(texto)

        separador = f"{colorama.Style.DIM}|{colorama.Style.RESET_ALL}"
        return separador + " " + f" {separador} ".join(partes) + f" {separador}"

    def _exibir_vertical(self):
        largura_header = max(len(str(header)) for header in self.headers)
        largura_valor = max(
            [len(str(valor)) for row in self.rows for valor in row] or [0]
        )
        larguras = [largura_header, largura_valor]
        divisoria = self._linha_divisoria(larguras)

        print(f"{colorama.Style.DIM}{divisoria}{colorama.Style.RESET_ALL}")
        for indice, header in enumerate(self.headers):
            for row in self.rows:
                valor = row[indice] if indice < len(row) else ""
                print(self._linha_dados(
                    [header, valor],
                    larguras,
                    colorir_headers=True,
                    indices_coloridos={0},
                ))
        print(f"{colorama.Style.DIM}{divisoria}{colorama.Style.RESET_ALL}")

    def exibir(self):
        if not self.headers:
            return

        print()
        print(f"{colorama.Fore.CYAN}{self.titulo}{colorama.Style.RESET_ALL}")
        if self.vertical:
            self._exibir_vertical()
        else:
            larguras = self._larguras()
            divisoria = self._linha_divisoria(larguras)

            print(f"{colorama.Style.DIM}{divisoria}{colorama.Style.RESET_ALL}")
            print(self._linha_dados(self.headers, larguras, colorir_headers=True))
            print(f"{colorama.Style.DIM}{divisoria}{colorama.Style.RESET_ALL}")

            for row in self.rows:
                print(self._linha_dados(row, larguras))

            print(f"{colorama.Style.DIM}{divisoria}{colorama.Style.RESET_ALL}")
        print()


class TabelaPadrao(Tabela):
    pass