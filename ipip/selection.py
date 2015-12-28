# coding: utf-8
class Selection:

    def __init__(self):
        self._items = set()

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        return iter(sorted(self._items, key=lambda x: x.lower()))

    def toggle(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            self._items.add(item)
