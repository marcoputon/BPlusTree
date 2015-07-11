import random

t = 5

class Nodo():
	def __init__(self, valor):
		self.pai = None
		self.lista = []
		self.info = valor
	
	def lenLista(self):
		return len(self.lista)


	def split(self, lista):
		l3 = []
		l2 = []
		ind = []
		nova = []
		
		# Divisao inteira:
		resto = t%2
		if resto == 0:
			v = t/2
		else:
			v = int(t/2) + 1
		
		l1 = lista[0:v]
		l2 = lista[v:t]
		ind.append(lista[0])
		ind.append(lista[v])
		
		nova.append(l1)
		nova.append(l2)
		nova.append(ind)
		
		return nova


	def insereLista(self, nodo):
		#i = len(self.lista) - 1
		#while i >= 0 and self.lista[i] > nodo.info:
		#	i = i - 1
		#self.lista.insert(i+1, nodo)
		
		if self.lenLista() == 0:
			nodo.pai = self
			self.lista.append(nodo)
			return
			
		else:
			i = 0
			for j in self.lista:
				if nodo.info == self.lista[i].info:
					return	
				if nodo.info < self.lista[i].info:
					nodo.pai = self
					self.lista.insert(i, nodo)
					return
				elif i >= self.lenLista()-1:
					nodo.pai = self
					self.lista.append(nodo)
					return
					
				i += 1
		

	# Funcao para printar a Arvore bonitinha
	def mostrarLista(self, k=0):
		for i in self.lista:
			i.mostrarLista(k + 4)
			if self.lenLista() == 0:
				print "\n",
		
		print " " * k, self.info,
		
		if self.pai:
			print  " |pai:", self.pai.info
		else:
			pass
	
	
	def setPai(self, pai):
		for i in self.lista:
			i.pai = pai
	
	
	def ArrumaArvore(self):	
		s = self.split(self.lista)
		
		# Se o pai for a raiz	
		if self.pai is None:
			
			# Arruma o pai
			self.pai = Nodo(None)
			self.pai.lista = s[2]
										
			# Arruma o indice 0
			aux3 = Nodo(s[0][0].info)
			aux3.lista = s[0]
			aux3.pai = self.pai
			aux3.setPai(aux3)
			
			# Arruma o indice 1
			aux2 = Nodo(s[1][0].info)
			aux2.lista = s[1]
			aux2.pai = self.pai
			aux2.setPai(aux2)
					
			self.pai.lista[0] = aux3
			self.pai.lista[1] = aux2
			return self.pai.lista[0]
		
		# Se o pai nao for None:
		else:										
			# Arruma o indice 0
			aux3 = Nodo(s[0][0].info)
			aux3.lista = s[0]
			aux3.pai = self.pai
			aux3.setPai(aux3)

			# Arruma o indice 1
			aux2 = Nodo(s[1][0].info)
			aux2.lista = s[1]
			aux2.pai = self.pai
			aux2.setPai(aux2)
								
			indi = 0
			for i in self.pai.lista:
				if i == self:
					self.pai.lista.pop(indi)
				indi += 1 
			
			# Insere no pai	
			self.pai.insereLista(aux3)
			self.pai.insereLista(aux2)
			
			return aux3
			
			
	def insereB(self, nodo):
		global t
		if self.lenLista() == 0:
			self.insereLista(nodo)
			return self
		else:
			i = 0
			
			while i < self.lenLista():
				if i+1 < self.lenLista():
					
					# Se for menor
					if nodo.info < self.lista[i+1].info:
						
						# Se o indice nao tem filho
						if self.lista[i].lenLista() == 0:
							self.insereLista(nodo)
							break
							
						# Se o indice tem filho
						else:
							self.lista[i].insereB(nodo)
							break		
				else:
					if self.lista[i].lenLista() == 0:
						self.insereLista(nodo)
						break
					else:
						self.lista[i].insereB(nodo)
						break
				i += 1
			
			##################################################################
			####       Se passar do tamanho maximo de nodos na lista      ####
			##################################################################
			
			if self.lenLista() >= t:
				self = self.ArrumaArvore()
				
				if self.lenLista() >= t:
					self = self.ArrumaArvore()
				else:
					return self.pai	
			else:
				return self
			
			
R = Nodo(None)

def tEntrada():
	raw_input("Entrada invalida. Pressione qualquer tecla para continuar")

def insereN(n):
	global R
	N = n
	R = Nodo(None)
	while n > 0:
		R = R.insereB(Nodo(random.randint(0, N)))
		n -= 1

while True:
	try:
		t = int(raw_input("Qual o tamanho maximo do nodo? "))
		break
	except:
		t = 5
		raw_input("Favor digitar um numero inteiro.")
		
while True:
	print(chr(27) + "[2J")
	try:
		op = int(raw_input("1) Inserir N elementos\n2) Mostrar arvore\n3) Sair\n\nOpcao: "))
	except Exception as e:
		print e
		tEntrada()
		continue
	
	if op is 1:
		while True:
			try:
				z = int(raw_input("Digite quantos elementos quer inserir: "))
				insereN(z)
				raw_input("Pressione qualquer tecla para continuar.")
				break
			except Exception as e:
				print e
				tEntrada()
	
	elif op is 2:
		R.mostrarLista()
		lixo = raw_input("Pressione qualquer tecla para continuar.")
	
	elif op is 3:
		break
	
	else:
		tEntrada()
