import requests
from .models import *


api_key = 'iEY7YfvIkvDKsrADtM0hbEEUBMGj20MwaEvZszeg'


def get_json(path):
	return requests.get(path, headers={'X-API-Key': api_key}).json()


def get_rep_spending(rep):
	for i in range(1, 5):
		quarter = get_json('http://api.propublica.org/congress/v1/members/%s/office_expenses/2017/%s.json' % (rep.pro_id, i)) 
		qi = Quarter.objects.get(quarter=i)
		q = Quarter_Spending(rep=rep, quarter=qi)
		for result in quarter['results']:
			if result['category_slug'] == 'equipment':
				q.equipment = result['amount']
			elif result['category_slug'] == 'franked-mail':
				q.franked_mail = result['amount']
			elif result['category_slug'] == 'other-services':
				q.other_services = result['amount']
			elif result['category_slug'] == 'personnel':
				q.personnel = result['amount']
			elif result['category_slug'] == 'printing':
				q.printing = result['amount']
			elif result['category_slug'] == 'rent-utilities':
				q.rent_utilities = result['amount']
			elif result['category_slug'] == 'supplies':
				q.supplies = result['amount']
			elif result['category_slug'] == 'travel':
				q.travel = result['amount']
			elif result['category_slug'] == 'total':
				q.total = result['amount']
		q.save()

def get_spending():
	reps = House_Rep.objects.all()
	for rep in reps:
		get_rep_spending(rep)


def create_rep(data):
	rep = House_Rep(pro_id=data['id'], first_name=data['first_name'], last_name=data['last_name'], party=data['party'])
	rep.state = State.objects.filter(name__iexact=data['state'])[0]
	rep.save()

def create_house():
	members = get_json('https://api.propublica.org/congress/v1/115/house/members.json')['results'][0]['members']
	print(len(members))
	print(type(members))
	for member in members:
		create_rep(member)