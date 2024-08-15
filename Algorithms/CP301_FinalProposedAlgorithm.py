import csv
import time
import matplotlib.pyplot as plt

execution_times=[]

bandGap = 5
with open("D:/Downloads/CP301_Data/testCase.csv",mode="r") as testcases:
    csv1=csv.reader(testcases)
    testcase=0
    for lines in csv1:
        t1=time.time()
        testcase+=1
        print("TestCase: ",testcase)
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
            distances = dict(zip([i for i in range(1, 31)], [[] for i in range(30)]))
            candidates=set()
            for i in range(1,31):
                candidates.add(i)
            types = ["new_dense", "new_sparse","new_medium"]
            with open(
                f"D:/Downloads/CP301_Data/{types[file_name]}.csv",
                mode="r",
            ) as file:
                csvFile = csv.reader(file)
                for line in csvFile:
                    if len(line) > 0 and line[0] != "X":
                        cx,cy=closest_coord(int(float(line[0])), int(float(line[1])))
                        dist=(int(float(line[0])-cx))**2+(int(float(line[1])-cy))**2
                        distances[int(line[2])].append(dist)
                        if dist<=(4*d+int(float(line[4])))**2:
                            for j in range(int(line[2])-bandGap//2,1+int(line[2])+bandGap//2):
                                candidates.discard(j)
            # candidates.add(1)
                            

            # dataSet = dict(zip([i for i in range(810, 1120, 10)], [[] for i in range(31)]))
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

            # freqDist = []
            # for i in range(1, 301):
            #     f = True
            #     for k in dataSet[i]:
            #         if (k[2][0] - k[0][0]) ** 2 + (k[2][1] - k[0][1]) ** 2 <= (
            #             4 * d + k[1]
            #         ) ** 2:
            #             f = False
            #     if f:
            #         fd = 0
            #         for j in dataSet:
            #             for k in dataSet[j]:
            #                 fd += abs(i - j) * (
            #                     ((k[2][0] - k[0][0]) ** 2) + ((k[2][1] - k[0][1]) ** 2)
            #                 )
            #         freqDist.append([fd, i])

            # freqDist.sort(reverse=True)
            candidates=list(candidates)
            score=[0]
            total=0
            cur=0
            front=0
            back=0
            for i in range(1,31):
                for j in distances[i]:
                    total+=abs(1-i)*j
                    if i==1:
                        back+=j
                    else:
                        front+=j
            cur=total
            score.append(cur)
            for i in range(2,31):
                cur+=back
                cur-=front
                for j in distances[i]:
                    back+=j
                    front-=j
                score.append(cur)


            reqFreq = []
            req=3
            i=0
            j=len(candidates)-1

            while req and i<=j:
                f=0
                if score[candidates[i]]>score[candidates[j]]:
                    f=candidates[i]
                    i+=1
                else:
                    f=candidates[j]
                    j-=1
                for k in reqFreq:
                    if abs(f-k)<=bandGap:
                        f=0
                        break
                if f!=0:
                    reqFreq.append(f)
                    req-=1
            if file_name==0:
                print("Channelss for Dense Distribution: ",end="")
            if file_name==1:
                print("Channelss for Sparse Distribution: ",end="")
            if file_name==2:
                print("Channelss for Medium Density Distribution: ",end="")
            reqFreq.sort()
            print(*reqFreq, sep=",")
        t2=time.time()
        execution_times.append(t2-t1)
                


            # for i in freqDist:
            #     f = True
            #     # for j in dataSet:
            #     #     for k in dataSet[j]:
            #     #         if (
            #     #             (k[2][0] - k[0][0]) ** 2 + (k[2][1] - k[0][1]) ** 2
            #     #             <= (4 * d + k[1]) ** 2
            #     #         ) and (abs(i[1] - j) <= bandGap):
            #     #             f = False
            #     #             break
            #     #     if not f:
            #     #         break
            #     for k in reqFreq:
            #         if abs(i[1] - k) <= bandGap:
            #             f = False
            #     if f:
            #         reqFreq.append(i[1])
            #     if len(reqFreq) == 10:
            #         break
            # 
            # print(*reqFreq, sep=",")
plt.plot(execution_times)
plt.xlabel("Test Case")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time vs Test Case (Proposed Algorithm)")
plt.grid(True)
plt.show()