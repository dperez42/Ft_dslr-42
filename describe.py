import sys
from data_analysis import data_analysis
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
      description=(
          "Calcula estadísticas descriptivas de un dataset CSV (estilo"
          " pandas.describe)."
      ),
      usage="python describe.py <dataset.csv>",
    )
    parser.add_argument(
        "dataset", type=str, help="Ruta al archivo CSV del dataset"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        load_data = data_analysis(args.dataset)
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
    
