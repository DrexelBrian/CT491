from Ingest.Ingest import Ingest

class Utilities(Ingest):    
    def execute(self, data, data_source_name) -> None:
        """
            This is the execution loop for the extraction
            :param data is a Dataframe that represents the data that is to be 
            ingested. It will go through several layers before persisting
            First we ingest the CSV and create a dataframe based on that
            We then do data cleaning within the transform layer and do checks along the way
            Return None
        """
        while True:
            try:
                # extract
                extraction_data = self.extract(data)
                print(f'Extraction Data-->{extraction_data}')
                # transform
                transfom_data, _ = self.transform(extraction_data)
                print(f'Transofrmed Data-->{transfom_data}')
                # load
                tx = self.load(transfom_data, data_source_name)

                if tx is None:
                    break
            except StopIteration:
                break