#encoding_utf-8
import MySQLdb

class GetData():
    def getDataFromMysql(self):
        conn=MySQLdb.connect(host='192.168.1.241',user='root',passwd='gszy',db='zhsq',port=7202,charset='utf-8')
        cursor=conn.cursor()

        a ="王伟高"
        a = a.decode("gbk").encode("utf-8")
        # sql='select user.experience from user where phone=18638135380'
        # sql="insert into zhsq_owner(create_date,modify_date,auth_flag,house_role,img,invitation_code,nick_name,owner_grade,owner_phone,pwd,user_name,owner_CommunityData_id,owner_member_id) VALUES ('2015-04-28 13:46:27','2015-05-06 14:03:39',0,2,'/zhsq/upload/201504/402881714cf9f8bd014cfe8febef000a/bd110d79c7454a4d9daf6e76fafbdc89.png','a1twek4i1','python','18638135380','96e79218965eb72c92a549dd5a330112','wwg2python','402881714cf9f8bd014cfe8b007b0006','4028813c4cda5ee7014cda77c5fc0001')"
        sql="insert into zhsq_owner_message(id,create_date,modify_date,detail_id,flag,pkg_path,title,message_member_id,message_owner_id) VALUES (%s,%s,%s,%s,%s,%s%s%s,%s)"
        param=('4028814d2c2819014d417cdea80042','2015-05-11 13:40:12','2015-05-11 13:40:12','402881714d2c2819014d4121c7c6004b','3','com.bd.community',a,'4028813c4cda5ee7014cda77c5fc0001','402881714d1c6c5d014d1d7210630001')
        # sql="select * from  zhsq_owner_message"
        cursor.execute(sql,param)
        # rs=cursor.fetchall()
        # for x in rs:
        #     print x
        # rs=cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        # conn=MySQLdb.connect(host='192.168.1.241',user='root',passwd='gszy',db='zhsq',port=7202)
        # cursor=conn.cursor()
        # conn.set_character_set('utf8')
        # a ="王伟高你好吗"
        # sql="insert into zhsq_owner_message(id,create_date,modify_date,detail_id,flag,pkg_path,title,message_member_id,message_owner_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # param=('4028814d2c2819014d417cd5ea80042p','2015-05-11 13:40:12','2015-05-11 13:40:12','402881714d2c2819014d4171c7c6004b','3','com.bd.community',a,'4028813c4cda5ee7014cda77c5fc0001','402881714d1c6c5d014d1d7210630001')
        # cursor.execute(sql,param)
        # conn.commit()
        # cursor.close()
        # conn.close()



        # for i in rs:
        #
        #     return i
        conn.close()
pp=GetData()
pp.getDataFromMysql()