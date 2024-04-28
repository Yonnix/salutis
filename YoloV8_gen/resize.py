import cv2
import os
import sys

def open_images(image_folder_path):
    """This function opens the images in the folder and yields them

    Args:
        image_folder_path (string): The path to the folder containing the images

    Yields:
        cv2 image: images of acnee
    """
    for image in os.listdir(image_folder_path):
        image_path = os.path.join(image_folder_path, image)
        yield image_path


def resize_images(images_path):
    """This function resizes the images to 640x640

    Args:
        images_path: Path to the images folder
    """
    images = open_images(images_path)
    for image in images:
        img = cv2.imread(image)
        if img is None:
            print(f"Failed to open image at {image}")
            continue
        print(f"Original size of {image}: {img.shape}")
        resized_img = cv2.resize(img, (640, 640))
        print(f"Resized size of {image}: {resized_img.shape}")
        write_status = cv2.imwrite(image, resized_img)
        if not write_status:
            print(f"Failed to write image at {image}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python resize.py <path_to_images_folder>")
        sys.exit(1)
    images_path = sys.argv[1]
    resize_images(images_path)