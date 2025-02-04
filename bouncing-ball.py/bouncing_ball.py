import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Physics constants
GRAVITY = 0.5
FRICTION = 0.8
RESTITUTION = 0.7
ROTATION_SPEED = 0.02

class Ball:
    def __init__(self, x, y, radius):
        self.pos = np.array([float(x), float(y)])
        self.vel = np.array([0.0, 0.0])
        self.radius = radius
        
    def update(self):
        # Apply gravity
        self.vel[1] += GRAVITY
        
        # Update position
        self.pos += self.vel
        
    def draw(self, screen):
        pygame.draw.circle(screen, RED, self.pos.astype(int), self.radius)

class Hexagon:
    def __init__(self, center_x, center_y, radius):
        self.center = np.array([center_x, center_y])
        self.radius = radius
        self.angle = 0
        self.points = self.calculate_points()
        
    def calculate_points(self):
        points = []
        for i in range(6):
            angle = self.angle + i * math.pi / 3
            x = self.center[0] + self.radius * math.cos(angle)
            y = self.center[1] + self.radius * math.sin(angle)
            points.append(np.array([x, y]))
        return points
    
    def rotate(self):
        self.angle += ROTATION_SPEED
        self.points = self.calculate_points()
    
    def draw(self, screen):
        points = [(int(p[0]), int(p[1])) for p in self.points]
        pygame.draw.polygon(screen, WHITE, points, 2)

def check_collision(ball, hexagon):
    for i in range(6):
        p1 = hexagon.points[i]
        p2 = hexagon.points[(i + 1) % 6]
        
        # Calculate wall vector and normal
        wall_vector = p2 - p1
        wall_normal = np.array([-wall_vector[1], wall_vector[0]])
        wall_normal = wall_normal / np.linalg.norm(wall_normal)
        
        # Calculate distance from ball to line segment
        ball_to_p1 = ball.pos - p1
        proj_length = np.dot(ball_to_p1, wall_vector) / np.dot(wall_vector, wall_vector)
        
        if 0 <= proj_length <= 1:
            distance = abs(np.dot(ball_to_p1, wall_normal))
            if distance < ball.radius:
                # Collision response
                penetration = ball.radius - distance
                ball.pos += wall_normal * penetration
                
                # Calculate relative velocity
                relative_velocity = ball.vel
                
                # Calculate impulse
                velocity_along_normal = np.dot(relative_velocity, wall_normal)
                
                if velocity_along_normal < 0:
                    # Apply restitution and friction
                    impulse = -velocity_along_normal * (1 + RESTITUTION)
                    ball.vel += wall_normal * impulse
                    
                    # Apply friction
                    tangent = np.array([wall_normal[1], -wall_normal[0]])
                    velocity_along_tangent = np.dot(ball.vel, tangent)
                    ball.vel -= tangent * velocity_along_tangent * (1 - FRICTION)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball in Rotating Hexagon")
    clock = pygame.time.Clock()
    
    # Create objects
    ball = Ball(WIDTH//2, HEIGHT//2, 10)
    hexagon = Hexagon(WIDTH//2, HEIGHT//2, 200)
    
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Reset ball position and give it random velocity
                ball.pos = np.array([float(WIDTH//2), float(HEIGHT//2)])
                ball.vel = np.array([np.random.uniform(-10, 10), np.random.uniform(-10, 10)])
        
        # Update
        hexagon.rotate()
        ball.update()
        check_collision(ball, hexagon)
        
        # Draw
        screen.fill(BLACK)
        hexagon.draw(screen)
        ball.draw(screen)
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()