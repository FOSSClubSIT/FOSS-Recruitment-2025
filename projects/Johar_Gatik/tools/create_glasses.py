"""
Placeholder glasses image for AR overlay.
"""
from PIL import Image, ImageDraw

def create_glasses_image():
    # Create a transparent image
    width, height = 200, 100
    glasses = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Draw simple glasses
    draw = ImageDraw.Draw(glasses)
    draw.rectangle([20, 30, 80, 70], fill=(0, 0, 0, 255))  # Left lens
    draw.rectangle([120, 30, 180, 70], fill=(0, 0, 0, 255))  # Right lens
    draw.rectangle([80, 45, 120, 55], fill=(0, 0, 0, 255))  # Bridge

    # Save the glasses image
    glasses.save("objects/glasses.png")

if __name__ == "__main__":
    create_glasses_image()
    print("Placeholder glasses image 'glasses.png' created successfully.")
