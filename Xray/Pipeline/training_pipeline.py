import sys
from Xray.Components.data_ingestion import DataIngestion
from Xray.Entity.artifact_entity import DataIngestionArtifact
from Xray.Entity.config_entity import DataIngestionConfig
from Xray.exception import XrayException
from Xray.logger import logging


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
        def start_data_ingestion(self) -> DataIngestionArtifact:
            logging.info("Entrered the start_data_ingestion method of TrainPipeline class")
        try:
            
            logging.info("Getting the data from the s3 buckets")

            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train_set and test_set from the s3 bucket")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
        
            return data_ingestion_artifact
        
        except Exception as e:
            raise XrayException(e, sys)

if __name__ == "__main__":
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.start_data_ingestion()
    except Exception as e:
        print(e)