# https://github.com/LahlouS/ft_dslr/blob/main/submission/dataloader.py
# https://github.com/rutgercap/ft_dslr/blob/main/src/describe.py


import  csv
import  sys
import  os.path
import  matplotlib.pyplot as plt
from pathlib import Path
from array import array
import math
import pandas as pd

class data_analysis:

    def __init__(self, filename="") :

        # init parameters
        self.size = {0, 0}
        self.data_raw = []
        self.data = []
        self.nb_features = 0
        self.features_names = []
        self.columns_type = [] # tipo columna 1 number 0 not number
        self.filename = filename
        self.check_csv()
        self.load_csv()

    def check_csv(self):
        # Check if file is correct
        check_file = Path(self.filename)
        # check file exist
        if check_file.is_file()== False:
            sys.exit("Error: File {:} not exist".format(check_file))
        # check file permission
        if (os.access(check_file, os.R_OK) == False) :
            sys.exit("Error:    Access denied for " + check_file)
        # check extension of the file
        if check_file.suffix != '.csv':
            sys.exit("Error: File {:} has to be a csv".format(check_file))
    
    def load_csv(self):
        with open(self.filename, 'r') as csv_file:
            try:
                dict_val = csv.reader(csv_file, delimiter = ",")
                for row in dict_val:
                    self.data_raw.append(row)
            except:
                sys.exit("Error: File {:} cannot be read".format(csv_file))
        self.set_column_type()
        #load data 
        num_filas = len(self.data_raw)
        num_columnas = len(self.data_raw[0])
        self.nb_features = num_columnas
        i = 0
        while i < num_filas:
            rowlist = []
            for j in range(num_columnas): # Recorre los índices de columna (0, 1, 2)
                # getting names
                if (i == 0):
                    self.features_names.append(self.data_raw[i][j])
                    rowlist.append(self.data_raw[i][j])
                    #print(i, self.data_raw[i][j], self.features_names)
                # getting values
                if (i > 0):
                    #print(f"Elemento en [{i}][{j}]: {self.data_raw[i][j]}")
                    #print(type(self.data_raw[i][j]))
                    try:
                        rowlist.append(float(self.data_raw[i][j]))
                    except:
                        if (self.columns_type[j]==0):
                            rowlist.append(self.data_raw[i][j])
                        else:
                            rowlist.append(float('nan'))
                        #sys.exit("Error: ")
            self.data.append(rowlist)
            i = i + 1
        #print(self.data[1]) 
        #print(len(self.data))
        print("Read ", num_filas, " rows from ", self.filename)
    
    def clean_nan_data(self):
        #print(self.data[1])
        clean_data = []
        num_filas = len(self.data)
        num_columnas = len(self.data[1])
        i = 0
        while i < num_filas :
            # getting names
            if (i == 0):
                #print("ll", self.data[i])
                clean_data.append(self.data[i])
            else:
                # getting not nan values in numerical
                is_nan = False
                #print(self.columns_type)
                for j in range(num_columnas): # Recorre los índices de columna (0, 1, 2)
                    # getting names
                    #print(" check row:", i, " colum", j, " type:",self.columns_type[j])
                    if self.columns_type[j] == 1: # is a numerical feature
                        # check is not nan
                        if math.isnan(self.data[i][j]) == True:
                            is_nan = True                
                        #print(i, self.data_raw[i][j], self.features_names)
                #if is_nan:
                    #print("no insert", i, self.data[i])
                if is_nan == False:  # si no hay nan añadelo
                    #print("insert", i, self.data[i])
                    clean_data.append(self.data[i])
            i = i+1
        self.data = clean_data
        #print(self.data)
        #print(self.data[1]) 
        print("Cleaned ",num_filas-len(self.data), " of ", num_filas, " rows. Total remain: ", len(self.data))

    def set_column_type(self):
        num_columnas = len(self.data_raw[0])
        self.columns_type = []
        for j in range(num_columnas): # Recorre los índices de columna (0, 1, 2)
            # getting values
            #print("Checking :",j, self.data_raw[1][j])
            try:
                l = float(self.data_raw[1][j])
                self.columns_type.append(1)
            except:
                self.columns_type.append(0)

    def get_column(self, mat, nb_col):
        columnlist = []
        num_filas = len(mat)
        #print(type(mat))
        #print("num", num_filas)
        i = 1
        while i < num_filas:
            #print("aa",i, type(i))
            for j in range(self.nb_features): 
                if (j==nb_col):
                    columnlist.append(mat[i][j])
            i = i +1
        #print("ll",self.data[1][1])   
        #print("ll",mat[i-1])       
        #print("ll",mat[1][0]) 

        #print("ll",mat[1600][18]) 
        #print(columnlist)
        return columnlist
    
    def print_data(self) :
        for row in self.data:
            for column in row:
                print (column, end="\t")
            print ("")
    
    def describe(self, only_numbers=True):
        ancho = 11
        # Titles
        i = 0
        parameter = "Feature"
        print(f'{parameter:{ancho}}',end="")
        while i < self.nb_features:
            feature_name = self.features_names[i]
            if len(feature_name)>ancho:
                feature_name = feature_name[0:ancho-3]+'..'
            if only_numbers:
                if self.columns_type[i]==1:
                    print(f'{feature_name:>{ancho}}',end="")
            else:
                print(f'{feature_name:>{ancho}}',end="")
            i = i + 1
        print()
        # Count
        i = 0
        parameter = "Count"
        print(f'{parameter:<{ancho}}',end="")
        while i < self.nb_features:
            if only_numbers:
                test= self.get_column(self.data,i)
                if self.columns_type[i]==1:
                    print(f'{self.count(test, self.columns_type[i]):>{ancho}.3f}',end="")
            else:
                print(f'{self.count(test, self.columns_type[i]):>{ancho}.3f}',end="")
            i = i + 1
        print()
        # Mean
        i = 0
        parameter = "Mean"
        print(f'{parameter:<{ancho}}',end="")
        while i < self.nb_features:
            if only_numbers:
                test= self.get_column(self.data,i)
                if self.columns_type[i]==1:
                    print(f'{self.mean(test, self.columns_type[i]):>{ancho}.3f}',end="")
            else:
                print(f'{self.mean(test, self.columns_type[i]):>{ancho}.3f}',end="")
            i = i + 1
        print()
        # Mean
        i = 0
        parameter = "Std"
        print(f'{parameter:<{ancho}}',end="")
        while i < self.nb_features:
            if only_numbers:
                test= self.get_column(self.data,i)
                if self.columns_type[i]==1:
                    print(f'{self.std(test, self.columns_type[i]):>{ancho}.3f}',end="")
            else:
                print(f'{self.std(test, self.columns_type[i]):>{ancho}.3f}',end="")
            i = i + 1
        print()
        # Min
        i = 0
        parameter = "Min"
        print(f'{parameter:<{ancho}}',end="")
        while i < self.nb_features:
            if only_numbers:
                test= self.get_column(self.data,i)
                if self.columns_type[i]==1:
                    print(f'{self.values_min(test, self.columns_type[i]):>{ancho}.3f}',end="")
            else:
                print(f'{self.values_min(test, self.columns_type[i]):>{ancho}.3f}',end="")
            i = i + 1
        print()
        # 25%
        i = 0
        parameter = "25%"
        print(f'{parameter:<{ancho}}',end="")
        while i < self.nb_features:
            if only_numbers:
                test= self.get_column(self.data,i)
                if self.columns_type[i]==1:
                    print(f'{self.percentile(test, 25, self.columns_type[i]):>{ancho}.3f}',end="")
            else:
                print(f'{self.percentile(test, 25, self.columns_type[i]):>{ancho}.3f}',end="")
            i = i + 1
        print()
         # 50%
        i = 0
        parameter = "50%"
        print(f'{parameter:<{ancho}}',end="")
        while i < self.nb_features:
            if only_numbers:
                test= self.get_column(self.data,i)
                if self.columns_type[i]==1:
                    print(f'{self.percentile(test, 50, self.columns_type[i]):>{ancho}.3f}',end="")
            else:
                print(f'{self.percentile(test, 50, self.columns_type[i]):>{ancho}.3f}',end="")
            i = i + 1
        print()
         # 75%
        i = 0
        parameter = "75%"
        print(f'{parameter:<{ancho}}',end="")
        while i < self.nb_features:
            if only_numbers:
                test= self.get_column(self.data,i)
                if self.columns_type[i]==1:
                    print(f'{self.percentile(test, 75, self.columns_type[i]):>{ancho}.3f}',end="")
            else:
                print(f'{self.percentile(test, 75, self.columns_type[i]):>{ancho}.3f}',end="")
            i = i + 1
        print()

        # Max
        i = 0
        parameter = "Max"
        print(f'{parameter:<{ancho}}',end="")
        while i < self.nb_features:
            if only_numbers:
                test= self.get_column(self.data,i)
                if self.columns_type[i]==1:
                    print(f'{self.values_max(test, self.columns_type[i]):>{ancho}.3f}',end="")
            else:
                print(f'{self.values_max(test, self.columns_type[i]):>{ancho}.3f}',end="")
            i = i + 1
        print()
        return()
    # Custom count function
    def count(self,values,type) -> float:
        nb = len(values)
        count = 1.0
        i  = 1
        while i < nb:
            if type==0:
                count = count +1
            else:
                try:
                    if math.isnan(values[i])==False:
                        count = count + 1
                except:
                    count = count +1
            i = i + 1
        return int(count)
    # Custom mean function
    def mean(self,values, type) -> float:
        if type==0:
            return float("nan")
        n = 1.0
        sum = 0.0
        nb = len(values)
        i  = 1
        while i < nb:
            try:
                if math.isnan(values[i])==False:
                    sum = sum + float(values[i])
                    n = n + 1
            except:
                l = 0
            i = i + 1
        if n == 1:
            return float("nan")
        return (sum) / n
    # Custom stnard deviation function
    def std(self,values, type) -> float:
        if type==0:
            return float("nan")
        mean = self.mean(values, type)
        n = 1
        sum_of_squares = 0.0
        nb = len(values)
        i  = 1
        while i < nb:
            try:
                if math.isnan(values[i])==False:
                    error = values[i] - mean
                    error = error**2
                    sum_of_squares += error
                    n += 1
            except:
                l = 0
            i = i + 1
        if n == 0:
            return float("nan")
        #print("std:", sum_of_squares, n, i)
        return math.sqrt(sum_of_squares / n)
    # Custom min function
    def values_min(self,values, type) -> float:
        if type==0:
            return float("nan")
        min_value = float("inf")
        n = 0
        for value in values:
            try:
                if value < min_value:
                    min_value = value
                    n = n + 1
            except:
                l = 0
        if n == 0:
            min_value = float("nan")
        return min_value
    # Custom max function
    def values_max(self, values, type) -> float:
        if type==0:
            return float("nan")
        max_value = float("-inf")
        n = 0
        for value in values:
            try:
                if value > max_value:
                    max_value = value
                    n = n + 1
            except:
                l = 0
        if n == 0:
            max_value = float("nan")
        return max_value
    # Custom percentile function
    def percentile(self, values, percentage: int, type) -> float:
        if type==0:
            return float("nan")
        filtered_values = []
        nb = len(values)
        i  = 0
        while i < nb:
            try:
                if math.isnan(values[i])==False:
                    filtered_values.append(values[i])
            except:
                l = 0
            i = i + 1
        
        if len(filtered_values) == 0:
            return float("nan")
        sorted_values = sorted(filtered_values)
        position = (percentage / 100) * len(sorted_values)
        if position == 0:
            return sorted_values[0]
        elif position == len(sorted_values):
            return sorted_values[-1]
        if position.is_integer():
            return sorted_values[int(position) - 1]
        lower_index = int(position)
        upper_index = lower_index + 1
        fractional_part = position - lower_index
        return (sorted_values[lower_index] * (1 - fractional_part)) + (
            sorted_values[upper_index] * fractional_part
        )

    # getters
    def get_feature_list(self):
        return self.features_names
    
    def get_number_feature(self):
        return (self.nb_features)
    
    def get_column_by_index(self, nb_col):
        columnlist = []
        num_filas = len(self.data)
        #print(type(mat))
        #print(self.nb_features, num_filas)
        i = 0
        while i < num_filas:
            #print("aa",i, type(i))
            for j in range(self.nb_features): 
                if (j==nb_col):
                    columnlist.append(self.data[i][j])
            i = i +1
        #print("ll",self.data[1][1])   
        #print("ll",mat[i-1])       
        #print("ll",mat[1][0]) 

        #print("ll",mat[1600][18]) 
        #print(columnlist)
        return columnlist
    
    def get_columns_by_index_list(self, list_col):
        row_list = []
        num_filas = len(self.data)
        i = 0
        while i < num_filas:
            column_list=[]
            for j in list_col: 
                #if (j>10):
                column_list.append(self.data[i][j])
            i = i +1
            row_list.append(column_list)
        return row_list
    
    def get_columns_type(self):
        return (self.columns_type)
    
    def get_data(self):
        return (self.data)

    def get_dataframe(self):
        columnas = self.get_feature_list()
        df = pd.DataFrame(self.data, columns=columnas)
        # Eliminar primera fila
        df = df.iloc[1:].reset_index(drop=True)
        df.drop(columns=["Index","First Name","Last Name","Birthday","Best Hand"], inplace=True)
        return (df)

    def count_type_columns(self):
        zeros = self.columns_type.count(0)
        ones = self.columns_type.count(1)
        return zeros, ones