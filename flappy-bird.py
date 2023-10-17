import pygame

pygame.init()

# Gaming window
screen_width = 770
screen_height = 350
game_window = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
orange = (255, 140, 0)

# Start page
start = pygame.image.load("f.jpg")
start = pygame.transform.scale(start, (screen_width, screen_height)).convert()

# Font
font = pygame.font.SysFont(None, 55)

# Game Title
pygame.display.set_caption("Chidiya ki uddan")

# Clock
clock = pygame.time.Clock()

def text_screen(text, color, x, y, font):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, (x, y))

# Bird properties
bird_x = 100
bird_y = 150
init_velocity = 0
gravity = 0.5
jump = False
jump_up = 10

# Bird image
bird_width = 60
bird_height = 40
b_img = pygame.image.load("bird.png")
b_img = pygame.transform.scale(b_img, (bird_width, bird_height))

# Background Image
bg_img = pygame.image.load("bg.jpg")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()
bg_x = 0

# Font
font = pygame.font.Font("Happy-Dance.ttf", 40)

# Starting Page
def starting_window():
    exit_game = False
    while not exit_game:
        
        game_window.blit(start, (0, 0))
        text_screen("Press Enter to play the game", orange, 100, 220, font)
      

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    global jump, bird_y, init_velocity, bg_x  # Declare variables as global
    game_over = False
    exit_game = False

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        jump = True

        init_velocity += gravity
        bird_y += init_velocity

        if bird_y > screen_height:
            game_over = True

        if jump:
            bird_y -= jump_up
            jump = False

        if bird_y < 0:
            bird_y = 0
            init_velocity = 0

        bg_x -= 5

        if bg_x < -bird_width:
            bg_x = 0

        game_window.blit(bg_img, (bg_x, 0))
        game_window.blit(b_img, (bird_x, bird_y))
        pygame.display.update()
        clock.tick(30)


starting_window()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
