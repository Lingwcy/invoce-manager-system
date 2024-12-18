import pdfplumber
from orm.invoice import Invoice
# 发票代码(470,0 , 576, 40)
# 发票号码(470,20 , 576, 60)
# 开票日期(470,40 , 576, 70)
# 校验码(470,60 , 576, 80)
# 购买方名称(110,80 , 220, 100)
# 购买方纳税人识别号(110,100 , 220, 120)
# 密码区(360,80 , 610, 130)
# 税率(470,160 , 504, 180)
# 税额(560,160 , 590, 180)
# 合计(450,240 , 480, 270)
# 价税合计(505,240 , 530, 288)
# 销售方名称(105,288 , 350, 310)
# 销售方纳税人识别号(105,310 , 350, 330)
# 销售方地址、电话(105,320 , 350, 340)
# 销售方开户行及账号(105,330 , 350, 350)


class InvoiceExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.fields = {
            'invoice_code': (470, 0, 576, 40),
            'invoice_number': (470, 30, 576, 60),
            'invoice_date': (470, 40, 576, 70),
            'verification_code': (470, 60, 576, 80),
            'buyer_name': (110, 80, 220, 100),
            'buyer_tax_id': (110, 100, 220, 120),
            'password_zone': (360, 80, 610, 130),
            'tax_rate': (470, 160, 504, 180),
            'tax_amount': (560, 160, 590, 180),
            'total_amount': (450, 240, 480, 270),
            'total_tax_amount': (505, 240, 530, 288),
            'seller_name': (105, 288, 350, 310),
            'seller_tax_id': (105, 310, 350, 330),
            'seller_address_phone': (105, 320, 350, 340),
            'seller_bank_account': (105, 330, 350, 350),
        }

    def extract_invoice(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            first_page = pdf.pages[0]
            invoice = Invoice()
            for field, coords in self.fields.items():
                page_area = first_page.within_bbox(coords)
                text = page_area.extract_text()
                if text:
                    setattr(invoice, field, text.strip())
            invoice.file_path = self.pdf_path
            return invoice

# # 使用示例
# pdf_path = '../out/20241010143314_20201223__1/91510100633168022E_937083446ff948eba0b1f6a46a88ed52.pdf'
# extractor = InvoiceExtractor(pdf_path)
# invoice = extractor.extract_invoice()
#
#
# print(invoice)