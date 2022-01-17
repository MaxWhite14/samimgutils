import cv2
import os
path = '/Users/maxwhite/PycharmProjects/50photok/'
save_path = '/Users/maxwhite/PycharmProjects/50photok/'

for file in sorted(os.listdir(path)):
        if file != '.DS_Store':
                print(file)

                image_path = os.path.join(path, file)
                print(image_path)
                image = cv2.imread(os.path.join(path,file))
                size = 4000, 4000
                image = cv2.resize(image, size)
                cv2.imwrite(f'{save_path}{file}', image)