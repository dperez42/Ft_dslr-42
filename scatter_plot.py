import sys
from data_analysis import data_analysis
from data_visualization import data_visualization

def main():
    args = sys.argv[1:]
    if len(args) != 3:
        print("\033[33m[WARNING]\033[0m Usage: python scatter_plot.py <dataset.csv> feature1 feature2")
        exit(1)
    data = data_analysis(args[0])
    df = data.get_dataframe()
    plot = data_visualization(title="Distribución de asignaturas por Hogwarts House")
    plot.scatter(df, feature1=args[1],feature2=args[2])

if __name__=="__main__":
    main()