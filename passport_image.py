from PIL import Image

# Load the original image
image_path = "C:\\Users\\Abinaya\\OneDrive\\Pictures\\2021-Himalayan-Royal-Enfield-7.jpg"
original_image = Image.open(image_path)

# Define the size of a passport photo (e.g., 35x45 mm, 413x531 pixels at 300 dpi)
passport_size = (413, 531)

# Resize the original image to passport size
passport_image = original_image.resize(passport_size, Image.ANTIALIAS)

# Create a new image to hold 8 passport photos
output_image = Image.new('RGB', (passport_size[0] * 4, passport_size[1] * 2), (255, 255, 255))

# Paste the passport image into the output image in 2 rows and 4 columns
for i in range(2):
    for j in range(4):
        output_image.paste(passport_image, (j * passport_size[0], i * passport_size[1]))

# Save the output image
output_path = "passport_photos.png"
output_image.save(output_path)

# Display the output image
output_image.show()

print(f"Passport photos saved at {output_path}")
