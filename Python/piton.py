import os
import requests
from bs4 import BeautifulSoup

# URL da página inicial
url_base = "https://app.garanhuns.pe.leg.br/transparencia/retornaDados/Visualizacao.aspx?sessao=lei&ID=34&e=C"

# Diretório para salvar os PDFs
diretorio = "pdfs"
os.makedirs(diretorio, exist_ok=True)

# Função para baixar PDFs
def baixar_pdf(url, nome_arquivo):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        caminho = os.path.join(diretorio, nome_arquivo)
        with open(caminho, "wb") as arquivo:
            for chunk in response.iter_content(chunk_size=8192):
                arquivo.write(chunk)
        print(f"Baixado: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao baixar {nome_arquivo}: {e}")

# Função para extrair e baixar PDFs
def extrair_pdfs(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Encontrar todos os botões "Visualizar" e seus links
        links_visualizar = soup.find_all("a", string="Visualizar")
        
        for link in links_visualizar:
            href = link["href"]
            if "javascript" not in href:  # Ignorar links não diretos
                pdf_url = href if href.startswith("http") else url_base + href
                nome_arquivo = pdf_url.split("/")[-1] + ".pdf"
                baixar_pdf(pdf_url, nome_arquivo)
    except Exception as e:
        print(f"Erro ao processar {url}: {e}")

# Inicia a busca e o download
extrair_pdfs(url_base)
