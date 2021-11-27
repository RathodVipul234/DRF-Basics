from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'p'
    page_size_query_param = 'record'
    max_page_size = 5

    '''
    two other pagination method here
    1).Limit Offset pagination
        ->in this method client have right to decide which page start(offset) and 
        how many record how in that page from write into url
           
    2).Cursor Pagination 
        ->in this method <next> and <previous> btn show and we can ordering according to us with model fields
         
    '''
