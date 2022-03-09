def dda(cg, x1, y1, x2, y2, show_step=False):
    """Creating a line using Digital Differential Algorithm(DDA)"""

    dx = x2 - x1
    dy = y2 - y1

    length = max(dx, dy)

    xinc = dx / length
    yinc = dy / length

    xi = x1
    yi = y1

    for i in range(length + 1):
        cg.putpixel(round(xi), round(yi), "@")
        xi = xi + xinc
        yi = yi + yinc
        if show_step:
            cg.run()

    if not show_step:
        cg.show()


if __name__ == "__main__":
    cg = CG(20, 20, ".")
    x1 = int(input("Enter the value of x1: "))
    y1 = int(input("Enter the value of y1: "))
    x2 = int(input("Enter the value of x2: "))
    y2 = int(input("Enter the value of y2: "))

    dda(x1, y1, x2, y2, True)
