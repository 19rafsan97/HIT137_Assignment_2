# Github repository: https://github.com/19rafsan97/HIT137_Assignment_2

from PIL import Image
import time

def modify_image_and_sum_red_pixels(input_image_path, output_image_path):
    """
    Generates a number based on the current time, modifies the RGB values of each pixel in the image,
    saves the modified image, and returns the sum of red pixel values.

    Args:
    input_image_path (str): Path to the input image file.
    output_image_path (str): Path to save the modified image file.
    
    Returns:
    int: Sum of all red pixel values in the modified image.
    """
    # Step 1: Generate the number
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50
    if generated_number % 2 == 0:
        generated_number += 10

    # Load the image
    input_image = Image.open(input_image_path)
    pixels = input_image.load()
    width, height = input_image.size

    # Step 2: Modify the image
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            new_pixel = (min(r + generated_number, 255), 
                         min(g + generated_number, 255), 
                         min(b + generated_number, 255))
            pixels[x, y] = new_pixel

    # Save the new image
    input_image.save(output_image_path)

    # Step 3: Calculate the sum of red pixel values
    red_sum = 0
    for y in range(height):
        for x in range(width):
            r, _, _ = pixels[x, y]
            red_sum += r

    return red_sum

# Example usage
if __name__ == "__main__":
    red_sum = modify_image_and_sum_red_pixels('chapter1.jpg', 'chapter1out.jpg')
    print("Sum of all red pixel values:", red_sum)
