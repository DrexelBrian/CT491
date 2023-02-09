from abc import abstractclassmethod
from ast import Dict
from collections import defaultdict
from typing import Any
import uuid

from elasticsearch import Elasticsearch
import pandas as pd

class Ingest:
    
    
    def __init__(self, name: str, index: str):
        self.name = name
        self.index = index
        
        self.es = ElasticSearch('http://localhost:9200')
    
    @abstractclassmethod
    def normalize(self , data: ...):
       raise NotImplementedError
    
    
    def extract(self, data):
        print('Inside extract')
        
    def transform(self, data) -> ...:
        """
        This layer is responsible for extracting out column headers, data cleaning & any misc tasks 
        that are needed
        :param data Dataframe
        Returns Dataframe
        """
        if len(data) <= 0 or data is None:
            self.logger.info('Failed to extract properly')

       
        transform_doc: Dict[str, Any] = defaultdict(str, Any)
        
        df = pd.DataFrame(data)
        column_headers = list(df.columns.values)

        df.fillna('No data provided at this time', inplace=True)
        df.columns = column_headers
        
        results = self.normalize_df(df) 
        transform_doc = {
            'MAIN_DATA': results,
            'ID': uuid.uuid4().hex 
        }
        
        print(transform_doc)

        return transform_doc, column_headers

    
    
    def load(self, data, name) -> None:
        """
            :param data Dictionary
            Returns None
        """
        print('start the loading phase')
        self.es.indicies.create(index='project_name', data=data)
        return None
    

