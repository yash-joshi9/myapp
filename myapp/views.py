from django.http import HttpResponse
from .models import Topic, Course, Student, Order
# Create your views here.
from django.shortcuts import render

def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'top_list': top_list})


# def index(request):
#     top_list = Topic.objects.all().order_by('id')[:10]
#     top_course = Course.objects.all().order_by('title')[:5]
#     response = HttpResponse()
#     heading1 = '<p>' + 'List of topics: ' + '</p>'
#     response.write(heading1)
#
#     for topic in top_list:
#         para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
#         response.write(para)

    # heading2 = '<p>' + 'List of Courses: ' + '</p>'
    # response.write('<br></br>')
    # response.write(heading2)
    # for course in top_course:
    #     para = '<p>' + " " + str(course.title) + ': ' + str(course.price) + '</p>'
    #     response.write(para)
    #
    # return response

def about(request):
    response = HttpResponse()
    response.write("<p>" + "This is an E-learning Website! Search our Topics to find all available Courses." + "</p>")
    return render(request, 'myapp/about.html')

def  detail(request, topic_id):
    response = HttpResponse()
    course = Course.objects.filter(topic_id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)

    response.write("<p>" + str(topic).upper() + "  " + "length: " + str(topic.length) + "</p>")

    for i in course:
        response.write("<p>" + "name: " + str(i.title) + "</p>")

    # return response
    return render(request, 'myapp/detail.html', {"topic_": topic, "course_": course})


from django.shortcuts import render, get_object_or_404

# Create your views here.
