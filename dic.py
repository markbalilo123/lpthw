

student = {
	'1' : {'fname': 'marco', 'age' : 26},
	'2' : {'fname': 'balilo', 'age' : 28}
}

print(student['1']['fname'])


# print all value of key

for s_id, s_info in student.items():
	print('id ', s_id)

	for key in s_info:
		print(key + ':', s_info[key])
