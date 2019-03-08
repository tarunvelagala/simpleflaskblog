from flaskblog import create_app
from flaskblog import db

app = create_app()
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
