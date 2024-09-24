import pygame
import sys
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
class SnakeGame:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(None, 24)
        self.snake_pos = [(200, 100), (220, 100), (240, 100)]
        self.direction = "right"
        self.score = 0
        self.food_pos = (400, 300)
    def draw_text(self, text):
        return self.font.render(text, True, (255, 255, 255))

    def draw_snake(self):
        for pos in self.snake_pos:
            pygame.draw.rect(self.display_surface, SNAKE_COLOR,
                              pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    def draw_food(self):
        pygame.draw.rect(self.display_surface, FOOD_COLOR,
                          pygame.Rect(self.food_pos[0], self.food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    def update_snake_pos(self):
        head = self.snake_pos[-1]
        if self.direction == "right":
            new_head = (head[0] + BLOCK_SIZE, head[1])
        elif self.direction == "left":
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == "up":
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == "down":
            new_head = (head[0], head[1] + BLOCK_SIZE)

        if (new_head in self.snake_pos[:-1] or
                new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
                new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
            return False
        self.snake_pos.append(new_head)
        return True
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != "down":
                    self.direction = "up"
                elif event.key == pygame.K_DOWN and self.direction != "up":
                    self.direction = "down"
                elif event.key == pygame.K_LEFT and self.direction != "right":
                    self.direction = "left"
                elif event.key == pygame.K_RIGHT and self.direction != "left":
                    self.direction = "right"
    def main_loop(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            if random.random() < 0.05:
                new_food_pos = (random.randint(0, SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                                random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
                self.food_pos = new_food_pos
            if self.update_snake_pos():
                self.score += 1
                self.snake_pos.pop(0)  
            else:
                text = self.draw_text(f"Game Over! Final score: {self.score}")
                text_rect = text.get_rect()
                text_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                self.display_surface.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(2000)  
                return
            self.display_surface.fill((0, 0, 0)) 
            self.draw_snake()
            self.draw_food()
            score_text = self.draw_text(f"Score: {self.score}")
            score_rect = score_text.get_rect()
            score_rect.midtop = (10, 10)
            self.display_surface.blit(score_text, score_rect)

            pygame.display.flip()
            clock.tick(10)
game = SnakeGame()
while True:
    game.main_loop()