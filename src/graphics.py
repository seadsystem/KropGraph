__author__ = "Your name"
__email__ = "Your email"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class Graphics(object):

    def __init__(self):
        pass

    def build_graph(self):
        """
        returns a widget containing the graph
        """
        # print("test")
        # return Label(text='Hello World')
        return GraphWidget()

    def build_buttons(self):
        """
        returns a widget containing the buttons
        """
        return ButtonsWidget()

    def build_battery(self):
        return BatteryWidget()

    def build_layout(self):
        """
        returns a layout containing all the other elements
        this should be called 
        """
        return ContainerLayout()


class GraphWidget(Widget):
    def __init__(self, **kwargs):
        super(GraphWidget, self).__init__(**kwargs)

class BatteryWidget(Widget):
    def __init__(self, **kwargs):
        super(BatteryWidget, self).__init__(**kwargs)

class ButtonsWidget(Widget):
    def __init__(self, **kwargs):
        super(ButtonsWidget, self).__init__(**kwargs)

class ContainerLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerLayout, self).__init__(**kwargs)

class TestApp(App):
    def build(self):
        Builder.load_file('./kvlayouts/container.kv')
        graphics = Graphics()
        containerlayout = graphics.build_layout()
        return containerlayout


def main():
    # test = Graphics()
    # test.build_graph()
    TestApp().run()

if __name__ == "__main__":
    main()
