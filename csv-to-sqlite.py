import pandas as pd
import sqlite3


# importing csv
new_tag = pd.read_csv('SG_tag_database_custom.csv')
print('new tag\n', new_tag)

# creating our sqlite database
tags = sqlite3.connect('SG_tag_database.sqlite')

# sql command to list all the tables
sql_query = """SELECT name from sqlite_master WHERE type='table';"""

# create a cursor object to execute sql queries on a database table
cursor = tags.cursor()

# executes the sql query, followed by a print command of all the tables in the sql database
cursor.execute(sql_query)
print('List of tables \n')

# printing all tables list
print(cursor.fetchall()) # table name is tags

# Read sqlite query results into a pandas Dataframe
df = pd.read_sql_query("SELECT * from tags", tags)
print('tag database\n', df)

# needed to use the new_tag dataframe and append it to tags connection
new_tag.to_sql('tags', tags, if_exists='append', index=False)

print('appended tag database\n', tags)
tags.close()
