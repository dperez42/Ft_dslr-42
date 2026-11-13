import sys
from data_analysis import data_analysis
from ft_dslr import LogisticRegression

import numpy as np
import pandas as pd

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python logreg_train.py <dataset.csv>")
        exit(1)
    # Cargo los datos y los separo en Y (classes) y X (features)
    data = data_analysis(sys.argv[1])        #data.describe()
    data.describe()
    list_features = [6,7,8,9,10,11,12,13,14,15,16,17,18]
    list_category = 1  
    y_train = data.get_column_by_index(list_category)
    X_train = data.get_columns_by_index_list(list_features)
    print(X_train[0])
    model = LogisticRegression()
    model.load_model("model.json")  
    model.test(X_train, y_train)

if __name__=="__main__":
    main()