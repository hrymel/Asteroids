import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    pygame.font.init()
    score = 0
    score_increment = 10
    player_lives = 5
    
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        # setting up the font object
        font = pygame.font.Font(None, 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # reduce hit timer for invulnerability period
        player.player_hit_timer -= dt 

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.doesCollide(shot):
                    asteroid.split()
                    asteroid.kill()
                    shot.kill()
                    score += score_increment

            if player.doesCollide(asteroid):
                if player.player_hit_timer <= 0:
                    player_lives-= 1
                    player.player_hit_timer = 2
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

            if player_lives == 0:
                sys.exit(f"Game over! Your score was {score}")
                return

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # Draw the score to the screen
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        # draw player lives to screen
        player_lives_text = font.render(f'Lives: {player_lives}', True, (255, 255, 255))
        screen.blit(player_lives_text, (10, 35))

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
