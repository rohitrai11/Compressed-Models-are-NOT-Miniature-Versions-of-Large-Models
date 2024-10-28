import pickle
import pandas as pd
from openpyxl import Workbook
import json

bert_large = "/TIDF_80/tidf80-user/rohit/extractive_question_answering/rohit_copy/misclassifications/bert_large.json"
bert_base = "/TIDF_80/tidf80-user/rohit/extractive_question_answering/rohit_copy/misclassifications/bert_base.json"
distil_bert = "/TIDF_80/tidf80-user/rohit/extractive_question_answering/rohit_copy/misclassifications/distil_bert.json"
bert_medium = "/TIDF_80/tidf80-user/rohit/extractive_question_answering/rohit_copy/misclassifications/bert_medium.json"
bert_mini = "/TIDF_80/tidf80-user/rohit/extractive_question_answering/rohit_copy/misclassifications/bert_mini.json"
tiny_bert = "/TIDF_80/tidf80-user/rohit/extractive_question_answering/rohit_copy/misclassifications/tiny_bert.json"


# Open the file in read mode
with open(bert_large, "r") as file:
    # Load the JSON data
    bert_large_inc = json.load(file)

print(len(bert_large_inc))

# Open the file in read mode
with open(bert_base, "r") as file:
    # Load the JSON data
    bert_base_inc = json.load(file)

print(len(bert_base_inc))

# Open the file in read mode
with open(distil_bert, "r") as file:
    # Load the JSON data
    distil_bert_inc = json.load(file)

print(len(distil_bert_inc))

# Open the file in read mode
with open(bert_medium, "r") as file:
    # Load the JSON data
    bert_medium_inc = json.load(file)

print(len(bert_medium_inc))

# Open the file in read mode
with open(bert_mini, "r") as file:
    # Load the JSON data
    bert_mini_inc = json.load(file)

print(len(bert_mini_inc))

# Open the file in read mode
with open(tiny_bert, "r") as file:
    # Load the JSON data
    tiny_bert_inc = json.load(file)

print(len(tiny_bert_inc))


'''
bert_large_inc = list(set(qn_ids).difference(set(bert_large)))
bert_base_inc = list(set(qn_ids).difference(set(bert_base)))
bert_small_inc = list(set(qn_ids).difference(set(bert_small)))
tiny_bert_inc = list(set(qn_ids).difference(set(tiny_bert)))
distil_bert_inc = list(set(qn_ids).difference(set(distil_bert)))
'''

rows = []

fields = ['Squad_v2','BERT-large','BERT-base','Distil-BERT', 'BERT-medium','BERT-mini','Tiny-BERT']

rows.append(fields)

large_base = len(set(bert_large_inc).intersection(bert_base_inc))/len(set(bert_large_inc).union(bert_base_inc))

large_medium = len(set(bert_large_inc).intersection(bert_medium_inc))/len(set(bert_large_inc).union(bert_medium_inc))

large_mini = len(set(bert_large_inc).intersection(bert_mini_inc))/len(set(bert_large_inc).union(bert_mini_inc))

large_tiny = len(set(bert_large_inc).intersection(tiny_bert_inc))/len(set(bert_large_inc).union(tiny_bert_inc))

large_distil = len(set(bert_large_inc).intersection(distil_bert_inc))/len(set(bert_large_inc).union(distil_bert_inc))

row_value = ['BERT-large','1.0',round(large_base,3),round(large_distil,3),round(large_medium,3),round(large_mini,3),round(large_tiny,3)]

rows.append(row_value)

base_medium = len(set(bert_base_inc).intersection(bert_medium_inc))/len(set(bert_base_inc).union(bert_medium_inc))

base_mini = len(set(bert_base_inc).intersection(bert_mini_inc))/len(set(bert_base_inc).union(bert_mini_inc))

base_tiny = len(set(bert_base_inc).intersection(tiny_bert_inc))/len(set(bert_base_inc).union(tiny_bert_inc))

base_distil = len(set(bert_base_inc).intersection(distil_bert_inc))/len(set(bert_base_inc).union(distil_bert_inc))

row_value = ['BERT-base','*','1.0',round(base_distil,3),round(base_medium,3),round(base_mini,3),round(base_tiny,3)]

rows.append(row_value)

distil_medium = len(set(distil_bert_inc).intersection(bert_medium_inc))/len(set(distil_bert_inc).union(bert_medium_inc))

distil_mini = len(set(distil_bert_inc).intersection(bert_mini_inc))/len(set(distil_bert_inc).union(bert_mini_inc))

distil_tiny = len(set(distil_bert_inc).intersection(tiny_bert_inc))/len(set(distil_bert_inc).union(tiny_bert_inc))

row_value = ['Distil-BERT','*','*','1.0',round(distil_medium,3),round(distil_mini,3),round(distil_tiny,3)]

rows.append(row_value)

medium_mini = len(set(bert_medium_inc).intersection(bert_mini_inc))/len(set(bert_medium_inc).union(bert_mini_inc))

medium_tiny = len(set(bert_medium_inc).intersection(tiny_bert_inc))/len(set(bert_medium_inc).union(tiny_bert_inc))

row_value = ['BERT-medium','*','*','*','1.0',round(medium_mini,3),round(medium_tiny,3)]

rows.append(row_value)

mini_tiny = len(set(bert_mini_inc).intersection(tiny_bert_inc))/len(set(bert_mini_inc).union(tiny_bert_inc))

row_value = ['BERT-mini','*','*','*','*','1.0',round(mini_tiny,3)]

rows.append(row_value)

row_value = ['Tiny-BERT','*','*','*','*','*','1.0']

rows.append(row_value)

print(rows)


wb = Workbook()

ws = wb.active

# Write data to the worksheet
for row in rows:
    ws.append(row)

# Save the workbook
wb.save("/TIDF_80/tidf80-user/rohit/extractive_question_answering/rohit_copy/jaccard.xlsx")
