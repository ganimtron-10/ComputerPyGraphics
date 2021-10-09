import numpy

class CG:
	"""A Basic implementation of Pixels on screen in 
	simple array format to try somebasic computer graphics algorithms.

	Parameters:
	-----------
	x: (int) Maximum x coordinate
	y: (int) Maximum y coordinate
	bgchar: (str) A char to fill the background
	"""
	def __init__(self,x=25,y=25,bgchar="-"):
		x = x+1 if x%2==0 else x
		y = y+1 if y%2==0 else y
		self.pixelmatrix = numpy.full((x,y),bgchar)
		self.origin = (x//2,y//2)

	def putpixel(self,x,y,putchar="@"):
		"""Puts a char at the given x y coordinate.

		Parameters:
		-----------
		x: (int) x coordinate of pixel
		y: (int) y coordinate of pixel
		putchar: (str) A char to put at that pixel
		"""
		x = self.origin[0] + x
		y = self.origin[1] - y
		self.pixelmatrix[y][x] = putchar

	def show(self):
		"""Shows the Pixel Matrix.
		"""
		for i in self.pixelmatrix:
			for j in i:
				print(j,end="")
			print()