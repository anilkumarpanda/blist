# Code for connecting to Google Sheets

from gsheetsdb import connect
from loguru import logger
import streamlit as st

class GSheetConnector :
    
        def __init__(self, credentials) :
            self.credentials = credentials
            self.scopes = [
                "https://www.googleapis.com/auth/spreadsheets",
            ]
            self.credentials = credentials
            self.conn = connect(credentials=credentials)
            
    
        def connect(self) :
            """
            Connect to Google Sheets.

            """
            logger.info("Connecting to Google Sheets")
            return connect(credentials=self.credentials)

        def get_data(self):
            """
            Get data from Google Sheets.

            """
            logger.info("Getting data from Google Sheets")
            # Perform SQL query on the Google Sheet.
            # Uses st.cache to only rerun when the query changes or after 10 min.
            @st.cache(allow_output_mutation=True, max_entries=100)
            def _run_query(query):
                rows = self.conn.execute(query, headers=1)
                return rows

            sheet_url = st.secrets["private_gsheets_url"]
            rows = _run_query(f'SELECT * FROM "{sheet_url}"')

            return rows