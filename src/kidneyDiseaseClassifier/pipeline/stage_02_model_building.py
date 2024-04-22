from kidneyDiseaseClassifier.config.configuration import ConfigurationManager
from kidneyDiseaseClassifier.components.model_building import PrepareBaseModel
from kidneyDiseaseClassifier import logger

STAGE_NAME = "Model Building"


class ModelBuildingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager(
            config_filepath=r'D:\newfolder\Kidney-Disease-Classification-Deep-Learning-Project\config\config.yaml',
            params_filepath=r'D:\newfolder\Kidney-Disease-Classification-Deep-Learning-Project\params.yaml'
        )
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelBuildingPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



