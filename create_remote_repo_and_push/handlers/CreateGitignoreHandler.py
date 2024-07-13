from .BaseHandler import BaseHandler
from ..models.request import Request


class CreateGitignoreHandler(BaseHandler):
    def process(self, request: Request):
        print("processing create gitignore")

        if self.next_handler is not None:
            self.next_handler.process(request)
        else:
            return
