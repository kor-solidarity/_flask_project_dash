from app import app
from flask import render_template, url_for
from article.models import Article


@app.route('/board/<int:page_num>')
def dashboard(page_num):
    if not page_num:
        page_num = 1

    threads = Article.query.paginate(page=page_num, error_out=False)

    return render_template('index.html', threads=threads)
