import pprint as pp
import psycopg2


def DatabaseConnection():
    """Connection to database"""
    connection = (
        "dbname='connect_api' user='hassan' host='localhost' password='yahya' port='5432'"
    )
    try:
        return psycopg2.connect(connection)
    except:
        pp.pprint("Cannot connect to database")
