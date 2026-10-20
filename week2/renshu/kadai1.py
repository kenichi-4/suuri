import time
import numpy as np

n = 100
A = [[float(i + j) for j in range(n)] for i in range(n)]
B = [[float(i + j) for j in range(n)] for i in range(n)]
C = [[float(0) for j in range(n)] for i in range(n)]

start_time = time.perf_counter()
##############################################
######### Python の 2 次元リストによる行列積 ##########
##############################################



##############################################
end_time = time.perf_counter()
print(end_time - start_time, " [sec]")

A = np.array(A)
B = np.array(B)

start_time = time.perf_counter()

##############################################
############## Numpy による行列積 ###############
##############################################


##############################################

end_time = time.perf_counter()
print(end_time - start_time, " [sec]")
