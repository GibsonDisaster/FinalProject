import pygame

'''
    Ball splitting
    Ball becomes lazor shark
    Mouths
    Ladies
    Point system
    Acid
    Ball animation
    Fix logo
    Make good
'''

def flatten(lst):
  r = []

  for x in lst:
    r.append(x[0])
    r.append(x[1])

  return r

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

pygame.font.init()

# Load images
intro_logo = pygame.image.load("res/logo.png")

point_images = []
point_links = ["res/p0.png", "res/p1.png", "res/p2.png", "res/p3.png", "res/p4.png", "res/p5.png"]

for link in point_links:
  point_images.append(pygame.image.load(link))

test = []
image_links = ["res/mouth1.png", "res/mouth2.png", "res/mouth3.png", "res/mouth4.png", "res/mouth5.png"]

zipped_images = list(zip(image_links, image_links))

for link in flatten(zipped_images):
  test.append(pygame.image.load(link))

class Paddle:

  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.spd = 30
    self.vx = 10
    self.vy = (-10)
    self.width = w
    self.height = h
    self.v = 0
    self.pts = 0

class Ball:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.r = 15
    self.vx = 10
    self.vy = 10

class PowerUp:

  def __init__(self, x, y, effect, direct, spd):
    self.x = x
    self.y = y
    self.effect = effect
    self.dir = direct
    self.spd = spd

def main():
  pygame.init()
  gameDisplay = pygame.display.set_mode((1280, 720))
  pygame.display.set_caption("Pong On Acid")
  clock = pygame.time.Clock()

  p1 = Paddle(100, 0, 50, 300)
  p2 = Paddle(1180, 0, 50, 300)
  ball = Ball(300, 400)

  counter = 0

  point1 = 0
  point2 = 0

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

      # Collide with screen edges
      if (ball.x + ball.vx >= 1280):
        point1 += 1
        ball.x = 600
      else:
        ball.x += ball.vx

      if (ball.x + ball.vx <= 0):
        point2 += 1
        ball.x = 600
      else:
        ball.x += ball.vx

      if (ball.y + ball.vy >= 720 or ball.y + ball.vy <= 0):
        ball.vy *= (-1)
      else:
        ball.y += ball.vy

      # Collide with p1
      if (ball.x + ball.vx <= p1.x + p1.width and ball.y >= p1.y and ball.y <= p1.y + p1.height):
        ball.vx *= (-1)
      # Collide with p2
      if (ball.x + ball.vx >= p2.x and ball.y >= p2.y and ball.y <= p2.y + p2.height):
        ball.vx *= (-1)

      # Getting events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            p2.v = (-10)
          if event.key == pygame.K_DOWN:
            p2.v = 10
          if event.key == pygame.K_w:
            p1.v = (-10)
          else:
            p1.v = 0
          if event.key == pygame.K_s:
            p1.v = 10
          if event.key == pygame.K_ESCAPE:
            done = True
        elif event.type == pygame.KEYUP:
            p1.v = 0
            p2.v = 0

      p1.y += p1.v
      p2.y += p2.v

      # Render
      gameDisplay.fill(black)
      gameDisplay.blit(test[counter], (100, 100))
      gameDisplay.blit(point_images[point1], (100, 0))
      gameDisplay.blit(point_images[point2], (1180, 0))

      pygame.draw.rect(gameDisplay, white, (p1.x, p1.y, p1.width, p1.height), 3)
      pygame.draw.rect(gameDisplay, white, (p2.x, p2.y, p2.width, p2.height), 3)
      pygame.draw.circle(gameDisplay, white, (ball.x, ball.y), ball.r, 3)
      
      pygame.display.flip()

      if counter == len(test) - 1:
        counter = 0
      else:
        counter += 1

    pygame.display.update()
    clock.tick(60)

  pygame.quit()
  quit()

if __name__ == "__main__":
  main()
