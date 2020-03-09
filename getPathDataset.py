import os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
val_folder = os.path.join(current_dir,"images_labels_relative")

# Create and/or truncate train.txt and test.txt
file_val = open('val_pssc.txt', 'w')

ls = os.listdir(val_folder)
ls.sort()
for fname in ls:
    fpath   = os.path.join(val_folder, fname)
    if os.path.splitext(fpath)[1] != '.bmp':
        continue
    else:
        file_val.write(fpath + "\n")

file_val.close()
