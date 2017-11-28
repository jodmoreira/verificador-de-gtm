# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def escreversaida():
	records.append((tag, linha))
	dataframe = pd.DataFrame(records)
	dataframe.to_csv("saida.csv", mode="w", header=["GTM", "Pag"])

with open("lista.txt", "r+") as urls:
	with open("saida.txt", "w+") as saida:
		x = 0
		records = []
		for linha in urls:
			try:
				linha = linha.strip()
				requisicao = requests.get(linha.strip()) #strip verifica se ele realmente tirou a nova linha, caso tenha ficado
				requisicao = requisicao.text
				soup = BeautifulSoup(requisicao, "html.parser")
				gtm = soup.findAll('script')
				gtm = str(gtm)
				tag = re.search(r'GTM-\w+', gtm).group(0)
				x = x + 1
				print x, "paginas verificadas"
				print linha.strip()
				print tag, "\n"
				escreversaida()
			except:
				print "ERRO!!!"
				print linha, "\n"
				tag = "Encontrei algum erro"
				escreversaida()
	saida.close()
urls.close()
print "Terminei"
