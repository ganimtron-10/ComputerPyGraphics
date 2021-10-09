from ComputerPyGraphics import CG

print("Enter the value of x1: ")
x1 = int(input())
print("Enter the value of y1: ")
y1 = int(input())
print("Enter the value of x2: ")
x2 = int(input())
print("Enter the value of y2: ")
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

length = max(dx, dy)

xinc = dx/length
yinc = dy/length

xi = x1
yi = y1

cg = CG(15,15,".")

for i in range(length+1):
	cg.putpixel(round(xi), round(yi))
	xi = xi + xinc
	yi = yi + yinc


cg.show()