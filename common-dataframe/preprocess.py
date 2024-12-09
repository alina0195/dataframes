from typing import Union
import pandas as pd

class Preprocess(pd.DataFrame):
    
    def __init__(self, df: pd.DataFrame):
        super().__init__()
        self.df = df
        
    def has_duplicated_rows(self)->bool:
        pass
    
    def delete_duplicated_rows(self)->bool:
        pass
    
    def have_duplicated_values(self, column_1: str, column_2: str)->bool:
        pass
    
    def delete_duplicated_values(self, column_1: str, column_2: str)->bool:
        pass
    
    def delete_null_rows(self)->bool:
        pass
    
    def has_null_values(self, column_name:str)->bool:
        pass
    
    def delete_null_values(self, column_name:str, inplace=True)->bool:
        pass

    def concatenate_rows(self, second_df:pd.DataFrame, inplace=True)->bool:
        pass
    
    def concatenate_columns(self, second_df:pd.DataFrame, inplace=True)->bool:
        pass

    def delete_shorter_content(self, column_name: str, min_tokens:int, inplace=True)->bool:
        pass

    def apply_transformation_on_rows(self, column_name:str, func: function):
        pass
    
    def delete_rows_based_on_column_values(self, column_name:str, values:list):
        """
        Usually works for values as list of integers (eg. values=ids)
        """
        if column_name not in self.df.columns:
            raise NameError('Column not found')
        try:
            self.df = self.df[~self.df[column_name].isin(values)]
        except Exception as e:
            print(f'Could not delete values {values} from column <<{column_name}>>:', str(e))
    
    
    def delete_extra_spaces(self, column_name:str)->bool:
        pass
    
    def delete_urls(self, column_name:str)->bool:
        pass
    
    def delete_ro_diacritics(self, column_name:str)->bool:
        pass
    
    
    def add_prompt(self, column_name:str)->bool:
        pass
    
    def find_rows(self, column_name:str, pattern:Union[str, int])->pd.DataFrame:
        pass
