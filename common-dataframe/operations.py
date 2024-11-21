import pandas as pd


class Operation(pd.DataFrame):
    def __init__(self, df:pd.DataFrame):
        super().__init__()
        self.df=df
        
    def __eq__(self, df_other:pd.DataFrame)->bool:
        return self.df.equals(df_other)
    
    
    def get_common_rows_based_on_index(self, df_other:pd.DataFrame, subset_columns:list[str])->pd.DataFrame:
        if subset_columns==[]:
            print('Checking for all columns...')
            df_common = self.df[self.df.index.isin(df_other.index)]
            return df_common
        
        if (subset_columns in df_other.columns) and (subset_columns in self.df.columns):
            df_common = self.df[self.df[subset_columns]][self.df.index.isin(df_other[df_other[subset_columns]].index)]
            return df_common
        else:
            raise KeyError('Subset columns provided do no match one of dataframes columns.')
        
    
    def get_different_rows_based_on_index(self, df_other:pd.DataFrame, subset_columns:list[str])->pd.DataFrame:
        if subset_columns==[]:
            print('Considering all the columns')
            df_diff = self.df[~self.df.index.isin(df_other.index)]
        
        if (subset_columns in df_other.columns) and (subset_columns in self.df.columns):
            df_common = self.df[self.df[subset_columns]][~self.df.index.isin(df_other[df_other[subset_columns]].index)]
            return df_common
        else:
            raise KeyError('Subset columns provided do no match one of dataframes columns.')
    
    
    def has_equal_values(self, other_df:pd.DataFrame, subset_columns:list[str], show_different_rows:bool=False)->bool:
        if subset_columns==[]:
            df_concat = pd.concat([self.df,other_df], axis=0).drop_duplicates(keep=False)
        
        if (subset_columns in other_df.columns) and (subset_columns in self.df.columns):
            df_concat = pd.concat([self.df[subset_columns],other_df[subset_columns]], axis=0).drop_duplicates(keep=False)
        else:
            raise KeyError('Subset columns provided do no match one of dataframes columns.')
            
        if len(df_concat)!=0:
            if show_different_rows:
                print(df_concat)
            return False
        else:
            return True
        
        