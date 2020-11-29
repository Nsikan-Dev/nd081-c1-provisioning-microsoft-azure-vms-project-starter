import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'nuproject1storage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '+ocjJeji324m5iIfuTx+YIFtP0Y+6pSgEnYkvh6P7d+32J+FlRQYljas+nEgKUCMWetNrar3/fsSrg9xDGZGdg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'nu-project1-dev-container'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'nu-project1-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'nu-project1-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'adminuser'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Sh@ka_6ula'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "P.hX7n0tPimAfC-~S_vd41j---Ab4iD0-R"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "bf53abc5-ea9b-4ba9-a1da-ce8aaf6a6bac"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session