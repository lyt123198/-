import random
import time
import pymysql

# 连接数据库
connection = pymysql.connect(host='127.0.0.1', user='root', password='1234', database='db')


def generate_interests():
    # 生成随机兴趣值
    interests = random.sample(range(1, 11), 6)
    interests_dict = {
        '汽车': interests[0],
        '旅游': interests[1],
        '财经': interests[2],
        '教育': interests[3],
        '软件': interests[4],
        '其他': interests[5]
    }
    return interests_dict


def generate_echarts_data():
    # 生成随机数据
    echarts_data = [
        ('商超门店', random.randint(100, 500)),
        ('教育培训', random.randint(100, 500)),
        ('房地产', random.randint(100, 500)),
        ('生活服务', random.randint(100, 500)),
        ('汽车销售', random.randint(100, 500)),
        ('旅游酒店', random.randint(100, 500)),
        ('五金建材', random.randint(100, 500))
    ]
    return echarts_data


def generate_chart_data():
    # 生成随机数据
    chart_data = [
        ('浙江', random.randint(100, 500)),
        ('上海', random.randint(100, 500)),
        ('江苏', random.randint(100, 500)),
        ('广东', random.randint(100, 500)),
        ('北京', random.randint(100, 500)),
        ('深圳', random.randint(100, 500)),
        ('安徽', random.randint(100, 500))
    ]
    return chart_data


def generate_as_data():
    # 生成随机数据
    as_data = []
    for i in range(1, 25):
        category = '安卓'  # 将 category 设为固定的 '安卓'
        value = random.randint(1, 10)  # 随机生成 1 到 10 的整数
        as_data.append((i, category, value))
    return as_data


def generate_ios_data():
    # 生成随机数据
    ios_data = []
    for i in range(1, 25):
        category = 'ios'  # 将 category 设为固定的 '安卓'
        value = random.randint(1, 10)  # 随机生成 1 到 10 的整数
        ios_data.append((i, category, value))
    return ios_data


def generate_pie_data():
    # 生成随机数据
    pie_data = [
        ('浙江', random.randint(1, 100)),
        ('上海', random.randint(1, 100)),
        ('广东', random.randint(1, 100)),
        ('北京', random.randint(1, 100)),
        ('深圳', random.randint(1, 100))
    ]
    return pie_data


def generate_age_data():
    # 生成随机数据
    age_data = [
        ('0岁以下', random.randint(1, 10)),
        ('20-29岁', random.randint(1, 10)),
        ('30-39岁', random.randint(1, 10)),
        ('40-49岁', random.randint(1, 10)),
        ('50岁以上', random.randint(1, 10))
    ]
    return age_data


def generate_fb_data(cursor):
    # 生成随机数据
    fb_data = [
        ('电子商务', random.randint(1, 10)),
        ('教育', random.randint(1, 10)),
        ('IT/互联网', random.randint(1, 10)),
        ('金融', random.randint(1, 10)),
        ('学生', random.randint(1, 10)),
        ('其他', random.randint(1, 10))
    ]
    return fb_data


def generate_random_increase():
    # 生成随机增加数据
    revenue_increase = random.randint(1000000, 5000000)
    expenditure_increase = random.randint(500000, 3000000)

    return revenue_increase, expenditure_increase


def update_interest_distribution(cursor):
    interests_dict = generate_interests()
    try:
        # 更新 interest_distribution 表中的兴趣值
        for interest_name, interest_value in interests_dict.items():
            sql = f"UPDATE interest_distribution SET interest_value = {interest_value} WHERE interest_name = '{interest_name}'"
            cursor.execute(sql)

        # 提交更改
        connection.commit()
        print("interest_distribution 数据已更新")
    except Exception as e:
        print("更新 interest_distribution 数据时发生错误:", e)


