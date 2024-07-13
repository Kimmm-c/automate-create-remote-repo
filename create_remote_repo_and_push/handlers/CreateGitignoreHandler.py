from .BaseHandler import BaseHandler
from ..models.Repository import Repository


class CreateGitignoreHandler(BaseHandler):
    def process(self, request: Repository):
        print("processing create gitignore")

        if self.next_handler is not None:
            self.next_handler.process(request)
        else:
            return
