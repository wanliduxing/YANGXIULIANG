import MySQLdb

db = MySQLdb.connect(host="192.168.10.128", user="ze", passwd="123456", db="devops")
c = db.cursor()

print('MySQL 连接成功！')