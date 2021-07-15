import csv


import settings


columns = [
	"id",
	"login",
	"password",
	"role",
]

def add_new_user(login, password):
	users = get_user_names()
	if login not in users:
		next_index = get_index()
		write_row(next_index, login, password, 0)
	else:
		print("wrong name")	


def write_row(user_id, login, password, role):
	print(user_id, login, password, role)
	with open(settings.DB_NAME, 'a') as f:
		csvwriter = csv.writer(f)
		csvwriter.writerow([user_id, login, password, role])

def get_user_names():
	data = get_data()
	return [line[1] for line in data]


def get_index():
	return int(get_data()[-1][0]) + 1 if get_data() else 0 


def get_data():
	with open(settings.DB_NAME, 'r') as csvfile:
		data = list(csv.reader(csvfile))
	return data[1:]	

add_new_user('tim2', 1111)
	
