from django.shortcuts import render, redirect  
from APP.forms import MoviesForm  
from APP.models import *  
from django.db.models import Q
from django.shortcuts import render_to_response
# Create your views here.  
def mvi(request):  
    if request.method == "POST":  
        form = MoviesForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/APP/show')  
            except:  
                pass  
    else:  
        form = MoviesForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
	msg = []
	if request.method == 'POST':
		username = request.POST['u']
		password = request.POST['p']
		user = Users.objects.filter(uname=username, upassword=password)
		if user is not None:
			for us in user:
				movies = Movies.objects.all()  
				return render(request,"show.html",{'movies':movies,'role':us.role})  
		else:
			msg.append("invalid login")
	return render_to_response('login.html', {'errors': msg})
    
def edit(request, id):
    movies = Movies.objects.get(mid=id)  
    return render(request,'edit.html', {'movies':movies})  

def update(request, id):  
    movies = Movies.objects.get(mid=id) 
    form = MoviesForm(request.POST, instance = movies)  
    if form.is_valid():  
        form.save()  
        return redirect("/APP/show")  
    return render(request, 'edit.html', {'movies': movies})  

def destroy(request, id):  
    movies = Movies.objects.get(mid=id)  
    movies.delete()  
    return redirect("/APP/show")  

def search(request):
	query_string = ''
	found_entries = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		movies = Movies.objects.filter(Q(mname=query_string) | Q(mactor=query_string) | Q(mactress=query_string) | Q(mdirector=query_string))
		return render(request, 'show.html', { 'query_string': query_string, 'movies': movies })
	else:
		return render(request, 'show.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })

def login(request):
    return render_to_response('login.html', {'errors': []})
