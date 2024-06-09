import logging
from typing import Any, Dict, Optional

from psycopg2.extras import RealDictCursor

from quizzify.db.session import connect_to_db

logger = logging.getLogger(__name__)


class QueryExecutor:
    """Connect to the database and execute queries."""

    def __init__(self):
        """Initialize the QueryExecutor class."""
        self.connection = connect_to_db()

    def __enter__(self):
        """Make a database connection and return the cursor."""
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the cursor and the connection to the database."""
        self.cursor.close()
        self.connection.close()

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
