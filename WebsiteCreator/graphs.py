# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import cast, Any, Generator
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter, MultipleLocator
import matplotlib.pyplot as plt
from matplotlib.spines import Spines
from matplotlib.axes import Axes
from matplotlib.axis import XAxis, YAxis
import numpy as np
import sympy as sp
plt.style.use('classic')


class _Domain():

    def __init__(self):
        self._domain_min = -10
        self._domain_max = 10

    @property
    def min(self) -> float:
        return self._domain_min

    @min.setter
    def min(self, value: float) -> None:
        self._domain_min = value

    @property
    def max(self) -> float:
        return self._domain_max

    @max.setter
    def max(self, value: float) -> None:
        self._domain_max = value

    @property
    def interval(self) -> sp.Interval:
        return sp.Interval(self._domain_min, self._domain_max)


class _Range():

    def __init__(self, y_values: list[float]):
        self._y_values = y_values

    @property
    def min(self) -> float:
        return min(self._y_values)

    @property
    def max(self) -> float:
        return max(self._y_values)

    @property
    def interval(self) -> sp.Interval:
        return sp.Interval(self.min, self.max)


class _SeriesStyle():

    def __init__(self):
        self._colour = 'blue'

    @property
    def colour(self) -> Any:
        return self._colour

    @colour.setter
    def colour(self, value: Any) -> None:
        self._colour = value


class DataSeries():

    def __init__(self):
        self._domain = _Domain()
        self._range = None
        self._expression = None
        self._number_of_points = 1000
        self._series_style = _SeriesStyle()
        self._x = sp.symbols('x')

    @property
    def domain(self):
        return self._domain

    @property
    def style(self) -> _SeriesStyle:
        return self._series_style

    @property
    def range(self):
        self._range = _Range(self.y_values)
        return self._range

    @property
    def expression(self) -> sp.Expr | None:
        return self._expression

    @expression.setter
    def expression(self, value: sp.Expr):
        self._expression = value

    @property
    def number_of_points(self) -> int:
        return self._number_of_points

    @number_of_points.setter
    def number_of_points(self, value: int):
        self._number_of_points = value

    @property
    def x_values(self) -> list[float]:
        return np.linspace(
            cast(Any, self._domain.min),
            cast(Any, self._domain.max),
            self._number_of_points)

    @property
    def y_values(self) -> list[float]:
        graph_function = sp.lambdify(self._x, self._expression, "numpy")
        return graph_function(self.x_values)

    @property
    def label(self):
        return_value = '$ f(x) = ' + sp.latex(self._expression) + '$'
        return_value = return_value.replace(r'\frac', r'\dfrac')
        return return_value


class _DataSet():

    def __init__(self):
        self._data = []

    def add(self, data: DataSeries) -> None:
        self._data.append(data)

    @property
    def data_series_items(self) -> Generator[DataSeries, None, None]:
        for item in self._data:
            yield item

    @property
    def max_domain(self) -> float | None:
        """Returns the max of alll the domain maximums in the data set"""
        max_found = None
        for data_series in self.data_series_items:
            if max_found is None:
                max_found = data_series.domain.max
            elif data_series.domain.max > max_found:
                max_found = data_series.domain.max
        return max_found

    @property
    def min_domain(self) -> float | None:
        min_found = None
        for data_item in self.data_series_items:
            if min_found is None:
                min_found = data_item.domain.min
            elif data_item.domain.min < min_found:
                min_found = data_item.domain.min
        return min_found

    @property
    def max_range(self) -> float | None:
        max_found = None
        for data_item in self.data_series_items:
            if max_found is None:
                max_found = data_item.range.max
            elif data_item.range.max > max_found:
                max_found = data_item.range.max
        return max_found

    @property
    def min_range(self) -> float | None:
        min_found = None
        for data_item in self.data_series_items:
            if min_found is None:
                min_found = data_item.range.min
            elif data_item.range.min < min_found:
                min_found = data_item.range.min
        return min_found


class _Spines():

    def __init__(self, spines: Spines):
        self._spines = spines

    def move_to_centre(self):
        """Centres spines at zero on x and y-axis"""
        self._spines[["left", "bottom"]].set_position(("data", 0))
        self._spines[["top", "right"]].set_visible(False)


