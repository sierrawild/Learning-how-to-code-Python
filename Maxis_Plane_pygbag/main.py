import pygame
import asyncio
import clouds
import random
import os
from coin import CoinStreak
from bird import ObstacleManager
from sound_manager import SoundManager

# pygame setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.joystick.init()

# Initialize controller
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controller connected: {joystick.get_name()}")
else:
    print("No controller detected, using keyboard only")

screen = pygame.display.set_mode((0, 0))
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Max's Plane")
clock = pygame.time.Clock()
delta_time = 0

# CONSTANTS
TILT_PLANE_BY = 20
TILT_SPEED = 25
LANE_SWITCH_SPEED = 800

# Lane positions (top, middle, bottom)
LANES = [225, 450, 675]
current_lane = 1
target_lane = 1

tilt_angle = 0
target_tilt = 0

# player setup
BASE_DIR = os.path.dirname(__file__)
plane = pygame.image.load(os.path.join(BASE_DIR, "files", "max_plane_drawing.png")).convert_alpha()
plane.set_colorkey((255, 255, 255))
scale_by = 2.2
plane = pygame.transform.scale(plane, (plane.get_width() / scale_by,
                                       plane.get_height() / scale_by))
plane = pygame.transform.flip(plane, True, False)
plane_original = plane

