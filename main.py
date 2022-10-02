import pgerom as pe
pe.init()
pe.display.make((700, 600), "Curvers")

def calculateP(lines, t):
    distance = pe.math.dist(*lines)
    pos = pe.math.lerp(*lines, distance*t)
    return (pos.x, pos.y)

class quadratic_curve:
    def __init__(self, left, center, right, color=(0,0,0), width=1):
        self.line0 = (left, center)
        self.line1 = (center, right)
        self.width = width
        self.color = color
    def draw(self, color=None, width=None):
        if not color:
            color = self.color
        if not width:
            width = self.width
        a = calculateP(self.line0, 0)
        b = calculateP(self.line1, 0)
        pvp = calculateP([a, b], 0)
        maxline = int(max(max(pe.math.dist(*self.line0), pe.math.dist(*self.line1)), pe.math.dist(a, b)))
        for i in range(0, maxline):
            t = i/maxline
            a = calculateP(self.line0, t)
            b = calculateP(self.line1, t)
            new = calculateP([a, b], t)
            pe.draw.circle(color, new, width/2, 0)
            pe.draw.line(color, pvp, new, width)
            pvp = calculateP([a, b], t)
    def draw_handles(self, color=(50, 50, 50), color2=(200, 75, 75)):
        pe.draw.line(color, *self.line0, 2)
        pe.draw.line(color, *self.line1, 2)
        a = calculateP(self.line0, 0.5)
        b = calculateP(self.line1, 0.5)
        pe.draw.line(color, a,b, 2, 0)
        pe.draw.circle(color2, calculateP([a, b], .5), 10, 2)
        pe.draw.circle(color2, self.line0[0], 10, 2)
        pe.draw.circle(color2, self.line1[0], 10, 2)
        pe.draw.circle(color2, self.line1[1], 10, 2)

curve = quadratic_curve((50, 550), (50, 300), (650, 50),pe.color.white, 3)

while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    pe.fill.full(pe.color.black)

    curve.draw()
    curve.draw_handles()


    pe.display.update()