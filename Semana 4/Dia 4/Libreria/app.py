from flask import Flask
from config.base_datos import bd
app = Flask(__name__)
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
#                                    formato://username:password@host:port/databasename
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost:3306/flasklibreria'
print(app.config)

if __name__ == '__main__':
    app.run(debug=True)
