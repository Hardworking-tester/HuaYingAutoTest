#encoding:utf-8
import MySQLdb

class GetData():
    def getDataFromMysql(self,productid):
        conn=MySQLdb.connect(host='192.168.1.241',user='root',passwd='gszy',db='zhsq',port=7202)
        cursor=conn.cursor()

        conn.set_character_set('utf8')


        id=productid
        sql="SELECT mm.name from zhsq_goods mm where mm.id='"+id+"'"

        cursor.execute(sql)
        # rs=cursor.fetchall()
        # for x in rs:
        #     print x
        rs=cursor.fetchone()

        # print rs[0]
        cursor.close()
        conn.close()

        return rs[0]

# pp=GetData()
# pp.getDataFromMysql('402881714df525a3014df53689bf000e')