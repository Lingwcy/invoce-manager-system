from flask import Blueprint, request,jsonify
from flask_cors import CORS
# from paddle.incubate.autograd.primops import select

from orm.repo.invoice_repo import InvoiceRepo
# 实例化蓝图对象，参数一类似于蓝图对象的名称
# 一个app下的蓝图对象不可重名
new_list = Blueprint('invoice_api',__name__)
CORS(new_list)

# 蓝图对象的使用和app类似
# 一个蓝图下的视图函数名、endpoint不可重复
@new_list.route('/invoice', methods=['GET', 'POST'])
def invoice():
    if request.method == 'GET':
        invoice_code = request.args.get('invoice_code')
        invoice_number = request.args.get('invoice_number')
        if invoice_code is not None or invoice_number is not None:
            invoices = InvoiceRepo.query(invoice_code=invoice_code,invoice_number=invoice_number)
            return jsonify(invoices)
        else:
            invoices = InvoiceRepo.query()
            return jsonify(invoices)

    elif request.method == 'POST':
        pass


