# -*- coding: utf-8 -*-
from python_cli_skeleton import app, db
from python_cli_skeleton.cron import Cron
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

manager.add_command("runserver", Server(use_debugger=app.config['DEBUG'],
                                        use_reloader=app.config['RELOAD'],
                                        host=app.config['HOST'],
                                        port=int(app.config['PORT'])))
manager.add_command('cron', Cron)

if __name__ == "__main__":
    manager.run()
