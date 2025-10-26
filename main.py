from django.http import HttpResponse

def index():
    return HttpResponse("Main")

class book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year =year

