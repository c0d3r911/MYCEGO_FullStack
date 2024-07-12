from PIL import Image
import os

def collect_images(folder_list):
    images = []
    
    for folder in folder_list:
        for filename in os.listdir(folder):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.tif')):
                file_path = os.path.join(folder, filename)
                img = Image.open(file_path)
                images.append(img)
                
    return images

def save_images_as_tiff(images, output_file):
    if images:
        images[0].save(output_file, save_all=True, append_images=images[1:])
    else:
        print("No images found to save.")

def main():
    folders = ['Для тестового/1369_12_Наклейки 3-D_3',
               'Для тестового/1388_2_Наклейки 3-D_1',
               'Для тестового/1388_6_Наклейки 3-D_2',
               'Для тестового/1388_12_Наклейки 3-D_3',]
    output_file = 'Result.tif'
    
    images = collect_images(folders)
    save_images_as_tiff(images, output_file)
    print(f'Saved {len(images)} images to {output_file}')

if __name__ == '__main__':
    main()
