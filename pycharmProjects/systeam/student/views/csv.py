import csv
from django.shortcuts import HttpResponse

def some_view(req):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['first','a','b'])
    writer.writerow(['second','AA','BB'])
    return response
