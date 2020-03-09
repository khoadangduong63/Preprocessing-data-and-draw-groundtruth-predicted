import cv2
while(True):
    path = input("Enter the path: ")
    image = cv2.imread(path)
    w = image.shape[1]
    h = image.shape[0]
    f = open(path.split("jpg")[0] + 'txt','r')
    window_name = 'Image'
    for line in f.readlines():
        line = line.strip()
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