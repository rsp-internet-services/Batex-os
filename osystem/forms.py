from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DateTimeField, PasswordField, DecimalField, FieldList, TextField, FormField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class OrderItem(Form):
    code = StringField('Title')
    description = StringField('description')


class OrderForm(Form):
    order_number = DecimalField('Numero do Pedido')
    date = DateTimeField('Data')
    costumer = StringField('Cliente')
    items = FieldList(FormField(OrderItem), min_entries=2)
