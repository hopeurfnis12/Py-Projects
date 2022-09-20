from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(main)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(400), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == "POST":
        title = request.form['title']
        text = request.form['text']

        article = Article(title = title, text = text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/all')
        except:
            return "1"
    else:
        return render_template("new.html")


@main.route('/all')
def all():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("all.html", articles=articles)


@main.route('/all/<int:id>')
def detail(id):
    article = Article.query.get(id)
    return render_template("detail.html", article=article)


@main.route('/all/<int:id>/delete')
def delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/all')
    except:
        return "2"


@main.route('/all/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.text = request.form['text']

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/all')
        except:
            return "3"
    else:
        article = Article.query.get(id)
        return render_template("edit.html", article=article)


if __name__ == "__main__":
    main.run(debug=True)
