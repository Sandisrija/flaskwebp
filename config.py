import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'local_dev_secret_key')

    # Blob storage configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT', 'images04')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER', 'images')

    # SQL Database configuration
    SQL_SERVER = os.environ.get('SQL_SERVER', 'cms-project.database.windows.net')
    SQL_DATABASE = os.environ.get('SQL_DATABASE', 'cms')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME', 'cmsadmin')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD', 'CMS4dmin')

    # Encode password for safe URI usage
    password = quote_plus(SQL_PASSWORD)

    # ✔ CORRECT SQLAlchemy connection string for Azure SQL + pyodbc
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{password}@{SQL_SERVER}:1433/"
        f"{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MS Authentication
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

    AUTHORITY = "https://login.microsoftonline.com/common"

    CLIENT_ID = os.getenv("CLIENT_ID")

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
