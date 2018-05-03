from django.db import models

# Create your models here.

class State(models.Model):
	name = models.CharField(max_length=2)
	long_name = models.CharField(max_length=20)

	def __str__(self):
		return '%s (%s)' % (self.name, self.long_name)


class House_Rep(models.Model):
	pro_id = models.CharField(max_length=7)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	state = models.ForeignKey('State', on_delete=models.CASCADE, related_name='house_reps')
	party = models.CharField(max_length=5)

	def equipment(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.equipment
		return total

	def franked_mail(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.franked_mail
		return total

	def other_services(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.other_services
		return total

	def personnel(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.personnel
		return total

	def printing(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.printing
		return total

	def rent_utilities(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.rent_utilities
		return total

	def supplies(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.supplies
		return total

	def travel(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.travel
		return total

	def total(self):
		total = 0
		for q in self.spending_quarters.all():
			total += q.total
		return total

	def __str__(self):
		return '%s %s – %s' % (self.first_name, self.last_name, self.state)


class Quarter(models.Model):
	quarter = models.SmallIntegerField()
	year = models.SmallIntegerField()

	def __str__(self):
		return 'Q%s %s' % (self.quarter, self.year)


class Quarter_Spending(models.Model):
	rep = models.ForeignKey('House_Rep', related_name='spending_quarters')
	quarter = models.ForeignKey('Quarter', related_name='spending')
	equipment = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	franked_mail = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	other_services = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	personnel = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	printing = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	rent_utilities = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	supplies = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	travel = models.DecimalField(default=0, max_digits=20, decimal_places=2)
	total = models.DecimalField(default=0, max_digits=20, decimal_places=2)

	def __str__(self):
		return '%s – %s' % (self.rep, self.quarter)