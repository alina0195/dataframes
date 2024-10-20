import pandas as pd


class Stats(pd.DataFrame):
    def __init__(self, df:pd.DataFrame):
        super().__init__()
        self.df=df
    
    def get_distribution_of_texts_length(self, column_name:str):
        pass
    
    def get_frequency_of_unique_values(self, column_name: str):
        pass
    
    def plot_distribution(self, column_name:str):
        pass
    