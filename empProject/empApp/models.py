
from django.db import models
# from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
 
    def __str__(self):
        return self.name
    
class Role(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role


 

class Employee(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="deptEmp")
    role = models.ForeignKey(Role, related_name='roleEmp', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joined_date = models.DateField()
    # address = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
 
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields = ['first_name', 'last_name', 'phone'],
    #             name = 'no same phn no have same emp'
    #         )
    #     ]





    

    
    