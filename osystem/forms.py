import datetime
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DateTimeField, PasswordField, \
    DecimalField, FieldList, FormField, FloatField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class OrderItem(Form):
    id_product = FloatField('Codigo')
    qtd = DecimalField('Quantidade')
    product_name = StringField('Name')
    description = StringField('Description')
    price = FloatField('Valor')


class OrderForm(Form):
    order_number = DecimalField('Numero do Pedido')
    date = DateTimeField('Data', format="%Y-%m-%d %H:%M:%S", default=datetime.datetime.today)
    costumer = StringField('Cliente')
    items = FieldList(FormField(OrderItem), min_entries=1)
    add_recipient = SubmitField()
