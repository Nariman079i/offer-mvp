# from rest_framework import status
# from rest_framework.test import APITestCase , APIRequestFactory, APIClient
# from django.urls import reverse
#
# from users.models import DefaultUser
#
#
# # factory = APIRequestFactory()
# #
# # request = factory.post('/user/create' , {'email':'artur@mail.ru','password':'21'}, format='json')
# # print(request)
#
# # client = APIClient()
# #
# # for i in range(100):
# #     data = {
# #         'email': f'testing{i}@mail.ru',
# #         'password': 'artur'
# #     }
# #     res = client.post(reverse('users-list'),data,format='json' )
# #     print(res.data)
#
# client = APIClient()
# def r_url(name):
#     return reverse(name)
#
#
# def test_post(url ,data:dict, active=False ):
#     request = client.post(url, data, format="json")
#     print(request.data, request.status_code)
#
# def test_put():
#     pass
#
# def test_get():
#     pass
#
# def test_delete():
#     pass
#
# data = {
#         'email':'testcase1@mail.ru',
#         'password':'test'
#     }
#
# test_post(r_url('users-list'), data)
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status



