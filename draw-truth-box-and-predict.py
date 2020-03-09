import os
import cv2
import shutil

gt_path = "/home/dangkhoa/Desktop/Panasonic/20200224/darknet/test.txt"
pred_dir = "/home/dangkhoa/Desktop/Panasonic/20200224/yolov3-keras-onnx/mAP/predicted"
des = "/home/dangkhoa/Desktop/Panasonic/bbox/128/0.25"
if os.path.exists(des): 
    shutil.rmtree(des)
os.makedirs(des)
f = open(gt_path,"r")
for name in f.readlines(): 
    name = name.strip()
    if name:
        image = cv2.imread(name)
        w = image.shape[1]
        h = image.shape[0]
        name_pred = name.split("/")[-1]
        if "jpg" in name:
            f_gt = open(name.split("jpg")[0] + 'txt','r')
            f_pred = open(os.path.join(pred_dir,name_pred.split("jpg")[0] + 'txt'),'r')
        elif "bmp" in name:
            f_gt = open(name.split("bmp")[0] + 'txt','r')
            f_pred = open(os.path.join(pred_dir,name_pred.split("bmp")[0] + 'txt'),'r')
        
        # for line in f_gt.readlines():
        #     line = line.strip()
        #     line = line. split(" ")

        #     xcenter = float(line[1])
        #     ycenter = float(line[2])
        #     width = float(line[3])
        #     height = float(line[4])
        #     x_min = int((xcenter - width/2)*w)
        #     y_min = int((ycenter - height/2)*h) 
        #     x_max = int((xcenter + width/2)*w)
        #     y_max = int((ycenter + height/2)*h)

        #     cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),thickness=1)

        for line in f_pred.readlines():
            line = line.strip()
            line = line. split(" ")
            text = " " + line[0] + " " + str(round(float(line[1]),2)) + " "
            x_min = int(line[2])
            y_min = int(line[3])
            x_max = int(line[4])
            y_max = int(line[5])

            font_scale = 0.5
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
            text_x_min = x_min
            text_y_min = y_min - text_height - 2
            text_x_max = x_min + text_width
            text_y_max = y_min
            cv2.rectangle(image, (text_x_min,text_y_min), (text_x_max,text_y_max), (255,0,0), cv2.FILLED)
            cv2.putText(image, text, (x_min, y_min - 2), font, fontScale=font_scale, color=(255, 255, 255), thickness=1)
            cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(255,0,0),thickness=1)
        
        img = cv2.resize(image,(512,512))
        cv2.imwrite(os.path.join(des,name.split("/")[-1]),img)