import matplotlib.pyplot as plt
import math
import sys

class data_visualization:

    def __init__(self, title = "Title") :
        # init parameters
        self.title = title
        
    def histogram(self, df):
        label_col = df.columns[0]  # Hogwarts House
        features = df.columns[1:]  # resto de columnas
        houses = sorted(df[label_col].dropna().unique())
        
        cols = 4
        rows = math.ceil(len(features) / cols)
        fig, axes = plt.subplots(rows,cols,figsize=(16, 12))
        fig.canvas.manager.set_window_title("Histogram")
        axes = axes.flatten()
        
        for i, feature in enumerate(features):
                # Una distribución por casa
                for label in houses:
                        values = df.loc[df[label_col] == label,feature].dropna()
                        axes[i].hist(values,bins=30,alpha=0.5,label=label)
                axes[i].set_title(feature, fontsize=12)
                axes[i].set_ylabel("Frecuencia")
                axes[i].legend(fontsize=6)
        # Eliminar subplots sobrantes
        for i in range(len(features), len(axes)):
                axes[i].axis("off")
        fig.suptitle(self.title,fontsize=16)
        plt.tight_layout()
        plt.show()

    def pair_plot(self, df):
        label_col = df.columns[0]   # Hogwarts House
        features = df.columns[1:]   # asignaturas
        n = len(features)
        fig, axes = plt.subplots(n,n,figsize=(24, 24)) #,constrained_layout=True)
        fig.canvas.manager.set_window_title("Pair Plot")
        houses = sorted(df[label_col].dropna().unique())
        for row, feature_y in enumerate(features):
                for col, feature_x in enumerate(features):
                        ax = axes[row, col]
                        # Diagonal: histograma
                        if row == col:
                                for house in houses:
                                        values = df.loc[df[label_col] == house,feature_x].dropna()
                                        ax.hist(values,bins=20,alpha=0.4,label=house)
                        # Resto: scatter
                        else:
                                for house in houses:
                                        data = df[df[label_col] == house]
                                        ax.scatter(data[feature_x], data[feature_y], s=5, alpha=0.5, label=house)
                        # Nombre de columnas arriba
                        if row == 0:
                                ax.set_title(feature_x, fontsize=6, rotation=0)
                        # Nombre de filas a la izquierda
                        if col == 0:
                                ax.set_ylabel(feature_y, fontsize=6)
                        ax.tick_params(axis="both", labelsize=6)
        # Crear leyenda única arriba
        handles, labels = axes[0, 0].get_legend_handles_labels()
        fig.suptitle(self.title, x=0.02, y=0.98, ha="left", fontsize=18)
        fig.legend(handles,labels,loc="upper right",bbox_to_anchor=(0.98, 0.985),ncol=len(houses),fontsize=11,frameon=True,)
        plt.subplots_adjust(top=0.93, bottom=0.04, left=0.04, right=0.98, hspace=0.25, wspace=0.25)
        plt.show()

    def scatter(self, df, feature1, feature2):
        valid_features = [col for col in df.columns if col != "Hogwarts House"]
        if feature1 not in valid_features or feature2 not in valid_features:
                print("\033[1;31m[ERROR]\033[0m Alguna de las asignaturas no existe en el dataset.")
                print(f"   Recibido : '{feature1}', '{feature2}'")
                print(f"   Válidas  : {', '.join(valid_features)}")
                sys.exit(1)
        houses =sorted(df["Hogwarts House"].dropna().unique()) 
        plt.figure(figsize=(10, 6))
        for house in houses:
                df_feature1 = df[feature1][df['Hogwarts House']==house]   # asignaturas
                df_feature2 = df[feature2][df['Hogwarts House']==house]   # asignaturas
                plt.scatter(df_feature1, df_feature2, alpha=0.5, label=house)
        plt.title(f"{feature1} vs {feature2}", fontsize=14)
        plt.xlabel(feature1, fontsize=11)
        plt.ylabel(feature2, fontsize=11)
        plt.legend(title="Hogwarts House")
        plt.grid(True, linestyle="--", alpha=0.3)
        plt.tight_layout()
        plt.show()


        
                



                