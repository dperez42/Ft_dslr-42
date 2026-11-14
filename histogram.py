import sys
from data_analysis import data_analysis
from data_visualization import data_visualization
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
      description=(
          "Muestra los histogramas del dataset"
      ),
      usage="python histogram.py <dataset.csv>",
    )
    parser.add_argument(
        "dataset", type=str, help="Ruta al archivo CSV del dataset"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    data = data_analysis(args.dataset)
    df = data.get_dataframe()
    plot = data_visualization("Distribución de asignaturas por Hogwarts House")
    plot.histogram(df)

if __name__=="__main__":
    main()