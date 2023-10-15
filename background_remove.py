from PIL import Image

# Load the image
input_image_path = 'C:/Users/KPS/Downloads/Telegram Desktop/MAADco A5 logo (1).jpg'
output_image_path = 'output_image_removed_background.png'

image = Image.open(input_image_path)

# Convert the image to RGBA mode (if it's not already)
if image.mode != 'RGBA':
    image = image.convert('RGBA')

# Get the image data as a numpy array
image_data = image.load()

# Set a threshold for white color
white_threshold = 200

# Create a new image with a white background
new_image_data = []
for y in range(image.size[1]):
    row = []
    for x in range(image.size[0]):
        r, g, b, a = image_data[x, y]
        if r > white_threshold and g > white_threshold and b > white_threshold:
            # Make the pixel fully transparent (remove white background)
            row.append((0, 0, 0, 0))
        else:
            # Make the pixel white (everything else)
            row.append((255, 255, 255, a))
    new_image_data.append(row)

# Create a new image with the modified data
new_image = Image.new('RGBA', image.size)
new_image_data = [pixel for row in new_image_data for pixel in row]
new_image.putdata(new_image_data)

# Save the new image with the white background removed
new_image.save(output_image_path, format='PNG')

print(f"Image with white background removed saved as '{output_image_path}'")
