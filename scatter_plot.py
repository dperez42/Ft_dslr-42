import sys
from data_analysis import data_analysis
from data_visualization import data_visualization
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
      description=(
          "Muestra el scatter plot entre features del dataset"
      ),
      usage="python histogram.py <dataset.csv> feature1 feature2",
    )
    parser.add_argument(
        "dataset", type=str, help="Ruta al archivo CSV del dataset"
    )
    parser.add_argument(
        "feature1", type=str, help="Nombre de la primera feature"
    )
    parser.add_argument(
        "feature2", type=str, help="Nombre de la primera feature"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    data = data_analysis(args.dataset)
    df = data.get_dataframe()
    plot = data_visualization(title="Distribución de asignaturas por Hogwarts House")
    plot.scatter(df, feature1=args.feature1,feature2=args.feature2)

if __name__=="__main__":
    main()