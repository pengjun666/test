from flask import Blueprint

blu_order = Blueprint('order', __name__)

@blu_order.route('/order/list')
def order_list():
    return 'order_list'