class _SymbolicNumbers():
    """Manages list of sympy numbers and equivalent floats"""
    # TODO attempt to add hinting couldn't easily get this working

    def __init__(self, symbols):
        self._symbols = symbols

    @property
    def as_symbols(self):
        return self._symbols

    @property
    def as_latex(self):
        return ['$' + sp.latex(x).replace(r'\frac', r'\dfrac') + '$'
                for x in self._symbols]

    @property
    def as_latex_in_degrees(self):
        return ['$' + sp.latex(sp.deg(x))
                .replace(r'\frac', r'\dfrac') + r'\degree $'
                for x in self._symbols]

    @property
    def as_floats(self):
        return [float(x) for x in self._symbols]


class _SymbolicNumberIntervals():
    """manages a list of sympy symbolic values with given start,
    end and interval.  If zero lies in the range the intervals
    are calculated from zero, otherwise from start"""
    # TODO attempt to add hinting couldn't easily get this working

    def __init__(self, start, end, interval):
        self._start = start
        self._end = end
        self._interval = interval

    @property
    def values(self) -> _SymbolicNumbers:
        return _SymbolicNumbers(self._as_list)

    @property
    def _as_list(self):

        if self._range_spans_zero():
            return (self._intervals_from_start_to_zero()
                    + [sp.Rational(0)]
                    + self._intervals_from_zero_to_end()
                    )
        else:
            return self._intervals_from_start_to_end()

    def _range_spans_zero(self) -> bool:
        return (float(self._start) * float(self._end)) < 0

    def _intervals_from_start_to_end(self):
        return_list = []
        current_item = self._start
        while current_item <= self._end:
            return_list.append(current_item)
            current_item += self._interval
        return return_list

    def _intervals_from_start_to_zero(self):
        return_list = []
        current_item = -self._interval
        while current_item >= self._start:
            return_list.append(current_item)
            current_item -= self._interval
        return sorted(return_list)

    def _intervals_from_zero_to_end(self):
        return_list = []
        current_item = self._interval
        while current_item <= self._end:
            return_list.append(current_item)
            current_item += self._interval
        return return_list


class _Dimensions():

    def __init__(self):
        self._width = 20
        self._height = 20

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value


class _DisplayBuffer():
    """Records percentage buffer to display over graph domain and range"""

    def __init__(self):
        self._left = 0.1
        self._right = 0.1
        self._top = 0.1
        self._bottom = 0.1

    @property
    def left(self) -> float:
        return self._left

    @left.setter
    def left(self, value: float):
        self._left = value

    @property
    def right(self) -> float:
        return self._right

    @right.setter
    def right(self, value: float):
        self._right = value

    @property
    def top(self) -> float:
        return self._top

    @top.setter
    def top(self, value: float):
        self._top = value

    @property
    def bottom(self) -> float:
        return self._bottom

    @bottom.setter
    def bottom(self, value: float):
        self._bottom = value


