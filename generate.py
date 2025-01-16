from PIL import Image
import cv2


video_length = 218

# ASCII characters
ASCII_CHARS = '@%#*+=-:. ' 

def scale_image(image, new_width, new_height):
    """Resizes an image to the given width and height."""
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    """Converts an image to grayscale."""
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width):
    """Maps each pixel to an ASCII character."""
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [
        ASCII_CHARS[min(int(pixel_value / range_width), len(ASCII_CHARS) - 1)]
        for pixel_value in pixels_in_image
    ]
    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width, new_height):
    """Converts an image to ASCII art."""
    range_width = 256 / len(ASCII_CHARS)  # Dynamically calculate range width
    image = scale_image(image, new_width, new_height)
    image = convert_to_grayscale(image)
    pixels_to_chars = map_pixels_to_ascii_chars(image, range_width)
    len_pixels_to_chars = len(pixels_to_chars)
    ascii_image = [
        pixels_to_chars[index: index + new_width]
        for index in range(0, len_pixels_to_chars, new_width)
    ]
    return "\n".join(ascii_image)

def handle_image_conversion(image_filepath, new_width, new_height):
    """Handles the conversion of an image to ASCII."""
    image = Image.open(image_filepath)
    ascii_image = convert_image_to_ascii(image, new_width, new_height)
    return ascii_image

if __name__ == '__main__':
    import os

    # Set target resolution
    target_width = 1200
    target_height = 800

    # Estimate ASCII grid dimensions
    font_width = 10  # Approximate width of a character in pixels
    font_height = 20  # Approximate height of a character in pixels
    ascii_width = target_width // font_width
    ascii_height = target_height // font_height

    print(f"Generating ASCII art with dimensions {ascii_width}x{ascii_height}")

    # Process video
    vidcap = cv2.VideoCapture('video.mp4')
    time_count = 0
    frames = []
    while time_count <= video_length * 1000:
        print('Generating ASCII frame at ' + str(time_count))
        vidcap.set(0, time_count)
        success, image = vidcap.read()
        if success:
            cv2.imwrite('output.jpg', image)
            frames.append(handle_image_conversion('output.jpg', ascii_width, ascii_height))
        time_count += 100  # Advance by 100 ms (10 FPS)

    # Save frames to play.txt
    with open('play.txt', 'w') as f:
        f.write('SPLIT'.join(frames))
