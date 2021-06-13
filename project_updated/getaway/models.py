from datetime import datetime
from getaway import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()

    schema = 'customers'
    id = 'email'

    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema),  sql.Identifier(id))

    cur.execute(user_sql, ((user_id),))
    if cur.rowcount > 0:
        return Customers(cur.fetchone())
    else:
        return None


class Customers(tuple, UserMixin):
    def __init__(self, user_data):
        self.email = user_data[0]
        self.likes_heat = user_data[1]
        self.plane_pref = user_data[2]
        self.boat_pref = user_data[3]
        self.train_pref = user_data[4]
        self.budget = user_data[5]
        self.password = user_data[6]
        self.name = user_data[7]
        print('customer class')

    def get_id(self):
        return (self.email)


class Countries(tuple):
    def __init__(self, user_data):
        self.country = user_data[0]
        self.id = user_data[1]
        self.hot = user_data[2]
        self.price = user_data[3]
        print('countries class')

    def get_id(self):
        return (self.country)




def insert_Customers(email, likes_heat, plane_pref, boat_pref, train_pref, budget, password, name):
    cur = conn.cursor()
    sql = """
    INSERT INTO Customers(email,likes_heat, plane_pref, boat_pref, train_pref, budget, password, name)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (email, likes_heat, plane_pref, boat_pref, train_pref, budget, password, name))
    conn.commit()
    cur.close()


def select_Customers(email):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Customers
    WHERE email = %s
    """
    cur.execute(sql, (email,))
    user = Customers(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user


def hot_countries(likes_heat, Budget):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Countries c
    JOIN transportation t on c.ctryName = t.ctryName 
    WHERE hot = %s AND ((c.price + t.avg_plane_price) < %s OR  (c.price + t.avg_boat_price) < %s OR (c.price + t.avg_train_price) < %s)
    """
    print('finding hot countries')
    cur.execute(sql, (likes_heat, Budget, Budget, Budget,))
    tuple_resultset = cur.fetchall() if cur.rowcount > 0 else None
    cur.close()
    return tuple_resultset

def cont_all():
    cur = conn.cursor()
    sql = """
    SELECT * FROM Countries 
    """
    cur.execute(sql)
    print('I JUST FETCHED ALL')
    result = cur.fetchall() if cur.rowcount > 0 else None
    cur.close()
    return result
