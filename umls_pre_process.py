import pandas as pd
import os

code_desc_filename = "./INPUT/code_desc_100.csv"
code_relation_filename = "./INPUT/code_relation_code_100.csv" #columns = ['code_1', 'relation', 'code_2']

text_out_filename = "./INPUT/codes_input_train.txt"

code_column = "code"
desc_column = "description"



# if not os.path.isfile(text_out_filename):
if True:
	df_desc = pd.read_csv(code_desc_filename)
	# create input text filename for training
	with open(text_out_filename, "w") as text_file:
		for ind, row in df_desc.iterrows():
			text_file.write(row[desc_column] + "\n")
		text_file.close()

	num_codes = df_desc.shape[0]
	# save dict of code, index and desc (if required)
	code_desc  = dict(zip(df_desc[code_column], df_desc[code_column]))

	code_index = dict(zip(df_desc[code_column], range(df_desc.shape[0])))

	index_code = dict(zip(range(df_desc.shape[0]), df_desc[code_column]))

	df_rel = pd.read_csv(code_relation_filename)
	print("df_rel Shape" , df_rel.shape)

	# save relations tuple in a dict { key : code_index , value: list of list([code_1, relation, code_2])}
	num_rel = 0
	rel_index = dict()

	rel_tuple = dict(zip(index_code.keys(), [[] for _ in range(len(index_code))]))

	for ind, row in df_rel.iterrows():
		try:
			code_1 = code_index[row['code_1']]
			code_2 = code_index[row['code_2']]
			try:
				relation = rel_index[row['relation']]
			except KeyError as ke:
				num_rel += 1
				rel_index[row['relation']] = num_rel
				relation = rel_index[row['relation']]

			rel_tuple[code_1].append([code_1, relation, code_2])
	
		except:
			continue

	# save count of relations for each code in dict { key : code_index , value: #relation with head as code_index }
	rel_count = dict()

	for key in rel_tuple:
		rel_count[key] = len(rel_tuple[key])

	print("rel_count dict = ", rel_count)
	print("___rel_tuple = ", rel_tuple)



