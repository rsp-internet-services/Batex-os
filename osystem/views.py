from osystem import app, lm, db
from flask import render_template, flash, redirect, session, url_for, request, g, flash
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, OrderForm
from .models import User, Order, OrderItems


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
            login_user(user, remember=False)
            return redirect(request.args.get('next') or url_for('index'))
        else:
            flash("Invalid Login")
            return redirect(url_for('login'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    form = OrderForm()
    form.order_number.data = 1
    if form.add_recipient.data:
        form.items.append_entry()

    if request.method == 'POST':
        order = Order()
        order.timestamp = form.date.data
        order.costumer = form.costumer.data
        db.session.add(order)
        db.session.commit()
        for item in form.items.data:
            order_items = OrderItems()
            order_items.id_order = order.id
            order_items.id_product = item['id_product']
            db.session.add(order_items)
            db.session.commit()

        order.order_items = order_items.id
        db.session.commit()
        flash(order.id)

    return render_template('order_form.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
