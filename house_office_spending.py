import requests
from statistics import *

api_key = 'iEY7YfvIkvDKsrADtM0hbEEUBMGj20MwaEvZszeg'

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

def get_json(path):
	r = requests.get(path, headers={'X-API-Key': api_key})
	return r.json()


def get_missing_names():
	members = get_json('https://api.propublica.org/congress/v1/115/house/members.json')['results'][0]['members']
	for member in members:
		if member['state'] not in states:
			print(member['state'])


def get_state_totals():
	members = get_json('https://api.propublica.org/congress/v1/115/house/members.json')['results'][0]['members']
	for state in states:
		state_mems = [member for member in members if member['state'] == state]
		state_total = 0
		for mem in state_mems:
			spending = get_json('https://api.propublica.org/congress/v1/members/%s/office_expenses/category/total.json' % mem['id'])
			if len(spending['results']) > 0:
				recent = spending['results'][0]['amount']
			state_total += recent
		print('\n\n%s - $%s' % (state, round(state_total, 2)))
		print('    Average: $%s' % round(state_total / len(state_mems), 2))

get_missing_names()

# print(get_json('https://api.propublica.org/congress/v1/115/house/m')
