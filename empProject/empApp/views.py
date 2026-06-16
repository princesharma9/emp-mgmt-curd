from django.shortcuts import render, get_object_or_404, redirect
from empApp.models import Employee
# Create your views here.
def empList(request):
    empData = Employee.objects.all()
    return render(request, 'empApp/empList.html', {
        'empData':empData
    })

def empEdit(request, edit_id):
    editEmp = get_object_or_404(Employee, id = edit_id)
    if request.method == 'POST':
        editEmp.first_name = request.POST.get('first_name')
        editEmp.last_name = request.POST.get('last_name')
        editEmp.email = request.POST.get('email')
        editEmp.phone = request.POST.get('phone')
        editEmp.salary = request.POST.get('salary')
        editEmp.address = request.POST.get('address')
         
        editEmp.save()
        return redirect('empList')
    return render(request, 'empApp/empEdit.html', {
        'editEmp': editEmp
    })

     


def empRemove(request, remove_id):
    RemoveEmp = get_object_or_404(Employee, id = remove_id)
    if request.method == 'POST':
        RemoveEmp.delete()
        return redirect('empList')
    return render(request, 'empApp/empRemove.html')
    pass
