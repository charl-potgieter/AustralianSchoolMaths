# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import os
from graphs import Figure, DataSeries
from data_sources import DataSource
import sympy as sp


def save_sin_graph_radians(target_dir: str, figure_width: int):

    my_graph = Figure()
    x = sp.symbols('x')

    my_graph.dimensions.width = figure_width
    my_graph.dimensions.height = figure_width * 0.4

    graph_data = DataSeries()
    graph_data.domain.min = -10
    graph_data.domain.max = 10
    graph_data.expression = sp.sin(x)
    graph_data.style.colour = 'blue'
    graph_data.style.has_left_arrow = True
    graph_data.style.has_right_arrow = True
    my_graph.axes.add_plot_data(graph_data)

    my_graph.axes.x_axis_tick_symbolic_interval = sp.pi
    my_graph.axes.y_axis_tick_interval = 0.5

    my_graph.axes.display_buffer.top = 0.5
    my_graph.axes.display_buffer.right = 0.05
    my_graph.axes.display_buffer.left = 0.05
    my_graph.axes.legend_location = 'upper right'

    fname = target_dir + os.path.sep + 'trig_sin_radians.jpg'
    print(fname)
    my_graph.save(fname)


def save_cos_graph_radians(target_dir: str, figure_width: int):

    my_graph = Figure()
    x = sp.symbols('x')

    my_graph.dimensions.width = figure_width
    my_graph.dimensions.height = figure_width * 0.4

    graph_data = DataSeries()
    graph_data.domain.min = -10
    graph_data.domain.max = 10
    graph_data.expression = sp.cos(x)
    graph_data.style.colour = 'blue'
    graph_data.style.has_left_arrow = True
    graph_data.style.has_right_arrow = True
    my_graph.axes.add_plot_data(graph_data)

    my_graph.axes.x_axis_tick_symbolic_interval = sp.pi
    my_graph.axes.y_axis_tick_interval = 0.5

    my_graph.axes.display_buffer.top = 0.5
    my_graph.axes.display_buffer.right = 0.05
    my_graph.axes.display_buffer.left = 0.05
    my_graph.axes.legend_location = 'upper right'

    fname = target_dir + os.path.sep + 'trig_cos_radians.jpg'
    print(fname)
    my_graph.save(fname)


if __name__ == '__main__':
    image_dir = DataSource().static_images_directory
    GRAPH_WIDTH = 20
    save_sin_graph_radians(image_dir, GRAPH_WIDTH)
    save_cos_graph_radians(image_dir, GRAPH_WIDTH)