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
		self.carregado = True	# Define a flag carregado como True para indicar que o nó foi carregado
		with open(nome_arquivo, "r") as f:
			linhas = f.readlines()	# Lê todas as linhas do arquivo e armazena em 'linhas'
			i = 0	# Índice para percorrer as linhas do arquivo
			while i < len(linhas):	# Loop para percorrer as linhas do arquivo
				filho_nome = linhas[i].strip()	# Remove espaços em branco
				i += 1
				if i < len(linhas):	# Verifica se ainda há linhas para
					chave = int(linhas[i].strip())
					self.chaves.append(chave)
					self.filhos.append(noh(filho_nome))
					self.folha = False
				else:  # Se for a última linha do arquivo
					self.filhos.append(noh(filho_nome))
				i += 1
		print(f"Chaves lidas: {self.chaves}")
		print(f"Filhos lidos: {[filho.fileName for filho in self.filhos]}")
        
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
