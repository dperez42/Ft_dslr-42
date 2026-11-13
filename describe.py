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
    
      
    text_col, num_col = load_data.count_type_columns()
    print(f"Columnas Texto: {text_col}, Numéricas: {num_col}")
    
    df = load_data.get_dataframe()
    print("Data example of numerical columns:")
    print(df[0:2])
    exit()
if __name__=="__main__":
    main()
    
