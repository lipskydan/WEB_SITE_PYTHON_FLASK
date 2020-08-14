from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# БД - Таблица - Записи
# Таблица:
# id    title    price      isActive
# 1     Some      100         True
# 2     Some2     200         False
# 3     Some3     300         True


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    # text = db.Colum(db.Text, nullable=False)

    def __repr__(self):
        return f'Запись: {self.title}'


@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/addItem', methods=['POST', 'GET'])
def addItem():
    if request.method
    return render_template('addItem.html')


@app.route('/delItem')
def delItem():
    return render_template('delItem.html')


if __name__ == "__main__":
    app.run(debug=True)