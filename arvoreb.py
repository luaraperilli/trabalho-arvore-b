# Luara do Val Perilli - 2022004841
# Pedro Nogueira Barbosa - 2023006500

class noh:
	def __init__(self, fileName_="None"):
		self.fileName = fileName_	# Todo nó corresponde a um arquivo no disco
		self.carregado = False	# A flag carregado indica se aquele nó já foi lido do disco
		self.folha = True	# Indica se o nó é folha
		# Listas das chaves e filhos ficam vazias até serem lidos do disco
		self.chaves = []	# Armazenará as chaves do nó
		self.filhos = []	# Armazenará os filhos do nó
		
	# Quando essa função é chamada o arquivo é lido e as chaves e os filhos são preenchidos
	def carrega_arquivo(self, nome_arquivo):
		print("Lendo: ", nome_arquivo)
		self.carregado = True    # Define a flag carregado como True para indicar que o nó foi carregado
		f = open(nome_arquivo, "r")
		i = 0	# Contador de linhas
		for linha in f:	# Itera sobre cada linha do arquivo
			linha = linha.strip()  # Remove espaços em branco
			if i % 2 == 0:	# Se a linha é par é o nome de um filho
				linha_atual = linha  # Salva a linha atual como o nome do filho
			else:	# Se a linha é ímpar é uma chave
				# Verifica se a linha é um número (chave)
				if linha.isdigit():	
					chave = int(linha)	# Converte a linha para inteiro
					self.chaves.append(chave)	# Adiciona a chave à lista de chaves
					if linha_atual == "None":	# Se o nome do filho for None adiciona à lista de filhos
						self.filhos.append(None)	
					else:
						self.filhos.append(noh(linha_atual))	# Cria um novo nó e adiciona à lista de filhos
						self.folha = False

			i += 1  # Incrementa i 

		# Se a última linha do arquivo for um nome de filho sem chave correspondente
		if i % 2 == 1:  # Verifica se i é ímpar (última linha é um nome de filho)
			if linha_atual == "None":
				self.filhos.append(None)
			else:
				self.filhos.append(noh(linha_atual))

		f.close()

		return None	 # Retorna None para indicar que a chave não foi encontrada na árvore

class arvoreB:
	def __init__(self, t, filename):
		self.t = t	# Define o grau mínimo da árvore B
		self.raiz = noh(filename)	# Raíz da árvore

	def busca(self, k, x):	# Método que realiza busca na árvore B. K é a chave a ser buscada e X é o nó a partir do qual começa a busca
		if x.carregado == False:	# Verifica se o nó não foi carregado e, em caso positivo, carrega o arquivo associado
			x.carrega_arquivo(x.fileName)
		i = 0
		while i < len(x.chaves) and k > x.chaves[i]:	# Itera sobre as chaves do nó x para encontrar a posição onde k deve ser inserido ou onde a chave igual a k é encontrada
			i += 1
		
		if i < len(x.chaves) and k == x.chaves[i]:	# Se a chave k é encontrada no nó x,  retorna uma tupla indicando que a chave foi encontrada no próprio nó x
			return (x, i)
		elif x.folha:
			# Se x é folha e k não foi encontrada retorna None (chave não existe na árvore)
			return None
		else:
			# Se x não é folha e k não foi encontrada em x, recursivamente chama busca para continuar a busca
			return self.busca(k, x.filhos[i])
		

B = arvoreB(2, "0.tree")	# Cria o objeto árvore com grau mínimo 2 e raiz 0.tree
i = int(input())	# Lê um número inteiro
while(i != -1):
	if(B.busca(i, B.raiz) == None):
		print(str(i) + " nao encontrado")
	else:
		print(str(i) + " encontrado")
	i = int(input())
