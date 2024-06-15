import logging
import os
from typing import Any, Dict, Optional

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

logger = logging.getLogger(__name__)
load_dotenv()

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")


class QueryExecutor:
    """Connect to the database and execute queries."""

    def __init__(self):
        """Initialize the QueryExecutor class."""
        self.connection = self.connect_to_db()

    def __enter__(self):
        """Make a database connection and return the cursor."""
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the cursor and the connection to the database."""
        self.cursor.close()
        self.connection.close()

    @staticmethod
    def connect_to_db():
        """
        Connect to the PostgreSQL database.

        Returns
        -------
        connection : psycopg2.extensions.connection
            The connection to the PostgreSQL database.
        """
        connection = psycopg2.connect(
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
        )
        return connection

    def execute(
        self,
        query: str,
        variables: Optional[Dict[str, Any]] = None,
        fetch: bool = False,
        one: bool = False,
    ):
        """Execute a query on the database.

        Parameters
        ----------
        query : str
            The query to execute.
        variables : dict, optional
            The variables to pass to the query, by default None.
        fetch : bool, optional
            Whether to fetch the results of the query, by default False.
        one : bool, optional
            Whether to fetch one result or all results, by default False.

        Returns
        -------
        list
            The results of the query if fetch is True.
        """
        self.cursor.execute(query=query, vars=variables)
        logger.debug(
            f"Executed query: {query} with vars: {variables}"
            if variables
            else f"Executed query: {query}"
        )
        if fetch and one:
            return self.cursor.fetchone()
        elif fetch:
            return self.cursor.fetchall()

        self.connection.commit()
        return None
