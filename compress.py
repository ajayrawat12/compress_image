import os
import sys
from PIL import Image, ImageOps
import time

size = 630, 430


def compressMe(file, verbose=False):
    filepath = os.path.join(os.getcwd(), file)
    oldsize = os.stat(filepath).st_size
    picture1 = Image.open(filepath)
    # picture2 = picture1
    # picture3 = picture1
    # dim = picture1.size

    # this to maintain the aspect ratio and IMage resize
    newImg = ImageOps.fit(picture1, size, Image.ANTIALIAS)
    print(newImg)
    newImg.save("comp_resize_img" + file, "JPEG", optimize=True, quality=80)

    # set quality= to the preferred quality.
    # I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number

    # # without using ImageOps
    # print(picture1.size, 'pic size')
    # pic1 = picture1.resize((300, 600), Image.ANTIALIAS)
    # # print('after maintaining ratio')
    # print(pic1.size, 'pic size after resize')

    # pic1.save("Compressed_" + file, "JPEG", optimize=True, quality=80)

    newsize = os.stat(os.path.join(os.getcwd(), "Compressed_" + file)).st_size
    percent = (oldsize - newsize) / float(oldsize) * 100
    if (verbose):
        print("File compressed from {0} to {1} or {2}%".format(oldsize, newsize, percent))
    return percent


def main():
    start = time.time()
    verbose = False
    # checks for verbose flag
    if (len(sys.argv) > 1):
        if (sys.argv[1].lower() == "-v"):
            verbose = True

    # finds present working dir
    pwd = os.getcwd()

    tot = 0
    num = 0
    for file in os.listdir(pwd):
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
            num += 1
            print(num)
            tot += compressMe(file, verbose)

    end = time.time()
    print(end - start, 'time diff')
    print("Average Compression: %d" % (float(tot) / num))
    print("Done")


if __name__ == "__main__":
    main()
