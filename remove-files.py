import glob, os

os.chdir("./datasets/new_dir/labels/val")
file_name = []
for file in glob.glob("*.txt"):
    a = str(file[:len(file)-4])
    file_name.append(a)


os.chdir("../../images/val")
for file in glob.glob("*.jpg"):
    img = file[:len(file)-4]
    if img not in file_name:
        os.remove(file)