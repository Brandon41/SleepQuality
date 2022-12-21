#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Import dependencies such as numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#!pip install pyexcel

import pyexcel as pe
import pyexcel.ext.xls

# Make a global 2-D array ( the rows will store the column of the data, the number of features, while the columns will store each of the values of the particular feature)

#Matrix = [[]]

#Rows_total = 2
# Make a global 2-D array that will store the x and y values for the cluster center for each cluster. 
K = 0
m = 0
n = 0

def Cluster( K, array = [m][n]):
    
    #Col_total = len(array[0])
    #K = 4
    Rows_total = len(array)
    Temp_array = [ 0 for i in range(Rows_total)]
    Temp_array2 = [ 0 for i in range(K)]
    Answer_1 = 0
    array_1 = np.array(array).T
    #**print("Print array_1")
    #**print(array_1)
    Col_total = len(array_1)
    #**print("print Col_total")
    #**print(Col_total)
    num_array = []
    count_7 = 0
    
    
    Keep = []
    Temp_array12 = []
    Temp_array23 = []
    Sum_1 = 0
    Sum_2 = 0
    #Rows_total = 2
    #K = 2
    check = True
    
    Answer_2 = 0
    
    print('the number of rows in the array is', Rows_total)
    Min_value = [Rows_total]
    Max_value = [Rows_total]
    rows, cols = (K, Rows_total)
    Cluster_array = [[0 for i in range(cols)] for j in range(rows)]
    #KMeans_array = [[0 for i in range(cols)] for j in range(rows)]
    KMeans_array = [[] for i in range(K)]
    
    Min_value = np.max(array, axis = 1)
    Max_value = np.min(array, axis = 1)
    
    count = 0
    count_1 = 0
    while count < K:
        count_1 = 0
        while count_1 < Rows_total:
            Cluster_array[count][count_1]= round(random.uniform(Min_value[count_1],Max_value[count_1] ), 2)
            count_1 += 1
        count += 1
        
    count = 0
    count_1 = 0
    

    #print("print Cluster_array")
    #print(Cluster_array)
        
    count_8 = 0
    while count_8 < 50:
        
        #print("")
        #print("Count_8 is", count_8)
        
        #KMeans_array = [[],[]]
        KMeans_array = [[] for i in range(K)]
        
        count = 0
        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0
        while count < Col_total:
            count_1 = 0
            while count_1 < K:
                count_2 = 0
                while count_2 < Rows_total:
                    #print("count_2 is ", count_2, "count_1 is ", count_1, " count is", count)
                    #print("Cluster_array")
                    #print(Cluster_array)
                    #print("array")
                    #print(array)
                    
                    #print("print out array_1 at that index")
                    #print(array_1[count][count_2])
                    
                    #print("print out Cluster_array at that index")
                    #print(Cluster_array[count_1][count_2])
                    
                    Answer_2 = (array_1[count][count_2] - Cluster_array[count_1][count_2]) ** 2
                    #print("print Answer_2")
                    #print(Answer_2)
                    Temp_array[count_2] = float("{0:.2f}".format(Answer_2))
                    count_2 += 1
                
                #print("Temp_array")
                #print(Temp_array)
                
                Answer_1 =  sum(Temp_array)
                Answer_1 = math.sqrt(Answer_1)
                Answer_1 = float("{0:.2f}".format(Answer_1))
                Temp_array2[count_1] = Answer_1
                #count_1 += 1
                if count_1 == (K - 1):
                    min_value = min(Temp_array2)
                    min_index =Temp_array2.index(min_value)
                    count_3 = 0
                    while count_3 < Rows_total:
                        KMeans_array[min_index].append( array_1[count][count_3] )
                        count_3 += 1
                count_1 += 1
            count += 1
        
        #print("print KMeans_array")
        #print(KMeans_array)
        
        ###
        count = 0
        count_1 = 0
        #Cluster_array = [[] for i in range(K)]
     
        
        while count < len(KMeans_array):
            Sum_1 = len(KMeans_array[count])
            Sum_1 = Sum_1/Rows_total
            Keep.append(Sum_1)
            count += 1
        #print("print out Keep array")
        #print(Keep)
        
        
        
        count = 0
        #count_1 keeps track of features
        count_1 = 0
    
        
        count_2 = 0
        count_3 = 0
        count_7 = 0
        
        count_4 = 0
        count_5 = 0
        count_6 = 0
        while count < K:
            count_1 = 0
            while count_1 < Rows_total:
                count_2 = 0
                if count_1 > 0:
                    count_2 = count_1
                while count_2 < len(KMeans_array[count]):
                    Temp_array12.append(KMeans_array[count][count_2])
                    count_2 += Rows_total
                count_1 += 1
            #print("Print Temp_array12 at K = ", count)
            #print(Temp_array12)
            #print("print Keep array")
            #print(Keep)
            
            
            #print("length of Temp_array12")
            #print(len(Temp_array12))
            count_5 = 0
            count_4 = 0
            while count_4 < len(Temp_array12):
                if check == False:
                    count_5 = 0
                    check = True
        
                Temp_array23.append(Temp_array12[count_4])
                
                if count_5 == (Keep[count] - 1):    
                    
                    #print("Print Temp_array23 at K = ", count)
                    Sum_2 = sum(Temp_array23) / len(Temp_array23)
                    Sum_2 = float("{0:.2f}".format(Sum_2))
                    
                    
                    Cluster_array[count][count_7] = Sum_2
                    count_7 += 1
                    
                    #print(Temp_array23)
                    #print("print Temp_array23 mean", Sum_2)
                    Temp_array23 = []
                    check = False
                    count_5 = 0
                count_5 += 1
                count_4 += 1
    
            Temp_array12 = []
            count_7 = 0
            #print("")
            count += 1
        
        Keep = []
        
        #**if count_8 == 49:
            #**print("KMeans_array")
            #**print(KMeans_array)
        #**print("print out Cluster_array", Cluster_array)
        ####
        count_8 += 1
    
    
    
    count= 0
    count_1 = 0
    count_3 = 0
    count_4 = 0
    All = 0
    while count < len(KMeans_array):

        if len(KMeans_array[count]) != 0:
           #**print("-------------------","Cluster is", count + 1)
            count_4 = 1
            count_1 = 0
            while count_1 < len(KMeans_array[count]):
                
                #**print("Dimentions for Feature set", count_4)
                if count_1 == 0:
                    count_3 = 0

                if count_3 > 0:
                    count_3 = count_1
                    #print("---")
                    
                count_4 += 1
                All = count_3 + 2
                
                while count_3 < All  and count_3 < len(KMeans_array[count]) :
                    #**print(KMeans_array[count][count_3])
                    count_3 += 1
                    count_1 += 1
        count += 1
    
    #**print("KMeans_array")
    #**print(KMeans_array)
    #**print("print Cluster_array")
    #**print(Cluster_array)
    
    
    col = ['green', 'blue', 'orange', 'red', 'yellow', 'brown', 'black', 'gray', 'magenta', 'cyan']
    
    
    if Rows_total == 2:
        count= 0
        count_1 = 0
        count_2 = 0
        var = 0
        var_1 = 0
    
        while count < len(KMeans_array):
    
            count_2 = 0
            while count_2 < len(Cluster_array[count]) and count_2 != (len(Cluster_array[count]) -1):
                var_1 = count_2
                var_1 += 1
                plt.scatter(Cluster_array[count][count_2],Cluster_array[count][var_1], marker = "^", color = col[count] ) 
                count_2 += 2
    
            if len(KMeans_array[count]) != 0:
        
                count_1 = 0
                while count_1 < len(KMeans_array[count]) and count_1 != (len(KMeans_array[count]) -1) :
                    var = count_1
                    var += 1
                    plt.scatter(KMeans_array[count][count_1], KMeans_array[count][var], c = col[count], s = 10, linewidth = 0)
                    
                    count_1 += 2
            count += 1
    
        plt.xlabel('swsLengthM')
        plt.ylabel('epochCapacity')
        plt.title('K-Means Graph')
        plt.show()
    
    return Rows_total, array_1, KMeans_array
    

    
    
    
    

