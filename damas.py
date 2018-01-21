#coding: utf-8
'''
projeto - computação 1º periodo - UFCG - 
Matheus Lisboa Oliveira dos Santos
versão 0.02
'''
import pygame

tam_x = 420
tam_y = 420

tam_pxy = (50,50)

cor_preta  = (0,0,0)
cor_branca = (255,255,255)
cor_marrom = (210,180,140)
cor_vermelha = (255,0,0)
cor_azul = (0,206,209)

#matriz de controle
matriz = [[(i+j)%2 for i in range(8)] for j in range(8)]

## controle de vez ###################
vez = 2

#inicia o pygame #######
pygame.init()

tela = pygame.display.set_mode((420,420))
tela.fill(cor_marrom)
########################


def retangulo(pos_x, pos_y,cor):
	ret = pygame.Rect(pos_x,pos_y,50,50)
	pygame.draw.rect(tela,cor,ret)

def preenche():
	l = [cor_preta,cor_branca]
	for i in range(8):
		for j in range(8):
			retangulo(10+j*50,10+i*50,l[(i+j)%2])
			if matriz[i][j] == 0 and  (2 >= i or i >= 5):
				if i <= 2:
					colocaPeca(j*50 + 10, i * 50 + 10,cor_azul)
				else:
					colocaPeca(j*50 + 10, i * 50 + 10,cor_vermelha)

def mostra():
	for i in range(8):
		print matriz[i]
	print ""

def colocaPeca(x,y,cor):
	matriz[(y-10)/50][(x-10)/50] = 2 if cor == cor_azul else 4
	pygame.draw.circle(tela,cor,(((x-10)/50 * 50 + 35),((y-10)/50 * 50 + 35)),20)

def movePeca(antes, depois,cor):
	retangulo(10+((antes[0]-10)/50)*50,10+((antes[1]-10)/50)*50,cor_preta)
	matriz[(antes[1]-10)/50][(antes[0]-10)/50] = 0
	colocaPeca(depois[0],depois[1],cor)

def mudaCor(pos_x,pos_y,cor):
	pos1 = pos_y*50 + 10
	pos2 = pos_x*50 + 10
	if 10 <= pos1 <= 400 and 10 <= pos2 <= 400:
		retangulo(pos_y*50 + 10,pos_x*50 +10,cor)

def pinta(pos_x,pos_y, cor, num):
	m_y = (pos_y - 10)/50
	m_x = (pos_x - 10)/50

	if matriz[m_y][m_x] % 2 == 0:
		if m_y + 1 <= 7 and m_x + 1 <= 7 and (matriz[m_y + 1][m_x + 1] == 0 or matriz[m_y + 1][m_x + 1] == 6):
			mudaCor(m_y + 1,m_x + 1,cor)
			matriz[m_y + 1][m_x + 1]  = num
		elif m_y + 2 <= 7 and m_x + 2 <= 7 and (matriz[m_y + 2][m_x + 2] == 0 or matriz[m_y + 2][m_x + 2] == 6):
			mudaCor(m_y + 2,m_x + 2,cor)
			matriz[m_y + 2][m_x + 2] = num

		if m_y + 1 <= 7 and m_x - 1 >= 0 and (matriz[m_y + 1][m_x - 1] == 0 or matriz[m_y + 1][m_x - 1] == 6):
			mudaCor(m_y  + 1, m_x - 1,cor)
			matriz[m_y + 1][m_x - 1] = num
		elif m_y + 2 <= 7 and m_x - 2 >= 0 and (matriz[m_y + 2][m_x - 2] == 0 or matriz[m_y + 2][m_x - 2] == 6):
			matriz[m_y + 2][m_x - 2]  = num
			mudaCor(m_y + 2,m_x - 2,cor)

		if m_y - 1 >= 0 and m_x + 1 <= 7 and (matriz[m_y  - 1][m_x + 1] == 0 or matriz[m_y  - 1][m_x + 1] == 6):
			matriz[m_y  - 1][m_x + 1] = num
			mudaCor(m_y - 1, m_x + 1,cor)
		elif m_y - 2 >= 0 and m_x + 2 <= 7 and (matriz[m_y  - 2][m_x + 2] == 0 or matriz[m_y  - 2][m_x + 2] == 6):
			matriz[m_y - 2][m_x + 2] = num
			mudaCor(m_y - 2, m_x + 2,cor)

		if m_y - 1 >= 0 and m_y - 1 >= 0 and (matriz[m_y -  1][m_x - 1] == 0 or matriz[m_y -  1][m_x - 1] == 6):
			matriz[m_y -  1][m_x - 1] = num
			mudaCor(m_y - 1,m_x - 1,cor)
		elif m_y - 2 >= 0 and m_y - 2 >= 0 and (matriz[m_y -  2][m_x - 2] == 0 or matriz[m_y -  2][m_x - 2] == 6):
			matriz[m_y -  2][m_x - 2] = num
			mudaCor(m_y - 2,m_x - 2,cor)

def main():
	global vez
	preenche()
	mostra()

	sair = False
	clique = False
	while not sair:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sair = True

			if not clique:
				if event.type == pygame.MOUSEBUTTONDOWN:
					an_x,an_y = pygame.mouse.get_pos()
					if (10 < an_x < 400) and (10 < an_y < 400) and matriz[(an_y-10)/50][(an_x-10)/50] == vez:
						pinta(an_x,an_y,cor_vermelha,6)
						clique = True
						
			else:
				if event.type == pygame.MOUSEBUTTONDOWN:
					de_x,de_y = pygame.mouse.get_pos()
					if (10 < de_x < 400) and (10 < de_y < 400) and  matriz[(de_y-10)/50][(de_x-10)/50] == 6:
						pinta(an_x,an_y,cor_preta,0)
						movePeca((an_x,an_y),(de_x,de_y), cor_azul if vez == 2 else cor_vermelha)
						a = 50 if an_x > de_x else -50
						b = 50 if an_y > de_y else -50
						matriz[(de_y+b - 10) / 50][(de_x+a - 10)/50] = 0
						retangulo(10+(de_x+a-10)/50*50,10+(de_y+b-10)/50*50,cor_preta)
						vez = 2 if vez == 4 else 4
						clique = False
					else:
						pinta(an_x,an_y,cor_preta,0)
						clique = False
		
		pygame.display.update()

	pygame.quit()


main()