def update_echarts_data(cursor):
    echarts_data = generate_echarts_data()
    try:
        # 清空 echarts_data 表数据
        cursor.execute("TRUNCATE TABLE echarts_data")

        # 插入数据到 echarts_data 表
        sql = "INSERT INTO echarts_data (category, value) VALUES (%s, %s)"
        cursor.executemany(sql, echarts_data)

        # 提交更改
        connection.commit()
        print("echarts_data 数据已更新")
    except Exception as e:
        print("更新 echarts_data 数据时发生错误:", e)


def update_chart_data(cursor):
    chart_data = generate_chart_data()
    try:
        # 清空 chart_data 表数据
        cursor.execute("TRUNCATE TABLE chart_data")

        # 插入数据到 chart_data 表
        sql = "INSERT INTO chart_data (region, value) VALUES (%s, %s)"
        cursor.executemany(sql, chart_data)

        # 提交更改
        connection.commit()
        print("chart_data 数据已更新")
    except Exception as e:
        print("更新 chart_data 数据时发生错误:", e)


def update_as_data(cursor):
    new_as_data = generate_as_data()
    try:
        # 清空 as_data 表数据
        cursor.execute("TRUNCATE TABLE as_data")

        # 插入新数据到 as_data 表
        sql = "INSERT INTO as_data (id, category, value) VALUES (%s, %s, %s)"
        cursor.executemany(sql, new_as_data)

        # 提交更改
        connection.commit()
        print("as_data 数据已更新")
    except Exception as e:
        print("更新 as_data 数据时发生错误:", e)


def update_ios_data(cursor):
    new_ios_data = generate_ios_data()
    try:
        # 清空 ios_data 表数据
        cursor.execute("TRUNCATE TABLE ios_data")

        # 插入新数据到 ios_data 表
        sql = "INSERT INTO ios_data (id, category, value) VALUES (%s, %s, %s)"
        cursor.executemany(sql, new_ios_data)

        # 提交更改
        connection.commit()
        print("ios_data 数据已更新")
    except Exception as e:
        print("更新 ios_data 数据时发生错误:", e)


def update_pie_data(cursor):
    pie_data = generate_pie_data()
    try:
        # 清空 pie_data 表数据
        cursor.execute("TRUNCATE TABLE pie_data")

        # 插入新数据到 pie_data 表
        sql = "INSERT INTO pie_data (name, value) VALUES (%s, %s)"
        cursor.executemany(sql, pie_data)

        # 提交更改
        connection.commit()
        print("pie_data 数据已更新")
    except Exception as e:
        print("更新 pie_data 数据时发生错误:", e)


def update_age_data(cursor):
    new_age_data = generate_age_data()
    try:
        # 清空 age_data 表数据
        cursor.execute("TRUNCATE TABLE age_data")

        # 插入新数据到 age_data 表
        sql = "INSERT INTO age_data (age_group, value) VALUES (%s, %s)"
        cursor.executemany(sql, new_age_data)

        # 提交更改
        connection.commit()
        print("age_data 数据已更新")
    except Exception as e:
        print("更新 age_data 数据时发生错误:", e)


# 在适当的地方调用 update_age_data() 函数，传入游标对象，以更新 age_data 表的数据
# 例如，在处理请求的路由函数中调用该函数来更新 age_data 表的数据
def update_fb_data(cursor):
    fb_data = generate_fb_data(cursor)
    try:
        # 清空 fb_data 表数据
        cursor.execute("TRUNCATE TABLE fb_data")

        # 插入新数据到 fb_data 表
        sql = "INSERT INTO fb_data (name, value) VALUES (%s, %s)"
        cursor.executemany(sql, fb_data)

        # 提交更改
        connection.commit()
        print("fb_data 数据已更新")
    except Exception as e:
        print("更新 fb_data 数据时发生错误:", e)


# 循环生成随机数据并更新数据库
def generate_and_update_data():
    while True:
        with connection.cursor() as cursor:
            update_interest_distribution(cursor)
            update_echarts_data(cursor)
            update_chart_data(cursor)
            update_as_data(cursor)
            update_ios_data(cursor)
            update_pie_data(cursor)
            update_age_data(cursor)
            update_fb_data(cursor)
        # 休眠一段时间
        time.sleep(5)  # 休眠60秒



