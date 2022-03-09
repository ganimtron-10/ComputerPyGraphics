def midpoint_circle_algo(cg, r, xc=None, yc=None, show_step=False):
    """Creating a Circle using Midpoint Circle Drawing Algorithm"""

    if xc == None or yc == None:
        xc = cg.width // 2
        yc = cg.height // 2

    x, y = 0, r
    d = 1 - r

    while x <= y:
        cg.putpixel(x + xc, y + yc)
        cg.putpixel(-x + xc, y + yc)
        cg.putpixel(x + xc, -y + yc)
        cg.putpixel(-x + xc, -y + yc)
        cg.putpixel(y + yc, x + xc)
        cg.putpixel(-y + yc, x + xc)
        cg.putpixel(y + yc, -x + xc)
        cg.putpixel(-y + yc, -x + xc)
        if d < 0:
            d = d + 2 * x + 1
            x += 1
        else:
            d = d + 2 * (x - y) + 1
            x += 1
            y -= 1

        if show_step:
            cg.run()

    if not show_step:
        cg.show()


if __name__ == "__main__":
    cg = CG(25, 25, ".")
    r = int(input("Enter the value of r: "))
    midpoint_circle_algo(cg, r, show_step=True)