class _SingleAxes():
    """A simpler purpose specfic wrapper for Matplotlib axes"""

    def __init__(self, axes: Axes):
        self._data_set = _DataSet()
        self._axes = axes
        self._display_buffer = _DisplayBuffer()
        self._spines = _Spines(axes.spines)
        self._spines.move_to_centre()
        self._legend_location = 'upper right'
        self._x_ticks_symbolic = []
        self._y_ticks_symbolic = []
        self._x_axis_tick_interval = None
        self._y_axis_tick_interval = None
        self._display_x_ticks_in_degrees = False
        self._display_y_ticks_in_degrees = False

    @property
    def legend_location(self) -> str | tuple[float, float]:
        return self._legend_location

    @legend_location.setter
    def legend_location(self, value: str | tuple[float, float]):
        self._legend_location = value

    @property
    def x_ticks_symbolic(self) -> list[sp.Expr]:
        return self._x_ticks_symbolic

    @x_ticks_symbolic.setter
    def x_ticks_symbolic(self, value: list[sp.Expr]):
        self._x_ticks_symbolic = value

    @property
    def y_ticks_symbolics(self) -> list[sp.Expr]:
        return self._y_ticks_symbolic

    @y_ticks_symbolics.setter
    def y_ticks_symbolic(self, value: list[sp.Expr]):
        self._y_ticks_symbolic = value

    @property
    def x_axis_tick_interval(self) -> None | sp.Expr:
        return self._x_axis_tick_interval

    @x_axis_tick_interval.setter
    def x_axis_tick_interval(self, value):
        self._x_axis_tick_interval = value

    @property
    def y_axis_tick_interval(self) -> None | sp.Expr:
        return self._y_axis_tick_interval

    @y_axis_tick_interval.setter
    def y_axis_tick_interval(self, value):
        self._y_axis_tick_interval = value

    @property
    def display_x_ticks_in_degrees(self) -> bool:
        return self._display_x_ticks_in_degrees

    @display_x_ticks_in_degrees.setter
    def display_x_ticks_in_degrees(self, value: bool):
        self._display_x_ticks_in_degrees = value

    @property
    def display_y_ticks_in_degrees(self) -> bool:
        return self._display_y_ticks_in_degrees

    @display_y_ticks_in_degrees.setter
    def display_y_ticks_in_degrees(self, value: bool):
        self._display_y_ticks_in_degrees = value

    def add_plot_data(self, plot_data: DataSeries) -> None:
        self._data_set.add(plot_data)

    @property
    def display_buffer(self) -> _DisplayBuffer:
        return self._display_buffer

    @display_buffer.setter
    def display_buffer(self, value: _DisplayBuffer):
        self._display_buffer = value

    def create(self):
        self._set_tick_position()
        self._set_axes_limits()
        if self._x_ticks_symbolic:
            self._set_x_ticks()
        elif self._x_axis_tick_interval:
            self._set_x_ticks_based_on_intervals()
        if self._y_ticks_symbolic:
            self.set_y_ticks()
        elif self._y_axis_tick_interval:
            self._set_y_ticks_based_on_intervals()

        self._generate_plot()
        self._setlegend()

    def _set_tick_position(self) -> None:
        self._axes.xaxis.set_ticks_position('bottom')
        self._axes.yaxis.set_ticks_position('left')

    def _set_axes_limits(self):
        self._axes.set(xlim=self._x_display_limits,
                       ylim=self._y_display_limits)

    def _set_x_ticks_based_on_intervals(self):
        x_ticks = _SymbolicNumberIntervals(
            self._x_display_limits[0],
            self._x_display_limits[1],
            self._x_axis_tick_interval)
        if self._display_x_ticks_in_degrees:
            self._axes.set_xticks(x_ticks.values.as_floats,
                                  x_ticks.values.as_latex_in_degrees)
        else:
            self._axes.set_xticks(x_ticks.values.as_floats,
                                  x_ticks.values.as_latex)

    def _set_y_ticks_based_on_intervals(self):
        y_ticks = _SymbolicNumberIntervals(
            self._y_display_limits[0],
            self._y_display_limits[1],
            self._y_axis_tick_interval)
        if self._display_y_ticks_in_degrees:
            self._axes.set_yticks(y_ticks.values.as_floats,
                                  y_ticks.values.as_latex_in_degrees)
        else:
            self._axes.set_yticks(y_ticks.values.as_floats,
                                  y_ticks.values.as_latex)

    def _set_x_ticks(self):
        ticks = _SymbolicNumbers(self._x_ticks_symbolic)
        if self._display_x_ticks_in_degrees:
            self._axes.set_xticks(ticks.as_floats,
                                  ticks.as_latex_in_degrees)
        else:
            self._axes.set_xticks(ticks.as_floats,
                                  ticks.as_latex)

    def set_y_ticks(self):
        ticks = _SymbolicNumbers(self._y_ticks_symbolic)
        if self._display_y_ticks_in_degrees:
            self._axes.set_yticks(ticks.as_floats,
                                  ticks.as_latex_in_degrees)
        else:
            self._axes.set_yticks(ticks.as_floats,
                                  ticks.as_latex)

    def _generate_plot(self):
        for data_series in self._data_set.data_series_items:
            self._axes.plot(data_series.x_values, data_series.y_values,
                            color=data_series.style.colour,
                            label=data_series.label)

    def _setlegend(self):
        self._axes.legend(framealpha=1, frameon=True,
                          loc=self._legend_location)

    @property
    def _x_display_limits(self) -> tuple[float, float]:
        if (self._data_set.max_domain is None
                or self._data_set.min_domain is None):
            return (0, 0)
        x_interval = self._data_set.max_domain - self._data_set.min_domain
        x_min = (self._data_set.min_domain
                 - x_interval * self.display_buffer.left)
        x_max = (self._data_set.max_domain +
                 x_interval * self.display_buffer.right)
        return (x_min, x_max)

    @property
    def _y_display_limits(self) -> tuple[float, float]:
        if (self._data_set.max_range is None
                or self._data_set.min_range is None):
            return (0, 0)
        y_interval = self._data_set.max_range - self._data_set.min_range
        y_min = (self._data_set.min_range
                 - y_interval * self.display_buffer.bottom)
        y_max = (self._data_set.max_range +
                 y_interval * self.display_buffer.top)
        return (y_min, y_max)


