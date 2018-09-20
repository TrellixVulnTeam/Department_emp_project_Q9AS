from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Employee
from .forms import AddForm, EmpForm
from django.contrib import messages, auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    deptobjs= Department.objects.all()
    page= request.GET.get('page', 1)
    paginator = Paginator(deptobjs, 4)
    try:
        deptobj = paginator.page(page)
    except PageNotAnInteger:
        deptobj = paginator.page(1)
    except EmptyPage:
        deptobj = paginator.page(paginator.num_pages)
    return render(request, 'deptapp/home.html', {'deptobj': deptobj})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('deptapp:home')
        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'deptapp/index.html')

def logout(request):
    auth.logout(request)
    return render(request, 'deptapp/logout.html')

def adddept(request):
    if request.method == "POST":
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():
            dept = form.save(commit=False)
            dept.save()
            return redirect('deptapp:home')
    else:
        form = AddForm()
    return render(request, 'deptapp/add.html', {'form': form})


def detail_dept(request, dept_id):
    dept = get_object_or_404(Department, pk=dept_id)
    return render(request, 'deptapp/detail.html', {'dept': dept})

def delete_dept(request, dept_id):
    dept = Department.objects.get(pk=dept_id)
    dept.delete()
    return redirect('deptapp:home')

def add_emp(request, dept_id):
    form = EmpForm(request.POST or None)
    dept = get_object_or_404(Department, pk=dept_id)
    if form.is_valid():
        dept_emp = dept.employee_set.all()
        for e in dept_emp:
            if e.empname == form.cleaned_data.get("empname"):
                context = {'dept': dept, 'form':form, 'error_msg':'You have already added that employee'}
                return render(request, 'deptapp/add_emp.html', context)

        emp=form.save(commit=False)
        emp.dept=dept
        emp.save()
        return redirect('deptapp:detail_dept', dept_id)

    context={'dept': dept, 'form':form}
    return render(request, 'deptapp/add_emp.html', context)


def delete_emp(request, dept_id, emp_id):
    dept = get_object_or_404(Department, pk=dept_id)
    emp = Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect('deptapp:detail_dept', dept_id)


def edit_dept(request, dept_id):
    dept = get_object_or_404(Department, pk=dept_id)
    form = AddForm(request.POST, request.FILES, instance=dept)
    print("form", form)
    if form.is_valid():
        form.save()
        return redirect('deptapp:home')

    return render(request, 'deptapp/edit_dept.html', {'dept': dept})


