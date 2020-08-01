import pymysql
import  time
import  datetime
conn = pymysql.connect(host="127.0.0.1",port=3306,user='root',password='123456',database='test1',charset='utf8')
time_now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
cursor = conn.cursor()
t = "shiwo<'sdfs'$s><div rou "">tana加息"
text = pymysql.escape_string(t)
sql = f"INSERT INTO `test1`.`student2` (`id`, `name`, `xiaoshu`, `text`, `time`) VALUES ('4', 'cq', '23.2321', '{text}', '{time_now}');"

  nimabi
  father
  zijia zai gongsi xiagai yidun !!!!!!
i =cursor.execute(sql)
conn.commit()

print(f"={i}"*10)
cursor.close()
conn.close()


# print()








