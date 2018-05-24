import pygame

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

# Load images
intro_logo = pygame.image.load("res/logo.png")

class Paddle:
  
  def __init__(self, x, y):
    self.img = pygame.image.load("res/paddle.png")
    self.x = x
    self.y = y
    self.spd = 30
    self.vx = 2
    self.vy = (-2)

class Ball:
  
  def __init__(self, x, y):
    self.img = pygame.image.load("res/ball.png")
    self.x = x
    self.y = y
    self.vx = 2
    self.vy = 2

def main():
  pygame.init()
  gameDisplay = pygame.display.set_mode((1280, 720))
  pygame.display.set_caption("Pong On Acid")
  clock = pygame.time.Clock()

  p1 = Paddle(100, 0)
  p2 = Paddle(1180, 0)
  ball = Ball(300, 400)

  done = False
  show_logo = True
  play_game = False

  while not done:

    if show_logo:
      # Update
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        elif event.type == pygame.KEYDOWN:
          show_logo = False
          play_game = True

      # Render
      gameDisplay.fill(black)
      gameDisplay.blit(intro_logo, (0,0))
      pygame.display.flip()
    elif play_game:
      # Update

      if (ball.x + ball.vx >= 1280 or ball.x + ball.vx <= 0):
        ball.vx *= (-1)
      else:
        ball.x += ball.vx

      if (ball.y + ball.vy >= 720 or ball.y + ball.vy <= 0):
        ball.vy *= (-1)
      else:
        ball.y += ball.vy

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            p2.y -= p2.spd
          if event.key == pygame.K_DOWN:
            p2.y += p2.spd
          if event.key == pygame.K_w:
            p1.y -= p1.spd
          if event.key == pygame.K_s:
            p1.y += p1.spd
      # Render
      gameDisplay.fill(black)
      gameDisplay.blit(p1.img, (p1.x, p1.y))
      gameDisplay.blit(p2.img, (p2.x, p2.y))
      gameDisplay.blit(ball.img, (ball.x, ball.y))
      pygame.display.flip()

    pygame.display.update()
    clock.tick(60)

  pygame.quit()
  quit()

if __name__ == "__main__":
  main()