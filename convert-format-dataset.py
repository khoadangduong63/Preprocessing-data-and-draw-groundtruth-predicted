import os
import cv2


root = '/home/dangkhoa/Desktop/Panasonic/PSSC/images_labels'
results = open("val_pssc_bbox.txt","w")
files = []
for f in os.listdir(root):
    full_path = os.path.join(root, f)
    if os.path.splitext(full_path)[1].lower() in ['.bmp']:
        image = cv2.imread(full_path)
        w = image.shape[1]
        h = image.shape[0]
        f_txt = open(full_path.split("bmp")[0] + 'txt','r')
        to_write = full_path
        for line in f_txt.readlines():
            line = line.strip()
            if line:
                line = line. split(" ")
                l = int(line[0])
                xcenter = float(line[1])
                ycenter = float(line[2])
                width = float(line[3])
                height = float(line[4])
                x_min = int((xcenter - width/2)*w)
                y_min = int((ycenter - height/2)*h) 
                x_max = int((xcenter + width/2)*w)
                y_max = int((ycenter + height/2)*h)
                classes = 0
                to_write = to_write + " " + str(x_min) + "," + str(y_min) + "," + str(x_max) + "," + str(y_max) + "," + str(classes)
        results.write(to_write + "\n")
results.close()