from flask import jsonify
from sqlalchemy.orm import sessionmaker
# from orm.t_invoice import Invoice
import json
from orm.invoice import Invoice
from orm.config import engine
class InvoiceRepo:
    # @staticmethod
    # def add(invoice_dto, t_invoice = Invoice()):
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
    #     # 将DTO对象的属性值赋给Invoice对象
    #     t_invoice.id = invoice_dto.id
    #     t_invoice.number = invoice_dto.number
    #     t_invoice.date = invoice_dto.date
    #     t_invoice.check_number = invoice_dto.check_number
    #     t_invoice.machine_number = invoice_dto.machine_number
    #     t_invoice.buyer_name = invoice_dto.buyer_name
    #     t_invoice.buyer_taxpayer_identification_number = invoice_dto.buyer_taxpayer_identification_number
    #     t_invoice.buyer_address_number = invoice_dto.buyer_address_number
    #     t_invoice.buyer_bank_account = invoice_dto.buyer_bank_account
    #     t_invoice.password = invoice_dto.password
    #     t_invoice.total_price = invoice_dto.total_price or '0.00'
    #     t_invoice.seller_name = invoice_dto.seller_name
    #     t_invoice.seller_taxpayer_identification_number = invoice_dto.seller_taxpayer_identification_number
    #     t_invoice.seller_address_number = invoice_dto.seller_address_number
    #     t_invoice.seller_account_number = invoice_dto.seller_account_number
    #     t_invoice.receiver = invoice_dto.receiver
    #     t_invoice.checker = invoice_dto.checker
    #     t_invoice.drawer = invoice_dto.drawer
    #     # 将Invoice对象添加到会话中
    #     session.add(t_invoice)
    #     # 提交会话以保存数据到数据库
    #     session.commit()
    #     # 关闭会话
    #     session.close()

    @staticmethod
    def query(invoice_code=None, invoice_number=None):
        # 创建会话
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(Invoice)

        if invoice_code:
            query = query.filter(Invoice.invoice_code == invoice_code)
        if invoice_number:
            query = query.filter(Invoice.invoice_number == invoice_number)

        invoices = query.all()
        data_list = []
        for invoice in invoices:
            data_list.append(Invoice.getdata(invoice))
        json_string = json.dumps(data_list, indent=4, ensure_ascii=False)
        # 关闭会话
        session.close()
        return json_string

    from sqlalchemy.orm.exc import NoResultFound

    @staticmethod
    def add(invoices):
        Session = sessionmaker(bind=engine)
        session = Session()
        flag = False
        for invoice in invoices:
            # 检查数据库中是否已存在相同的invoice_code和invoice_number
            existing_invoice = session.query(Invoice).filter_by(invoice_code=invoice.invoice_code,
                                                                invoice_number=invoice.invoice_number).first()
            if existing_invoice is None:
                # 如果不存在，添加到会话中
                session.add(invoice)
                flag = True
            else:
                # 如果存在，可以选择抛出异常或者进行其他处理
                print(
                    f"上传过程存在重复发票: 代码 {invoice.invoice_code} 号码: {invoice.invoice_number}. 跳过...")
                flag = False
        # 提交会话并关闭
        try:
            session.commit()
            return flag
        except Exception as e:
            # 如果提交失败，可以在这里处理异常，例如回滚会话
            session.rollback()
            print(f"异常: {e}")
        finally:
            session.close()

