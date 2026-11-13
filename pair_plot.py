import sys
from data_analysis import data_analysis
from data_visualization import data_visualization

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("\033[33m[WARNING]\033[0m Usage: python pair_plot.py <dataset.csv>")
        exit(1)
    data = data_analysis(sys.argv[1])
    df = data.get_dataframe()
    plot = data_visualization(title="Distribución de asignaturas por Hogwarts House")
    plot.pair_plot(df)

if __name__=="__main__":
    main()