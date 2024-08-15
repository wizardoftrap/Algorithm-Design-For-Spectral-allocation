import csv
import matplotlib.pyplot as plt
import time

execution_times=[]

bandGap = 5
execution_times=[]

with open("D:/Downloads/CP301_Data/testCase.csv",mode="r") as testcases:
    csv1=csv.reader(testcases)
    testcase=0
    for lines in csv1:
        t1=time.time()
        t1=time.time()
        testcase+=1
        print("TestCase: ", testcase)
        x1=(float(lines[0]))
        x2=(float(lines[1]))
        y1=(float(lines[2]))
        y2=(float(lines[3]))
        d=(float(lines[4]))
        print("X_Min: ",x1,"   X_Max: ",x2,"   Y_Min: ",y1,"   Y_Max: ",y2,"   Range: ",d)
        def closest_coord(x, y):
            cx = 0
            cy = 0
            if x <= x1:
                cx = x1
            elif x >= x2:
                cx = x2
            else:
                cx = x
            if y <= y1:
                cy = y1
            elif y >= y2:
                cy = y2
            else:
                cy = y
            return [cx, cy]


        for file_name in range(3):
            dataSet = dict(zip([i for i in range(1, 301)], [[] for i in range(300)]))
            dataSetSize = 0
            types = ["new_dense", "new_sparse","new_medium"]
            with open(
                f"D:/Downloads/CP301_Data/{types[file_name]}.csv",
                mode="r",
            ) as file:
                csvFile = csv.reader(file)
                for line in csvFile:
                    if len(line) > 0 and line[0] != "X":
                        dataSet[int(line[2])].append(
                            [
                                [float(line[0]), float(line[1])],
                                float(line[4]),
                                closest_coord(float(line[0]), float(line[1])),
                            ]
                        )
                        dataSetSize += 1

            # f1 = open(f"C:/Users/91790/Downloads/dataSet_{i}/ranges.txt", "r")
            # f2 = open(f"C:/Users/91790/Downloads/dataSet_{i}/coordinates.txt", "r")
            # f3 = open(f"C:/Users/91790/Downloads/dataSet_{i}/frequencyChannels_KHz.txt", "r")
            # rang = f1.readlines()
            # coord = f2.readlines()
            # freq = f3.readlines()
            # for j in range(len(coord)):
            #     x, y = coord[j].split(" ")
            #     cx = 0
            #     cy = 0
            #     if float(x) >= x1:
            #         cx = x1
            #     elif float(x) <= x2:
            #         cx = x2
            #     else:
            #         cx = float(x)
            #     if float(y) >= y1:
            #         cy = y1
            #     elif float(y) <= y2:
            #         cy = y2
            #     else:
            #         cy = float(y)
            #     dataSet[int(freq[j]) * 10].append(
            #         [[float(x), float(y)], float(rang[j]), [cx, cy]]
            #     )

            freqDist = []
            fd = 0
            for j in dataSet:
                fd += abs(1 - j) * len(dataSet[j])
            freqDist.append([fd, 1])
            left = 0
            for i in range(2, 301):
                left += len(dataSet[i - 1])
                fd += left
                fd -= dataSetSize - left
                f = True
                for k in dataSet[i]:
                    if (k[2][0] - k[0][0]) ** 2 + (k[2][1] - k[0][1]) ** 2 <= (
                        4 * d + k[1]
                    ) ** 2:
                        f = False
                if f:
                    freqDist.append([fd, i])
            freqDist.sort(reverse=True)

            reqFreq = []

            for i in freqDist:
                f = True
                # for j in dataSet:
                # for k in dataSet[j]:
                #     if (
                #         (k[2][0] - k[0][0]) ** 2 + (k[2][1] - k[0][1]) ** 2
                #         <= (4 * d + k[1]) ** 2
                #     ) and (abs(i[1] - j) <= bandGap):
                #         f = False
                #         break
                # if not f:
                #     break
                for k in reqFreq:
                    if abs(i[1] - k) <= bandGap:
                        f = False
                if f:
                    reqFreq.append(i[1])
                if len(reqFreq) == 3:
                    break

            print(*reqFreq, sep=",")
        t2=time.time()
        execution_times.append(t2-t1)


plt.plot(execution_times)
plt.xlabel("Test Case")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time vs Test Case (Initial Approach)")
plt.grid(True)
plt.show()