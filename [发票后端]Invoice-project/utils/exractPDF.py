import zipfile
import os
import re
import pdfplumber
def extract_zip(zip_path, target_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(target_folder)

def process_zip_files(data_folder, out_folder):
    # 遍历data文件夹中的所有文件和子文件夹
    for subdir, dirs, files in os.walk(data_folder):
        for file in files:
            if file.endswith('.zip'):
                # 构建完整的文件路径
                zip_path = os.path.join(subdir, file)
                # 获取压缩包的名称（不包括扩展名）
                zip_name = os.path.splitext(file)[0]
                # 确定在out文件夹中的对应目录
                relative_path = os.path.relpath(subdir, data_folder)
                target_folder = os.path.join(out_folder, relative_path, zip_name)
                os.makedirs(target_folder, exist_ok=True)

                # 解压最外层的压缩包
                extract_zip(zip_path, target_folder)

                # 删除原始压缩包
                os.remove(zip_path)

                # 处理内部的压缩包
                for inner_file in os.listdir(target_folder):
                    if inner_file.endswith('.zip'):
                        inner_zip_path = os.path.join(target_folder, inner_file)
                        extract_zip(inner_zip_path, target_folder)
                        # 删除内部的压缩包
                        os.remove(inner_zip_path)

# 弃用
def extract_invoice_info(pdf_path):
    # 存储提取的信息
    invoice_info = []
    key_value_info = []

    # 定义正则表达式来匹配所需的数据
    detail_pattern = re.compile(
        r"(.+?)\s+"  # 项目名称
        r"(\S+)\s+"  # 车牌号
        r"(.+?)\s+"  # 类型
        r"(\d{4})(\d{2})(\d{2})\s+"  # 通行日期起
        r"(\d{4})(\d{2})(\d{2})\s+"  # 通行日期止
        r"(\d+\.\d+)\s+"  # 金额
        r"(.+?)\s+"  # 税率
        r"(\d+\.\d+)"  # 税额
    )

    # 更通用的键值对正则表达式
    key_value_pattern = re.compile(r"(.+?):(.+)")

    # 打开PDF文件
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # 将文本按行分割
                lines = text.split('\n')
                for line in lines:
                    # 尝试使用定制化的正则表达式匹配特定发票信息
                    match = detail_pattern.search(line)
                    if match:
                        info_dict = {
                            "项目名称": match.group(1).strip(),
                            "车牌号": match.group(2).strip(),
                            "类型": match.group(3).strip(),
                            "通行日期起": f"{match.group(4)}-{match.group(5)}-{match.group(6)}",
                            "通行日期止": f"{match.group(7)}-{match.group(8)}-{match.group(9)}",
                            "金额": match.group(10).strip(),
                            "税率": match.group(11).strip(),
                            "税额": match.group(12).strip()
                        }
                        invoice_info.append(info_dict)
                    # 同时使用通用正则表达式匹配任何形式的键值对
                    matches = key_value_pattern.findall(line)
                    if matches:
                        key_value_dict = {key.strip(): value.strip() for key, value in matches}
                        key_value_info.append(key_value_dict)

    return invoice_info, key_value_info