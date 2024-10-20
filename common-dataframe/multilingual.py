import pandas as pd
# detectlang


class Linguistics(pd.DataFrame):
    def __init__(self,df:pd.DataFrame):
        super().__init__()
        self.df=df
        
    def get_nonromanian_sentences(self, column_name:str)->bool:
        pass
    
    def backtranslate(self, column_name:str, new_column_name:str, src_lang:str, tgt_lang:str)->bool:
        pass
    
    def backtranslate_with_two_languages(self,column_name:str, new_column_name:str, src_lang:str, additional_lang:str, tgt_lang:str)->bool:
        pass
    
    