__version__ = "1.9.3"

from kivy.app import App
from kivy.core import text
from kivy.uix.widget import Widget
from kivy.base import EventLoop
from kivy.utils import get_color_from_hex as x
from kivy.graphics import Color, Line
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ToggleButtonBehavior
class RadioButton(ToggleButton):

    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)


class CanvasWidget(Widget):
    line_width = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return
        with self.canvas:
            touch.ud['current_line'] = Line(points =(touch.x, touch.y),width = self.line_width)
    
    
    def on_touch_move(self, touch):
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)
        return super().on_touch_move(touch)

    def set_line_width(self, line_width = 'normal'):
        self.line_width = {'Thin': 1, 'Normal': 2, 'Thick': 4}[line_width]

    def clear(self):
        saved = self.children[:]
        self.clear_widgets()
        self.canvas.clear()
        for widget in saved:
            self.add_widget(widget)

    def set_color(self, new_color):
        self.canvas.add(Color(*new_color))
        
class paintApp(App):
    def build(self):
        self.canvas_widget = CanvasWidget()
        self.canvas_widget.set_color(c("#2980B9"))
        EventLoop.ensure_window()
        return self.canvas_widget

if __name__=="__main__":

    #Window Settins
    from kivy.config import Config
    Config.set('graphics', 'width', '300')
    Config.set('graphics', 'height', '500')
    Config.set('graphics', 'resizable', '0')

    #Background Color Setting
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex as c
    Window.clearcolor = c("#FFFFFF")
    Window.set_system_cursor('crosshair')
    paintApp().run()