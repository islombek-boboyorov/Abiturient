from django.db import connection
from contextlib import closing


def get_about():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from about""")
        about = dict_fetchall(cursor)
    return about


def get_courses_details():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from courses_info """)
        info = dict_fetchall(cursor)
    return info


def get_courses():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from courses""")
        info = dict_fetchall(cursor)
    return info


def get_trainer():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from trainers""")
        trainer = dict_fetchall(cursor)
    return trainer


def get_events():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from events""")
        even = dict_fetchall(cursor)
    return even


def get_pricing():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from pricing""")
        info = dict_fetchall(cursor)
    return info


def get_pricing_1():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from pricings""")
        info = dict_fetchall(cursor)
    return info


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
