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
		if self.lenLista() == 0:
			self.lista.append(nodo)
			#if self.pai:
			#	self.info = self.lista[0].pai
			return
		else:
			i = 0
			for j in self.lista:
				if nodo.info == self.lista[i].info:
					return
					
				if nodo.info < self.lista[i].info:
					l1 = self.lista[0:i]
					l2 = self.lista[i:self.lenLista()]
					l1.append(nodo)
					self.lista = l1 + l2
					#if self.pai:
					#	self.info = self.lista[0].info
					return
				
				elif i >= self.lenLista()-1:
					self.lista.append(nodo)
					#if self.pai:
					#	self.info = self.lista[0].info
					return
				i += 1
			
			
	# Funcao para printar a Arvore bonitinha
	def mostrarLista(self, k=0):

		for i in self.lista:
			i.mostrarLista(k + 4)
		
		print " " * k, self.info
		
	
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

			# Arruma o indice 1
			aux2 = Nodo(s[1][0].info)
			aux2.lista = s[1]
			aux2.pai = self.pai
					
			self.pai.lista[0] = aux3
			self.pai.lista[1] = aux2
			return self.pai.lista[0]
		
		# Se o pai nao for None:
		else:
			print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"										
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
					
			for i in self.pai.lista:
				print i.info, "antes de inserir"
						
					
			indi = 0
			for i in self.pai.lista:
				if i == self:
					self.pai.lista.pop(indi)
				indi += 1 
			
			# Insere no pai	
			self.pai.insereLista(aux3)
			print "aux3:", str(aux3.info) + ":"
			for i in self.pai.lista:
				print i.info, "insere 0"
			
			
			
			# Insere no pai
			self.pai.insereLista(aux2)
			print "aux2:", str(aux2.info) + ":"
			for i in self.pai.lista:
				print i.info, "insere 1"
				
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
				for i in self.pai.lista:
					print i.info, "papai"
				
				
				if self.pai.lenLista() >= t:
					print "o pai estourou o limite"
					self = self.pai.ArrumaArvore()
					
					# Wow
					for i in self.lista:
						print i.info, "papaizinho"
				else:
					return self.pai
									
			else:
				return self
			
			
			
R = Nodo(None)

while True:
	#try:
	if True:
		l = int(raw_input("Digite o numero: "))
		R = R.insereB(Nodo(l))
		R.mostrarLista()
	#except:
	
		#raw_input("Um numero!!!")
								



print "\n\n\n"
R.mostrarLista()

##### Area de testes #####

##########################
