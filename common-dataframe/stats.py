import pandas as pd


class Stats(pd.DataFrame):
    def __init__(self, df:pd.DataFrame):
        super().__init__()
        self.df=df
    
    def get_distribution_of_texts_length(self, column_name:str):
        self.df['len'] = self.df[column_name].apply(lambda x: len(x.split(' ')))
        return self.get_frequency_of_unique_values(column_name='len')
        
    def get_frequency_of_unique_values(self, column_name: str):
        return self.df[column_name].value_counts()
    
    def plot_distribution(self, column_name:str):
        pass
    
    def plot_confusion_map(self, column_name_src:str, column_name_tgt:str, title:str):
        import matplotlib as plt
        import seaborn as sns
        plt.subplots(figsize=(4,4))
        df_2hist = pd.DataFrame({
            x_label: grp[column_name_src].value_counts() for x_label, grp in self.df.groupby(column_name_tgt)
            
        })
        sns.heatmap(df_2hist, cmap='viridis')
        plt.xlabel(column_name_tgt)
        _ = plt.ylabel(column_name_src)
        plt.title(title)
        plt.show()
        