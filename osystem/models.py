from osystem import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    user_name = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)  # python 2

    def authenticate_user(self):
        return User.query.filter_by(username=self.username, password=self.password).first()

    def __repr__(self):
        return '<User %r, id %r>' % (self.username, self.id)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    price = db.Column(db.Float)


class OrderItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_order = db.Column(db.Float, db.ForeignKey('order.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return '<Order_item %r, Order %r>' % (self.id, self.id_order)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime)
    costumer = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_items = db.Column(db.Integer, db.ForeignKey('order_items.id'))

    def __repr__(self):
        return '<Order %r>' % (self.id)
