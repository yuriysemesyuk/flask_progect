class Configuration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:@db/postgres'
    SECRET_KEY = "mysecertkey"

    ###flask_security
    SECURITY_PASSWORD_SALT = "salt"
    SECURITY_PASSWORD_HASH = "sha512_crypt"
