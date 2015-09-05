#encoding:utf-8
import MySQLdb
conn=MySQLdb.connect(host='192.168.1.241',user='root',passwd='gszy',db='zhsq',port=7202)
cursor=conn.cursor()
conn.set_character_set('utf8')
a ="王伟高你好吗"
sql="insert into zhsq_owner_message(id,create_date,modify_date,detail_id,flag,pkg_path,title,message_member_id,message_owner_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
param=('4028814d2c2819014d417cd5ea80042p','2015-05-11 13:40:12','2015-05-11 13:40:12','402881714d2c2819014d4171c7c6004b','3','com.bd.community',a,'4028813c4cda5ee7014cda77c5fc0001','402881714d1c6c5d014d1d7210630001')
cursor.execute(sql,param)
conn.commit()
cursor.close()
conn.close()


