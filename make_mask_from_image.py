import cv2
import numpy as np
import os
def make_masks_from_image(path, save_path):
        # load image with alpha channel
        for file in os.listdir(path):
                print(file)
                img = cv2.imread(f'{path}{file}', cv2.IMREAD_UNCHANGED)
                print(img.shape)
                # extract alpha channel
                alpha = img[:, :, 3]

                # threshold alpha channel
                alpha = cv2.threshold(alpha, 0, 255, cv2.THRESH_BINARY)[1]

                # save output
                cv2.imwrite(f'{save_path}{file}', alpha)


from PIL import Image


def convertImage(path):
    for image in os.listdir(path):
        if image.endswith('3_removebg.png'):
            print(image)
            img = Image.open(f'{path}{image}')
            img = img.convert("RGBA")

            datas = img.getdata()

            newData = []

            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)

            img.putdata(newData)
            img.save(f'{path}{image}', "PNG")
            print("Successful")

def make_white(path):
    for image in os.listdir(path):
            try:
                print(image)
                input = Image.open(f"{path}{image}")
                img = Image.new("RGBA", input.size, "WHITE")
                img.paste(input, (0, 0), input)
                img.save(f"{path}{image}")
            except:
                pass


if __name__ == "__main__":
    path = '/Users/maxwhite/Downloads/7-removebg/'
    save_path = '/Users/maxwhite/PycharmProjects/new_50_photok/'
    make_white(path)

