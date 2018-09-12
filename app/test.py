from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Set the path
import os, sys
sys.path.append(os.path.abspath
                (os.path.join(os.path.dirname(__file__), '..')))
app = Flask(__name__)
app.config.from_object('app.settings')
db = SQLAlchemy(app)
class Aaa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Integer)


@app.route('/thread/<int:page_num>')
def thread(page_num):
    threads = Aaa.query.paginate(per_page=5, page=page_num, error_out=False)

    return render_template('thr.html', threads=threads)

if __name__ == '__main__':
    app.run(debug=True)