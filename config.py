import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gdfsrgehkjdbcjdsgfhkgkhfgdhgfyug'

    # Values for Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'images11'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'zSZjzn12q08qOyfv5briVYoy8badQR9If2J+8Yr8xwNjBXBUTqAPLiFGDWFDBXpbMvv+P2abM0I7+AStrnlL1Q=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Values for Azure SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsc14.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # The client secret from your App Registration
    CLIENT_SECRET = "lKr8Q~~RnuuOopYPNqfNdNgXTkWenbA9loV2qbMg"

    # The authority URL, which includes your tenant ID
    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"

    # The client ID from your App Registration
    CLIENT_ID = "c439e07a-c4c5-45c4-b663-d89f06430479"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session

