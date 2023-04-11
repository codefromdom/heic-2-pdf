import os
from PIL import Image

# Directory in which the script is executed
directory = os.getcwd()

# Loop through all .heic files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".heic"):
        # Open the .heic file using PIL
        image = Image.open(os.path.join(directory, filename))

        # Compress the image
        image = image.convert('RGB')
        image.save(os.path.join(directory, f"{os.path.splitext(filename)[0]}.jpg"), optimize=True, quality=85)

        # Convert the image to PDF
        pdf_filename = os.path.join(directory, f"{os.path.splitext(filename)[0]}.pdf")
        os.system(f"convert {os.path.join(directory, f'{os.path.splitext(filename)[0]}.jpg')} {pdf_filename}")
