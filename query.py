from myapp.models import User, Order, Course, Student, Topic


# a. List all the courses in the db.
courses = Course.objects.all()
print(courses)

# b. List all the students in the db.
students = Student.objects.all()
print(students)


# c. List all the orders in the db.
orders = Order.objects.all()
print(orders)

# 2. Write queries to do the following.


# a. List all students whose last name is ‘Jones’
lastJones = Student.objects.all().filter(last_name="Jones")

# b. List all topics whose course length is 8 weeks
Topic.objects.filter(length=8)
# <QuerySet [<Topic: Sports>]>

# c. List all students that live on ‘Sunset Avenue’.
Student.objects.filter(address__contains="Sunset Avenue")
# <QuerySet [<Student: MaryJones>, <Student: JoshJones>]>

# d. List all students that live on an ‘Avenue’ and live in province ‘ON’.
Student.objects.filter(address__contains="Avenue").filter(province="ON")
# <QuerySet [<Student: JohnSmith>]>


# e. List all the students that are interested in Topic 'Sports'
Student.objects.filter(interested_in__in=Topic.objects.filter(name="Sports"))
# <QuerySet [<Student: AlanGeorge>, <Student: JoshJones>]>


# f. List the courses that cost more than $150.00
Course.objects.filter(price__gt=150)
# <QuerySet [<Course: CCNA>, <Course: Oracle SQL>, <Course: Microeconomics>, <Course: Introduction to Economics>, <Course: Global Economics>, <Course: Web Dev Bootcamp>, <Course: Web Design>, <Course: Innovation for business>, <Course: Leadership Skills>, <Course: Sport Psychology>]>

# g. List the students that do NOT live in ON.
Student.objects.exclude(province="ON")
# <QuerySet [<Student: MaryJones>, <Student: AlanGeorge>, <Student: JoshJones>]>

# h. List the Orders placed by a student whose first_name is ‘Chris’.
student = Student.objects.filter(first_name='Chris')
Order.objects.filter(student__in=student)
# <QuerySet [<Order: Chris Hall>]>

# i.List the courses that are currently NOT for_everyone.
Course.objects.filter(for_everyone=False)
# <QuerySet [<Course: CCNA>, <Course: CompTIA Security>, <Course: Oracle SQL>, <Course: Microeconomices>, <Course: Web Design>, <Course: Build Responsive Websites>]>

# j. Get the first name of the student of the Order with pk=1.
Order.objects.get(pk=1).student.first_name
# 'John'

# k. List all topics that the student with username ‘john’ is interested_in.
Student.objects.get(username='john').interested_in.all()
# <QuerySet [<Topic: IT Certification>, <Topic: Web Development>, <Topic: Management>]>

# l. List all the courses with a price < $150 and is for_everyone.
Course.objects.filter(price__lt=150).filter(for_everyone=True)
# <QuerySet [<Course: AWS>, <Course: Global Economics>, <Course: Web Development Masterclass>, <Course: Project Management>, <Course: Introduction to Soccer>, <Course: Swimming Guide for Beginners>]>

# m. List the Topics that the student who ordered a Web Dev Bootcamp is interested_in. Assume there is exactly one order for Web Dev Bootcamp course.
course = Course.objects.filter(title='Web Dev Bootcamp')
Order.objects.get(courses__in=course).student.interested_in.all()
# <QuerySet [<Topic: IT Certification>, <Topic: Web Development>, <Topic: Management>]>

# n. Find the length of the courses for the topic that ‘chris’ is interested in. (You may assume that ‘alan’ is interested in exactly one topic.)
Student.objects.get(username='chris').interested_in.all()[0].length
# 10

# o. Find the number of courses that ‘chris’ is registered in.
Student.objects.get(username='chris').registered_courses.count()
# 2
