#coding: utf-8
import pygame

tam_x = 420
tam_y = 420

tam_pxy = (50,50)

cor_preta  = (0,0,0)
cor_branca = (255,255,255)
cor_marrom = (210,180,140)
cor_vermelha = (255,0,0)
cor_azul = (0,206,209)

#classe celula
class celula(object):
	#inicia o objeto o tamanho e a posição na tela com a cor desejada
	def __init__(self,tam_xy,pos_xy,tela,cor):
		self.pos_x = pos_xy[0]#pos x da celula ; vai servir para localização e colocação da peça
		self.pos_y = pos_xy[1]#pos y da celula
		self.cor = cor#cor da peça
		self.tela = tela#tela onde vai ser colocada
		self.ret = pygame.Rect(self.pos_x,self.pos_y,tam_xy[0],tam_xy[1])#variavel que vai guardar o objeto para alterações futuras

		#metodo que desenha
		self.desenha()

	#metodo que desenha a celula, para organização
	def desenha(self):
		pygame.draw.rect(self.tela,self.cor,self.ret)

#classe que controla o tabuleiro
class tabuleiro(object):
	global tam_pxy,cor_branca,cor_preta,cor_marrom#import das variaveis globais
	#metodo que inicia a classe
	def __init__(self,tela,celula):
		self.matriz_tabuleiro = [[0 for i in range(8)] for i in range(8)]#matriz que guarda os objetos celula
		self.tela = tela#tela que vai sae guardada
		self.celula = celula#atributo celula, não quis usar herança

		self.desenha_tabu()

	#metodo que desenha o tabuleiro e guarda as celulas
	def desenha_tabu(self):
		for linha in range(8):
			for coluna in range(8):
				if (linha+coluna)%2 == 0:
					self.matriz_tabuleiro[linha][coluna] = self.celula(tam_pxy,(10+(coluna*50),10+(linha*50)),self.tela,cor_preta)
				else:
					self.matriz_tabuleiro[linha][coluna] = self.celula(tam_pxy,(10+(coluna*50),10+(linha*50)),self.tela,cor_branca)

	#metodo que muda a cor de uma celula em especifico
	def muda_cor(self,x,y,cor_nova):
		self.matriz_tabuleiro[x][y] = self.celula(tam_pxy,(self.matriz_tabuleiro[x][y].pos_x,self.matriz_tabuleiro[x][y].pos_y),self.tela,cor_nova)

#classe que cria a peça
class pecas(object):
	#metodo que inicia a classe
	def __init__(self,tela,cor,pos_xy,raio,tabuleiro):
		self.tela = tela
		self.raio = raio
		self.cor = cor
		self.tabuleiro = tabuleiro
		self.cir = pygame.draw.circle(self.tela,self.cor,pos_xy,self.raio)

	#metodo que muda a peça de lugar
	def muda_lugar(self,pos_xy):
		self.tela.fill(cor_marrom)
		self.tabuleiro.desenha_tabu()
		self.cir = pygame.draw.circle(self.tela,self.cor,pos_xy,self.raio)


#função que inicia o programa
def main():
	#globais com tamanho da tela
	global tam_x,tam_y,cor_vermelha,cor_marrom,cor_azul

	#cores usadas


	#pygame iniciado
	pygame.init()

	#inicando a tela
	tela = pygame.display.set_mode((tam_x,tam_y))
	tela.fill(cor_marrom)

	tabu = tabuleiro(tela,celula)

	#testes para futuras implementações
	peca = pecas(tela,cor_azul,(35,35),20,tabu)
	peca.muda_lugar((85,85))
	peca.muda_lugar((135,135)) 

	tabu.muda_cor(7,7,cor_vermelha)

	sair = False
	while not sair:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair = True
		pygame.display.update()

	pygame.quit()


main()
