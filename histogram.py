import sys
from data_analysis import data_analysis
from data_visualization import data_visualization

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python histogram.py <dataset.csv>")
        exit(1)
    data = data_analysis(sys.argv[1])
    data.describe()
    #print(data.get_feature_list())
    #print(data.get_number_feature())
    plot = data_visualization()
    #print(data.get_column_by_index(0),data.get_column_by_index(11))
    plot.scatter(data.get_column_by_index(0),data.get_column_by_index(11) )
    plot.histogram()
    plot.pair()
if __name__=="__main__":
    main()