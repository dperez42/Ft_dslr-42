import  matplotlib.pyplot as plt
import math

class data_visualization:

    def __init__(self, title = "Title") :

        # init parameters
        self.size = {0, 0}
        self.data = []
        self.nb_features = 0
        self.title = title

        
    def histogram(self, df):
        label_col = df.columns[0]  # Hogwarts House
        features = df.columns[1:]  # resto de columnas
        cols = 4
        rows = math.ceil(len(features) / cols)
        fig, axes = plt.subplots(
                rows,
                cols,
                figsize=(16, 12)
        )
        fig.canvas.manager.set_window_title("Histogram")
        axes = axes.flatten()
        for i, feature in enumerate(features):
                # Una distribución por casa
                for label in df[label_col].dropna().unique():
                        values = df.loc[
                                df[label_col] == label,
                                feature
                        ].dropna()
                        axes[i].hist(
                                values,
                                bins=30,
                                alpha=0.5,
                                label=label
                        )
                axes[i].set_title(feature, fontsize=12)
                #axes[i].set_xlabel("Valor")
                axes[i].set_ylabel("Frecuencia")
                axes[i].legend(fontsize=6)
        # Desactivar subplots sobrantes
        for i in range(len(features), len(axes)):
                axes[i].axis("off")
        fig.suptitle(
                self.title,
                fontsize=16
        )
        plt.tight_layout()
        plt.show()

    def pair_plot(self, df):
        label_col = df.columns[0]   # Hogwarts House
        features = df.columns[1:]   # asignaturas

        n = len(features)
        fig, axes = plt.subplots(
                n,
                n,
                figsize=(24, 24),
                constrained_layout=True
        )
        fig.canvas.manager.set_window_title("Pair Plot")
        houses = df[label_col].dropna().unique()
        for row, feature_y in enumerate(features):
                for col, feature_x in enumerate(features):
                        ax = axes[row, col]
                        # Diagonal: histograma
                        if row == col:
                                for house in houses:
                                        values = df.loc[df[label_col] == house,feature_x].dropna()
                                        ax.hist(
                                                values,
                                                bins=20,
                                                alpha=0.4,
                                                #color=colors.get(house),
                                                label=house
                                        )
                        # Resto: scatter
                        else:
                                for house in houses:
                                        data = df[df[label_col] == house]
                                        ax.scatter(
                                                data[feature_x],
                                                data[feature_y],
                                                s=5,
                                                alpha=0.5,
                                                #color=colors.get(house),
                                                label=house
                                        )

                        # Nombre de columnas arriba
                        if row == 0:
                                ax.set_title(
                                feature_x,
                                fontsize=6,
                                rotation=0
                                )

                        # Nombre de filas a la izquierda
                        if col == 0:
                                ax.set_ylabel(
                                feature_y,
                                fontsize=6
                                )

                        ax.tick_params(
                                axis="both",
                                labelsize=6
                        )

        fig.suptitle("Relación entre las asignaturas por Hogwarts House",fontsize=18)
        plt.show()

    def scatter(self, df):
                label_col = df.columns[0]   # Hogwarts House
                features = df.columns[1:]   # asignaturas

                n = len(features)
                fig, axes = plt.subplots(
                        n,
                        n,
                        figsize=(24, 24),
                        constrained_layout=True
                )
                fig.canvas.manager.set_window_title("Pair Plot")
                houses = df[label_col].dropna().unique()
                #colors = {
                #        "Ravenclaw": "blue",
                #        "Slytherin": "green",
                #        "Gryffindor": "red",
                #        "Hufflepuff": "orange"
                #}
                for row, feature_y in enumerate(features):
                        for col, feature_x in enumerate(features):
                                ax = axes[row, col]
                                # Diagonal: histograma
                                if row != col:
                                       for house in houses:
                                                data = df[df[label_col] == house]
                                                ax.scatter(
                                                        data[feature_x],
                                                        data[feature_y],
                                                        s=5,
                                                        alpha=0.5,
                                                        #color=colors.get(house),
                                                        label=house
                                                )

                                # Nombre de columnas arriba
                                if row == 0:
                                        ax.set_title(
                                        feature_x,
                                        fontsize=8,
                                        rotation=0
                                        )

                                # Nombre de filas a la izquierda
                                if col == 0:
                                        ax.set_ylabel(
                                        feature_y,
                                        fontsize=8
                                        )

                                ax.tick_params(
                                        axis="both",
                                        labelsize=6
                                )

                fig.suptitle(
                        "Relación entre las asignaturas por Hogwarts House",
                        fontsize=18
                )

                plt.tight_layout()
                plt.show()

        
                



                