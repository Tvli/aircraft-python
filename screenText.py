import pygame 

def screen_text(screen, text, x, y, size = 20, color = (19, 241, 19), 
				font_type = 'monospace'):
	try:
		text = str(text)
		font = pygame.font.SysFont(font_type, size)
		text = font.render(text, True, color)
		screen.blit(text, (x,y))

	except Exception:
		raise