class Figure():
    """A simpler purpose specfic wrapper for Matplotlib figure"""

    def __init__(self):
        self._figure = plt.figure()
        self._dimensions = _Dimensions()
        # TODO consider changing to allow multiple Axes in plot need dependent
        axes = self._figure.add_axes([0, 0, 1, 1])
        self._axes = _SingleAxes(axes)

    @property
    def axes(self) -> _SingleAxes:
        return self._axes

    def _apply_properties(self):
        self._figure.set_figheight(self._dimensions.height)
        self._figure.set_figwidth(self._dimensions.width)
        self._figure.frameon = False

    def render(self):
        self._apply_properties()
        self._axes.create()

    def save(self, fname: str) -> None:
        self._apply_properties()
        self._axes.create()
        self._figure.savefig(fname)

    # def _setup_graph_figure(self, fig_width, fig_height):
    #     '''returns a hidden matlpotlib figure containing one axes'''
    #     fig = plt.figure()
    #     fig.set_size_inches(fig_width, fig_height)
    #     fig.set_visible(False)
    #     return (fig)

    # def _setup_graph_axes(self):
    #     '''Sets up a single axis on self._graph_figure and moves spine to origin'''
    #     ax = self._graph_figure.add_axes([0, 0, 1, 1])

    #     # making the top and right spine invisible:
    #     ax.spines['top'].set_color('none')
    #     ax.spines['right'].set_color('none')

    #     # moving bottom spine up to y=0 position:
    #     ax.xaxis.set_ticks_position('bottom')
    #     ax.spines['bottom'].set_position(('data', 0))

    #     # moving left spine to the right to position x == 0:b
    #     ax.yaxis.set_ticks_position('left')
    #     ax.spines['left'].set_position(('data', 0))

    #     return (ax)

    # def _plot_graphs(self):
    #     '''Plots the graph on the axes'''
    #     ax = self._graph_axes

    #     # f(x)
    #     ax.plot(self.x_plots, self.y_plots,
    #             color='blue',
    #             label=self.graph_label)

    #     # -f(x)
    #     # Need to make this conditional on choice of flag.  Move these y-plot calcs to a seperate
    #     # property / method.  Need to make this calcualtion / display conditional on an init
    #     # parameter
    #     minus = [-x for x in self.y_plots]
    #     ax.plot(self.x_plots, minus,
    #             color='red',
    #             label='TBA')

    # def _apply_axis_formatting(self):
    #     '''Applies axes formatting'''
    #     ax = self._graph_axes
    #     ax.xaxis.set_major_formatter(
    #         plt.FuncFormatter(self._format_x_tick_mark))
    #     ax.yaxis.set_major_formatter(
    #         plt.FuncFormatter(self._format_y_tick_mark))
    #     # ax.plot(self.x_plots, self.y_plots ,
    #     #         color = 'blue',
    #     #         label = self.graph_label)
    #     ax.legend(loc='upper right', frameon=False, fontsize='x-large')
    #     ax.set(
    #         xlim=self._x_limits(),
    #         ylim=self._y_limits(),
    #         xticks=self.x_ticks_floats,
    #         yticks=self.y_ticks_floats
    #     )
    #     self._AddlegendInBbox(ax, borderaxespad=5)

    # def display(self):
    #     '''Displays the graph'''
    #     self._plot_graphs()
    #     self._apply_axis_formatting()
    #     self._graph_figure.set_visible(True)


# class _GraphCore():

#     def __init__(self, points_to_plot: int = 1000):

#         self.points_to_plot = points_to_plot


