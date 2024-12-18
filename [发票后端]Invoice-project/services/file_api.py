import shutil
from distutils.command.config import config

from flask import Blueprint, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from orm.repo.invoice_repo import InvoiceRepo
from utils.Extractor import InvoiceExtractor
from utils.utils import find_filenames_with_length
import os
from datetime import datetime
from utils.exractPDF import process_zip_files
import io
import zipfile
# 实例化蓝图对象，参数一类似于蓝图对象的名称
# 一个app下的蓝图对象不可重名
new_list = Blueprint('file_api',__name__)
CORS(new_list)

# 蓝图对象的使用和app类似
# 一个蓝图下的视图函数名、endpoint不可重复
@new_list.route('/upload', methods=['POST'])
def upload_and_process_file():
    if 'file' not in request.files:
        return '没有文件部分', 400
    file = request.files['file']
    if file.filename == '':
        return '没有选择文件', 400
    if file:
        # 获取当前时间并格式化为字符串
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        # 原始文件名
        filename = secure_filename(file.filename)
        # 在文件名上添加时间戳
        new_filename = f"{timestamp}_{filename}"
        # 保存文件
        file.save(os.path.join('../uploads', new_filename))
        process_zip_files('../uploads', '../out')
        #寻找增值税发票
        #去掉文件后缀
        name, extension = os.path.splitext(new_filename)
        #获取增值税发票名称列表
        invoice_file_name_list = find_filenames_with_length('../out/'+name)
        #构建发票对象数组
        invoice_list = []
        #抽取信息
        for invoice_file_name in invoice_file_name_list:
            extractor = InvoiceExtractor('../out/'+name+'/'+invoice_file_name)
            invoice = extractor.extract_invoice()
            invoice_list.append(invoice)
        # 将发票送入数据库
        res = InvoiceRepo.add(invoice_list)
        # 操作失败/重复上传文件
        if res is False:
            # 检查文件是否存在
            remove_file_path = '../out/'+ name
            if os.path.exists(remove_file_path):
                try:
                    # 删除文件
                    shutil.rmtree(remove_file_path)
                    print(f"重复文件 {remove_file_path} 被检测到.")
                except PermissionError:
                    print(f"无法删除文件 {remove_file_path}。文件可能正在被使用，或者你没有足够的权限。")
                except Exception as e:
                    print(f"删除文件 {remove_file_path} 时发生错误：{e}")
            else:
                print(f"重复文件 {remove_file_path} 不存在.")
            return 'fail', 201
        return 'ok', 200

@new_list.route('/download', methods=['POST'])
def download():
    file_list_path = request.get_json()
    #invoice_files = find_invoices_from_name(file_list)
    #print(invoice_files)
    # 将文件路径转换为文件对象
    files = [open(file, 'rb') for file in file_list_path]

    # 创建一个 zip 文件来包含所有发票
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for file in files:
            zip_file.writestr(file.name.split('/')[-1], file.read())

    # 将 zip_buffer 的位置回到开始
    zip_buffer.seek(0)
    # 设置下载的文件名
    download_filename = 'invoices.zip'
    # 获取当前时间并格式化为字符串
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # 在文件名上添加时间戳
    new_filename = f"{timestamp}_{download_filename}"
    # 使用 Flask 的 send_file 方法返回 zip 文件
    return send_file(
        zip_buffer,
        download_name=new_filename,
        as_attachment=True,
        mimetype='application/zip'
    )
