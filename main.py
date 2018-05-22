import pygame

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

# Load images
introLogo = pygame.image.load("res/logo.png")
paddleImg = pygame.image.load("res/paddle.png")

def main():
  pygame.init()
  gameDisplay = pygame.display.set_mode((1280, 720))
  pygame.display.set_caption("Pong On Acid")
  clock = pygame.time.Clock()

  done = False
  show_logo = True

  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      print(event)

    gameDisplay.fill(black)
    gameDisplay.blit(introLogo, introLogo.get_rect())
    gameDisplay.blit(paddleImg, paddleImg.get_rect())
    pygame.display.flip()

    pygame.display.update()
    clock.tick(60)

  pygame.quit()
  quit()

if __name__ == "__main__":
  main()
