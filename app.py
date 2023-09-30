from flask import Flask
from utils.db import db
from routes.contact import contact
from config import DATABASE_CONNECTION

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
app.config['SQLALCHEMY_MAX_OVERFLOW']=-1 #NO sabemos cuantos se van a conectar

db.init_app(app)
app.register_blueprint(contact)

if __name__ == "__main__":
    app.run(debug=True)
