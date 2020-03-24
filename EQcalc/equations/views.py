from django.shortcuts import render

from variables.models import Variable
from .models import Equation

# Create your views here.

def index(request):

	return render(request, "index.html") 


def calcVal(id, values):
	
	if id == (1,1):   # Force = Mass*Acceleration
		m = values[0]
		a = values[1]

		result = m*a
		return result

	if id == (1,2): # Mass = Force/Acceleration
		F = values[0]
		a = values[1]

		result = F/a
		return result

	if id == (1,3): #Acceleration = Force/Mass
		F = values[0]
		m = values[1]

		result = F/m
		return result


def base(request):
	equations = Equation.objects.all()

	form = request.POST.get('eqform', '')
	if form != '':
		formulaID = Equation.objects.get(name=form).formulaID
		eqlist = Equation.objects.filter(formulaID=formulaID)
		eqout = []
		for eq in eqlist:
			eqout.append((eq.param, eq.formulaID, eq.inversion))

	else:
		eqout = ''


	return {'equations': equations, 'form':form, 'eqout':eqout}
