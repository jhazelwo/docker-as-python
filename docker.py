""" -*- coding: utf-8 -*- """


class Docker(object):
    def __init__(self, dockerfile, name):
        self.dockerfile = dockerfile
        self.name = name
        self.volumes = []
        self.ports = []
        self.hostname = None
        self.run_name = None

    def build(self):
        pass

    def run(self):
        pass