#         self._graph_figure = self._setup_graph_figure(fig_width, fig_height)
#         self._graph_axes = self._setup_graph_axes()
#         self.set_x_ticks()
#         self.set_y_ticks()

#     def set_x_plots(self, x_values: list[float]):
#         '''Set x plots'''
#         self.x_plots = x_values

#     def set_y_plots(self, y_values: list[float]):
#         '''Set y plots'''
#         self.y _plots = y_values

#     @property
#     def _y_limits(self) -> tuple[float]:
#         y_range = max(self.y_plots) - min(self.y_plots)

#         # Cover scenerio where no graph or graph paralell to x-axis
#         if y_range == 0:
#             return (self._x_limits)
#         else:
#             y_lim_min = min(self.y_plots) - (y_range *
#                                              self.graph_buffer_over_domain)
#             y_lim_max = max(self.y_plots) + (y_range *
#                                              self.graph_buffer_over_domain)
#             return (y_lim_min, y_lim_max)


#     def _AddlegendInBbox(self, ax, x0=0, y0=0, pad=0.5, **kwargs):
#         '''Creates legend in a box for matplotlib'''

#         # Adapted from here
#         # https://stackoverflow.com/questions/47539628/showing-legend-under-matplotlib-plot-with-varying-number-of-plots
#         otrans = ax.figure.transFigure
#         t = ax.legend(bbox_to_anchor=(x0, y0), loc='lower left',
#                       bbox_transform=otrans, frameon=False, fontsize='x-large', **kwargs)
#         # ax.figure.tight_layout(pad=pad)
#         ax.figure.canvas.draw()
#         tbox = t.get_window_extent().transformed(ax.figure.transFigure.inverted())
#         bbox = ax.get_position()
#         ax.set_position([bbox.x0, bbox.y0+tbox.height,
#                         bbox.width, bbox.height-tbox.height])

#     def _setup_graph_figure(self, fig_width, fig_height):
#         '''returns a hidden matlpotlib figure containing one axes'''
#         fig = plt.figure()
#         fig.set_size_inches(fig_width, fig_height)
#         fig.set_visible(False)
#         return (fig)

#     def _setup_graph_axes(self):
#         '''Sets up a single axis on self._graph_figure and moves spine to origin'''
#         ax = self._graph_figure.add_axes([0, 0, 1, 1])

#         # making the top and right spine invisible:
#         ax.spines['top'].set_color('none')
#         ax.spines['right'].set_color('none')

#         # moving bottom spine up to y=0 position:
#         ax.xaxis.set_ticks_position('bottom')
#         ax.spines['bottom'].set_position(('data', 0))

#         # moving left spine to the right to position x == 0:b
#         ax.yaxis.set_ticks_position('left')
#         ax.spines['left'].set_position(('data', 0))

#         return (ax)

#     def _plot_graphs(self):
#         '''Plots the graph on the axes'''
#         ax = self._graph_axes

#         # f(x)
#         ax.plot(self.x_plots, self.y_plots,
#                 color='blue',
#                 label=self.graph_label)

#         # -f(x)
#         # Need to make this conditional on choice of flag.  Move these y-plot calcs to a seperate
#         # property / method.  Need to make this calcualtion / display conditional on an init
#         # parameter
#         minus = [-x for x in self.y_plots]
#         ax.plot(self.x_plots, minus,
#                 color='red',
#                 label='TBA')

#     def _apply_axis_formatting(self):
#         '''Applies axes formatting'''
#         ax = self._graph_axes
#         ax.xaxis.set_major_formatter(
#             plt.FuncFormatter(self._format_x_tick_mark))
#         ax.yaxis.set_major_formatter(
#             plt.FuncFormatter(self._format_y_tick_mark))
#         # ax.plot(self.x_plots, self.y_plots ,
#         #         color = 'blue',
#         #         label = self.graph_label)
#         ax.legend(loc='upper right', frameon=False, fontsize='x-large')
#         ax.set(
#             xlim=self._x_limits(),
#             ylim=self._y_limits(),
#             xticks=self.x_ticks_floats,
#             yticks=self.y_ticks_floats
#         )
#         self._AddlegendInBbox(ax, borderaxespad=5)

#     def display(self):
#         '''Displays the graph'''
#         self._plot_graphs()
#         self._apply_axis_formatting()
#         self._graph_figure.set_visible(True)


