# Clase linear_regression
import sys
from data_analysis import data_analysis

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python describe.py <dataset.csv>")
        exit(1)
    load_data = data_analysis(sys.argv[1])
    load_data.describe()
    #load_data.describe(False)
    print(load_data.get_feature_list())
    print(load_data.get_columns_type())
    exit()
if __name__=="__main__":
    main()
    
