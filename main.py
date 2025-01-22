import time
import pygame 

def play_ascii_in_pygame():
    # Read ASCII art frames
    with open('play.txt', 'r') as f:
        frames = f.read().split('SPLIT')

    # Initialize Pygame (pg)
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Badapple")

    # Get the size of the screen for full screen.
    screen_width, screen_height = screen.get_size()

    # Font settings
    font_size = 20  # Default = 20 pixels
    font = pygame.font.SysFont('Courier', font_size)  # Font
    text_color = ("#FFFFFF")
    bg_color = ("#000000")

    # Audio settings
    pygame.mixer.init()
    pygame.mixer.music.load("badapple.mp3")
    pygame.mixer.music.play()

    # Sync with the frame
    init_time = time.time()
    duration = 218  

    running = True
    try:
        while running and time.time() <= init_time + duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False 

            screen.fill(bg_color)

            # Get the current frame
            elapsed_time = time.time() - init_time
            frame_index = int(elapsed_time * 10)  
            if frame_index < len(frames):
                ascii_frame = frames[frame_index].split('\n')

                # Centering the text
                line_height = font.size("A")[1] #Height
                text_height = len(ascii_frame) * line_height
                start_y = (screen_height - text_height) // 2 

                for i, line in enumerate(ascii_frame):
                    rendered_line = font.render(line, True, text_color)

                    
                    text_width = rendered_line.get_width()
                    start_x = (screen_width - text_width) // 2
                    screen.blit(rendered_line, (start_x, start_y + i * line_height)) 

            # Update the display
            pygame.display.flip()
            time.sleep(0.05)

    except KeyboardInterrupt:
        pass
    finally:
        pygame.mixer.music.stop()
        pygame.quit()


if __name__ == "__main__":
    play_ascii_in_pygame()
