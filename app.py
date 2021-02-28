from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config
from flask_security import SQLAlchemySessionUserDatastore, Security, SQLAlchemyUserDatastore

# app config
app = Flask(__name__)
app.config.from_object(Config)

# db init
db = SQLAlchemy(app)

# import late due to circular error
from models import *

# migration init
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# admin config
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))

# flask security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.errorhandler(404)
def page_not_found(event):
    return render_template('404.html'), 404