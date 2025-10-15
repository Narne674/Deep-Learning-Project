import os
import sys
from Xray.exception import XRayException

class S3Operation:

    def sync_folder_to_s3()->None:
        try:
            pass
            os.system("aws s3 sync ./Xray s3://xray-logs-bucket --exclude '*.pyc' --exclude '__pycache__/*'")
        except Exception as e:
            raise XRayException(e, sys) from e
        
    def sync_s3_to_folder()->None:
        try:
            pass
        except Exception as e:
            raise XRayException(e, sys) from e