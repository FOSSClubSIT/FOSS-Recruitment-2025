"""
Glasses image for AR overlay.
"""
from PIL import Image, ImageDraw

def create_glasses_image():
    # Create a transparent image
    width, height = 200, 100
    glasses = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    draw = ImageDraw.Draw(glasses)
    # Draw left lens
    draw.ellipse([20, 30, 80, 90], fill=(0, 0, 0, 255))
    # Draw right lens
    draw.ellipse([120, 30, 180, 90], fill=(0, 0, 0, 255))
    # Draw bridge
    draw.rectangle([80, 50, 120, 70], fill=(0, 0, 0, 255))

    glasses.save("glasses.png")

if __name__ == "__main__":
    create_glasses_image()
    print("Glasses image 'glasses.png' created successfully.")
