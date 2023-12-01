from PIL import Image
import os

def resize_and_replace(folder_path, output_size):
    files = os.listdir(folder_path)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        img = Image.open(image_path)
        resized_img = img.resize(output_size)
        resized_img.save(image_path)

if __name__ == "__main__":
    folder_path = "./dataset/pure_custom/val/high"
    output_size = (600, 400)
    resize_and_replace(folder_path, output_size)
