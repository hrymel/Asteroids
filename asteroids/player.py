import pygame
from circleshape import CircleShape
import constants
from shot import Shot

class Player(CircleShape):

	def __init__(self, x, y):
		super().__init__(x, y, constants.PLAYER_RADIUS)
		self.rotation = 0
		self.timer = 0
		self.player_hit_timer = 0

	def draw(self, screen):
		if self.player_hit_timer <= 0:
			pygame.draw.polygon(screen, "white", self.triangle(), 2)
		if self.player_hit_timer > 0:
			pygame.draw.polygon(screen, "green", self.triangle(), 2)

	# in the player class
	def triangle(self):
	    forward = pygame.Vector2(0, 1).rotate(self.rotation)
	    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
	    a = self.position + forward * self.radius
	    b = self.position - forward * self.radius - right
	    c = self.position - forward * self.radius + right
	    return [a, b, c]

	def rotate(self, dt):
		self.rotation += constants.PLAYER_TURN_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

		if self.timer >= 0:
			self.timer -= dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * constants.PLAYER_SPEED * dt

	def shoot(self):
		
		if self.timer <= 0:
			shot = Shot(self.position.x, self.position.y)
			shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
			self.timer = constants.PLAYER_SHOOT_COOLDOWN