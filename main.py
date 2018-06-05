import pygame
import random
import itertools
from math import (sin, tan, hypot)

'''
    Ball splitting
    Ball becomes lazor shark
    Mouths
    Ladies
  X Point system
    Acid
  X Ball animation (explosion when bouncing)
  X Fix logo
    Make good
'''

'''
    Effect Ideas:
    1) Split Ball
    2) Fast balls
    3) slow balls
    4) target line for where balls are heading?
    5) double points
    6) mouth eats a ball
    7) lazer to kill other player
'''

def flatten(lst):
  r = []

  for x in lst:
    r.append(x[0])
    r.append(x[1])

  return r

def get_sprite(name):
  return {
    'split': pygame.image.load("res/split.png"),
    'fast': pygame.image.load("res/fast.png"),
    'slow': pygame.image.load("res/slow.png"),
    'target': pygame.image.load("res/target.png"),
    'double': pygame.image.load("res/double.png"),
    'mouth': pygame.image.load("res/mouth_effect.png"),
    'laser': pygame.image.load("res/laser.png")
  }.get(name, pygame.image.load("res/power_up_error.png"))

def ball_colliding(b, p):
  if (hypot(p.x - b.x, p.y - b.y) < b.r + 30):
    return True
  else:
    return False

display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)

# Load animations

explosion_animation_frames = []
explosion_links = ["res/explosion1.png", "res/explosion2.png", "res/explosion3.png", "res/explosion4.png", "res/explosion5.png", "res/explosion6.png"]

for link in explosion_links:
  explosion_animation_frames.append(pygame.image.load(link))

mouth_animation_frames = []
mouth_links = ["res/mouth1.png", "res/mouth2.png", "res/mouth3.png", "res/mouth4.png", "res/mouth5.png", "res/mouth5.png"]

for link in mouth_links:
  mouth_animation_frames.append(pygame.image.load(link))

laser_animation_frames = []
laser_links = ["res/laser1.png", "res/laser2.png", "res/laser3.png", "res/laser4.png", "res/laser5.png", "res/laser6.png"]

for link in laser_links:
  laser_animation_frames.append(pygame.image.load(link))

# Load images
intro_logo = pygame.image.load("res/logo.png")

background_image = pygame.image.load("res/background.png")

point_images = []
point_links = ["res/p0.png", "res/p1.png", "res/p2.png", "res/p3.png", "res/p4.png", "res/p5.png"]

for link in point_links:
  point_images.append(pygame.image.load(link))

# Classes

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

  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.r = 15
    self.vx = vx
    self.vy = vy

class PowerUp:

  def __init__(self, x, y, effect, direct):
    self.x = x
    self.y = y
    self.effect = effect
    self.dir = direct
    self.used = False

  def move(self):
    self.x += self.dir[0]
    self.y += self.dir[1]

class Anim:

  def __init__(self, x, y, dur, frames):
    self.x = x
    self.y = y
    self.dur = dur
    self.counter = 0
    self.current_frame = 0
    self.frames = frames
    self.showing = True

