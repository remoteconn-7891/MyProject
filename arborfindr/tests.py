from django.test import TestCase

# Create your tests here.
def application(env, start_response):
    start_response('200 OK', [('Cotent-Type', 'text/html')])
    return [b"Hello World"]