"""
        Unsupervised Learning

        We have data but we do not have label

        k-means Clustering :)
        k denotes number of classes which we want to achieve

        X    Y   P


        1    1   A
        1    0   B
        0    2   C
        2    4   D
        3    5   E


     Step1:
        Assume 2 centroids randomly for two clusters/classes
        eg.A(1,1) and C(0,2)

     Step2:
        Compute distance of all the points from each centroid
        Euclidean Distance Formula->sqrt[(x2-x1)**2 + (y2-y1)**2)]

     -------------------------------------
     P      C1(1,1)           C2(0,2)
     -------------------------------------
     A         0               1.4
     B         1               2.2
     C         (1.4)sqrt(2)    0
     D         (3.2)sqrt(10)   2.8
     E         (4.5)sqrt(20)   4.2


     Step3:
        Arrange points as per the distance from the centroids

        P  NearestTo
        A    C1
        B    C1
        C    C2
        D    C2
        E    C2

    Step4:

         X    Y   P  NearestTo


        1    1   A    C1
        1    0   B    C1
        0    2   C    C2
        2    4   D    C2
        3    5   E    C2

        Re-check again with new centroids of the created new clusters
        Cluster Mean
        CM1 = (1+1)/2, (1+0)/2
        CM2 = (0+2+3)/3, (2+4+5)/3

        CM1 = (1, 0.5)
        CM2 = (1.7, 3.7)


      -------------------------------------
     P      CM1(1,0.5)           CM2(1.7,3.7)
     -------------------------------------
     A         .5                   2.7
     B         .5                   3.7
     C         1.8(sqrt(3.25))      2.4
     D         3.6                  0.5
     E         4.9                  1.9




        X    Y   P  NearestTo


        1    1   A    CM1
        1    0   B    CM1
        0    2   C    CM1
        2    4   D    CM2
        3    5   E    CM2


     Redo the same steps till we donot get the same clusters


     CM3 = (1+1+0)/3, (1+0+2)/3
     CM4 = (2+4)/2, (4+5)/2


     CM3 = (0.66, 1)
     CM4 = (3, 4.5)


      CM3           CM4     NearestT0
    A  0.34        4.03        CM3
    B   1.05       4.93        CM3




"""
import matplotlib.pyplot as plt
X = [1, 1, 0, 2, 3]
Y = [1, 0, 2, 4, 5]
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.scatter(X, Y)
# plt.plot(X, Y)
plt.show()

