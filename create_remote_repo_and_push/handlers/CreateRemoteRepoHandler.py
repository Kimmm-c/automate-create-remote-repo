from .BaseHandler import BaseHandler
from ..models.request import Request


class CreateRemoteRepoHandler(BaseHandler):
    def process(self, request: Request):
        print("processing create remote repo")

        if self.next_handler is not None:
            self.next_handler.process(request)
        else:
            return
