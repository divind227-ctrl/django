from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mark(request):
    marks = {
        'maths': 85,
        'science': 90,
        'english': 88
    }
    return render(request, 'mark.html', {'marks': marks})

def course(request):
    courses = ['Python', 'Django', 'Flask', 'Machine Learning']
    return render(request, 'course.html', {'courses': courses})


def dep(request):
    department = {
        'departments': ['CS', 'Maths', 'IT', 'B.Com']  # ✅ use key:value for context
    }
    return render(request, 'department.html', department)



def building(request):
    building ={
        'buildings':['a block','b block','c block','d block']
    }
    return render(request,'building.html',building)

