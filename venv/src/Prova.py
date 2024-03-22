# Prova.py
class Prova:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.questoes = []

    def ler_pdf(self):
        # Código para ler o PDF e extrair o texto das questões
        pass

    def adicionar_questao(self, questao):
        self.questoes.append(questao)

    def obter_questoes(self):
        return self.questoes
