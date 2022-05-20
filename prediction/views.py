from django.shortcuts import render
from django.http import HttpResponseRedirect
from prediction.forms import RegisterForm
from prediction.forms import PredictionForm
from prediction.models import RegisterModel
from prediction.models import PredictionModel
from django.core.files.storage import default_storage
from django.urls import reverse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
import threading

def index(request):
	return render(request, 'index.html')

def companies(request):
	return render (request, 'companies.html')

def philips(request):
	return render (request, 'philips.html')

def dell(request):
	return render (request, 'dell.html')

def apply(request):
	global name, email, phone, address, tenth, puc, degree, branch 

	if request.method == 'POST':
		r_form = RegisterForm(request.POST)

		if r_form.is_valid():
			r_form.save()			                       
			name = r_form.cleaned_data.get('name')			
			email = r_form.cleaned_data.get('email')
			phone= r_form.cleaned_data.get('phone')
			address= r_form.cleaned_data.get('address')
			tenth= r_form.cleaned_data.get('tenth')
			puc= r_form.cleaned_data.get('puc')
			degree= r_form.cleaned_data.get('degree')
			branch= r_form.cleaned_data.get('branch')
			
		return render(request, 'done.html', { 'r_form': r_form})
		return HttpResponseRedirect("/apply")
    
	else:
		r_form = RegisterForm()
	return render(request, 'apply.html',{ 'r_form': r_form})

def marks(request):
	global emailid, technical, aptitude, gd, pi, tenth, puc, degree
	if request.method == 'POST':
		#emailid = request.POST.get('emailid')
		#print(emailid)
		p_form = PredictionForm(request.POST)

		if p_form.is_valid():
			p_form.save()
			emailid = p_form.cleaned_data.get('emailid')			                       
			technical = p_form.cleaned_data.get('technical')			
			aptitude = p_form.cleaned_data.get('aptitude')
			gd= p_form.cleaned_data.get('gd')
			pi= p_form.cleaned_data.get('pi')
			tenth= p_form.cleaned_data.get('tenth')
			puc= p_form.cleaned_data.get('puc')
			degree= p_form.cleaned_data.get('degree')
			print(emailid)

			if (int(technical) <=10) and (int(aptitude) <=10) and (int(gd) <=10)  and  (int(pi) <=10) and (int(tenth) <=10) and (int(puc) <=10) and (int(degree) <=10):
				data = pd.read_csv("placement_data.csv", sep=",")
				y = data.target
				x = data.drop('target', axis=1)        		
				x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=2)
				model = tree.DecisionTreeClassifier(max_depth=5, max_leaf_nodes=10, criterion='entropy')
				model.fit(x_train, y_train)
				predictions=model.predict(x_test)
				y_predict = model.predict([[technical,aptitude,gd,pi,tenth,puc,degree]])
				print(y_predict)

				if y_predict =='yes':
					html = 'Candidate Selected!!'
					subject = "Placement Results"
					message = "Dear Candidate,\n\nCONGRAGULATION!!! You are selected !\n All the best!\n\nRegards,\nDELL"
					from_email = settings.EMAIL_HOST_USER
					to_list = [str(emailid)]
					sendemail = EmailMessage(str(subject), str(message), str(from_email), to_list)
					sendemail.send(fail_silently=False)

					return render(request, 'marks.html', {'html': html})
					#return HttpResponseRedirect(reverse('marks'),{'html': html})

				else:
					html = 'Candidate Not selected!!'
					subject = "Placement Results"
					message = "Dear Candidate,\n\nSorry to inform you that you are not selected. Better luck next time.\n \nRegards,\nSameeksha Anthony"            		
					from_email = settings.EMAIL_HOST_USER
					to_list = [str(emailid)]
					sendemail = EmailMessage(str(subject), str(message), str(from_email), to_list)
					sendemail.send(fail_silently=False)
			
					return render(request, 'marks.html', {'html': html})
				
			return render(request, 'marks.html',{ 'p_form': p_form})

		return HttpResponseRedirect("/marks")			
		    
	else:
		p_form = PredictionForm()
	return render(request, 'marks.html',{ 'p_form': p_form})
	
def login(request):
	global username, password
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username == 'admin' and password == 'admin':
			html = ''
			#p_form = PredictionForm()
			return render(request, 'marks.html', {'html':html})
			return HttpResponseRedirect("/marks")

		else:
			html = 'Invalid User!!!!'
			return render(request, 'login.html', {'html': html})
	return render(request, 'login.html', {})    

