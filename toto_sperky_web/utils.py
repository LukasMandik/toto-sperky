from PIL import Image
import re
from django.utils.html import strip_tags

def remove_background(image_path, threshold=200, background_color=(255, 255, 255)):
    """
    Removes background from an image using PIL.

    Args:
        image_path (str): Path to the image file.
        threshold (int, optional): Threshold value for pixel transparency. Defaults to 200.
        background_color (tuple, optional): RGB color for the background. Defaults to white (255, 255, 255).

    Returns:
        PIL.Image: The image with the background removed, or None on error.
    """

    try:
        image = Image.open(image_path).convert('RGBA')  # Convert to RGBA for transparency

        width, height = image.size
        mask = Image.new('L', (width, height))  # Create a mask for transparency
        for x in range(width):
            for y in range(height):
                r, g, b, a = image.getpixel((x, y))
                if sum((r, g, b)) < threshold:  # Check against threshold
                    mask.putpixel((x, y), 0)  # Set transparent pixel in mask
                else:
                    mask.putpixel((x, y), 255)  # Set opaque pixel in mask

        image.putalpha(mask)  # Apply mask to image for transparency
        return image
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error during image processing: {e}")
        return None


def clean_html_for_search(html_content):
    """
    Odstráni HTML tagy a vyčistí text pre vyhľadávanie.
    
    Args:
        html_content (str): HTML obsah z CKEditoru
        
    Returns:
        str: Vyčistený text bez HTML tagov
    """
    if not html_content:
        return ""
    
    # Odstráni HTML tagy
    clean_text = strip_tags(html_content)
    
    # Odstráni prebytočné medzery a nové riadky
    clean_text = re.sub(r'\s+', ' ', clean_text)
    
    # Odstráni medzery na začiatku a konci
    clean_text = clean_text.strip()
    
    return clean_text