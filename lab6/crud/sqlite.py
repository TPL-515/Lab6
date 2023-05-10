from dagster import asset, get_dagster_logger, Output
import sqlite3
from pathlib import Path
from datetime import datetime
import random
import pandas as pd
# Get our Logger
logger = get_dagster_logger()

# Get our sql session
db = Path('database.db')
con = sqlite3.connect(db)
cursor = con.cursor()


@asset(description="This checks if our table exists")
def create_table():

    logger.info('Create table if it does not exist within our database')

    create_table_text = """CREATE TABLE IF NOT EXISTS demods (
        feature1 real NOT NULL,
        feature2 real NOT NULL, 
        label integer NOT NULL
    )"""

    try:
        cursor.execute(create_table_text)
    except:
        logger.error('Had issues with creating the table in the database')
        raise Exception

@asset(description="Return metadata for the database")
def display_db_meta(create_table):
    logger.info('Getting the meta data for our database')
    
    cursor.execute("SELECT * FROM demods")
    dat = cursor.fetchall()

    rows = len(dat)
    cols = ['feature1', 'feature2', 'label']
    logger.info(f'Total number of entries in the table {rows}')
    logger.info(f'Total number of columns in the table {len(cols)}')
    return Output(None, metadata={"num_rows": rows, "num_cols": len(cols), "columns": cols})

@asset(description="This ingests an example bit of data into the database")
def add_data(create_table):

    data = []
    for i in range(10):
        if i < 5:
            f1 = random.uniform(10.5, 20.5)
            f2 = random.uniform(21, 41)
            label = 0
        else:
            f1 = random.uniform(10.5, 20.5)
            f2 = random.uniform(21, 41)
            # f1 = random.uniform(15.5, 25.5)
            # f2 = random.uniform(31, 51)
            label = 1
        data.append((f1, f2, label))
    
    logger.info(f'Injesting {len(data)} rows into the database')
    
    cursor.executemany("INSERT INTO demods VALUES(?, ?, ?)", data)
    con.commit()
    con.close()

@asset(description="This allows the user to delete all the data from the database")
def remove_data():
    logger.info('Deleting all data from the database.')
    cursor.execute('DELETE FROM demods')
    con.commit()
    con.close()

@asset(description="This allows the user to read the data from within the table")
def read_data(create_table):

    logger.info('Pulling the data from the table.')
    cursor.execute("SELECT * FROM demods")
    dat = cursor.fetchall()

    logger.info(f'Pulled {len(dat)} rows from the data table')
    df = pd.DataFrame(dat, columns=['feature1', 'feature2', 'label'])

    return df