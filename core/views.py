from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from core.pakages.SinglePageBS4 import SinglePageBS4
from core.models import FontionBooks
from django.views.generic import (ListView)
import xlsxwriter
import io
import time
from core.models import FontionBooks
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, 'f_books/index.html', context={})


def toExcel(request):
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=books_list.xlsx'
    excel_file = createExcelFile()
    response.write(excel_file)
    return response


def DeleteAllBooks(request):
    FontionBooks.objects.all().delete()
    return redirect('books-list')

class BooksListView(ListView):
    model = FontionBooks
    template_name= 'f_books/books_list.html'
    context_object_name = 'books'
    paginate_by = 48

def start_scraping_books(request):
    threads =[]
    for page in range(1,1000):
        base_url = f'https://www.wob.com/en-gb/category/fiction-books/{page}'
        threads.append(SinglePageBS4(base_url,page))


    rang = 40

    ln = len(threads)
    for i in range(0,ln,rang):
        for th in threads[i:i+rang]:
            th.start()

        time.sleep(30)

    for i in range(0,ln,rang):
        for th in threads[i:i+rang]:
            th.join()

        time.sleep(30)
    # for th in threads:
    #     th.start()

    # for th in threads:
    #     th.join()
    return HttpResponse('Done')





def createExcelFile():
    # employees = Employee.objects.all()
    output      = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    headers = [
                {'name':'productId', 'width':20},
                {'name':'productType', 'width':8},
                {'name':'imageUrl', 'width':40},
                {'name':'name', 'width':30},
                {'name':'currency', 'width':5},
                {'name':'sku', 'width':8},
                {'name':'urlSlug', 'width':30},
                {'name':'title', 'width':20},
                {'name':'author', 'width':10},
                {'name':'description', 'width':20},
                {'name':'price', 'width':5},
                {'name':'formatType', 'width':8},
            ]
    worksheet = workbook.add_worksheet('books')

    for col, obj in enumerate(headers):
        worksheet.set_column(col, col, obj['width'])
        worksheet.write(0, col , str(obj['name']))

    books = FontionBooks.objects.all()

    for row, book in enumerate(books):
        worksheet.write(row+1, 0,str(book.productId))
        worksheet.write(row+1, 1,str(book.productType))
        worksheet.write(row+1, 2,str(book.imageUrl))
        worksheet.write(row+1, 3,str(book.name))
        worksheet.write(row+1, 4,str(book.currency))
        worksheet.write(row+1, 5,str(book.sku))
        worksheet.write(row+1, 6,str(book.urlSlug))
        worksheet.write(row+1, 7,str(book.title))
        worksheet.write(row+1, 8,str(book.author))
        worksheet.write(row+1, 9,str(book.description))
        worksheet.write(row+1, 10,str(book.price))
        worksheet.write(row+1, 11,str(book.formatType))



    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data