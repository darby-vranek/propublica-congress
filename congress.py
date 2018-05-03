import requests

api_key = 'iEY7YfvIkvDKsrADtM0hbEEUBMGj20MwaEvZszeg'

def get_url():
	path = input('url to search:\n')
	print('starting')
	r = requests.get(path, headers={'X-API-Key': api_key})
	print(r.status_code)
	print(r.text)

get_url()


def get_office_spending():
	r = requests.get('https://api.propublica.org/congress/v1/115/house/members.json', headers={'X-API-Key': api_key})
	members = r.json()['results'][0]['members']
	for member in members:
		if member['state'] != 'CO':
			continue
		id = member['id']
		spend_request = requests.get('https://api.propublica.org/congress/v1/members/%s/office_expenses/category/total.json' % id, headers={'X-API-Key': api_key})
		# spending = spend_request.json()['results'][0]['amount']
		print('\n\n%s %s (%s):' % (member['first_name'], member['last_name'], member['state']))
		print(spend_request.text)

# get_office_spending()




def get_gender_by_party():
	r = requests.get('https://api.propublica.org/congress/v1/115/senate/members.json', headers={'X-API-Key': api_key})
	members = r.json()
	mems = members['results'][0]['members']
	d_f = 0
	d_m = 0
	i_f = 0
	i_m = 0
	r_f = 0
	r_m = 0
	for member in mems:
		if member['gender'] == 'F':
			if member['party'] == 'D':
				d_f += 1
			elif member['party'] == 'I':
				i_f += 1
			elif member['party'] == 'R':
				r_f += 1
		else:
			if member['party'] == 'D':
				d_m += 1
			elif member['party'] == 'I':
				i_m += 1
			elif member['party'] == 'R':
				r_m += 1
	print('Democrats: %s:\n%s F (%s)\n%s M' % (str(d_f + d_m), str(d_f), str(int((d_f / (d_f + d_m)) * 100)), str(d_m)))
	print('Republicans: %s:\n%s F (%s)\n%s M' % (str(r_f + r_m), str(r_f), str(int((r_f / (r_f + r_m)) * 100)), str(r_m)))