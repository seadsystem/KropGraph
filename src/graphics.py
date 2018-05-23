__author__ = "Your name"
__email__ = "Your email"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import Clock
from seads_core import SeadsCore
from backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

import matplotlib.patches as patches
from matplotlib.path import Path
import battery
from functools import partial

class Graphics(object):

    def __init__(self):
        pass

    def build_graph(self):
        """
        returns a widget containing the graph
        """
        # print("test")
        # return Label(text='Hello World')
        # return GraphWidget()

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
    def my_callback(self, dt):
        for appliance in self.core.get_appliances():
            self.plot_data(appliance.get_data())


    def battery_callback(self,percent,temp):
        self.box2.clear_widgets()
        plt.cla()
        plt.close()
        battery.draw_battery(self.box2,percent)
    def plot_data(self, data):
        if data == []:
            return
        values = data[0][0]
        values.reverse()
        self.box.clear_widgets()
        plt.cla()
        plt.close()
        plt.plot(values, color='blue')
        plt.ylabel('kWh')
        self.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))


    def build(self):
        battery_temp = 1    ##temporary for demonstration purposes
        battery_temp2 = .5  ##temporary for demonstration purposes
        self.core = SeadsCore()
        Builder.load_file('./kvlayouts/container.kv')
        graphics = Graphics()
        containerlayout = graphics.build_layout()
        Clock.schedule_interval(self.my_callback, 45)
        graph_widget = containerlayout.ids['graph_widget']
        battery_widget = containerlayout.ids['battery_widget']
        self.box = graph_widget.ids['boxlayout_h']
        self.box2 = battery_widget.ids['boxlayout_h']
        self.battery_callback(battery_temp,5)
        Clock.schedule_once(self.my_callback, 5)
        Clock.schedule_interval(partial(self.battery_callback,battery_temp2), 20)
        return containerlayout


def main():
    # test = Graphics()
    # test.build_graph()

    TestApp().run()

if __name__ == "__main__":
    main()