def Dunn_index(Feature, arr = [m][n]):
    
    print("Feature is", Feature)
    print("KMeans_array is")
    print(arr)
    
    
    Temp_array = [0 for i in range (Feature)]
    Temp_array2 = [0 for i in range (Feature)]
    Temp_array3 = [0 for i in range (Feature)]
    Temp_array4 = [0 for i in range (Feature)]
    value = 0
    value_1 = 0
    Numerator = []
    min_value = 100
    storage = 0
    storage_1 = 0
    check = False
    check_1 = False
    count = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    while count < len(arr):
        count_1 = 0
        count_3 = 0
        min_value = 0
        while count_1 < len(arr[count]) :
            if check == True:
                count_2 += 1
            if count == 0 or check == False:
                check = True
            Temp_array[count_2] = arr[count][count_1]
            if count_2 == (Feature - 1):
                check = False
                count_2 = 0
                count_3 = count + 1
       
                while count_3 < len(arr):
                    count_4 = 0
                    min_value = 100
                    while count_4 < len(arr[count_3]):
                        if check_1 == True:
                            count_5 += 1
                        if count_4 == 0 or check_1 == False:
                            check_1 = True
                        Temp_array2[count_5] = arr[count_3][count_4]
                        if count_5 == (Feature -1):
                            count_5 = 0
                            check_1 = False
                            Temp_array3 = np.subtract(Temp_array, Temp_array2)
                            Temp_array4 = np.square(Temp_array3)
                            storage_1 = sum(Temp_array4)
                            if storage_1 < min_value:
                                min_value = storage_1
                            if count_4 == (len(arr[count_3]) - 1) :
                                Numerator.append(min_value)
                                min_value = 100
                        count_4 += 1
                    count_3 += 1
            count_1 += 1
        count += 1
    
    value = max(Numerator)


    check_3 = False
    check_4 = False
    Ans = 0
    Max = 0
    temp = [0 for i in range(Feature)]
    temp_1 = [0 for i in range(Feature)]
    temp_2 = [0 for i in range(Feature)]
    Deno = []
    count = 0
    count_1 = 0
    count_2 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    while count < len(arr):
        count_1 = 0
    
        while count_1 < len(arr[count]):

            if check_3 == True:
                count_2 += 1
            
            if count_1 == 0 or check_3 == False:
                check_3 = True
        
     
            temp[count_2] = arr[count][count_1]
        
            if count_2 == (Feature - 1):
                count_2 = 0
                check_3 = False
            
                count_5 = 0
                count_4 = count_1 + 1
            
                while count_4 < len(arr[count]):
      
                    if check_4 == True:
                        count_5 += 1
                    
                    if count_5 == 0 or check_4 == True:
                        check_4 = True
        
                    temp_1[count_5] = arr[count][count_4]
                
                    if count_5 == (Feature - 1):
                        count_5 = 0
                        check_4 = False
                        temp_2 = np.subtract(temp, temp_1)
                   
                        temp_2 = np.square(temp_2)
                        Ans = sum(temp_2)
                        if Ans > Max:
                            Max = Ans
                
                    count_4 += 1
            if count_1 == (len(arr[count]) - 1):
                Deno.append(Max)
                Max = 0
        
            count_1 += 1
    
        count += 1
    
    value_1 = max(Deno)
    
    value_1 = value/value_1
    value_1 = math.sqrt(value_1)
    value_1 = float("{0:.2f}".format(value_1))
    
    return value_1

    
