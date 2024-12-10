from flask import Flask, render_template, request, redirect, url_for
from models import db, Product

app = Flask(__name__)

# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supermarket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db.init_app(app)

@app.route('/')
def product_list():
    products = Product.query.all()
    return render_template('list.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']

        # Создание нового товара
        new_product = Product(name=name, quantity=int(quantity))
        db.session.add(new_product)
        db.session.commit()
        
        return redirect(url_for('product_list'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

