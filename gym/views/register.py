from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from gym.models import*




def home(request):
	if request.method=='GET':
		enquiry=Enquiry.objects.all()
		equipment=Equipment.objects.all()
		plan=Plan.objects.all()
		member=Member.objects.all()
		en=0
		eq=0
		pl=0
		me=0
		for i in enquiry:
			en+=1
		for i in equipment:
			eq+=1
		for i in plan:
			pl+=1
		for i in member:
			me+=1	
		dictt={'en':en,'eq':eq,'pl':pl,'me':me}		
		return render(request,'home.html',dictt)


def register(request):
	try:
		if request.method=='GET':
			return render(request,'register.html')
		elif request.method=='POST':
			firstname = request.POST['firstname']
			lastname = request.POST['lastname']
			username = request.POST['username']
			email = request.POST['email']
			password1 = request.POST['password1']
			password2 = request.POST['password2']
			address = request.POST['address']

			if password1==password2:
				if User.objects.filter(username=username).exists():
					print('username taken')
				elif User.objects.filter(email=email).exists():
					print('email taken')
				else:
					user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password1, email=email)	
					print('32')
					user.save();
					print('user created')
					return redirect('loginpage')
			else:
				print('password does not matching')
				messages.add_message(request, messages.INFO,'Password does not matching')

			return render(request,'register.html')	
		else:
			return render(request,'register.html')
	except Exception as e:
		print(e)
		return render(request,'register.html')	


def login(request):
	try:
		if request.method=='GET':
			return render(request,'login.html')
		elif request.method=='POST':
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			print('47')
			if user is not None:
				auth.login(request,user)
				print('login successful')
				return render(request,'home.html')
			else:
				print('53')
				messages.add_message(request, messages.SUCCESS,'invalid cardentials')
				return redirect('loginpage')
		else:
			print('something went wrong')
			return render(request,'login.html')	
	except Exception as e:
		print('error is :',e)
		return render(request,'login.html')	

def add_enquiry(request):

	dictt={}
	if not request.user.is_staff:
		return redirect('loginpage')
	enq = Enquiry.objects.all()
	if request.method=='GET':
		return render(request,'add_enquiry.html')
	elif request.method=='POST':
		name = request.POST['name']
		contact = request.POST['contact']
		emailid = request.POST['emailid']
		age = request.POST['age']
		gender = request.POST['gender']
		try:
			Enquiry.objects.create(name=name, contact=contact, emailid=emailid, age=age, gender=gender)
			dictt={'msg':'SUCCESS'}
			return render(request,'add_enquiry.html',dictt)
		except Exception as e:
			print(e)
			dictt={'msg':'something went wrong'}
			return render(request,'add_enquiry.html',dictt)

def view_enquiry(request):
	
	if not request.user.is_staff:
		return redirect('loginpage')
	enq = Enquiry.objects.all()
	dictt={'enq':enq}
	return render(request,'view_enquiry.html',dictt)
	
def delete_enquiry(request,id):
	
	if not request.user.is_staff:
		return redirect('loginpage')
	enquiry = Enquiry.objects.get(id=id)
	enquiry.delete()
	enq=Enquiry.objects.all()
	dictt={'enq':enq}
	return render(request,'view_enquiry.html',dictt)
	

def add_equipment(request):

	dictt={}
	if not request.user.is_staff:
		return redirect('loginpage')
	enq = Enquiry.objects.all()
	if request.method=='GET':
		return render(request,'add_equipment.html')
	elif request.method=='POST':
		name = request.POST['name']
		price = request.POST['price']
		unit = request.POST['unit']
		date = request.POST['date']
		description = request.POST['description']
		try:
			Equipment.objects.create(name=name, price=price, unit=unit, date=date, description=description)
			dictt={'msg':'SUCCESS'}
			return render(request,'add_equipment.html',dictt)
		except Exception as e:
			print(e)
			dictt={'msg':'something went wrong'}
			return render(request,'add_equipment.html',dictt)


def view_equipment(request):
	
	if not request.user.is_staff:
		return redirect('loginpage')
	equ = Equipment.objects.all()
	dictt={'equ':equ}
	return render(request,'view_equipment.html',dictt)
	
def delete_equipment(request,id):
	
	if not request.user.is_staff:
		return redirect('loginpage')
	equ = Equipment.objects.get(id=id)
	equ.delete()
	equ=Equipment.objects.all()
	dictt={'equ':equ}
	return render(request,'view_equipment.html',dictt)

def add_plan(request):

	dictt={}
	if not request.user.is_staff:
		return redirect('loginpage')
	enq = Enquiry.objects.all()
	if request.method=='GET':
		return render(request,'add_plan.html')
	elif request.method=='POST':
		name = request.POST['name']
		amount = request.POST['amount']
		duration = request.POST['duration']
		
		try:
			Plan.objects.create(name=name, amount=amount, duration=duration)
			dictt={'msg':'SUCCESS'}
			return render(request,'add_plan.html',dictt)
		except Exception as e:
			print(e)
			dictt={'msg':'something went wrong'}
			return render(request,'add_plan.html',dictt)


def view_plan(request):
	
	if not request.user.is_staff:
		return redirect('loginpage')
	equ = Plan.objects.all()
	dictt={'equ':equ}
	return render(request,'view_plan.html',dictt)
	
def delete_plan(request,id):
	
	if not request.user.is_staff:
		return redirect('loginpage')
	equ = Plan.objects.get(id=id)
	equ.delete()
	equ=Plan.objects.all()
	dictt={'equ':equ}
	return render(request,'view_plan.html',dictt)	
	
def add_member(request):

	dictt={}
	if not request.user.is_staff:
		return redirect('loginpage')
	enq = Member.objects.all()
	if request.method=='GET':
		return render(request,'add_member.html')
	elif request.method=='POST':
		name = request.POST['name']
		contact = request.POST['contact']
		emailid = request.POST['emailid']
		age = request.POST['age']
		gender = request.POST['gender']
		plan = request.POST['plan']
		joindate = request.POST['joindate']
		expiredate = request.POST['expiredate']
		initialamount = request.POST['initialamount']
		
		try:
			Member.objects.create(name=name, contact=contact, emailid=emailid, age=age, gender=gender, plan=plan, 
			joindate=joindate, expiredate=expiredate, initialamount=initialamount)
			dictt={'msg':'SUCCESS'}
			return render(request,'add_member.html',dictt)
		except Exception as e:
			print(e)
			dictt={'msg':'something went wrong'}
			return render(request,'add_member.html',dictt)


def view_member(request):
	
	if not request.user.is_staff:
		return redirect('loginpage')
	equ = Member.objects.all()
	dictt={'equ':equ}
	return render(request,'view_member.html',dictt)
	
def delete_member(request,id):
	
	if not request.user.is_staff:
		return redirect('loginpage')
	equ = Member.objects.get(id=id)
	equ.delete()
	equ=Member.objects.all()
	dictt={'equ':equ}
	return render(request,'view_member.html',dictt)	



def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')	



