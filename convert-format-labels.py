import os
import cv2


# root = '/home/dangkhoa/Desktop/Panasonic/PSSC/images_labels'
# des = '/home/dangkhoa/Desktop/Panasonic/PSSC/labels_absolute'
# classes = "person"
# files = []
# for f in os.listdir(root):
#     full_path = os.path.join(root, f)
#     if os.path.splitext(full_path)[1].lower() in ['.bmp']:
#         image = cv2.imread(full_path)
#         w = image.shape[1]
#         h = image.shape[0]
#         f_txt = open(full_path.split('bmp')[0] + 'txt','r')
#         f_results = open(os.path.join(des,f.split('bmp')[0] + 'txt'),'w')
#         for line in f_txt.readlines():
#             line = line.strip()
#             if line:
#                 line = line. split(" ")
#                 l = int(line[0])
#                 xcenter = float(line[1])
#                 ycenter = float(line[2])
#                 width = float(line[3])
#                 height = float(line[4])
#                 x_min = int((xcenter - width/2)*w)
#                 y_min = int((ycenter - height/2)*h) 
#                 x_max = int((xcenter + width/2)*w)
#                 y_max = int((ycenter + height/2)*h)
                
#                 to_write = classes + " " + str(x_min) + " " + str(y_min) + " " + str(x_max) + " " + str(y_max) + "\n"
#                 f_results.write(to_write)
#         f_results.close()


# Normalize labels
root = '/home/dangkhoa/Desktop/Panasonic/PSSC/new dataset/02_annotation'
des = '/home/dangkhoa/Desktop/Panasonic/PSSC/new dataset/images_labels_1080'

for f in os.listdir(root):
    full_path = os.path.join(root, f)
    if os.path.splitext(full_path)[1].lower() in ['.txt']:
        f_txt = open(full_path,'r')
        f_results = open(os.path.join(des,f),'w')
        for line in f_txt.readlines():
            line = line.strip()
            if line:
                line = line. split(" ")
                classes = line[0]
                if classes == '38':
                    classes = '0'
                
                to_write = classes + " " + line[1] + " " + line[2] + " " + line[3] + " " + line[4] + "\n"
                f_results.write(to_write)
        f_results.close()