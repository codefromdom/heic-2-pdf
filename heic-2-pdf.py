import os
from PIL import Image
import shlex

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
        cmd = f'convert "{os.path.join(directory, f"{os.path.splitext(filename)[0]}.jpg")}" "{pdf_filename}"'
        os.system(shlex.quote(cmd))

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if file is not a PDF or Python script and delete it
    if not (filename.endswith(".pdf") or filename.endswith(".py")):
        os.remove(os.path.join(directory, filename))
