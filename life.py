import pygame as PG
import random
import sys


def l2copy(ll):
	return [ i.copy() for i in ll ]


def update(cells, x, y, WC, HC):
	count = 0
	for i in (x - 1, x, x + 1):
		for j in (y - 1, y, y + 1):
			if i < 0 or i >= WC: i = abs(abs(i) - WC)
			if j < 0 or j >= HC: j = abs(abs(j) - HC)
			if cells[i][j]: count += 1
	if cells[x][y] and 3 <= count <= 4: 	return 1
	elif not cells[x][y] and count == 3: 	return 1
	else: 									return 0


def main():
	if len(sys.argv) == 3 and sys.argv[1] == '-seed':
		random.seed(int(sys.argv[2]))

	PG.init()
	PG.display.set_caption('Game of Life v.1')
	W, H = 980, 640
	TILE = 6
	WC, HC = W // TILE, H // TILE
	FPS = 24
	BGCLR = PG.Color((7, 1, 7))
	CCLR_S = PG.Color((50, 50, 150))
	CCLR_D = PG.Color((125, 125, 50))
	SCREEN = PG.display.set_mode((W, H))
	CLOCK = PG.time.Clock()

	if len(sys.argv) == 2 and sys.argv[1] == '-sc':
		cells = [[0 for i in range(HC)] for j in range(WC)]
		cells[75][35] = 1
		cells[76][36] = 1
		cells[76][37] = 1
		cells[75][37] = 1
		cells[74][37] = 1
		for i in range(WC):
			for j in range(HC//2, HC):
				if i%3 and j%3:
					cells[i][j] = 1
	else:
		cells = [[random.randint(0, 1) for i in range(HC)] for j in range(WC)]

	newc = [[0 for i in range(HC)] for j in range(WC)]
	oldc = [[0 for i in range(HC)] for j in range(WC)]

	while True:
		for e in PG.event.get():
			if e.type == PG.QUIT or (e.type == PG.KEYDOWN and e.key == PG.K_ESCAPE):
				exit()

		SCREEN.fill(BGCLR)

		for x in range(WC):
			for y in range(HC):
				if cells[x][y]:
					CCLR = CCLR_S if oldc[x][y] else CCLR_D
					PG.draw.rect(SCREEN, CCLR, PG.Rect((x*TILE + 1 ,y*TILE + 1), (TILE - 1,TILE - 1)))
				newc[x][y] = update(cells, x, y, WC, HC)

		oldc = l2copy(cells)
		cells = l2copy(newc)

		PG.display.update()
		CLOCK.tick(FPS)

if __name__ == '__main__':
	main()