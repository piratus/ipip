# -*- coding: utf-8 -*-
import urwid


class ActionButton(urwid.Button):
    def __init__(self, caption, callback):
        super().__init__("")
        urwid.connect_signal(self, 'click', callback)
        self._w = urwid.AttrMap(
            urwid.SelectableIcon(caption, 1),
            None, focus_map='reversed')


class Item(urwid.WidgetWrap):
    def __init__(self, name, model):
        super().__init__(ActionButton(["   ", str(name)], self.select))
        self.name = name
        self.model = model

    def select(self, button):
        self.model.toggle(self.name)
        marker = " * " if self.name in self.model else "   "
        self._w = ActionButton([marker, self.name], self.select)


class TextPanel(urwid.Pile):
    def __init__(self, text):
        super().__init__([
            urwid.AttrWrap(urwid.Divider(), 'divider'),
            urwid.Text('\n'.join(text)),
        ])
