import os

# 指定包含txt文件的文件夹路径
folder_path = '/home/zps/yolov5/datasets/labels1'

# 遍历文件夹中的所有txt文件
for file_name in os.listdir(folder_path):
    # 确保处理的文件是txt文件
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)

        # 打开文件以读取内容
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 打开文件以写入修改后的内容
        with open(file_path, 'w') as file:
            for line in lines:
                words = line.split()

                if len(words) >= 1:
                    # 检查第一列数字并替换
                    if words[0] == '0':
                        words[0] = '9'
                    elif words[0] == '1':
                        words[0] = '0'
                    elif words[0] == '2':
                        words[0] = '5'
                    elif words[0] == '3':
                        words[0] = '2'
                    elif words[0] == '4':
                        words[0] = '6'
                    elif words[0] == '5':
                        words[0] = '4'
                    elif words[0] == '6':
                        words[0] = '1'
                    elif words[0] == '7':
                        words[0] = '3'
                    elif words[0] == '8':
                        words[0] = '7'
                    elif words[0] == '9':
                        words[0] = '8'
                    new_line = ' '.join(words)
                    file.write(new_line + '\n')
                else:
                    file.write(line)
