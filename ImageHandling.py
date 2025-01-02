#!/usr/bin/python3

from PIL import Image
import numpy as np
import sys
import os


# to-do: upgrade the argument handling 
def is_image(file_path):
    valid_image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    _, ext = os.path.splitext(file_path)
    return ext.lower() in valid_image_extensions

if len(sys.argv) < 2:
    print("No argument provided. Please specify a file path.")
    sys.exit(1)
    
elif len(sys.argv) > 2:
    print("Too many arguments.")
    sys.exit(1)

file_path = sys.argv[1]

if os.path.isfile(file_path):
    if is_image(file_path):
        print(f"The file '{file_path}' is valid.")
    else:
        print(f"The file '{file_path}' is not an image. Allowed extensions: jpg, jpeg, png, gif, bmp, tiff, webp")
        sys.exit(1) 
else:
    print(f"Invalid file: '{file_path}' does not exist or is not a file.")
    sys.exit(1)

'''
Fazer com que de alguma forma não destrua a nitidez da imagem quando a cor principal for branca

def convert_to_black_white(image, threshold=127): 
  
    image_array = np.array(image)
    
    bw_array = np.where(image_array > threshold, 255, 0).astype(np.uint8)

    return Image.fromarray(bw_array, mode="L")
'''


def ImageHandling(file_path):
    puffin_image = Image.open(file_path)
    print(f"Image size (width, height): {puffin_image.size}")

    puffin_image_resized = puffin_image.resize((300, 300))

    puffin_image_quantize = puffin_image_resized.quantize(16)
    grayscale_image = puffin_image_quantize.convert("L")

    grayscale_image.save("end_result_"+file_path)
    #bw_image = convert_to_black_white(grayscale_image, threshold=127)
    #bw_image.save("end_result_" + file_path)
    print(f"Black-and-white image saved as 'end_result_{file_path}'.")

    A = np.array(grayscale_image, dtype=np.integer)
    A = A / 255.0  
    csv_path = 'pixel_matrix'  + file_path + '.csv'
    np.savetxt(csv_path, A, delimiter=',', fmt='%i')
    print(f"Final Matrix saved to '{csv_path}': \n{A}")

    return A

ImageHandling(file_path=file_path)
