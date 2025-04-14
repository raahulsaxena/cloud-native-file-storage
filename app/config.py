import os

class Config:
    """
    Configuration class for Flask app and AWS S3 settings.
    """

    # Flask settings
    DEBUG = False
    TESTING = False

    # AWS credentials and S3 bucket config
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
    AWS_REGION = os.getenv('AWS_REGION')
