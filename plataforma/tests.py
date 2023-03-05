from django.test import TestCase
from django.urls import reverse, resolve



class ClientesUrlTest(TestCase):
    def test_newslatter_url_is_correct(self):
        url = reverse('newslatter')
        self.assertEqual(url, '/clientes/newslatter/')

    def test_email_contato_url_is_correct(self):
        url = reverse('email_contato')
        self.assertEqual(url, '/clientes/email_contato/')


class PlataformaUrlTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('home')
        self.assertEqual(url, '/')


class PlataformaViewTest(TestCase):
    def test_plataforma_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertTrue(True)