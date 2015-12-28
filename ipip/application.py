# coding: utf-8
import os

import urwid

from .packages import Packages
from .selection import Selection
from .widgets import Item, TextPanel


class Appication:
    palette = [
        ('head', 'light gray', 'dark blue'),
        ('divider', 'light gray', 'dark blue'),
        ('foot', 'light gray', 'black'),
        ('bold', 'white', 'dark blue'),
        ('reversed', 'standout', ''),
        ('flag', 'dark gray', 'light gray'),
        ('key', 'light cyan', 'dark blue', 'underline'),
    ]

    def __init__(self):
        self.selection = Selection()
        self.packages = Packages()
        self.dir = os.environ.get('VIRTUAL_ENV', 'NO VIRTUAL_ENV')

        self.header = urwid.Text([
            ('key', 'ipip 0.1.0'), ' | ',
            ('bold', self.dir), ' | ',
            ('key', '+'), ' Update  ',
            ('key', '-'), ' Uninstall  ',
            ('key', 'F'), 'reeze  ',
            ('key', 'Q'), 'uit',
        ])

        self.log = urwid.SimpleListWalker(
            [Item(i, self.selection) for i in self.packages])

        self.footer = TextPanel(self.packages[0].info)

        urwid.connect_signal(self.log, 'modified', self.on_change)

        self.list = urwid.ListBox(self.log)
        self.top = urwid.Frame(
            urwid.AttrWrap(self.list, 'body'),
            header=urwid.AttrWrap(self.header, 'head'),
            footer=urwid.AttrWrap(self.footer, 'foot')
        )

    def on_change(self):
        widget, index = self.log.get_focus()
        self.top._footer = TextPanel(self.packages[index].info)

    def handle_input(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def main(self):
        loop = urwid.MainLoop(
            self.top,
            palette=self.palette,
            unhandled_input=self.handle_input)
        loop.run()
