from bs4 import BeautifulSoup
import requests

def main():
  findFirstLink()
  findPdfLink()
  downloadPdfLink()

def findFirstLink():
  # URL do site requisitado
  url = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss"
  # Puxar o código fonte HTML da URL do site escolhido
  pagina1 = requests.get(url)
  # Usar o interpretador da biblioteca BeautifulSoup para facilitar a visualização do código fonte HTML
  soup = BeautifulSoup(pagina1.content, "html.parser")
  # Guardar em variável resultado o conteúdo achado no elemento de id="parent-fieldname-text"
  resultado1 = soup.find(id="parent-fieldname-text")
  # Guardar em variável link todo o conteúdo da primeira tag <a> que está dentro da variável resultado
  link = resultado1.find("a")
  # Printar apenas o link contido no elemento href da tag <a>
  global tiss 
  tiss = link.get("href")

def findPdfLink():
  # Repetir o processo inicial mas desta vez no link novo encontrado para procurar o componente organizacional
  url = tiss
  pagina2 = requests.get(url)
  soup = BeautifulSoup(pagina2.content, "html.parser")
  resultado2 = soup.find(class_="table-responsive")
  compOrg = resultado2.find("a")
  global pdfLink
  pdfLink = compOrg.get("href")

def downloadPdfLink():
  # Baixar o componente organizacional em .pdf
  response = requests.get(pdfLink)
  file = open("padrao-tiss_componente-organizacional_202111.pdf", "wb")
  file.write(response.content)
  file.close()

main()
