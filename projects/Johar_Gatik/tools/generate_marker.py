"""
Generate a placeholder marker image programmatically.
"""
from PIL import Image, ImageDraw

def create_placeholder_marker():
    # Create a transparent image
    width, height = 200, 100
    marker = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Draw a simple rectangle as the marker
    draw = ImageDraw.Draw(marker)
    draw.rectangle([20, 20, 180, 80], fill=(255, 0, 0, 128), outline=(255, 0, 0))

    # Save the marker image
    marker.save("marker.png")

if __name__ == "__main__":
    create_placeholder_marker()
    print("Placeholder marker image 'marker.png' created successfully.")