# class graph_function():

#     def __init__(self,
#                  fn,  # where fn is a sympy expression
#                  # Sympy set for example an interval
#                  domain_set=sp.Interval(-10, 10),
#                  points_to_plot=1000, fig_width=10, fig_height=10, set_ticks_equal_intercepts=True,
#                  x_tick_mark_type='standard', y_tick_mark_type='standard', graph_buffer_over_domain=0.1, graph_label=None):
#         '''Graph function inits with the same parameters as graph with the addition of the function parameter'''

#         self.fn = fn
#         self.x = sp.Symbol('x', real=True)
#         self.y = sp.Symbol('y', real=True)

#         if graph_label is None:
#             graph_label = '$ f(x) = ' + sp.latex(self.fn) + '$'
#             # use dfrac rather than frac to ensure raction characters are full size
#             graph_label = graph_label.replace('\frac', '\dfrac')

#         self._graph = _GraphCore(
#             domain_set=domain_set,
#             points_to_plot=points_to_plot,
#             fig_width=fig_width,
#             fig_height=fig_height,
#             x_tick_mark_type=x_tick_mark_type,
#             y_tick_mark_type=y_tick_mark_type,
#             graph_buffer_over_domain=graph_buffer_over_domain,
#             graph_label=graph_label)

#         self._graph.set_x_plots(self._calc_x_plots())
#         self._graph.set_y_plots(self._calc_y_plots(points_to_plot))

#         # Get intercepts in sympy numeric format
#         intercepts = graph_axes_intercepts(fn, domain_set)
#         self.x_intercepts = intercepts.x_intercepts
#         self.y_intercepts = intercepts.y_intercepts

#         if set_ticks_equal_intercepts:
#             self._graph.set_x_ticks(self.x_intercepts)
#             self._graph.set_y_ticks(self.y_intercepts)

#     def _discontinuities(self):
#         if self.fn.is_constant():
#             # Handle case fn=constant (no x in equation) = straight line parallel to x-axis
#             return ([])
#         else:
#             discontinuities = sp.singularities(self.fn, self.x)
#             discontinuities_in_domain = discontinuities.intersect(
#                 self._graph.domain_set)
#             sympy_list = list(discontinuities_in_domain)
#             float_list = [float(x) for x in sympy_list]
#             return (float_list)

#     def _calc_x_plots(self):
#         '''calc plot x-values'''
#         x_vals = np.linspace(float(self._graph.domain_set.start), float(
#             self._graph.domain_set.end), self._graph.points_to_plot)

#         # applies mask for example to prevent lines being drawn joining discontinuous portions of hyperbola, tan etc
#         for discontinuity in self._discontinuities():
#             first_value_after_discontinuity = next(
#                 (x for x in x_vals if x >= discontinuity), None)
#             first_value_before_discontinuity = next(
#                 (x for x in x_vals[::-1] if x < discontinuity), None)
#             # if first_value_before_discontinuity is not None and first_value_after_discontinuity is not None:
#             x_vals = np.ma.masked_where(
#                 (x_vals == first_value_before_discontinuity) | (
#                     x_vals == first_value_after_discontinuity),
#                 x_vals)

#         return (x_vals)

#     def _calc_y_plots(self, points_to_plot):
#         '''calc plot y-values'''
#         if self.fn.is_constant():
#             # Handle case fn=constant (no x in equation) = straight line parallel to x-axis
#             return ([float(self.fn)] * points_to_plot)
#         else:
#             fn_lambdify = sp.lambdify(self.x, self.fn)
#             return (fn_lambdify(self._graph.x_plots))

#     def display(self):
#         self._graph.display()


# class graph_straight_line():

#     def __init__(self,
#                  equation_form,  # string of either gradient-intercept, point-gradient, two-point, general-form, x-equals-constant, y-equals-constant
#                  # dictionary with keys m, c, x1, y1, x2, y2 depending on equation_form parameter
#                  equation_details,
#                  # Sympy set for example an interval
#                  domain_set=sp.Interval(-10, 10),
#                  # Sympy set for example an interval (only used for equation x=constant)
#                  range_for_line_parallel_to_y=sp.Interval(-10, 10),
#                  points_to_plot=1000, fig_width=10, fig_height=10, set_ticks_equal_intercepts=True,
#                  x_tick_mark_type='standard', y_tick_mark_type='standard', graph_buffer_over_domain=0.1):

