from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessar o site
drive = webdriver.Chrome()
drive.get('https://www.novaliderinformatica.com.br/computadores-gamers')

# extrair todos os titulos
titulos = drive.find_elements(By.XPATH, "//a[@class='nome-produto']")

# extrair todos os preços
precos = drive.find_elements(By.XPATH, "//strong[@class='preco-promocional']")


# criando planilha
workbook = openpyxl.Workbook()
# criando a página 'produtos'
workbook.create_sheet('produtos')
# selecionando a página 'produtos' e Inserindo nome nas células
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'


# inserir os titulos e preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])

workbook.save('produtos.xlsx')