# coding: utf-8
from core.base_handler import BaseHandler
from apps.hello_world.services import hello

from tornado.httpclient import AsyncHTTPClient, HTTPClient
from tornado.web import asynchronous
from tornado.gen import engine, Task


class IndexHandler(BaseHandler):
    @asynchronous
    @engine
    def get(self):
        client = AsyncHTTPClient()
        response = yield Task(client.fetch, 'http://localhost:8000/hello/')
        self.write('hello, world')
        self.finish()
        
