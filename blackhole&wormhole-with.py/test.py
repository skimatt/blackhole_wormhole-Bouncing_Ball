import pygame
import math
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole and Wormhole Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Black hole and wormhole parameters
BLACK_HOLE_POS = (WIDTH // 4, HEIGHT // 2)
WORMHOLE_POS = (3 * WIDTH // 4, HEIGHT // 2)
BLACK_HOLE_RADIUS = 50
WORMHOLE_RADIUS = 30
GRAVITY_STRENGTH = 0.5
SPEED_BOOST = 1.5

# Ball parameters
BALL_RADIUS = 10
NUM_BALLS = 50
FRICTION = 0.99

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.color = random.choice([RED, BLUE, GREEN])

    def update(self):
        # Apply gravity towards the black hole
        dx = BLACK_HOLE_POS[0] - self.x
        dy = BLACK_HOLE_POS[1] - self.y
        distance = math.hypot(dx, dy)
        if distance > 0:
            force = GRAVITY_STRENGTH / max(distance, 1)  # Avoid division by zero
            self.vx += force * dx / distance
            self.vy += force * dy / distance

        # Update position
        self.x += self.vx
        self.y += self.vy

        # Apply friction
        self.vx *= FRICTION
        self.vy *= FRICTION

    def check_black_hole(self):
        # Check if the ball is inside the black hole
        dx = self.x - BLACK_HOLE_POS[0]
        dy = self.y - BLACK_HOLE_POS[1]
        distance = math.hypot(dx, dy)
        if distance < BLACK_HOLE_RADIUS:
            # Teleport to wormhole with increased speed
            self.x = WORMHOLE_POS[0]
            self.y = WORMHOLE_POS[1]
            self.vx *= SPEED_BOOST
            self.vy *= SPEED_BOOST

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), BALL_RADIUS)

def create_balls():
    balls = []
    for _ in range(NUM_BALLS):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        balls.append(Ball(x, y))
    return balls

def main():
    balls = create_balls()

    while True:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update and draw balls
        for ball in balls:
            ball.update()
            ball.check_black_hole()
            ball.draw(screen)

        # Draw black hole
        pygame.draw.circle(screen, WHITE, BLACK_HOLE_POS, BLACK_HOLE_RADIUS, 2)

        # Draw wormhole
        pygame.draw.circle(screen, GREEN, WORMHOLE_POS, WORMHOLE_RADIUS, 2)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()