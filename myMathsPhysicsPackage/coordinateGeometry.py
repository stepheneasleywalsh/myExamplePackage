
def distance(point1, point2):
    #Gets the distance between points, the points are dicts
    x1 = point1["x"]
    y1 = point1["y"]
    x2 = point2["x"]
    y2 = point2["y"]
    d = (((x1-x2)**2) + ((y1-y2)**2))**0.5
    return(d)

