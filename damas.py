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
		self.preechida = False
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
	def __init__(self,tela,cor,pos_xy,tabuleiro):
		self.tela = tela
		self.cor = cor
		self.tabuleiro = tabuleiro
		self.cir = pygame.draw.circle(self.tela,self.cor,pos_xy,20)
		self.posxy = pos_xy

		self.tabuleiro.matriz_tabuleiro[(pos_xy[0]+15)/50 - 1][(pos_xy[1]+15)/50 - 1].preechida = True
		
	#metodo que muda a peça de lugar
	def muda_lugar(self,pos_xy):
		self.tabuleiro.matriz_tabuleiro[(self.posxy[0]+15)/50 - 1][(self.posxy[1]+15)/50 - 1].preechida = False
		self.tela.fill(cor_marrom)
		self.tabuleiro.desenha_tabu()
		self.tabuleiro.matriz_tabuleiro[(pos_xy[0]+15)/50 - 1][(pos_xy[1]+15)/50 - 1].preechida = True
		print (pos_xy[0]+15)/50 - 1,(pos_xy[1]+15)/50 - 1
		self.cir = pygame.draw.circle(self.tela,self.cor,pos_xy,20)




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
	peca = pecas(tela,cor_azul,(185,185),tabu)
	print tabu.matriz_tabuleiro[3][3].preechida

	sair = False
	aux = True
	while not sair:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair = True
			if aux:
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos_x,pos_y = pygame.mouse.get_pos()
					if tabu.matriz_tabuleiro[(pos_x-10)/50][(pos_y-10)/50].preechida:
						aux = False
			else:
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos_x,pos_y = pygame.mouse.get_pos()
					if not tabu.matriz_tabuleiro[(pos_x-10)/50][(pos_y-10)/50].preechida:
						peca.muda_lugar((((pos_x-10)/50)*50+35,((pos_y-10)/50)*50+35))
						aux = True
				

		pygame.display.update()	

pygame.quit()

main()




"""
pos_x,pos_y = pygame.mouse.get_pos()
peca.muda_lugar((((pos_x-10)/50)*50+35,((pos_y-10)/50)*50+35))
"""
