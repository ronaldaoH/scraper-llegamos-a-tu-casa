import requests
from bs4 import BeautifulSoup
from lxml import html, etree

def scrapear():
	page = requests.get("https://llegamosatucasa.com/list/lima")
	tree = html.fromstring(page.content)

	empresas = tree.xpath("//li[contains(@class,'w-full')]")[0]
	#NOMBRE
	print("NOMBRE")
	titulos = empresas.xpath("//h3[contains(@class,'text-2xl')]/text()")
	print(len(titulos))
	#DIRECCION
	print("DIRECCION")
	direcciones = empresas.xpath("//p[contains(@class,'text-xs sm:text-sm mb-2')]/text()")
	print(len(direcciones))
	#TELEFONOS
	print("TELEFONOS")
	telefonos = empresas.xpath("//p[contains(@class,'text-base')]/a/text()")
	print(telefonos)
	#CORREOS
	print("CORREOS")
	correos = empresas.xpath("//p[contains(@class,'text-base font-medium mb-4')]/a/text()")
	print(correos)
	#CONTENIDO
	print("CONTENIDO")
	contenidos = empresas.xpath("//p[contains(@class,'max-w-xl text-sm sm:text-base mb-4')]/text()") 
	#print(contenidos)
	


	#ETIQUETAS UL
	print("ETIQUETAS UL")
	etiquetas = empresas.xpath("//ul[contains(@class,'-m-1')]")
	count = 2
	for et in etiquetas:
		if count % 2 == 0:
			tags = etree.tostring(et, pretty_print=True)
			soup  = BeautifulSoup(tags, 'html.parser')
			tipos = soup.find_all("li")
			#for tipo in tipos:
			#	print(tipo.text)
			#print("###")
		else:
			distritos = etree.tostring(et, pretty_print=True)
			soup  = BeautifulSoup(distritos, 'html.parser')
			distritos = soup.find_all("li")
			#for distrito in distritos:
			#	print(distrito.text)
			#print("####")
		count = count +1
	
	for x in range(len(titulos)):
		print( '#### NUEVA TIENDA ####')
		print("[+] Titulo : " , titulos[x])
		#print("[+] Direccion : " , direcciones[x])
		print("[+] Telefonos : " , telefonos[x])
		#print("[+] Correos : " , correos[x])
		print("[+] Contenido : " , contenidos[x])
		print("[+] Tags : ")
		for tipo in tipos:
				print('[+]  ', tipo.text)
		print("[+] Distritos : " )
		for distrito in distritos:
				print('[+]  ',distrito.text)
	
	

scrapear()