#         self.y = sp.Symbol('y', real=True)
#         self.x = sp.Symbol('x', real=True)

#         # Use get rather than standard dictionary access in order to rerturn null if key is not found rather than generate an error
#         m = equation_details.get('m')
#         a = equation_details.get('a')
#         b = equation_details.get('b')
#         c = equation_details.get('c')
#         x1 = equation_details.get('x1')
#         y1 = equation_details.get('y1')
#         x2 = equation_details.get('x2')
#         y2 = equation_details.get('y2')

#         graph_label = self._calc_graph_label(equation_form, equation_details)

#         if equation_form == 'gradient-intercept':
#             fn = m * self.x + c
#             line_is_a_function = True

#         elif equation_form == 'point-gradient':
#             fn = m * (self.x - x1) + y1
#             line_is_a_function = True

#         elif equation_form == 'two-point':
#             if x1 == x2:
#                 # This effectively an equation of x= constant
#                 line_is_a_function = False
#                 c = x1
#             else:
#                 line_is_a_function = True
#                 fn = sp.Rational((y2 - y1), (x2 - x1)) * (x - x1) + y1

#         elif equation_form == 'general-form':
#             if b == 0:
#                 # Line is effecitvely in format x = constant
#                 line_is_a_function = False
#                 c = sp.Rational(-c, a)
#             else:
#                 line_is_a_function = True
#                 fn = -sp.Rational(a, b) * x - sp.Rational(c, b)

#         elif equation_form == 'x-equals-constant':
#             line_is_a_function = False

#         elif equation_form == 'y-equals-constant':
#             line_is_a_function = True
#             fn = c

#         if line_is_a_function:
#             self._graph = graph_function(fn=fn,
#                                          domain_set=domain_set,
#                                          points_to_plot=points_to_plot,
#                                          fig_width=fig_width,
#                                          fig_height=fig_height,
#                                          set_ticks_equal_intercepts=set_ticks_equal_intercepts,
#                                          x_tick_mark_type=x_tick_mark_type,
#                                          y_tick_mark_type=y_tick_mark_type,
#                                          graph_buffer_over_domain=graph_buffer_over_domain,
#                                          graph_label=graph_label)

#         else:
#             # Straight line is effectively in the format of x = constant (could be two-point format with x1=x2, or general form with b=0)
#             self._graph = _GraphCore(graph_label=graph_label)
#             self._graph.set_x_plots([c]*points_to_plot)
#             self._graph.set_y_plots(np.linspace(float(range_for_line_parallel_to_y.start), float(
#                 range_for_line_parallel_to_y.end), self._graph.points_to_plot))
#             self._graph.set_x_ticks([c])

#     def _calc_graph_label(self, equation_form, equation_details):
#         '''latex format to display on graph'''

#         if equation_form == 'gradient-intercept':
#             return (self._calc_graph_label_gradient_intercept(equation_details))

#         elif equation_form == 'point-gradient':
#             return (self._calc_graph_label_point_gradient(equation_details))

#         elif equation_form == 'two-point':
#             return (self._calc_graph_label_two_point(equation_details))

#         elif equation_form == 'general-form':
#             return (self._calc_graph_label_general_form(equation_details))

#         elif equation_form == 'x-equals-constant':
#             return (self._calc_graph_label_x_equals_constant(equation_details))

#         elif equation_form == 'y-equals-constant':
#             return (self._calc_graph_label_y_equals_constant(equation_details))

#         else:
#             # Should never arrive here
#             return ('undefined straight line format')

#     def _calc_graph_label_gradient_intercept(self, equation_details):
#         '''Calculates the latex display equation for straight line in gradient-intercept format'''

#         m = equation_details.get('m')
#         c = equation_details.get('c')
#         graph_label = '$(f(x) = ' + sp.latex(m*x + c) + '$'
#         # use dfrac rather than frac to ensure raction characters are full size
#         graph_label = graph_label.replace('\frac', '\dfrac')

#     def _calc_graph_label_point_gradient(self, equation_details):
#         '''Calculates the latex display equation for straight line in point gradient format'''

#         m = equation_details.get('m')
#         x1 = equation_details.get('x1')
#         y1 = equation_details.get('y1')

