import pygame
import random
import time
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Ride To Hell")

BG = pygame.transform.scale(pygame.image.load("hell.jpg"), (WIDTH, HEIGHT))
BG_SCROLL_SPEED = 2

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 6

STAR_WIDTH = 10
STAR_HEIGHT = 20

FONT = pygame.font.SysFont("ComicSans", 30)

def draw(player, stars, elapsed_time, bg_y1, bg_y2, level):
    # Scrolling background
    WIN.blit(BG, (0, bg_y1))
    WIN.blit(BG, (0, bg_y2))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    level_text = FONT.render(f"Level: {level}", 1, "white")
    WIN.blit(time_text, (10, 10))
    WIN.blit(level_text, (10, 40))

    pygame.draw.rect(WIN, "grey", player)

    for star in stars:
        pygame.draw.rect(WIN, "red", star)

    pygame.display.update()

def level_popup(message):
    popup = FONT.render(message, 1, "white")
    WIN.blit(popup, (WIDTH/2 - popup.get_width()/2, HEIGHT/2 - popup.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    run = True
    clock = pygame.time.Clock()

    player = pygame.Rect(WIDTH//2 - PLAYER_WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    bg_y1 = 0
    bg_y2 = -HEIGHT

    start_time = time.time()
    elapsed_time = 0

    stars = []

    level = 1
    level_duration = 20  
    star_add_increment = 2000
    star_count = 0
    STAR_VEL = 3

    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        
        bg_y1 += BG_SCROLL_SPEED
        bg_y2 += BG_SCROLL_SPEED
        if bg_y1 >= HEIGHT:
            bg_y1 = -HEIGHT
        if bg_y2 >= HEIGHT:
            bg_y2 = -HEIGHT

        
        if star_count > star_add_increment:
            for _ in range(level):  # more stars with higher level
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(500, star_add_increment - 20 * level)
            star_count = 0

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL

        
        for star in stars[:]:
            star.y += STAR_VEL + level  
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.colliderect(player):
                hit = True
                break

        
        if hit:
            lost_text = FONT.render("You Lost! Press R to Restart or Q to Quit", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()

            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:  # restart
                            main()
                            return
                        if event.key == pygame.K_q:  # quit
                            waiting = False
                            run = False
            break

        
        if elapsed_time > level * level_duration:
            level_popup(f"Level {level} Cleared!")
            level += 1
            
            stars.clear()

        
        draw(player, stars, elapsed_time, bg_y1, bg_y2, level)

    pygame.quit()

if __name__ == "__main__":
    main()
