import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


APPID = 'jp.outlook.program.taniyoshima.pyt_gt4_menubutton'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"

    menubutton = Gtk.Template.Child()
    toolmenu = Gtk.Template.Child()

    def __init__(self, app):
        self.app = app
        Gtk.ApplicationWindow.__init__(self, application=app)

        action = Gio.SimpleAction.new("file1", None)
        action.connect("activate", self.on_file1)
        self.add_action(action)

        action = Gio.SimpleAction.new("file2", None)
        action.connect("activate", self.on_file2)
        self.add_action(action)

        popover = Gtk.PopoverMenu.new_from_model(self.toolmenu)
        self.menubutton.set_popover(popover)

    def on_file1(self, action, param):
        print('file1 selected')

    def on_file2(self, action, param):
        print('file2 selected')

    @Gtk.Template.Callback()
    def on_exit_button_clicked(self, button):
        self.app.quit()


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
