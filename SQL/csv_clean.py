import csv

#open the file gwas_associations and remove all DATE ADDED TO CATALOG
associations_cleaned_list=[]
with open('gwas_associations.csv', 'r', encoding="ISO-8859-1") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row_id, row in enumerate (csv_reader):
        cleaned_row = row[1:]
        # if 95%CI(TEXT)field is empty, it does not append to data
        if row[6]!='':
            associations_cleaned_list.append(cleaned_row)

#open the file which is cleaned all DATE ADDED TO CATALOG
with open('gwas_association_cleaned.csv', 'w',encoding="ISO-8859-1", newline='') as cleaned_csv_file:
    csv_writer = csv.writer(cleaned_csv_file)
    csv_writer.writerows(associations_cleaned_list)

#open the file gwas_ancestry and remove all ADDITONAL ANCESTRY DESCRIPTION
ancestry_cleaned_list=[]
with open('gwas_ancestry.csv', 'r', encoding="ISO-8859-1") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row_id, row in enumerate (csv_reader):
        cleaned_row = row[:-1]
        ancestry_cleaned_list.append(cleaned_row)

#open the file which is cleaned the ADDITONAL ANCESTRY DESCRIPTION
with open('gwas_ancestry_cleaned.csv', 'w',encoding="ISO-8859-1", newline='') as cleaned_csv_file:
    csv_writer = csv.writer(cleaned_csv_file)
    csv_writer.writerows(ancestry_cleaned_list)
