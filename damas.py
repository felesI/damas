#coding: utf-8
'''
projeto - computação 1º periodo - UFCG - 
Matheus Lisboa Oliveira dos Santos
versão 0.02
'''
import pygame
 
tam_x = 420
tam_y = 420

cor_preta  = (0,0,0)
cor_branca = (255,255,255)
cor_marrom = (210,180,140)
cor_vermelha = (255,0,0)
cor_azul = (0,206,209)
cor_cinza = (128,128,128)

#matriz de controle
matriz = [[(i+j)%2 for i in range(8)] for j in range(8)]

## controle de vez ###################
vez = 2

############# controle de pontos #######
p_azul = 0
p_vermelho = 0

#inicia o pygame #######
pygame.init()

tela = pygame.display.set_mode((420,420))
tela.fill(cor_marrom)
########################



## desenha os retangulos no tabuleiro
def retangulo(pos_x, pos_y,cor):
	ret = pygame.Rect(pos_x,pos_y,50,50)
	pygame.draw.rect(tela,cor,ret)


#desenha o tabuleiro e as peças
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


##auxiliar para mostrar a matriz
def mostra():
	for i in range(8):
		print matriz[i]
	print ""

#seta a peça na matriz e desenha
def colocaPeca(x,y,cor):
	matriz[(y-10)/50][(x-10)/50] = 2 if cor == cor_azul else 4
	pygame.draw.circle(tela,cor,(((x-10)/50 * 50 + 35),((y-10)/50 * 50 + 35)),20)

#desenha a peça
def movePeca(antes, depois,cor):
	retangulo(10+((antes[0]-10)/50)*50,10+((antes[1]-10)/50)*50,cor_preta)
	matriz[(antes[1]-10)/50][(antes[0]-10)/50] = 0
	colocaPeca(depois[0],depois[1],cor)

#verifica se pode comer alguma peça
def canEat():
	for i in range(8):
		for j in range(8):
			if matriz[i][j] == vez:
				if (i+2 < 8) and (j+2 < 8) and matriz[i+1][j+1] == (4 if vez == 2 else 2) and matriz[i+2][j+2] == 0:
					return [1,i + 2,j + 2, i, j]
				elif (i+2 < 8) and (j-2 >= 0) and matriz[i+1][j-1] == (4 if vez == 2 else 2) and matriz[i+2][j-2] == 0:
					return [1,i + 2,j - 2, i, j]
				if (i-2 >= 0) and (j+2 < 8) and matriz[i-1][j+1] == (4 if vez == 2 else 2) and matriz[i-2][j+2] == 0:
					return [1,i - 2,j + 2, i, j]
				elif (i-2 >= 0) and (j - 2 >= 0) and matriz[i-1][j-1] == (4 if vez == 2 else 2) and matriz[i-2][j-2] == 0:
					return [1,i - 2,j - 2, i, j]
	return [0,0,0,0,0]

def mudaCor(pos_x,pos_y,cor):
	pos1 = pos_y*50 + 10
	pos2 = pos_x*50 + 10
	if 10 <= pos1 <= 400 and 10 <= pos2 <= 400:
		retangulo(pos_y*50 + 10,pos_x*50 +10,cor)

