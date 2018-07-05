"""Connection to database with psycopg2"""

import psycopg2
from V1.configurations.config import app_config
from psycopg2.extras import RealDictCursor


class connectorDB:
    """Class for database"""

    def init_app(self, config_name):
        """Initialize connectorDB"""
        config_object = app_config[config_name]
        self.db = config_object.DATABASE_URI
        self.conn = psycopg2.connect(self.db)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def query(self, query):
        """Query execution cursor"""
        self.cur.execute(query)

    def close(self):
        """close connection"""
        self.cur.close()
        self.conn.close()
