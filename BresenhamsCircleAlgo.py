from ComputerPyGraphics import CG

# print("Enter the value of xc: ")
# xc = int(input())
# print("Enter the value of yc: ")
# yc = int(input())
print("Enter the value of r: ")
r = int(input())

x = 0
y = r
d = 3-(2*r)

cg = CG(25,25,".")
while(x<=y):
	cg.putpixel(x, y)
	cg.putpixel(-x, y)
	cg.putpixel(x, -y)
	cg.putpixel(-x, -y)
	cg.putpixel(y, x)
	cg.putpixel(-y, x)
	cg.putpixel(y, -x)
	cg.putpixel(-y, -x)
	if d<0:
	    d = d + 4*x + 6
	    x += 1
	else:
	    d = d + 4*x - 4*y + 10
	    x += 1
	    y -= 1

cg.show()