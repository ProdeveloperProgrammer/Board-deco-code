from django.http.response import JsonResponse
from Student.models import StudentDetail

# Create your views here.
def get_all(request):
    try:
        All_student = list(StudentDetail.objects.all().values())
        return JsonResponse(All_student,safe=False)
    except:
        return JsonResponse({"error":"No Student Available"},safe=False)
    

def get_all_house(request,house_name):
    All_student = list(StudentDetail.objects.filter(House=house_name).values())
    if All_student == []:
        return JsonResponse({"error":f"No Student of {house_name}"},safe=False)
    else:
        return JsonResponse(All_student,safe=False)
    
def get_all_bus(request,bus_name):
    All_student = list(StudentDetail.objects.filter(Bus=bus_name).values())
    if All_student == []:
        return JsonResponse({"error":f"No Student from {bus_name}"},safe=False)
    else:
        return JsonResponse(All_student,safe=False)
def get_one(request,Name):
    Student = list(StudentDetail.objects.filter(Name__contains=Name).values())
    if Student == []:
        return JsonResponse({"error":f"No Student name {Name}"},safe=False)
    else:
        return JsonResponse(Student,safe=False)