import pygame
import random
import time
pygame.mixer.init()

pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

gamewindow=pygame.display.set_mode((2,7))
bgimg=pygame.image.load('/storage/emulated/0/ToonApp/IMG_20210320_170646.png')
bgimg=pygame.transform.scale(bgimg,(1100,1500)).convert_alpha()
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,80)
def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	gamewindow.blit(screen_text,[x,y])
	
def plot(gamewindow,color,snk_list,snake_size):
	for x,y in snk_list:
		pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
		
def gameloop():
	food_x=300
	food_y=500
	snake_x=500
	snake_y=500
	velocity_x=0
	velocity_y=0
	snake_size=40
	score=0
	snk_list=[ ]
	snk_len=1
	game_exit=False
	game_over=False
	while not game_exit:
		if game_over==True:
			gamewindow.fill(white)
			text_screen("game over! ",red,400,1000)
			text_screen(f"score:- {score}",red,400,1100)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					game_exit=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						gameloop()
			
		else:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					game_exit=True
				
				if event.type==pygame.KEYDOWN:		
					if event.key==pygame.K_RIGHT:
				 	   velocity_x=5
				 	   velocity_y=0
					if event.key==pygame.K_LEFT:
						velocity_x=-5
						velocity_y=0
					if event.key==pygame.K_UP:
						velocity_y=-5
						velocity_x=0
					if event.key==pygame.K_DOWN:
						velocity_y=5
						velocity_x=0
					if event.key==pygame.K_q:
						score=score+50
			snake_x=snake_x+velocity_x
			snake_y=snake_y+velocity_y
		
			if abs(snake_x-food_x)<30 and abs(snake_y-food_y)<30:
				snk_len=snk_len+10
				score=score+10
				pygame.mixer.music.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/Fullscreen scaling/assets/audio/point.ogg')
				pygame.mixer.music.play()
				time.sleep(0.3)
				food_x=random.randint(0,1000)
				food_y=random.randint(0,1000)
			gamewindow.fill(white)
			gamewindow.blit(bgimg,(0,0))
			text_screen(f"score:- {score}",red,10,10)
		
			head=[ ]
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)
			if len(snk_list)>snk_len:
				del snk_list[0]
			if snake_x<0 or snake_y<0 or snake_x>1050 or snake_y>2000:
				game_over=True
			plot(gamewindow,black,snk_list,snake_size)
			if head in snk_list[ :-1]:
				game_over=True
			pygame.mixer.music.load('/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/Fullscreen scaling/assets/audio/hit.ogg')
			pygame.mixer.music.play()
		
			pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
		pygame.display.update()
		clock.tick(50)
		
if __name__=="__main__":
	gameloop()