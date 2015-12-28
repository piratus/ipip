# coding: utf-8
from subprocess import check_output


class Package:

    def __init__(self, info_str, pip):
        self.name, version = info_str.split(' (')
        self.version = version[:-1]
        self.pip = pip
        self._info = None

    def __str__(self):
        return '{0} {1}'.format(self.name, self.version)

    @property
    def info(self):
        if not self._info:
            out = check_output('{0} show {1}'.format(self.pip, self.name),
                               shell=True)
            self._info = out.decode().split('\n')[1:-1]
        return self._info


class Packages:

    def __init__(self, pip=None):
        self.pip = pip or 'pip'
        self._items = None

    def __getitem__(self, index):
        return self.items[index]

    @property
    def items(self):
        if not self._items:
            out = check_output('{0} list'.format(self.pip), shell=True)
            items = sorted(out.decode().split('\n'), key=lambda x: x.lower())
            self._items = [Package(i, self.pip) for i in items if i]

        return self._items
