from PIL import Image
from time import sleep
import os
import math


class AsciiGenerator:
    def __init__(self):
        #self.characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        #self.characters = "oahkbzcvunxrjft?-_+~<>i!l;:,\"^`'. "' .\'`^",:;l!i><~+_-?tfjrxnuvczbkhao'
        self.characters = ' .\'`^",:;l!i><~+_-?tfjrxnuvczbkhao'
        #self.characters = '.\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
        self.image = None

        directory = os.getcwd()
        self.images_path = f'{directory}/pics/'
        self.output_path = f'{directory}/out/'

    def format_image(self, nwidth):
        width, height = self.image.size
        ratio = height / width

        nheight = math.ceil(nwidth * ratio)

        self.image = self.image.resize((nwidth, nheight))

        #converting to lightscale image
        self.image = self.image.convert('L')

    def get_pixel_data(self):
        return self.image.getdata()

    def get_ascii(self, pixel_data, nwidth):
        array = []
        for c in range(len(pixel_data)):
            rem = c % nwidth
            circle = ['-', '\\', '|', '/'],
            print(f"Generating ascii image... {circle[c%len(circle)]} -> {int(c/len(pixel_data)*100)}%", end='\r')

            if rem == nwidth - 1:
                value = self.characters[pixel_data[c] // len(self.characters)]
                array.append(value)
                array.append('\n')
            else:
                array.append(self.characters[pixel_data[c] // len(self.characters)])

        return ''.join(array)

    def generate(self, filename, nwidth, mode=0):
        imagepath = self.images_path + filename
        self.image = Image.open(imagepath)

        #resizing image
        self.format_image(nwidth)

        #getting pixel data
        pdata = self.get_pixel_data()

        #converting to ascii array
        ascii_art = self.get_ascii(pdata, nwidth)

        #writing to a file
        if mode == 0:
            ofilename = input("\nFilename: ")
            out_filename = self.output_path + ofilename + f"_{nwidth}_out.txt"
            with open(out_filename, 'w') as ofile:
                ofile.write(ascii_art)
                print(f'\nOutput File Saved -> {out_filename}')
                sleep(.3)
        if mode == 1:
            #display in terminal
            print("\n" + ascii_art)

if __name__ == '__main__':
    #driver program
    directory = os.getcwd()
    images_list = os.listdir(f'{directory}/pics')
    print("\nList of Images")
    for i in range(len(images_list)):
        print(f"\t{i}. {images_list[i]}")

    image_choice = int(input("\nEnter number of choice: "))
    filename = images_list[image_choice]
    width = int(input("\nEnter width: "))
    print("\nModes:\n\t0. Write to file\n\t1.Write to Terminal")
    mode = int(input("Mode to write: "))

    generator = AsciiGenerator()
    generator.generate(filename, width, mode)