def Fuzzy(K, arr = [m][n]):
    
    rows = len(arr)
    data_point = rows
    
    columns = len(arr[0])
    Feature = columns
    
    Box_1 =  [[0 for i in range(data_point)] for j in range(K)]
    
    
    
    print("columns in arr is", columns)
    
    
    
    
    
    
    


    
    


def main():
    #First you read the data from the data table (DF stands for data frame):
    DF = pd.read_excel('SleepQuality.xlsx')
    print(DF)

    #Convert the column you want from the dataframe, DF, into an array:
    #Array_1 = DF[["swsLengthM: 6"]].to_numpy()
    #Array_2 = DF[["epochCapacity: 12"]].to_numpy()
    
    Array_1 = DF.loc[:,'swsLengthM']
    #print('print out Array_1', Array_1)
    
    Array_2 = DF.loc[:,'epochCapacity']
    

    #append matrix two to the end of matrix one, and so on when you have more features. 
    Total_array = np.append(Array_1, Array_2)
    print("total array")
    print(Total_array)
    
    
    #You can define a list containing two lists as follows:

    #arr = [[],[]]
    #Or to define a longer list you could use:

    #arr = [[] for _ in range(5)]
    #or
    #arr[[], [], [], [], []]
    
    Matrix = [[],[]]
    

    #Get the length of the array
    Array_length = len(Array_1)
    print('print out the length of the array', Array_length)
    
    Feature = 2
    K = 2

    count = 0
    count_1 = 0
    count_2 = 0
    while count < Feature:
        count_1 = 0
        while count_1 < Array_length:
            Matrix[count].append(Total_array[count_2])
            count_2 += 1
            count_1 += 1
        count += 1
    
    Rows_total = len(Matrix)
    #print("total rows")
    #print(Rows_total)
    
    #print("print out the Matrix")
    #print(Matrix)

    Cluster(K, Matrix)
    
    array_4 = [0 for i in range(9)]
    Don = 0
    count_1 = 0
    count = 2
    while count < 11:
        (Feature,array_set, arr) = Cluster(count, Matrix)
        Don = Dunn_index(Feature, arr)
        array_4[count_1] = Don
        count_1 += 1
        count += 1
    
    print("print array_4")
    print(array_4)
    plt.scatter([2,3,4,5,6,7,8,9,10], array_4)
    plt.xlabel('K')
    plt.ylabel('Dunn_index value')
    plt.title('Dunn Index Graph')
    plt.show()
    
    
    Fuzzy(K, array_set)
    
    print("Hello World")

name = "main"
if name=="main":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




