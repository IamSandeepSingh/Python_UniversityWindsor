from django.shortcuts import render,get_object_or_404

# Import necessary classes
from django.http import HttpResponse
from myapp.models import Author, Book, Course,Student

def index(request):
    courselist = Course.objects.all().order_by('title')[:10]
    return render(request, 'myapp/index.html', {'courselist': courselist})
# Create your views here.
# def index(request):
#     courselist = Course.objects.all().order_by('title')[:10]
#    authorlist = Author.objects.all().order_by('birthdate')
#    studentlist= Student.objects.all()
#    response = HttpResponse()
#    heading1 = '<p>' + 'List of courses: ' + '</p>'
#    response.write(heading1)
#
#   for course in courselist:
#       para = '<p>' + str(course) + '</p>'
#       response.write(para)
#   heading2 = '<p>' + 'List of Authors: ' + '</p>'
#   response.write(heading2)
#   for author in authorlist:
#       para = '<p>' + str(author) + '</p>'
#       response.write(para)
#       heading3 = '<p>' + 'List of Students: ' + '</p>'
#       return render(request, 'myapp/index0.html', {'courselist': courselist})
#       response.write(heading3)

#   for user in studentlist:
#           para = '<p>' + str(user) + '</p>'
#           response.write(para)
#   return response

def about(request):
     return render(request, 'myapp/about.html')

def detail(request,course_no):

    course_no = get_object_or_404(Course, pk=course_no)
    return render(request, 'myapp/detail.html', {'course': course_no})
