# Transcritor.py
import pdfplumber

class Transcritor:
    def transcrever(self, pdf_path):
        # Abre o PDF e extrai o texto de cada página
        texto_total = ''
        with pdfplumber.open(pdf_path) as pdf:
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:  # Verifica se conseguiu extrair texto da página
                    texto_total += texto_pagina + '\n'
        return texto_total
