import pygame

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

paddleImg = pygame.image.load("res/paddle.png")

def main():
  pygame.init()
  gameDisplay = pygame.display.set_mode((800, 600))
  pygame.display.set_caption("Pong On Acid")
  clock = pygame.time.Clock()

  done = False

  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      print(event)

    pygame.display.update()
    clock.tick(60)

  pygame.quit()
  quit()

if __name__ == "__main__":
  main()