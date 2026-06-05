import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("極限連發射擊遊戲")
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

player_pos = [600, 700]
player_speed = 10 # 預設速度
bullets = []
drops = []
powerups = [] # {'rect': rect, 'type': 'double' or 'quintuple' or 'speed'}
explosions = []
score = 0
paused = False
power_level = 0 # 0:無, 1:雙排, 2:五排
power_up_end_time = 0
speed_up_end_time = 0
last_shot_time = 0
last_drop_time = 0
last_powerup_time = 0
fire_rate = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            paused = not paused

    if not paused:
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        
        # 移動速度控制
        if current_time > speed_up_end_time:
            player_speed = 10
        
        # 玩家移動
        if keys[pygame.K_a] and player_pos[0] > 0: player_pos[0] -= player_speed
        if keys[pygame.K_d] and player_pos[0] < WIDTH - 30: player_pos[0] += player_speed
        if keys[pygame.K_w] and player_pos[1] > 0: player_pos[1] -= player_speed
        if keys[pygame.K_s] and player_pos[1] < HEIGHT - 30: player_pos[1] += player_speed

        # 強力狀態結束檢查
        if power_level > 0 and current_time > power_up_end_time:
            power_level = 0

        # 發射邏輯
        if keys[pygame.K_SPACE] and current_time - last_shot_time > fire_rate:
            if power_level == 2:
                for i in range(-2, 3):
                    bullets.append(pygame.Rect(player_pos[0] + i * 15, player_pos[1], 10, 10))
            elif power_level == 1:
                bullets.append(pygame.Rect(player_pos[0], player_pos[1], 10, 10))
                bullets.append(pygame.Rect(player_pos[0] + 20, player_pos[1], 10, 10))
            else:
                bullets.append(pygame.Rect(player_pos[0] + 10, player_pos[1], 10, 10))
            last_shot_time = current_time

        # 生成寶石
        if current_time - last_powerup_time > 4000:
            ptype = random.choice(['double', 'quintuple', 'speed'])
            powerups.append({'rect': pygame.Rect(random.randint(0, WIDTH-30), 0, 30, 30), 'type': ptype})
            last_powerup_time = current_time
        
        # 掉落物
        if current_time - last_drop_time > 600:
            color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            drops.append({'rect': pygame.Rect(random.randint(0, WIDTH-40), 0, 40, 40), 'color': color, 'type': random.choice(['rect', 'circle'])})
            last_drop_time = current_time

        for b in bullets: b.y -= 15
        for d in drops: d['rect'].y += 4
        for p in powerups: p['rect'].y += 3
        
        player_rect = pygame.Rect(*player_pos, 30, 30)
        for p in powerups[:]:
            if player_rect.colliderect(p['rect']):
                if p['type'] == 'speed':
                    player_speed = 18
                    speed_up_end_time = current_time + 5000
                else:
                    power_level = 2 if p['type'] == 'quintuple' else 1
                    power_up_end_time = current_time + 5000
                powerups.remove(p)
        
        bullets_to_remove, drops_to_remove = [], []
        for b in bullets:
            for d in drops:
                if b.colliderect(d['rect']):
                    bullets_to_remove.append(b)
                    drops_to_remove.append(d)
                    score += 1
                    for _ in range(8):
                        explosions.append({'pos': list(d['rect'].center), 'vel': [random.uniform(-3, 3), random.uniform(-3, 3)], 'life': 20})
        
        bullets = [b for b in bullets if b not in bullets_to_remove and b.y > 0]
        drops = [d for d in drops if d not in drops_to_remove and d['rect'].y < HEIGHT]
        for e in explosions[:]:
            e['pos'][0] += e['vel'][0]; e['pos'][1] += e['vel'][1]; e['life'] -= 1
            if e['life'] <= 0: explosions.remove(e)

    # 繪圖
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (200, 200, 200), (*player_pos, 30, 30))
    for b in bullets: pygame.draw.rect(screen, (255, 255, 0), b)
    for d in drops:
        if d['type'] == 'rect': pygame.draw.rect(screen, d['color'], d['rect'])
        else: pygame.draw.circle(screen, d['color'], d['rect'].center, 20)
    
    # 寶石閃爍效果
    for p in powerups:
        if p['type'] == 'double' and (current_time // 200) % 2 == 0:
            pygame.draw.circle(screen, (255, 255, 255), p['rect'].center, 15)
        elif p['type'] == 'quintuple' and (current_time // 100) % 2 == 0:
            pygame.draw.circle(screen, (255, 0, 0), p['rect'].center, 15)
        elif p['type'] == 'speed' and (current_time // 200) % 2 == 0:
            pygame.draw.circle(screen, (255, 255, 0), p['rect'].center, 15)

    for e in explosions: pygame.draw.circle(screen, (255, 100, 0), [int(x) for x in e['pos']], 3)
    
    status = "Normal"
    if power_level == 1: status = "Double Shot!"
    if power_level == 2: status = "Quintuple Shot!"
    if player_speed > 10: status += " + SPEED UP!"
    screen.blit(font.render(f"Score: {score} | {status}", True, (255, 255, 255)), (20, 20))
    if paused: screen.blit(font.render("PAUSED", True, (255, 255, 255)), (WIDTH//2 - 70, HEIGHT//2 - 20))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()