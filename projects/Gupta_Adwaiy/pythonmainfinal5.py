import pygame
import random
import time
pygame.font.init()

# Window setup
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A Ride To Hell")

# Background
BG = pygame.transform.scale(pygame.image.load("hell.jpg"), (WIDTH, HEIGHT))
BG_SCROLL_SPEED = 2

# Player setup
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 6

# Star (projectile) setup
STAR_WIDTH = 10
STAR_HEIGHT = 20

# Powerups setup
POWERUP_WIDTH = 20
POWERUP_HEIGHT = 20
POWERUP_VEL = 3
POWERUP_TYPES = ["freeze", "speed", "shield"]

# Fonts (scary look)
FONT = pygame.font.SysFont("chiller", 40, bold=True)

# Track highest level
highest_level = 1

# Custom rectangle sprites
def create_sprite(width, height, color, border_color=(0,0,0)):
    surf = pygame.Surface((width, height))
    surf.fill(border_color)
    inner = pygame.Surface((width-4, height-4))
    inner.fill(color)
    surf.blit(inner, (2,2))
    return surf

PLAYER_SPRITE = create_sprite(PLAYER_WIDTH, PLAYER_HEIGHT, (100,100,100), (200,0,0))  # grey w/ red border
STAR_SPRITE = create_sprite(STAR_WIDTH, STAR_HEIGHT, (200,0,0), (50,0,0))             # red w/ dark border
FREEZE_SPRITE = create_sprite(POWERUP_WIDTH, POWERUP_HEIGHT, (0,200,255))
SPEED_SPRITE = create_sprite(POWERUP_WIDTH, POWERUP_HEIGHT, (0,255,0))
SHIELD_SPRITE = create_sprite(POWERUP_WIDTH, POWERUP_HEIGHT, (255,255,0))

def draw(player, stars, powerups, elapsed_time, bg_y1, bg_y2, level, shield_active):
    # Scrolling background
    WIN.blit(BG, (0, bg_y1))
    WIN.blit(BG, (0, bg_y2))

    # HUD
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    level_text = FONT.render(f"Level: {level}", 1, "red")
    highest_text = FONT.render(f"Highest: {highest_level}", 1, "white")
    WIN.blit(time_text, (10, 10))
    WIN.blit(level_text, (10, 50))
    WIN.blit(highest_text, (10, 90))

    # Player
    WIN.blit(PLAYER_SPRITE, (player.x, player.y))

    # Stars
    for star in stars:
        WIN.blit(STAR_SPRITE, (star.x, star.y))

    # Powerups
    for pu in powerups:
        if pu["type"] == "freeze":
            WIN.blit(FREEZE_SPRITE, (pu["rect"].x, pu["rect"].y))
        elif pu["type"] == "speed":
            WIN.blit(SPEED_SPRITE, (pu["rect"].x, pu["rect"].y))
        elif pu["type"] == "shield":
            WIN.blit(SHIELD_SPRITE, (pu["rect"].x, pu["rect"].y))

    # Shield indicator
    if shield_active:
        shield_text = FONT.render("SHIELD!", 1, "yellow")
        WIN.blit(shield_text, (WIDTH - 200, 10))

    pygame.display.update()

def level_popup(message):
    popup = FONT.render(message, 1, "white")
    WIN.blit(popup, (WIDTH/2 - popup.get_width()/2, HEIGHT/2 - popup.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    global highest_level
    run = True
    clock = pygame.time.Clock()

    # Player
    player = pygame.Rect(WIDTH//2 - PLAYER_WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    # Background scrolling vars
    bg_y1 = 0
    bg_y2 = -HEIGHT

    # Time
    start_time = time.time()
    elapsed_time = 0

    # Stars and powerups
    stars = []
    powerups = []

    # Difficulty / levels
    level = 1
    level_duration = 20  # seconds per level
    star_add_increment = 2000
    star_count = 0
    STAR_VEL = 3

    # Powerup effects
    freeze_active = False
    freeze_timer = 0
    speed_active = False
    speed_timer = 0
    shield_active = False

    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        # Background movement
        bg_y1 += BG_SCROLL_SPEED
        bg_y2 += BG_SCROLL_SPEED
        if bg_y1 >= HEIGHT:
            bg_y1 = -HEIGHT
        if bg_y2 >= HEIGHT:
            bg_y2 = -HEIGHT

        # Add stars
        if star_count > star_add_increment:
            for _ in range(level):  # more stars with higher level
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            # Chance to spawn powerup
            if random.random() < 0.2:
                pu_type = random.choice(POWERUP_TYPES)
                pu_x = random.randint(0, WIDTH - POWERUP_WIDTH)
                pu = {"rect": pygame.Rect(pu_x, -POWERUP_HEIGHT, POWERUP_WIDTH, POWERUP_HEIGHT),
                      "type": pu_type}
                powerups.append(pu)

            star_add_increment = max(500, star_add_increment - 20 * level)
            star_count = 0

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        current_vel = PLAYER_VEL * (2 if speed_active else 1)

        if keys[pygame.K_a] and player.x - current_vel >= 0:
            player.x -= current_vel
        if keys[pygame.K_d] and player.x + current_vel + PLAYER_WIDTH <= WIDTH:
            player.x += current_vel

        # Move stars
        for star in stars[:]:
            if not freeze_active:
                star.y += STAR_VEL + level  # difficulty scaling with level
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.colliderect(player):
                if shield_active:
                    stars.remove(star)
                    shield_active = False
                else:
                    hit = True
                    break

        # Move powerups
        for pu in powerups[:]:
            pu["rect"].y += POWERUP_VEL
            if pu["rect"].y > HEIGHT:
                powerups.remove(pu)
            elif pu["rect"].colliderect(player):
                if pu["type"] == "freeze":
                    freeze_active = True
                    freeze_timer = pygame.time.get_ticks()
                elif pu["type"] == "speed":
                    speed_active = True
                    speed_timer = pygame.time.get_ticks()
                elif pu["type"] == "shield":
                    shield_active = True
                powerups.remove(pu)

        # Handle powerup timers
        if freeze_active and pygame.time.get_ticks() - freeze_timer > 5000:
            freeze_active = False
        if speed_active and pygame.time.get_ticks() - speed_timer > 5000:
            speed_active = False

        # If player hit
        if hit:
            if level > highest_level:
                highest_level = level
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

        # Level progression
        if elapsed_time > level * level_duration:
            level_popup(f"Level {level} Cleared!")
            level += 1
            if level > highest_level:
                highest_level = level
            stars.clear()
            powerups.clear()

        # Draw everything
        draw(player, stars, powerups, elapsed_time, bg_y1, bg_y2, level, shield_active)

    pygame.quit()

if __name__ == "__main__":
    main()