def pinta(pos_x,pos_y, cor, num):
	m_y = (pos_y - 10)/50
	m_x = (pos_x - 10)/50
	if matriz[m_y][m_x] % 2 == 0:
		if vez == 2:
			if m_y + 1 <= 7 and m_x + 1 <= 7 and (matriz[m_y + 1][m_x + 1] == 0 or matriz[m_y + 1][m_x + 1] == 6):
				mudaCor(m_y + 1,m_x + 1,cor)
				matriz[m_y + 1][m_x + 1]  = num
			

			if m_y + 1 <= 7 and m_x - 1 >= 0 and (matriz[m_y + 1][m_x - 1] == 0 or matriz[m_y + 1][m_x - 1] == 6):
				mudaCor(m_y  + 1, m_x - 1,cor)
				matriz[m_y + 1][m_x - 1] = num
			
			
		else:
			if m_y - 1 >= 0 and m_x + 1 <= 7 and (matriz[m_y  - 1][m_x + 1] == 0 or matriz[m_y  - 1][m_x + 1] == 6):
				matriz[m_y  - 1][m_x + 1] = num
				mudaCor(m_y - 1, m_x + 1,cor)
			
			if m_y - 1 >= 0 and m_y - 1 >= 0 and (matriz[m_y -  1][m_x - 1] == 0 or matriz[m_y -  1][m_x - 1] == 6):
				matriz[m_y -  1][m_x - 1] = num
				mudaCor(m_y - 1,m_x - 1,cor)
			

		if m_y + 2 <= 7 and m_x + 2 <= 7 and (matriz[m_y + 2][m_x + 2] == 0 or matriz[m_y + 2][m_x + 2] == 6):
				if matriz[m_y + 1][m_x + 1] == (2 if vez == 4 else 4):
					mudaCor(m_y + 2,m_x + 2,cor)
					matriz[m_y + 2][m_x + 2] = num
		if m_y + 2 <= 7 and m_x - 2 >= 0 and (matriz[m_y + 2][m_x - 2] == 0 or matriz[m_y + 2][m_x - 2] == 6):
				if matriz[m_y + 1][m_x - 1] == (2 if vez == 4 else 4):
					matriz[m_y + 2][m_x - 2]  = num
					mudaCor(m_y + 2,m_x - 2,cor)
		if m_y - 2 >= 0 and m_x + 2 <= 7 and (matriz[m_y  - 2][m_x + 2] == 0 or matriz[m_y  - 2][m_x + 2] == 6):
				if matriz[m_y  - 1][m_x + 1] == (2 if vez == 4 else 4):
					matriz[m_y - 2][m_x + 2] = num
					mudaCor(m_y - 2, m_x + 2,cor)
		if m_y - 2 >= 0 and m_y - 2 >= 0 and (matriz[m_y -  2][m_x - 2] == 0 or matriz[m_y -  2][m_x - 2] == 6):
				if matriz[m_y -  1][m_x - 1] ==  (2 if vez == 4 else 4):
					matriz[m_y -  2][m_x - 2] = num
					mudaCor(m_y - 2,m_x - 2,cor)

			


				
def main():
	global vez,p_vermelho,p_azul
	preenche()

	sair = False
	clique = False
	lis = [0,0,0,0,0]
	while not sair:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sair = True

			if not clique:
				if event.type == pygame.MOUSEBUTTONDOWN:
					an_x,an_y = pygame.mouse.get_pos()
					if (10 < an_x < 400) and (10 < an_y < 400) and matriz[(an_y-10)/50][(an_x-10)/50] == vez:
						mudaCor((an_y-10)/50,(an_x-10)/50,cor_cinza)
						colocaPeca(an_x,an_y, cor_azul if vez == 2 else cor_vermelha)
						pinta(an_x,an_y,cor_cinza,6)
						clique = True

			else:
				if event.type == pygame.MOUSEBUTTONDOWN:
					de_x,de_y = pygame.mouse.get_pos()
					if (10 < de_x < 400) and (10 < de_y < 400) and  matriz[(de_y-10)/50][(de_x-10)/50] == 6:
						if (lis[0] == 1 and lis[1] == (de_y-10)/50 and lis[2] == (de_x-10)/50 and (an_y-10)/50 == lis[3] and (an_x-10)/50 == lis[4]) or lis[0] == 0:
							pinta(an_x,an_y,cor_preta,0)
							movePeca((an_x,an_y),(de_x,de_y), cor_azul if vez == 2 else cor_vermelha)

							a = 50 if an_x > de_x else -50
							b = 50 if an_y > de_y else -50
							if matriz[(de_y+b - 10) / 50][(de_x+a - 10)/50] != 0:
								if matriz[(de_y+b - 10) / 50][(de_x+a - 10)/50] == 2:
									p_vermelho += 1
								else:
									p_azul += 1
								matriz[(de_y+b - 10) / 50][(de_x+a - 10)/50] = 0
								print "pontos do vermelho: %d\npontos do azul: %d"%(p_vermelho,p_azul)
								if canEat()[0] == 0:
									vez = 2 if vez == 4 else 4
							else:
								vez = 2 if vez == 4 else 4

							retangulo(10+(de_x+a-10)/50*50,10+(de_y+b-10)/50*50,cor_preta)
							clique = False
							aux = lis
							lis = canEat()
							if lis[0] == aux[0] and lis[1] == aux[1] and lis[2] == aux[2]:
								lis[3] = aux[3]
								lis[4] = aux[]
					else:
						mudaCor((an_y-10)/50,(an_x-10)/50,cor_preta)
						colocaPeca(an_x,an_y, cor_azul if vez == 2 else cor_vermelha)
						pinta(an_x,an_y,cor_preta,0)
						clique = False


			if p_azul == 12 or p_vermelho == 12:
				sair = True
		
		pygame.display.update()

	pygame.quit()

main()
