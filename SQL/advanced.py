###########################################################################
# TODO 1: Create a table ancestry.                                        #
###########################################################################
#create_table_query1 = """
#CREATE TABLE ancestry  (PUBMEDID INTEGER,
#                         AUTHOR CHAR(10),
#                         CATEGORY CHAR(10),
#                         COUNTRY_ORIGIN VARCHAR(25),
#                         COUNTRY_RECRUIT VARCHAR(25)
#                                                                       #
#);"""
#cursor.execute(create_table_query)   #update table to cursor
###########################################################################

###########################################################################
# TODO 2: Insert all records from gwas_ancestry_cleaned.csv in ancestry.  #
###########################################################################
# for e in data_reader:
#     format_arg = """
#     INSERT INTO ancestry ( PUBMEDID,
#                           AUTHOR ,
#                           CATEGORY ,
#                           COUNTRY_ORIGIN ,
#                           COUNTRY_RECRUIT
#                           )
#     VALUES ("{PUBMEDID}",
#             "{AUTHOR}",
#             "{CATEGORY}",
#             "{COUNTRY_ORIGIN}",
#             "{COUNTRY_RECRUIT}",
#               );
#     """
#     information = format_str.format(PUBMEDID=arg[0],
#                                     AUTHOR=arg[1],
#                                     CATEGORY=arg[2],
#                                     COUNTRY_ORIGIN=arg[3],
#                                     COUNTRY_RECRUIT=arg[4]
#                                     )
#     cursor.execute(information)                                                   #
###########################################################################

###########################################################################
# TODO 3: Select all records from the table associate having any type of  #
#         cancer in DISEASE.                                              #
###########################################################################
# cursor.execute("SELECT * FROM associate WHERE TRIM(DISEASE) LIKE '%cancer%';")
# for row in cursor:
#         print(row)                                                #
###########################################################################

###########################################################################
# TODO 4: List all diseases for which CATEGORY contains the string        #
#         European.                                                       #
###########################################################################
# cursor.execute("SELECT DISEASE FROM associate INNER JOIN ancestry ON associate.AUTHOR= ancestry.AUTHOR WHERE Trim(CATEGORY) LIke 'European' ;")
# disease=[]
# for row in cursor:
#     disease.append(row)                                                   #
###########################################################################