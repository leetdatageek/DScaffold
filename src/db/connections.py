#[ ]
from sqlalchemy import create_engine

class Relational:
    def __init__(self, database_url):
        self._engine = create_engine(database_url)
        self._conn = self._engine.raw_connection()
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, qry, params=None):
        self.cursor.execute(qry, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, qry, params=None):
        """
        Return SQL query results with column names.

        Parameters
        ----------
        qry : string
            SQL query as-is.
        params :  tuple
            Prepared statement parameters.

        Returns
        -------
        list
            A list of results alongside the column names.
        """
        self.cursor.execute(qry, params or ())
        return [[col[0] for col in self.cursor.description]] + self.fetchall()



#with Test('mssql+pyodbc://APP_ANALYTICS:Analyticsapp01@ANALYTICS') as db:
#    print(db.query('select COUNT(*) from YellowFlagsV2'))