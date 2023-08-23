from PIL import Image
import sys

def reverse_image_y_axis(image_path, output_path):
    """
    Reverse an image over the y-axis.
    
    Args:
    - image_path (str): The path to the input image.
    - output_path (str): The path to save the reversed image.
    
    Returns:
    None
    """
    # Open the image
    with Image.open(image_path) as img:
        # Use the PIL method to reverse the image over the y-axis
        reversed_image = img.transpose(method=Image.FLIP_LEFT_RIGHT)
        
        # Save the reversed image to the specified output path
        reversed_image.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python reverse_image.py [path_to_image] [output_path]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = sys.argv[2]

    reverse_image_y_axis(image_path, output_path)
