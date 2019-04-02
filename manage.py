from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flaskblog import db
import app

migrate = Migrate(app, db)

manager = Manager(app, db)
manager.add_command('db', MigrateCommand)
if __name__ == '__main':
    manager.run()
