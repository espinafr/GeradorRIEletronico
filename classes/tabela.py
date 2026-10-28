import colorama


class Tabela:
    def __init__(self, titulo, headers, rows):
        self.titulo = titulo
        self.headers = headers
        self.rows = rows

    def _larguras(self):
        larguras = [len(str(header)) for header in self.headers]

        for row in self.rows:
            for indice, valor in enumerate(row):
                larguras[indice] = max(larguras[indice], len(str(valor)))

        return larguras

    def _linha_divisoria(self, larguras):
        partes = ["-" * (largura + 2) for largura in larguras]
        return "+" + "+".join(partes) + "+"

    def _linha_dados(self, valores, larguras, colorir_headers=False):
        partes = []
        for indice, valor in enumerate(valores):
            texto = str(valor).ljust(larguras[indice])
            if colorir_headers:
                texto = f"{colorama.Fore.WHITE}{colorama.Style.BRIGHT}{texto}{colorama.Style.RESET_ALL}"
            partes.append(texto)

        separador = f"{colorama.Style.DIM}|{colorama.Style.RESET_ALL}"
        return separador + " " + f" {separador} ".join(partes) + f" {separador}"

    def exibir(self):
        if not self.headers:
            return

        larguras = self._larguras()
        divisoria = self._linha_divisoria(larguras)

        print()
        print(f"{colorama.Fore.CYAN}{self.titulo}{colorama.Style.RESET_ALL}")
        print(f"{colorama.Style.DIM}{divisoria}{colorama.Style.RESET_ALL}")
        print(self._linha_dados(self.headers, larguras, colorir_headers=True))
        print(f"{colorama.Style.DIM}{divisoria}{colorama.Style.RESET_ALL}")

        for row in self.rows:
            print(self._linha_dados(row, larguras))

        print(f"{colorama.Style.DIM}{divisoria}{colorama.Style.RESET_ALL}")
        print()


class TabelaPadrao(Tabela):
    pass