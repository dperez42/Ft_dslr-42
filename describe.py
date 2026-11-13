import sys
from data_analysis import data_analysis

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("\033[33m[WARNING]\033[0m Usage: python describe.py <dataset.csv>")
        sys.exit(1)
    try:
        load_data = data_analysis(sys.argv[1])
        load_data.describe()
        text_col, num_col = load_data.count_type_columns()
        print(f"Columnas Texto: {text_col}, Numéricas: {num_col}")
        df = load_data.get_dataframe()
        print("Data example of numerical columns:")
        print(df[0:2])
        sys.exit(0)
    except FileNotFoundError:
      print(f"\033[1;31m[ERROR]\033[0m File '{sys.argv}' not found.")
      sys.exit(1)
    except Exception as e:
        print(f"\033[1;31m[ERROR]\033[0m {e}")
    sys.exit(1)
if __name__=="__main__":
    main()
    
