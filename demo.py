from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation
#test pipeline
def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()

        
    except Exception as e:
        logging.error(f"{e}")
        print(e)    



if __name__=="__main__":
    main()