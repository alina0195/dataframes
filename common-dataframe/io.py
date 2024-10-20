import pandas as pd
import json


class Cast(pd.DataFrame):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def read_and_cast_json(self, file_name: str)->pd.DataFrame:
        pass
    
    
    @staticmethod        
    def dict2dataframe(self, dict_obj: dict)->pd.DataFrame:
        pass
    
    @staticmethod        
    def json2dataframe(self, json_obj: json)->pd.DataFrame:
        pass
    
    @staticmethod        
    def save(self, df: pd.DataFrame, path: str)->bool:
        pass