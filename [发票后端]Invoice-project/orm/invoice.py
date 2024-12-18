from sqlalchemy import create_engine, Column,DECIMAL, String, DateTime, Float, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from orm.config import engine
# 创建一个基类
Base = declarative_base()

class Invoice(Base):
    __tablename__ = 'invoice'  # 定义表名

    # 定义表的列和类型
    id = Column(BigInteger, primary_key=True,autoincrement=True)
    invoice_code = Column(BigInteger, nullable=True)
    invoice_number = Column(String(255), nullable=True)
    invoice_date = Column(String(255),nullable=True)
    verification_code = Column(String(255), nullable=True)
    buyer_name = Column(String(255), nullable=True)
    buyer_tax_id = Column(String(255), nullable=True)
    password_zone = Column(String(255), nullable=True)
    tax_rate = Column(String(10), nullable=True)
    tax_amount = Column(DECIMAL(10,2), nullable=True)
    total_amount = Column(DECIMAL(10,2), nullable=True)
    total_tax_amount = Column(DECIMAL(10,2), nullable=True)
    seller_name = Column(String(255), nullable=True)
    seller_tax_id = Column(String(255), nullable=True)
    seller_address_phone = Column(String(255), nullable=True)
    seller_bank_account = Column(String(255), nullable=True)
    file_path = Column(String(255), nullable=True)

    # 定义初始化方法
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        return (f"发票代码: {self.invoice_code}\n"
                f"发票号码: {self.invoice_number}\n"
                f"开票日期: {self.invoice_date}\n"
                f"校验码: {self.verification_code}\n"
                f"购买方名称: {self.buyer_name}\n"
                f"购买方纳税人识别号: {self.buyer_tax_id}\n"
                f"密码区: {self.password_zone}\n"
                f"税率: {self.tax_rate}\n"
                f"税额: {self.tax_amount}\n"
                f"合计: {self.total_amount}\n"
                f"价税合计: {self.total_tax_amount}\n"
                f"销售方名称: {self.seller_name}\n"
                f"销售方纳税人识别号: {self.seller_tax_id}\n"
                f"销售方地址、电话: {self.seller_address_phone}\n"
                f"销售方开户行及账号: {self.seller_bank_account}\n"
                f"文件存储路径: {self.file_path}\n")
    @staticmethod
    def getdata(self):
        return {
            'id': self.id,
            'invoice_code': self.invoice_code,
            'invoice_number': self.invoice_number,
            'invoice_date': self.invoice_date,
            'verification_code': self.verification_code,
            'buyer_name': self.buyer_name,
            'buyer_tax_id': self.buyer_tax_id,
            'password_zone': self.password_zone,
            'tax_rate': self.tax_rate,
            'tax_amount': str(self.tax_amount),
            'total_amount': str(self.total_amount),
            'total_tax_amount': str(self.total_tax_amount),
            'seller_name': self.seller_name,
            'seller_tax_id': self.seller_tax_id,
            'seller_address_phone': self.seller_address_phone,
            'seller_bank_account': self.seller_bank_account,
            'file_path': self.file_path,
        }
# Base.metadata.create_all(engine)
#
# # 创建会话类
# Session = sessionmaker(bind=engine)
#
# # 创建会话实例
# session = Session()
#
# # 示例：添加一个新的Invoice对象到数据库
# new_invoice = Invoice(
#     invoice_code="1234567890",
#     invoice_number="INV001",
#     invoice_date=datetime.datetime.now(),
#     # ... 其他属性 ...
#     file_path="/path/to/invoice.pdf"
# )
#
# session.add(new_invoice)
# session.commit()
