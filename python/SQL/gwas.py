import csv
import sqlite3

data = open('gwas_ancestry_cleaned.csv', 'r',encoding="ISO-8859-1")
data_reader = csv.reader(data, delimiter=',')
header = next(data_reader, None)
data1 = open('gwas_associations_cleaned.csv', 'r',encoding="ISO-8859-1")
data_reader1 = csv.reader(data1, delimiter=',')
header1 = next(data_reader1, None)

# Connect to the GWAS catalog database.
db = sqlite3.connect("gwas.db")
cursor = db.cursor()

cursor.execute("""DROP TABLE IF EXISTS associate;""")
cursor.execute("""DROP TABLE IF EXISTS ancestry;""")

create_table_ance = """
CREATE TABLE ancestry (PUBMEDID INTEGER,
                         AUTHOR CHAR(10),
                         CATEGORY CHAR(10),
                         COUNTRY_ORIGIN VARCHAR(25),
                         COUNTRY_RECRUIT VARCHAR(25)
);"""

cursor.execute(create_table_ance)
#print(create_table_ance)

# Insert records into the table ancestry.
for arg in data_reader:
        format_arg = """
        INSERT INTO ancestry ( PUBMEDID,
                               AUTHOR ,
                               CATEGORY ,
                               COUNTRY_ORIGIN ,
                               COUNTRY_RECRUIT)
        VALUES ("{PUBMEDID}",
                 "{AUTHOR}",
                 "{CATEGORY}",
                "{COUNTRY_ORIGIN}",
                "{COUNTRY_RECRUIT}"
                 );
         """
        information = format_arg.format(PUBMEDID=arg[0],
                                        AUTHOR=arg[1],
                                        CATEGORY=arg[2],
                                        COUNTRY_ORIGIN=arg[3],
                                        COUNTRY_RECRUIT=arg[4]
                                        )
        cursor.execute(information)
        #print(information)
create_table_asso = """
CREATE TABLE associate (PUBMEDID INTEGER,
                        AUTHOR CHAR(10),
                        DISEASE VARCHAR(50),
                        PVALUE VARCHAR(25),
                        PVALUE_MLOG VARCHAR(100),
                        CI VARCHAR(100)
);"""

cursor.execute(create_table_asso)

# Insert records into the table associate.
for arg in data_reader1:
        format_arg = """
        INSERT INTO associate (PUBMEDID,
                                AUTHOR,
                                DISEASE,
                                PVALUE,
                                PVALUE_MLOG,
                                CI)
        VALUES ("{PUBMEDID}",
                 "{DISEASE}",
                 "{CATEGORY}",
                "{PVALUE}",
                "{PVALUE_MLOG}",
                "{CI}"
                );
         """
        information1 = format_arg.format(PUBMEDID=arg[0],
                                    DISEASE=arg[1],
                                    CATEGORY=arg[2],
                                    PVALUE=arg[3],
                                    PVALUE_MLOG=arg[4],
                                    CI=arg[5]
                                    )
        cursor.execute(information1)
        #print(information1)
# The table ancestry contains five columns.
# The statements below will output the five column names to the screen.

cursor.execute("SELECT * FROM associate WHERE DISEASE LIKE '%cancer%';")
#for cancer in cursor:
    #print(cancer)    # todo3


cursor.execute("SELECT DISEASE FROM associate INNER JOIN ancestry ON associate.AUTHOR= ancestry.AUTHOR "
               "WHERE CATEGORY LIke 'European%' ;")

disease=[]
for row in cursor:
    disease.append(row)   # todo4
    print(row)
###########################################################################
# TODO 1: Create a table ancestry.                                        #
###########################################################################
#make table as the ancestry’s value
create_table_ance = """
CREATE TABLE ancestry  (PUBMEDID INTEGER,
                         AUTHOR CHAR(10),
                         CATEGORY CHAR(10),
                         COUNTRY_ORIGIN VARCHAR(25),
                         COUNTRY_RECRUIT VARCHAR(25)
                                                                       #
);"""
cursor.execute(create_table_ance) #update table to cursor
                                                 #
###########################################################################

###########################################################################
# TODO 2: Insert all records from gwas_ancestry_cleaned.csv in ancestry.  #
###########################################################################
#read data by using for loop for adding value to table
for arg in data_reader:
     format_arg = """
     INSERT INTO ancestry ( PUBMEDID,
                           AUTHOR ,
                           CATEGORY ,
                           COUNTRY_ORIGIN ,
                           COUNTRY_RECRUIT
                           )
     VALUES ("{PUBMEDID}",
             "{AUTHOR}",
             "{CATEGORY}",
             "{COUNTRY_ORIGIN}",
             "{COUNTRY_RECRUIT}",
               );
     """
#indexing argument of  data_reader to make information
     information = format_arg.format(PUBMEDID=arg[0],
                                     AUTHOR=arg[1],
                                     CATEGORY=arg[2],
                                     COUNTRY_ORIGIN=arg[3],
                                     COUNTRY_RECRUIT=arg[4]
                                     )
     cursor.execute(information)   #update the information to cursor

###########################################################################

###########################################################################
# TODO 3: Select all records from the table associate having any type of  #
#         cancer in DISEASE.                                              #
###########################################################################
cursor.execute("SELECT * FROM associate WHERE DISEASE LIKE '%cancer%';")
# select the associate table and find disease part and it classfies disease which contains cancer
#for cancer in cursor:
     # print(cancer)

###########################################################################

###########################################################################
# TODO 4: List all diseases for which CATEGORY contains the string        #
#         European.                                                       #
###########################################################################
cursor.execute("SELECT DISEASE FROM associate INNER JOIN ancestry ON associate.AUTHOR= ancestry.AUTHOR"
               " WHERE Trim(CATEGORY) LIke 'European' ;")
#make European list from category of ancestry, use authors who are European to find disease

#disease=[]
#for dis in cursor:
   #disease.append(dis)
#print(disease)  # print list of disease
                                                 #
###########################################################################

# Save all changes made to the database.
db.commit()

# Close the database and disconnect.
db.close()

# Close the CSV file.
data.close()
