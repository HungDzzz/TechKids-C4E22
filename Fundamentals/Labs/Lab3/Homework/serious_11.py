def is_inside(t, l):
    if l[0] <= t[0] <= (l[0]+l[2]) and l[1] <= t[1] <= (l[1]+l[3]):
        print("Point is inside a rectangle")
        return True
    else:
        print("point is not inside a rectangle")
        return False
is_inside([200, 120], [140, 60, 100, 200])