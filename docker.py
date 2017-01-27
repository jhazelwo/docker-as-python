""" -*- coding: utf-8 -*- """


class Docker(object):
    def __init__(self, dockerfile, name):
        self.dockerfile = dockerfile
        self.name = name
        self.volumes = []
        self.ports = []
        self.hostname = None
        self.run_name = None
        self.build_rm = False
        self.run_rm = False
        self.detach = False

    def build(self):
        pass

    def run(self):
        pass
