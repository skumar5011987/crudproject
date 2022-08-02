from django.shortcuts import render, HttpResponseRedirect
from .models import Employee
from .forms import RegisterationForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            en = form.cleaned_data['name']
            er = form.cleaned_data['role']
            eem = form.cleaned_data['email']

            record = Employee(
                name=en,
                role=er,
                email=eem
            )
            record.save()
            form = RegisterationForm()
    else:
        form = RegisterationForm()

    # insert = Employee.objects.create(name="Mohak Maheshwary", email='mohak@gmail.com', role="FrontEnd Developer") #inserting new record
    # insert.save() #saving the newly inserted record so it reflect in DB
    all_records = Employee.objects.all().order_by('id') # getting all the records from DB
    # all_records = Employee.objects.filter(name__startswith = 'A') # getting all records where name starts with alphabet "A"
    # all_records = Employee.objects.filter(name__startswith = 'V', role = 'SE') # getting all records where name starts with alphabet "A" and role is "SE"
    # all_records = Employee.objects.filter(role = 'CMO') # getting all records where role is "CMO"
    # all_records = Employee.objects.get(pk=1)
    # Employee.objects.filter(pk=10).delete() # deleteing a record by its primary key
    # all_records = Employee.objects.exclude(name__startswith='S') # getting all records whose name is not starting with "S"
    # all_records = Employee.objects.filter(name__startswith='S')| Employee.objects.filter(name__startswith='A') # getting those records where name starting with "S" or with 'A'
    
    # print(Employee.objects.all().count())# counting all recordes present in the DB
    # all_records = Employee.objects.all().order_by('id')[:5] #getting first 5 records of from DB
    # all_records = Employee.objects.all().order_by('id')[7:] #getting record from 7th to the end from DB
    # all_records = Employee.objects.all().order_by('id')[4:12] #getting records from 4th to 12th end from DB

    # all_records = Employee.objects.all().order_by('id') # order by id in Ascending order
    # all_records = Employee.objects.all().order_by('-id') # order by id in Desending order
    

    # print(str(all_records.query))  # printing equivalent  sql query

    
    return render(request, 'crudapp/addorshow.html', {'form': form, 'all_records': all_records})


def delete(request, id):
    # record = Employee.objects.filter(pk=id)
    # record.delete()
    Employee.objects.filter(pk=id).delete()
    return HttpResponseRedirect('/')


def update(request, id):
    if request.method == "POST":
        data = Employee.objects.get(pk=id)
        record = RegisterationForm(request.POST, instance=data)
        if record.is_valid():
            record.save()
            return HttpResponseRedirect('/')
    else:
        data = Employee.objects.get(pk=id)
        record = RegisterationForm(instance=data)
        return render(request, 'crudapp/update.html',{'record':record})