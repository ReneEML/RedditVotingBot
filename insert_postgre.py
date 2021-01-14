#!/usr/bin/python

import psycopg2
from config import config


def insert_submission(submission_id, creation_date, author_name):
    """ insert a new submission into the submission_details table """
    sql = """INSERT into submission_details
             (submission_id, creation_date , author_name, voting_status)
            VALUES (%s, %s, %s, %s) RETURNING submission_id;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (submission_id, creation_date, author_name, False))
        # get the generated id back
        submission_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return submission_id


