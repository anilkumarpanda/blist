# Main application for the blist_app.

import streamlit as st
from google.oauth2 import service_account

from blist.blogparser import BlogParser
from blist.gsheetconnector import GSheetConnector

def main():

    # Create a credential for connection to GSheet.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
        ],
    )
    rows = GSheetConnector(credentials=credentials).get_data()


    # Print results.
    for row in rows:
        st.write(f"Parsing website {row.website}")

if __name__ == "__main__":
    main()