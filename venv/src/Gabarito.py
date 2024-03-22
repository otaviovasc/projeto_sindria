# Gabarito.py
class Gabarito:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.respostas = {}

    def ler_pdf(self):
        # Código para ler o PDF e extrair o texto do gabarito
        pass

    def definir_resposta(self, numero_questao, resposta):
        self.respostas[numero_questao] = resposta

    def obter_respostas(self):
        return self.respostas