plane_rec = plane.get_rect(center=screen.get_rect().center)
player_pos = pygame.Vector2(screen.get_width() // 4, LANES[current_lane])

# Create cloud manager
cloud_manager = clouds.CloudManager(1800, 900, num_clouds=8)

# Create sound manager
sound_manager = SoundManager()

# Track key presses
up_pressed = False
down_pressed = False

# Track controller button presses
dpad_up_pressed = False
dpad_down_pressed = False
leftstick_up_pressed = False
leftstick_down_pressed = False

# Touch control zones
TOUCH_ZONE_HEIGHT = screen.get_height() // 3
touch_zones = {
    'top': pygame.Rect(0, 0, screen.get_width(), TOUCH_ZONE_HEIGHT),
    'middle': pygame.Rect(0, TOUCH_ZONE_HEIGHT, screen.get_width(), TOUCH_ZONE_HEIGHT),
    'bottom': pygame.Rect(0, TOUCH_ZONE_HEIGHT * 2, screen.get_width(), TOUCH_ZONE_HEIGHT)
}

# Arrow button setup
ARROW_SIZE = 80
ARROW_MARGIN = 30
arrow_up_rect = pygame.Rect(
    screen.get_width() - ARROW_SIZE - ARROW_MARGIN,
    screen.get_height() - (ARROW_SIZE * 2) - ARROW_MARGIN - 20,
    ARROW_SIZE,
    ARROW_SIZE
)
arrow_down_rect = pygame.Rect(
    screen.get_width() - ARROW_SIZE - ARROW_MARGIN,
    screen.get_height() - ARROW_SIZE - ARROW_MARGIN,
    ARROW_SIZE,
    ARROW_SIZE
)

arrow_up_hover = False
arrow_down_hover = False

# Score
score = 0
coin_streaks = []

# Spawn one initial coin streak at game start
initial_lane = random.randint(0, 2)
coin_streaks.append(CoinStreak(LANES[initial_lane], screen.get_width() + 100))

# Spawn timer for coin streaks
coin_spawn_timer = 0
COIN_SPAWN_INTERVAL = random.uniform(3, 6)

# Track the last lane that had coins
last_coin_lane = initial_lane

# Obstacle manager
obstacle_manager = ObstacleManager(LANES)

# Game state
game_over = False
game_over_timer = 0

async def main():
    global running, delta_time, game_over, score, current_lane, target_lane
    global player_pos, coin_streaks, last_coin_lane, obstacle_manager
    global game_over_timer, coin_spawn_timer, COIN_SPAWN_INTERVAL
    global up_pressed, down_pressed, dpad_up_pressed, dpad_down_pressed
    global leftstick_up_pressed, leftstick_down_pressed
    global arrow_up_hover, arrow_down_hover, tilt_angle, target_tilt
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Only handle input if game is not over
            if not game_over:
                # Handle keyboard key press events
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and not up_pressed:
                        sound_manager.play_music()  # Start background music
                        up_pressed = True
                        if current_lane > 0:
                            current_lane -= 1
                            target_lane = current_lane
                            target_tilt = TILT_PLANE_BY
                            sound_manager.play_sound('whoosh')  # Play whoosh sound
                    
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and not down_pressed:
                        down_pressed = True
                        if current_lane < 2:
                            current_lane += 1
                            target_lane = current_lane
                            target_tilt = -TILT_PLANE_BY
                            sound_manager.play_sound('whoosh')  # Play whoosh sound
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        up_pressed = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        down_pressed = False
                
                # Handle Xbox controller events
                if joystick:
                    # D-pad events
                    if event.type == pygame.JOYHATMOTION:
                        hat = joystick.get_hat(0)
                        
                        # D-pad UP
                        if hat[1] == 1 and not dpad_up_pressed:
                            dpad_up_pressed = True
                            if current_lane > 0:
                                current_lane -= 1
                                target_lane = current_lane
                                target_tilt = TILT_PLANE_BY
                                sound_manager.play_sound('whoosh')
                        elif hat[1] != 1:
                            dpad_up_pressed = False
                        
                        # D-pad DOWN
                        if hat[1] == -1 and not dpad_down_pressed:
                            dpad_down_pressed = True
                            if current_lane < 2:
                                current_lane += 1
                                target_lane = current_lane
                                target_tilt = -TILT_PLANE_BY
                                sound_manager.play_sound('whoosh')
                        elif hat[1] != -1:
                            dpad_down_pressed = False
                    
                    # Left stick events
                    if event.type == pygame.JOYAXISMOTION and event.axis == 1:
                        if joystick.get_axis(1) < -0.5 and not leftstick_up_pressed:
                            leftstick_up_pressed = True
                            if current_lane > 0:
                                current_lane -= 1
                                target_lane = current_lane
                                target_tilt = TILT_PLANE_BY
                        elif joystick.get_axis(1) >= -0.5:
                            leftstick_up_pressed = False
                        
                        if joystick.get_axis(1) > 0.5 and not leftstick_down_pressed:
                            leftstick_down_pressed = True
                            if current_lane < 2:
                                current_lane += 1
                                target_lane = current_lane
                                target_tilt = -TILT_PLANE_BY
                        elif joystick.get_axis(1) <= 0.5:
                            leftstick_down_pressed = False
                    
                    # A and B buttons
                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:
                            if current_lane > 0:
                                current_lane -= 1
                                target_lane = current_lane
                                target_tilt = TILT_PLANE_BY
                                sound_manager.play_sound('whoosh')
                        
                        if event.button == 1:
                            if current_lane < 2:
                                current_lane += 1
                                target_lane = current_lane
                                target_tilt = -TILT_PLANE_BY
                                sound_manager.play_sound('whoosh')
                
                # Handle touchscreen events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    # Check if arrow buttons were clicked first
                    if arrow_up_rect.collidepoint(mouse_pos):
                        if current_lane > 0:
                            current_lane -= 1
                            target_lane = current_lane
                            target_tilt = TILT_PLANE_BY
                            sound_manager.play_sound('whoosh')
                    
                    elif arrow_down_rect.collidepoint(mouse_pos):
                        if current_lane < 2:
                            current_lane += 1
                            target_lane = current_lane
                            target_tilt = -TILT_PLANE_BY
                            sound_manager.play_sound('whoosh')
                    
                    # Touch zone controls
                    else:
                        if mouse_pos[0] < screen.get_width() * 0.85:
                            if touch_zones['top'].collidepoint(mouse_pos):
                                current_lane = 0
                                target_lane = 0
                                if player_pos.y > LANES[0]:
                                    target_tilt = TILT_PLANE_BY
                                    sound_manager.play_sound('whoosh')
                            
                            elif touch_zones['middle'].collidepoint(mouse_pos):
                                old_lane = current_lane
                                current_lane = 1
                                target_lane = 1
                                if old_lane < 1:
                                    target_tilt = -TILT_PLANE_BY
                                    sound_manager.play_sound('whoosh')
                                elif old_lane > 1:
                                    target_tilt = TILT_PLANE_BY
                                    sound_manager.play_sound('whoosh')
                            
                            elif touch_zones['bottom'].collidepoint(mouse_pos):
                                current_lane = 2
                                target_lane = 2
                                if player_pos.y < LANES[2]:
                                    target_tilt = -TILT_PLANE_BY
                                    sound_manager.play_sound('whoosh')
            
            # Restart game on space or click when game over
            if game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Reset game
                    game_over = False
                    score = 0
                    current_lane = 1
                    target_lane = 1
                    player_pos.y = LANES[1]
                    coin_streaks.clear()
                    
                    # Spawn one initial coin streak
                    initial_lane = random.randint(0, 2)
                    coin_streaks.append(CoinStreak(LANES[initial_lane], screen.get_width() + 100))
                    last_coin_lane = initial_lane
                    
                    obstacle_manager.obstacles.clear()
                    game_over_timer = 0
                    sound_manager.unpause_music()  # Resume music
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Reset game
                    game_over = False
                    score = 0
                    current_lane = 1
                    target_lane = 1
                    player_pos.y = LANES[1]
                    coin_streaks.clear()
                    
                    # Spawn one initial coin streak
                    initial_lane = random.randint(0, 2)
                    coin_streaks.append(CoinStreak(LANES[initial_lane], screen.get_width() + 100))
                    last_coin_lane = initial_lane
                    
                    obstacle_manager.obstacles.clear()
                    game_over_timer = 0
                    sound_manager.unpause_music()  # Resume music
        
        screen.fill("#94EAFF")
        
        if not game_over:
            # Check mouse hover for arrow buttons
            mouse_pos = pygame.mouse.get_pos()
            arrow_up_hover = arrow_up_rect.collidepoint(mouse_pos)
            arrow_down_hover = arrow_down_rect.collidepoint(mouse_pos)
        else:
            arrow_up_hover = False
            arrow_down_hover = False
            game_over_timer += delta_time
        
        # Only update game elements if not game over
        if not game_over:
            # Update coin spawn timer
            coin_spawn_timer += delta_time
            if coin_spawn_timer >= COIN_SPAWN_INTERVAL:
                coin_spawn_timer = 0
                COIN_SPAWN_INTERVAL = random.uniform(3, 6)
                
                # Only spawn if there are no active coin streaks visible on screen
                active_streaks = [s for s in coin_streaks if any(not c.is_off_screen() for c in s.coins)]
                
                if len(active_streaks) == 0:
                    # Spawn coins on a random lane (different from last time if possible)
                    available_lanes = [0, 1, 2]
                    if len(available_lanes) > 1 and last_coin_lane in available_lanes:
                        available_lanes.remove(last_coin_lane)
                    
                    random_lane_index = random.choice(available_lanes)
                    random_lane_y = LANES[random_lane_index]
                    coin_streaks.append(CoinStreak(random_lane_y))
                    last_coin_lane = random_lane_index
            
            # Get lanes currently occupied by coins
            occupied_lanes = set()
            for streak in coin_streaks:
                for coin in streak.coins:
                    if coin.x > screen.get_width() - 300 and not coin.collected:
                        for lane_index, lane_y in enumerate(LANES):
                            if abs(coin.y - lane_y) < 50:
                                occupied_lanes.add(lane_index)
                                break
            
            # Update obstacles with occupied lanes info
            obstacle_manager.update(delta_time, occupied_lanes)
            
            # Update coin streaks
            for streak in coin_streaks:
                streak.update(delta_time)
            
            # Remove completed streaks
            coin_streaks = [streak for streak in coin_streaks if not streak.is_complete()]
            
            # Update clouds
            cloud_manager.update(delta_time)
        
        # Move plane smoothly to target lane (only if not game over)
        if not game_over:
            target_y = LANES[target_lane]
            distance_to_target = abs(player_pos.y - target_y)
            
            if distance_to_target > 2:
                if player_pos.y < target_y:
                    player_pos.y += min(LANE_SWITCH_SPEED * delta_time, distance_to_target)
                else:
                    player_pos.y -= min(LANE_SWITCH_SPEED * delta_time, distance_to_target)
            else:
                player_pos.y = target_y
                target_tilt = 0
            
            # Tilting the plane
            tilt_angle += (target_tilt - tilt_angle) * TILT_SPEED * delta_time
        
        # Draw plane
        rotated_plane = pygame.transform.rotate(plane_original, tilt_angle)
        plane_rec = rotated_plane.get_rect(center=player_pos)
        
        # Draw clouds
        cloud_manager.draw(screen)
        
        # Draw obstacles
        obstacle_manager.draw(screen)
        
        # Draw coin streaks
        for streak in coin_streaks:
            streak.draw(screen)
        
        screen.blit(rotated_plane, plane_rec)
        
        # Check coin collisions
        if not game_over:
            for streak in coin_streaks:
                coins_collected = streak.check_collisions(plane_rec)
                if coins_collected > 0:
                    score += coins_collected
                    sound_manager.play_sound('coin')  # Play coin sound
            
            # Check obstacle collision
            if obstacle_manager.check_collision(plane_rec):
                game_over = True
                game_over_timer = 0
                sound_manager.play_sound('crash')  # Play crash sound
                sound_manager.pause_music()  # Pause music when game over
        
        # Draw arrow buttons
        def draw_arrow_button(rect, direction, is_hover):
            center = rect.center
            radius = ARROW_SIZE // 2
            
            bg_color = (255, 255, 255, 100) if is_hover else (255, 255, 255, 60)
            arrow_color = (100, 100, 100) if is_hover else (150, 150, 150)
            
            s = pygame.Surface((ARROW_SIZE, ARROW_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(s, bg_color, (radius, radius), radius)
            screen.blit(s, rect)
            
            if direction == "up":
                points = [
                    (center[0], center[1] - 20),
                    (center[0] - 18, center[1] + 15),
                    (center[0] + 18, center[1] + 15)
                ]
            else:
                points = [
                    (center[0], center[1] + 20),
                    (center[0] - 18, center[1] - 15),
                    (center[0] + 18, center[1] - 15)
                ]
            
            pygame.draw.polygon(screen, arrow_color, points)
        
        draw_arrow_button(arrow_up_rect, "up", arrow_up_hover)
        draw_arrow_button(arrow_down_rect, "down", arrow_down_hover)
        
        # Draw score counter
        font = pygame.font.Font(None, 72)
        score_text = font.render(f"{score}", True, (255, 255, 255))
        score_shadow = font.render(f"{score}", True, (0, 0, 0))
        
        screen.blit(score_shadow, (52, 32))
        screen.blit(score_text, (50, 30))
        
        # Draw game over screen
        if game_over:
            overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            
            game_over_font = pygame.font.Font(None, 120)
            game_over_text = game_over_font.render("GAME OVER!", True, (255, 100, 100))
            game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 80))
            screen.blit(game_over_text, game_over_rect)
            
            final_score_font = pygame.font.Font(None, 80)
            final_score_text = final_score_font.render(f"Score: {score}", True, (255, 255, 255))
            final_score_rect = final_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 20))
            screen.blit(final_score_text, final_score_rect)
            
            restart_font = pygame.font.Font(None, 50)
            restart_text = restart_font.render("Tap screen or press SPACE to restart", True, (200, 200, 200))
            restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 120))
            screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        delta_time = min(delta_time, 0.05)
        
        await asyncio.sleep(0)  # Critical for Pygbag!

# Run the game
asyncio.run(main())