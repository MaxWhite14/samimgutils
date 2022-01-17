import os
import numpy as np
import re
import cv2

def delete(path, path2):
    i = 0
    for file in sorted(os.listdir(path)):
        if (f'{os.path.splitext(file)[0]}.png') not in sorted(os.listdir(path2)):
            #if not file.endswith('-removebg-preview.png') and file.endswith('.png'):
            print(file)
            i += 1
            os.remove(f'{path}{file}')

                #os.rename(f'{path}{file}', f'{path}{new_file}')
                #os.rename(f'{path}{file}', f'{path}{os.path.splitext(file)[0]}-removebg-preview.png')
    print(i)
def rename(path):
    for file in sorted(os.listdir(path)):

            print(file)
            mod_file = file.replace('__', '_')
            #new_file = f'{path}{os.path.splitext(mod_file)[0]}_1_original_.png'
            #new_file1 = f'{path}{mod_file}'
            #print(mod_file)
            os.rename(f'{path}{file}', f'{path}{mod_file}')
def move():
    nums = 27
    for num in range(1, nums):
        num = str(num)
        path = f'/Users/maxwhite/PycharmProjects/masks/data/Data/{num}/jpg/'
        for file in sorted(os.listdir(path)):
            destination = '/Users/maxwhite/PycharmProjects/masks/data/human_im_unres/'


def resize():
    for file in sorted(os.listdir(path)):
        if file.endswith('_removebg.png'):
            img = cv2.imread(f'{path}{file}')
            size = (img.shape[1], img.shape[0])
            print(file, size)
            img2_name = file.replace('u2net', '1_nanosemantics_')
            img2 = cv2.imread(f'{path}{img2_name}')
            image3 = cv2.resize(img2, size)
            cv2.imwrite(f'{path}{img2_name}', image3)
def move_if(path, path2, save_path):

    i = 0
    for file in sorted(os.listdir(path)):
        if (f'{os.path.splitext(file)[0]}.png') in sorted(os.listdir(path2)):
            # if not file.endswith('-removebg-preview.png') and file.endswith('.png'):
            print(file)
            i += 1
            # os.remove(f'{path}{file}')
            #os.rename(f'{path2}{os.path.splitext(file)[0]}.png', f'{save_path}{os.path.splitext(file)[0]}.png')

            os.rename(f'{path}{file}', f'{save_path}{file}')
            # os.rename(f'{path}{file}', f'{path}{os.path.splitext(file)[0]}-removebg-preview.png')
    print(i)
def hui():
     b = 0
     for dir in os.listdir('/Users/maxwhite/PycharmProjects/TEST/shirts/'):
         if dir != '.DS_Store':
             print(dir)
             path = f'/Users/maxwhite/PycharmProjects/TEST/Data/{dir}/output/'
             path2 = f'/Users/maxwhite/PycharmProjects/TEST/maska_removebg/'
             save_path = f'/Users/maxwhite/PycharmProjects/TEST/orig_masks/'
             if not os.path.exists(save_path):
                 os.makedirs(save_path)
             i = 0

             for file in sorted(os.listdir(path)):
                 if (f'{os.path.splitext(file)[0]}.png') in sorted(os.listdir(path2)):
                     # if not file.endswith('-removebg-preview.png') and file.endswith('.png'):
                     print(file)
                     i += 1
                     # os.remove(f'{path}{file}')
                     # os.rename(f'{path2}{os.path.splitext(file)[0]}.png', f'{save_path}{os.path.splitext(file)[0]}.png')

                     os.rename(f'{path}{file}', f'{save_path}{file}')
                     # os.rename(f'{path}{file}', f'{path}{os.path.splitext(file)[0]}-removebg-preview.png')
             b += i
     print(b)
def shit():
    b = 0
    for dir in os.listdir('/Users/maxwhite/PycharmProjects/TEST/Data/'):
        if dir != '.DS_Store':
            print(dir)
            path = f'/Users/maxwhite/PycharmProjects/TEST/Data/{dir}/output/'
            # path2 = f'/Users/maxwhite/PycharmProjects/TEST/shirts/{dir}/{dir}/'
            # save_path = f'/Users/maxwhite/PycharmProjects/TEST/jpgs/'

            for file in sorted(os.listdir(path)):
                print(file)
                os.rename(f'{path}{file}', f'{path}{dir}_{file}')

    print(b)
def if_shit_goes():
    path = '/Users/maxwhite/PycharmProjects/TEST/shirts/'
    for dir in os.listdir(path):
        if dir != '.DS_Store':
            p = f'/Users/maxwhite/PycharmProjects/TEST/shirts/{dir}/jpg/'
            print(dir)
            rename(p)


if __name__ == "__main__":
    path1 = '/Users/maxwhite/PycharmProjects/TEST/im_aug_2/'
    path2 = '/Users/maxwhite/PycharmProjects/TEST/objective_test_final/original_gts/'
    save_path = '/Users/maxwhite/PycharmProjects/TEST/objective_test_final/jpgs/'
    #rename(path1)
    move_if(path1, path2, save_path)






