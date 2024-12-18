import os

# 发票文件名最长，用来寻找增值税发票文件名
def find_longest_filename(directory):
    # 确保提供的路径存在且是一个目录
    if not os.path.isdir(directory):
        print("提供的路径不存在或不是一个目录")
        return

    # 获取目录下的所有文件名
    filenames = os.listdir(directory)

    # 初始化最长文件名和最大长度
    longest_filename = ""
    max_length = 0

    # 遍历文件名列表
    for filename in filenames:
        # 检查文件是否是文件而不是目录
        if os.path.isfile(os.path.join(directory, filename)):
            # 获取当前文件名的长度
            current_length = len(filename)
            # 如果当前文件名更长，则更新最长文件名和最大长度
            if current_length > max_length:
                max_length = current_length
                longest_filename = filename

    # 打印最长的文件名
    if longest_filename:
        return longest_filename
    else:
        print("目录中没有文件。")
def find_filenames_with_length(directory, length=55):
    # 确保提供的路径存在且是一个目录
    if not os.path.isdir(directory):
        print("提供的路径不存在或不是一个目录")
        return []

    # 获取目录下的所有文件名
    filenames = os.listdir(directory)

    # 初始化一个列表来存储长度等于指定长度的文件名
    filenames_with_length = []

    # 遍历文件名列表
    for filename in filenames:
        # 检查文件是否是文件而不是目录
        if os.path.isfile(os.path.join(directory, filename)):
            # 如果当前文件名的长度等于指定长度，则添加到列表中
            if len(filename) == length:
                filenames_with_length.append(filename)

    # 返回长度等于指定长度的所有文件名
    return filenames_with_length
# # 使用示例
# directory_path = '../out/20241010143314_20201223__1'  # 替换为你的目录路径
# filenames_with_length_55 = find_filenames_with_length(directory_path, 55)
# print("长度为55的文件名有：", filenames_with_length_55)
# #print(find_longest_filename(directory_path))
def find_invoices_from_name(file_list):
    invoice_files = []
    for file_path in file_list:
        # 检查文件是否存在
        if os.path.exists(file_path):
            # 检查文件是否是PDF格式
            if file_path.lower().endswith('.pdf'):
                try:
                    # 打开文件并添加到列表中
                    with open(file_path, 'rb') as file:
                        invoice_files.append(file)
                except IOError as e:
                    print(f"无法打开文件 {file_path}: {e}")
            else:
                print(f"文件 {file_path} 不是PDF格式，已跳过。")
        else:
            print(f"文件 {file_path} 不存在，已跳过。")
    return invoice_files
 # 示例使用
# file_paths = [
#     '../out/20241013171408_20201223__1/91510100633168022E_937083446ff948eba0b1f6a46a88ed52.pdf',
#     '../out/20241013171441_20201223__3/91510000689919120D_f3c17dea5202450daa1d6b293390644c.pdf',
#     '../out/20241013171441_20201223__3/91510000709155317M_05fc60ecab6343deb5d96fb6b94e61f4.pdf',
#     '../out/20241013171441_20201223__3/91510100633168022E_140d21c2dcd3468eaf56816d9190eb5e.pdf'
# ]
#
# invoices = find_invoices_from_name(file_paths)
# print("找到的发票文件列表:", invoices)