#         # Flips signs to avoid display of +-
#         if y1 >= 0:
#             latex_str = "$ (y - " + sp.latex(y1) + ') = ' + sp.latex(m) + '(x '
#         else:
#             latex_str = "$ (y + " + sp.latex(-y1) + \
#                 ') = ' + sp.latex(m) + '(x '
#         if x1 >= 0:
#             latex_str = latex_str + " - " + sp.latex(x1) + ')$'
#         else:
#             latex_str = latex_str + " + " + sp.latex(-x1) + ')$'

#         latex_str = latex_str.replace('\frac', '\dfrac')
#         return (latex_str)

#     def _calc_graph_label_two_point(self, equation_details):
#         '''Calculates the latex display equation for straight line in two point form'''

#         x1 = equation_details.get('x1')
#         y1 = equation_details.get('y1')
#         x2 = equation_details.get('x2')
#         y2 = equation_details.get('y2')

#         if x1 == x2:
#             # graph is effectively in format x = constant.  Cannot write in 2-point form as it will result
#             # in dividing be zero
#             latex_str = '$ y = ' + sp.latex(x1) + '$'
#         else:
#             # Flips signs to avoid display of +-
#             if y1 >= 0:
#                 latex_str = '$ (y - ' + sp.latex(y1) + ')'
#             else:
#                 latex_str = '$ (y + ' + sp.latex(-y1) + ')'
#             if y1 >= 0:
#                 latex_str = latex_str + \
#                     '=\dfrac{(' + sp.latex(y2) + ' - ' + \
#                     sp.latex(y1) + ')}{(' + sp.latex(x2)
#             else:
#                 latex_str = latex_str + \
#                     '=\dfrac{(' + sp.latex(y2) + ' + ' + \
#                     sp.latex(-y1) + ')}{(' + sp.latex(x2)
#             if x1 >= 0:
#                 latex_str = latex_str + " - " + sp.latex(x1) + ' )}(x'
#             else:
#                 latex_str = latex_str + " + " + sp.latex(-x1) + ' )}(x'
#             if x1 >= 0:
#                 latex_str = latex_str + " - " + sp.latex(x1) + ')$'
#             else:
#                 latex_str = latex_str + " + " + sp.latex(-x1) + ')$'

#         latex_str = latex_str.replace('\frac', '\dfrac')
#         return (latex_str)

#     def _calc_graph_label_general_form(self, equation_details):
#         '''Calculates the latex display equation for straight line in two point form'''

#         a = equation_details.get('a')
#         b = equation_details.get('b')
#         c = equation_details.get('c')

#         latex_str = '$ ' + sp.latex(a) + 'x + ' + \
#             sp.latex(b) + 'y+' + sp.latex(c) + '=0 $'
#         latex_str = latex_str.replace('\frac', '\dfrac')
#         return (latex_str)

#     def _calc_graph_label_x_equals_constant(self, equation_details):
#         '''Calculates the latex display equation for straight line in two point form'''

#         c = equation_details.get('c')
#         latex_str = '$ x = ' + sp.latex(c) + '$'
#         latex_str = latex_str.replace('\frac', '\dfrac')
#         return (latex_str)

#     def _calc_graph_label_y_equals_constant(self, equation_details):
#         '''Calculates the latex display equation for straight line in two point form'''

#         c = equation_details.get('c')
#         latex_str = '$ y = ' + sp.latex(c) + '$'
#         latex_str = latex_str.replace('\frac', '\dfrac')
#         return (latex_str)

#     def display(self):
#         self._graph.display()


# class graph_axes_intercepts():
#     '''Class that calculates and returns the x and y-intercepts of graphs of functions in both sympy numeric format'''

#     def __init__(self, fn, domain_set):
#         self.x = sp.Symbol('x', real=True)
#         self.x_intercepts = self._calc_x_intercepts(fn, domain_set)
#         self.y_intercepts = self._calc_y_intercepts(fn)

#     def _calc_x_intercepts(self, fn, domain_set):
#         return (list(sp.solveset(fn, self.x, domain=domain_set)))

#     def _calc_y_intercepts(self, fn):
#         if fn.subs(self.x, 0) == sp.S.ComplexInfinity:
#             return ([])
#         else:
#             return ([fn.subs(self.x, 0)])
