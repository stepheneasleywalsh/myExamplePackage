from myMathsPhysicsPackage import coordinateGeometry, Physics

point1 = {
    "x": 0,
    "y": 0
}

point2 = {
    "x": 1,
    "y": 1,
}

u = 5
v = 7

distance = coordinateGeometry.distance(point1,point2)
print(distance)

average = Physics.averageVelocity(u,v)
print(average)

quit()
