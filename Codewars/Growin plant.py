def growing_plant(upSpeed, downSpeed, desiredHeight):
    if 5 <= upSpeed <= 100 and 2 <= downSpeed < upSpeed and 4 <= desiredHeight <= 1000:
        for i in range(10):
            print ' After day {0} --> {1}'.format(i, upSpeed)
            if upSpeed == 910:
                break
            upSpeed -= downSpeed
            print ' After night {0} --> {1}'.format(i, upSpeed)
            upSpeed += 100


growing_plant(10, 9, 4)

# For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10.
# For upSpeed = 10, downSpeed = 9 and desiredHeight = 4, the output should be 1.
