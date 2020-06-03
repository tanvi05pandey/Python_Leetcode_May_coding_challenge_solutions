def checkStraightLine(coordinates):
    # startingpoint(x1) + change in x value (delta x or x2-x1) * some constant (slope s) = destination (x3)
    #     i.e., x1 + (x2-x1) * s = x3
    #         s = (x3-x1) / (x2-x1)
    # similarly for y:
    #     y1 + (y2-y1) * s = y3
    #     s = (y3-y1)/(y2-y1)
    #
    #     (x3-x1) / (x2-x1) = (y3-y1)/(y2-y1)
    #     let's try to avoid division and turn this into a multiplication equation as below and code this up:
    #         (x3-x1) * (y2-y1) = (y3-y1) * (x2-x1)

    x1 = coordinates[0][0]
    y1 = coordinates[0][1]
    x2 = coordinates[1][0]
    y2 = coordinates[1][1]

    for i in range(2, len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        if (x-x1) * (y2-y1) != (y-y1) * (x2-x1):
            return False
    return True


print(checkStraightLine([[-5,1],[-4,-1],[-7,4],[-7,-7],[5,-7],[-3,2],[2,-5]]))