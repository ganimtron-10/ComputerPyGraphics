import numpy
import time
import os


class CG:
    def __init__(self, x=25, y=25, bgchar="-"):
        """A Basic implementation of Pixels on screen in
        simple array format to try somebasic computer graphics algorithms

                Parameters:
                -----------
                x: (int) Maximum x coordinate
                y: (int) Maximum y coordinate
                bgchar: (str) A char to fill the background"""

        self.width = x
        self.height = y
        self.pixelmatrix = numpy.full((y, x), bgchar)

    def putpixel(self, x, y, putchar="@"):
        """Puts a char at the given x y coordinate

        Parameters:
        -----------
        x: (int) x coordinate of pixel
        y: (int) y coordinate of pixel
        putchar: (str) A char to put at that pixel
        take_origin: (bool) translate origin to center of the window
        """
        try:
            self.pixelmatrix[y][x] = putchar
        except:
            print("Error!")

    def getpixel(self, x, y):
        """Gets a char at the given x y coordinate

        Parameters:
        -----------
        x: (int) x coordinate of pixel
        y: (int) y coordinate of pixel
        """
        try:
            return self.pixelmatrix[y][x]
        except:
            print("Error!")

    def show(self):
        """Shows the Pixel Matrix"""
        for i in self.pixelmatrix:
            for j in i:
                print(j, end="")
            print()

    def run(self, speed=0.25):
        """Loops the Pixel Matrix by some delay

        Parameters:
        -----------
        speed: (float) delay between the showing the pixel matrix"""

        os.system("clear")
        self.show()
        time.sleep(speed)
