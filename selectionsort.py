import time

def selection_sort(data, drawData, timeTick):
    curindex = 0
    while curindex < len(data)-1:
        smallindex = curindex
        for i in range(curindex + 1, len(data)):
            if data[smallindex] > data[i]:
                smallindex = i
        data[curindex], data[smallindex] = data[smallindex], data[curindex]
        curindex += 1
        drawData(data, ['green'  if x == curindex or  x == smallindex else 'white' for x in range(len(data))] )
        time.sleep(timeTick)
        drawData(data, ['purple' for x in range(len(data))])

