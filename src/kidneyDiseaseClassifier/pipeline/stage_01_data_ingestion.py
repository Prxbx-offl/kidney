

from kidneyDiseaseClassifier.config.configuration import ConfigurationManager
from kidneyDiseaseClassifier.components.data_ingestion import DataIngestion
from kidneyDiseaseClassifier import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager(
            config_filepath=r'D:\newfolder\Kidney-Disease-Classification-Deep-Learning-Project\config\config.yaml',
            params_filepath=r'D:\newfolder\Kidney-Disease-Classification-Deep-Learning-Project\params.yaml'
        )
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

