from django.shortcuts import render
from .models import Quarter_Spending, State, House_Rep


def index(request):
	return render(request, 'house_office_spending/table.html', context={'reps': House_Rep.objects.all() })
	# equipment = 0
	# franked_mail = 0
	# other_services = 0
	# personnel = 0
	# printing = 0
	# rent_utilities = 0
	# supplies = 0
	# travel = 0
	# for q in Quarter_Spending.objects.all():
	# 	if q.equipment == 0 and q.franked_mail == 0 and q.other_services == 0 and q.personnel == 0 and q.printing == 0 and rent_utilities == 0 and q.supplies == 0 and q.travel == 0:
	# 		continue
	# 	equipment += q.equipment
	# 	franked_mail += q.franked_mail
	# 	other_services += q.other_services
	# 	personnel += q.personnel
	# 	printing += q.printing
	# 	rent_utilities += q.rent_utilities
	# 	supplies += q.supplies
	# 	travel += q.travel
	# return render(request, 'house_office_spending/index.html', context={'equipment': equipment, 'franked_mail': franked_mail, 'other_services': other_services, 'personnel': personnel, 'printing': printing, 'rent_utilities': rent_utilities, 'supplies': supplies, 'travel': travel, 'states': State.objects.all()})