def main():
  pygame.init()
  gameDisplay = pygame.display.set_mode((display_width, display_height))
  pygame.display.set_caption("Pong On Acid")
  clock = pygame.time.Clock()

  p1 = Paddle(100, 0, 50, 300)
  p2 = Paddle(display_width - 100, 0, 50, 300)

  # init animations

  sin_x = 0

  current_animations = []

  explosion_animations = []
  mouth_animations = []
  laser_animations = []

  six_frame_count = 0

  power_up_chance = 99

  point1 = 0
  point2 = 0

  done = False
  show_logo = True
  play_game = False

  all_power_ups = [PowerUp(random.randint(200, 1080), random.randint(100, 620), "split", (1, 0)), PowerUp(random.randint(200, 1080), random.randint(100, 620), "fast", (1, 0)), PowerUp(random.randint(200, 1080), random.randint(100, 620), "slow", (1, 0)), PowerUp(random.randint(200, 1080), random.randint(100, 620), "target", (1, 0)), PowerUp(random.randint(200, 1080), random.randint(100, 620), "double", (1, 0)), PowerUp(random.randint(200, 1080), random.randint(100, 620), "mouth", (1, 0)), PowerUp(random.randint(200, 1080), random.randint(100, 620), "laser", (1, 0))]
  power_ups = []
  current_power_ups = []

  balls = [Ball(int(display_width / 2), int(display_height / 2), -(int(0.0078125 * display_width)), int(display_height * 0.013888))]

  while not done:

    if show_logo:
      # Update
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        elif event.type == pygame.KEYDOWN:
          show_logo = False
          play_game = True

      if sin_x == 1:
        sin_x = 0
      else:
        sin_x += 0.05

      # Render
      gameDisplay.fill(black)
      gameDisplay.blit(intro_logo, (400 + sin(sin_x) * 200, 400 + tan(sin_x) * 200))
      pygame.display.flip()

    elif play_game:
      # Update

      # Check to spawn powerups

      if random.choice([False] * power_up_chance + [True]) == True:
        power_ups.append(random.choice(all_power_ups))

      # Collide with screen edges
      for ball in balls:
        if (ball.x + ball.vx >= display_width):
          point1 += 1
          ball.x = 600
        else:
          ball.x += ball.vx

        if (ball.x + ball.vx <= 0):
          point2 += 1
          ball.x = 600
        else:
          ball.x += ball.vx

        if (ball.y + ball.vy >= display_height or ball.y + ball.vy <= 0):
          ball.vy *= (-1)
        else:
          ball.y += ball.vy

        # Collide with p1
        if (ball.x + ball.vx <= p1.x + p1.width and ball.y >= p1.y and ball.y <= p1.y + p1.height):
          ball.vx *= (-1)
          current_animations.append(Anim(ball.x, ball.y, len(explosion_animation_frames) - 1, explosion_animation_frames))
        # Collide with p2
        if (ball.x + ball.vx >= p2.x and ball.y >= p2.y and ball.y <= p2.y + p2.height):
          ball.vx *= (-1)
          current_animations.append(Anim(ball.x, ball.y, len(explosion_animation_frames) - 1, explosion_animation_frames))

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
      
      #gameDisplay.blit(point_images[point1], (100, 0))
      #gameDisplay.blit(point_images[point2], (display_width - 100, 0))

      for anim in current_animations:
        if anim.showing:
          gameDisplay.blit(anim.frames[anim.current_frame], (anim.x, anim.y))
        if (anim.current_frame == anim.dur):
          anim.showing = False
        else:
          anim.current_frame += 1

      itertools.filterfalse(lambda x: not x.showing, current_animations)

      for ball in balls:
        for power in power_ups:
          if (ball_colliding(ball, power) and not power.used):
            power.used = True
            current_power_ups.append(power.effect)

      for effect in current_power_ups:
        if effect == 'split':
          balls.append(Ball(balls[len(balls)-1].x, balls[len(balls)-1].y, balls[len(balls)-1].vx, -(balls[len(balls)-1].x)))
          current_power_ups.remove(effect)

      # Apply current effects
      for power in power_ups:
        if not power.used:
          gameDisplay.blit(get_sprite(power.effect), (power.x, power.y))

      pygame.draw.rect(gameDisplay, white, (p1.x, p1.y, p1.width, p1.height), 3)
      pygame.draw.rect(gameDisplay, white, (p2.x, p2.y, p2.width, p2.height), 3)
      
      for ball in balls:
        pygame.draw.circle(gameDisplay, white, (ball.x, ball.y), ball.r, 3)
      
      pygame.display.flip()

      if six_frame_count == 6:
        six_frame_count = 0
      else:
        six_frame_count += 1

    print(len(balls))
    pygame.display.update()
    clock.tick(60)

  pygame.quit()
  quit()

if __name__ == "__main__":
  main()
