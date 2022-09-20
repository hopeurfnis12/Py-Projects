from flask import render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create_test', methods=['POST', 'GET'])
def create_test():
    if request.method == "POST":
        title = request.form['title']
        text = request.form['text']

        article = Article(title = title, text = text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "ERROR CREATE"
    else:
        return render_template("create_test.html")


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>')
def detail(id):
    article = Article.query.get(id)
    return render_template("detail.html", article=article)


@app.route('/posts/<int:id>/delete')
def delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "ERROR DELETE"


@app.route('/posts/<int:id>/upd', methods=['POST', 'GET'])
def upd(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.text = request.form['text']

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "ERROR UPD"
    else:
        article = Article.query.get(id)
        return render_template("upd.html", article=article)


if __name__ == "__main__":
    app.run(debug=True)
