from flask import render_template
from app import app
from app.models.orders_list import orders
from app.models.tracker_list import trackers

@app.route('/')
def index():
    return render_template('index.html', title='Home', orders=orders, index=index)

@app.route('/orders/<index>')
def order_page(index):
    order = orders[int(index)]
    tracker = trackers[int(index)]
    return render_template('order.html', title='Orders', order=order, index=index, trackers=trackers)

@app.route('/trackers/<index>')
def tracker_page(index):
    tracker = trackers[int(index)]
    return render_template('tracker.html', title='Tracker', tracker=tracker, index=index)
