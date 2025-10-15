from datetime import datetime
from typing import List

import torch

TIMESTAMP: datetime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

ARTIFACT_DIR: str = "artifact"

BUCKET_NAME: str = "xray-pipeline"

S3_DTA_FOLDER: str = "data"

CLASS_LABEL_1: str = "NORMAL"
CLASS_LABEL_2: str = "PNEUMONIA"