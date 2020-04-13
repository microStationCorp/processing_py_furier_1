time = 0
points = []

def setup():
    size(800, 700)

def draw():
    global time
    background(51)

    x1 = 0
    y1 = 0
    translate(180, 500)
    for i in range(2):
        n = i * 1 + 1
        radius = 50 * (4 / (n * PI))
        prevx1 = x1
        prevy1 = y1
        x1 += radius * cos(radians(n * time))
        y1 += radius * sin(radians(n * time))

        stroke(255, 50)
        noFill()
        ellipse(prevx1, prevy1, radius * 2, radius * 2)
        stroke(255)
        line(prevx1, prevy1, x1, y1)

    x2 = 400
    y2 = -300
    for i in range(2):
        n = i * 1 + 1
        radius = 50 * ((4) / (n * PI))
        prevx2 = x2
        prevy2 = y2
        x2 += radius * cos(radians(n * time))
        y2 += radius * sin(radians(n * time))

        stroke(255, 50)
        noFill()
        ellipse(prevx2, prevy2, radius * 2, radius * 2)
        stroke(255)
        line(prevx2, prevy2, x2, y2)

    points.append([x2, y1])
    ellipse(x2, y1, 3, 3)
    line(x1, y1, x2, y1)
    line(x2, y2, x2, y1)
    if len(points) > 1000:
        points.pop(0)

    for p in points:
        point(p[0], p[1])

    time += .5
