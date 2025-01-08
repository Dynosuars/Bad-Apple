import time
import pygame

def play_ascii_in_pygame():
    # Read ASCII art frames
    with open('play.txt', 'r') as f:
        frames = f.read().split('SPLIT')

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode
    pygame.display.set_caption("ASCII Art Player")

    # Get screen dimensions
    screen_width, screen_height = screen.get_size()

    # Set up font
    font_size = 20  # Adjust for your ASCII size
    font = pygame.font.SysFont('Courier', font_size)  # Monospaced font
    text_color = (255, 255, 255)  # White
    bg_color = (0, 0, 0)  # Black

    # Initialize audio
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")  # Ensure you have extracted audio
    pygame.mixer.music.play()

    # Synchronize ASCII with audio
    init_time = time.time()
    duration = 218  # Replace with actual video duration if known

    running = True
    try:
        while running and time.time() <= init_time + duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False  # Exit fullscreen on Escape key

            # Clear screen
            screen.fill(bg_color)

            # Get the current frame
            elapsed_time = time.time() - init_time
            frame_index = int(elapsed_time * 10)  # 10 frames per second
            if frame_index < len(frames):
                # Render the current frame
                ascii_frame = frames[frame_index].split('\n')

                # Calculate the total height of the text block
                line_height = font.size("A")[1]  # Height of a single line
                text_height = len(ascii_frame) * line_height
                start_y = (screen_height - text_height) // 2  # Center vertically

                for i, line in enumerate(ascii_frame):
                    rendered_line = font.render(line, True, text_color)

                    # Center each line horizontally
                    text_width = rendered_line.get_width()
                    start_x = (screen_width - text_width) // 2
                    screen.blit(rendered_line, (start_x, start_y + i * line_height))  # Adjust spacing

            # Update the display
            pygame.display.flip()
            time.sleep(0.05)

    except KeyboardInterrupt:
        pass
    finally:
        pygame.mixer.music.stop()
        pygame.quit()


if __name__ == '__main__':
    play_ascii_in_pygame()
