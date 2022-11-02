from django.test import TestCase
from ..models import Student,Faculty,Book



class BookTestCase(TestCase):

    def  setUp(self):
        self.book1=Book.objects.create(
        bookName="Security",
        bookSerialNumber="SE1234",
        publisher="klb",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        author="smith",

        )

    def test_book_created(self):
        self.assertEquals(self.book1.bookName,"Security")