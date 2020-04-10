import MySQLdb

db = MySQLdb.connect(host="172.18.1.150", user="root", passwd="opshop", db="devops2")
c = db.cursor()

print('MySQL 连接成功！')