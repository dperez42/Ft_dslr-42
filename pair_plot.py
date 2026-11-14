import sys
from data_analysis import data_analysis
from data_visualization import data_visualization
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
      description=(
          "Muestra el pait_plot del dataset"
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
    plot = data_visualization(title="Distribución de asignaturas por Hogwarts House")
    plot.pair_plot(df)

if __name__=="__main__":
    main()