# main.py
import os
from Transcritor import Transcritor

def main():
    pdf_prova_path = '/Users/otaviovasconceloss/code/otaviovasc/projeto_sindria/venv/src/pdfs/2023_PV_impresso_D1_CD1.pdf'

    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.isfile(pdf_prova_path):
        print(f"Erro: O arquivo {pdf_prova_path} não foi encontrado.")
        return

    transcritor = Transcritor()
    texto_prova = transcritor.transcrever(pdf_prova_path)
    print(texto_prova)

if __name__ == '__main__':
    main()
