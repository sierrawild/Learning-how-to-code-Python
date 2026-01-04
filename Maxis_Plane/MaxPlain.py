import pygame
import clouds

# pygame setup
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

screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption("Max's Plane")
clock = pygame.time.Clock()
delta_time = 0

# CONSTANTS
TILT_PLANE_BY = 20
TILT_SPEED = 25
LANE_SWITCH_SPEED = 800  # How fast plane moves between lanes

# Lane positions (top, middle, bottom)
LANES = [225, 450, 675]  # Y positions for the 3 lanes
current_lane = 1  # Start in middle lane (0=top, 1=middle, 2=bottom)
target_lane = 1

tilt_angle = 0
target_tilt = 0

# player setup
plane = pygame.image.load("Maxis_Plane/files/Max plain.png").convert()
plane.set_colorkey((255, 255, 255))
scale_by = 2.2
plane = pygame.transform.scale(plane, (plane.get_width() / scale_by,
                                       plane.get_height() / scale_by))
plane = pygame.transform.flip(plane, True, False)
plane_original = plane

plane_rec = plane.get_rect(center=screen.get_rect().center)
player_pos = pygame.Vector2(screen.get_width() // 4, LANES[current_lane])  # Fixed X position

# Create cloud manager
cloud_manager = clouds.CloudManager(1800, 900, num_clouds=8)

# Track key presses to prevent holding
up_pressed = False
down_pressed = False

# Track controller button presses
dpad_up_pressed = False
dpad_down_pressed = False
leftstick_up_pressed = False
leftstick_down_pressed = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle keyboard key press events
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_w or event.key == pygame.K_UP) and not up_pressed:
                up_pressed = True
                if current_lane > 0:
                    current_lane -= 1
                    target_lane = current_lane
                    target_tilt = TILT_PLANE_BY
            
            if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and not down_pressed:
                down_pressed = True
                if current_lane < 2:
                    current_lane += 1
                    target_lane = current_lane
                    target_tilt = -TILT_PLANE_BY
        
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
                elif hat[1] != 1:
                    dpad_up_pressed = False
                
                # D-pad DOWN
                if hat[1] == -1 and not dpad_down_pressed:
                    dpad_down_pressed = True
                    if current_lane < 2:
                        current_lane += 1
                        target_lane = current_lane
                        target_tilt = -TILT_PLANE_BY
                elif hat[1] != -1:
                    dpad_down_pressed = False
            
            # Left stick events (axis 1 is vertical)
            if event.type == pygame.JOYAXISMOTION and event.axis == 1:
                # Up (negative values)
                if joystick.get_axis(1) < -0.5 and not leftstick_up_pressed:
                    leftstick_up_pressed = True
                    if current_lane > 0:
                        current_lane -= 1
                        target_lane = current_lane
                        target_tilt = TILT_PLANE_BY
                elif joystick.get_axis(1) >= -0.5:
                    leftstick_up_pressed = False
                
                # Down (positive values)
                if joystick.get_axis(1) > 0.5 and not leftstick_down_pressed:
                    leftstick_down_pressed = True
                    if current_lane < 2:
                        current_lane += 1
                        target_lane = current_lane
                        target_tilt = -TILT_PLANE_BY
                elif joystick.get_axis(1) <= 0.5:
                    leftstick_down_pressed = False
            
            # A button to move up, B button to move down (alternative controls)
            if event.type == pygame.JOYBUTTONDOWN:
                # A button (usually button 0) - move up
                if event.button == 0:
                    if current_lane > 0:
                        current_lane -= 1
                        target_lane = current_lane
                        target_tilt = TILT_PLANE_BY
                
                # B button (usually button 1) - move down
                if event.button == 1:
                    if current_lane < 2:
                        current_lane += 1
                        target_lane = current_lane
                        target_tilt = -TILT_PLANE_BY
    
    screen.fill("#94EAFF")
    
    # Move plane smoothly to target lane
    target_y = LANES[target_lane]
    if abs(player_pos.y - target_y) > 1:
        if player_pos.y < target_y:
            player_pos.y += LANE_SWITCH_SPEED * delta_time
        else:
            player_pos.y -= LANE_SWITCH_SPEED * delta_time
        
        # Clamp to exact lane position when close
        if abs(player_pos.y - target_y) < 5:
            player_pos.y = target_y
    else:
        player_pos.y = target_y
        target_tilt = 0  # Level out when in lane
    
    # Tilting and drawing the plane
    tilt_angle += (target_tilt - tilt_angle) * TILT_SPEED * delta_time
    rotated_plane = pygame.transform.rotate(plane_original, tilt_angle)
    
    # build plane rectangle 
    plane_rec = rotated_plane.get_rect(center=player_pos)
    
    # Update and draw clouds
    cloud_manager.update(delta_time)
    cloud_manager.draw(screen)

    screen.blit(rotated_plane, plane_rec)
    
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000
    delta_time = min(delta_time, 0.05)

pygame.quit()