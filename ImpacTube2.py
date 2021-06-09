Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> canais = ["Clow Podcast", 2700000, 500.99, "não"]
tabela = []
tabela.append(canais)
>>> tabela
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tabela
NameError: name 'tabela' is not defined
>>> canais = ["Clow Podcast", 2700000, 500.99, "não"]
>>> canais
['Clow Podcast', 2700000, 500.99, 'não']
>>> tabela = []
>>> tabela.append(canais)
>>> tabela
[['Clow Podcast', 2700000, 500.99, 'não']]
>>> canais = ["Felipe Nelson", 3500000, 1000.25, "sim"]
>>> canais
['Felipe Nelson', 3500000, 1000.25, 'sim']
>>> tabela.append(canais)
>>> tabela
[['Clow Podcast', 2700000, 500.99, 'não'], ['Felipe Nelson', 3500000, 1000.25, 'sim']]
>>> canais = ['Porta dos Mundos',16800000, 2000.00, "sim" ]
>>> canais
['Porta dos Mundos', 16800000, 2000.0, 'sim']
>>> tabela.append(canais)
>>> tabela
[['Clow Podcast', 2700000, 500.99, 'não'], ['Felipe Nelson', 3500000, 1000.25, 'sim'], ['Porta dos Mundos', 16800000, 2000.0, 'sim']]
>>> canais = ["PodHá",2120000, 450.00, "não"]
>>> canais
['PodHá', 2120000, 450.0, 'não']
>>> canais = ["PodHá!",2120000, 450.00, "não"]
>>> canais
['PodHá!', 2120000, 450.0, 'não']
>>> tabela.append(canais)
>>> tabela
[['Clow Podcast', 2700000, 500.99, 'não'], ['Felipe Nelson', 3500000, 1000.25, 'sim'], ['Porta dos Mundos', 16800000, 2000.0, 'sim'], ['PodHá!', 2120000, 450.0, 'não']]
>>> canais = ["Winter SonNones",42400000, 20000.00, "sim" ]
>>> tabela.append(canais)
>>> tabela
[['Clow Podcast', 2700000, 500.99, 'não'], ['Felipe Nelson', 3500000, 1000.25, 'sim'], ['Porta dos Mundos', 16800000, 2000.0, 'sim'], ['PodHá!', 2120000, 450.0, 'não'], ['Winter SonNones', 42400000, 20000.0, 'sim']]
>>> canais = ["Manual do Urso";14600000;1800.50; "sim"]
SyntaxError: invalid syntax
>>> canais = ["Manual do Urso",14600000,1800.50, "sim"]
>>> canais
['Manual do Urso', 14600000, 1800.5, 'sim']
>>> tabela.append(canais)
>>> canais = ["Humorado Games",4130000,5000.00,"não"]
>>> canais
['Humorado Games', 4130000, 5000.0, 'não']
>>> tabela.append(canais)
>>> canais = ["Joãozinho TôComeçando",950,10.00,"não"]
>>> canais
['Joãozinho TôComeçando', 950, 10.0, 'não']
>>> tabela.append(canais)]
SyntaxError: unmatched ']'
>>> tabela.append(canais)
>>> tabela
[['Clow Podcast', 2700000, 500.99, 'não'], ['Felipe Nelson', 3500000, 1000.25, 'sim'], ['Porta dos Mundos', 16800000, 2000.0, 'sim'], ['PodHá!', 2120000, 450.0, 'não'], ['Winter SonNones', 42400000, 20000.0, 'sim'], ['Manual do Urso', 14600000, 1800.5, 'sim'], ['Humorado Games', 4130000, 5000.0, 'não'], ['Joãozinho TôComeçando', 950, 10.0, 'não']]
>>> def exibe_tabela(tabela):
	for canais in tabela:
		print(canais)
	print()
	
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
>>> tabela
[['Clow Podcast', 2700000, 500.99, 'não'], ['Felipe Nelson', 3500000, 1000.25, 'sim'], ['Porta dos Mundos', 16800000, 2000.0, 'sim'], ['PodHá!', 2120000, 450.0, 'não'], ['Winter SonNones', 42400000, 20000.0, 'sim'], ['Manual do Urso', 14600000, 1800.5, 'sim'], ['Humorado Games', 4130000, 5000.0, 'não'], ['Joãozinho TôComeçando', 950, 10.0, 'não']]
>>> exibe_tabela(canais)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    exibe_tabela(canais)
NameError: name 'exibe_tabela' is not defined
>>> exibe_tabela(canais)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    exibe_tabela(canais)
NameError: name 'exibe_tabela' is not defined
>>> 
============================================================================================================== RESTART: Shell ==============================================================================================================
>>> canais[['Clow Podcast', 2700000, 500.99, 'não'], ['Felipe Nelson', 3500000, 1000.25, 'sim'], ['Porta dos Mundos', 16800000, 2000.0, 'sim'], ['PodHá!', 2120000, 450.0, 'não'], ['Winter SonNones', 42400000, 20000.0, 'sim'], ['Manual do Urso', 14600000, 1800.5, 'sim'], ['Humorado Games', 4130000, 5000.0, 'não'], ['Joãozinho TôComeçando', 950, 10.0, 'não']]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    canais[['Clow Podcast', 2700000, 500.99, 'não'], ['Felipe Nelson', 3500000, 1000.25, 'sim'], ['Porta dos Mundos', 16800000, 2000.0, 'sim'], ['PodHá!', 2120000, 450.0, 'não'], ['Winter SonNones', 42400000, 20000.0, 'sim'], ['Manual do Urso', 14600000, 1800.5, 'sim'], ['Humorado Games', 4130000, 5000.0, 'não'], ['Joãozinho TôComeçando', 950, 10.0, 'não']]
NameError: name 'canais' is not defined
>>> exibe_tabela(canais)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    exibe_tabela(canais)
NameError: name 'exibe_tabela' is not defined
>>> 