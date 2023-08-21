# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from enum import Enum
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
plt.style.use('classic')


class TickMarkType(Enum):
    STANDARD = 1
    DEGREES = 2


class GraphDomain():

    def __init__(self, domain_min: float, domain_max: float):
        self._domain_min = domain_min
        self._domain_max = domain_max
        self._interval = sp.Interval(domain_min, domain_max)

    @property
    def interval(self):
        return self._interval

    @property
    def min(self) -> float:
        return self._domain_min

    @property
    def max(self) -> float:
        return self._domain_max


class GraphXAxis():

    def __init__(self, domain: GraphDomain,
                 percent_buffer_over_domain: float = 0.1,):
        self._domain = domain
        self._percent_buffer_over_domain = percent_buffer_over_domain

    @property
    def limits(self) -> tuple[float, float]:
        """ x_limits factors in buffer over domain"""
        x_range = self._domain.max - self._domain.min
        x_lim_min = (self._domain.min
                     - x_range * self._percent_buffer_over_domain)
        x_lim_max = float(self._domain.max
                          + x_range * self._percent_buffer_over_domain)
        return (x_lim_min, x_lim_max)


class GraphTicks():

    def __init__(self, tick_values:sp.Set, tick_mark_type:TickMarkType):
        self.__tick_values = tick_values
        self._tick_mark_type = tick_mark_type

    def _format_tick_mark(self, tick_value, tick_position)->str:
        _ = tick_position  # Required by matplotlib but not needed here
        if self._tick_mark_type == TickMarkType.DEGREES:
            degree_equivalant = sp.deg(tick_value)
            latex_equivalent = sp.latex(degree_equivalant) + r'\degree'
        else:
            latex_equivalent = sp.latex(tick_value)
        # use dfrac rather than frac to ensure fraction characters are full
        # size
        latex_equivalent = latex_equivalent.replace(r'\frac', r'\dfrac')
        return ("$" + latex_equivalent + "$")


class GraphCanvas():

    def __init__(self, width:float, height:float, label:str):
        self._width = width
        self._height = height
        self._label = label



class _GraphCore():

    def __init__(self, points_to_plot: int = 1000):

        self.points_to_plot = points_to_plot


        self._graph_figure = self._setup_graph_figure(fig_width, fig_height)
        self._graph_axes = self._setup_graph_axes()
        self.set_x_ticks()
        self.set_y_ticks()

    def set_x_plots(self, x_values: list[float]):
        '''Set x plots'''
        self.x_plots = x_values

    def set_y_plots(self, y_values: list[float]):
        '''Set y plots'''
        self.y _plots = y_values

    @property
    def _y_limits(self) -> tuple[float]:
        y_range = max(self.y_plots) - min(self.y_plots)

        # Cover scenerio where no graph or graph paralell to x-axis
        if y_range == 0:
            return (self._x_limits)
        else:
            y_lim_min = min(self.y_plots) - (y_range *
                                             self.graph_buffer_over_domain)
            y_lim_max = max(self.y_plots) + (y_range *
                                             self.graph_buffer_over_domain)
            return (y_lim_min, y_lim_max)



    def _AddlegendInBbox(self, ax, x0=0, y0=0, pad=0.5, **kwargs):
        '''Creates legend in a box for matplotlib'''

        # Adapted from here
        # https://stackoverflow.com/questions/47539628/showing-legend-under-matplotlib-plot-with-varying-number-of-plots
        otrans = ax.figure.transFigure
        t = ax.legend(bbox_to_anchor=(x0, y0), loc='lower left',
                      bbox_transform=otrans, frameon=False, fontsize='x-large', **kwargs)
        # ax.figure.tight_layout(pad=pad)
        ax.figure.canvas.draw()
        tbox = t.get_window_extent().transformed(ax.figure.transFigure.inverted())
        bbox = ax.get_position()
        ax.set_position([bbox.x0, bbox.y0+tbox.height,
                        bbox.width, bbox.height-tbox.height])

    def _setup_graph_figure(self, fig_width, fig_height):
        '''returns a hidden matlpotlib figure containing one axes'''
        fig = plt.figure()
        fig.set_size_inches(fig_width, fig_height)
        fig.set_visible(False)
        return (fig)

    def _setup_graph_axes(self):
        '''Sets up a single axis on self._graph_figure and moves spine to origin'''
        ax = self._graph_figure.add_axes([0, 0, 1, 1])

        # making the top and right spine invisible:
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        # moving bottom spine up to y=0 position:
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))

        # moving left spine to the right to position x == 0:b
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

        return (ax)

    def _plot_graphs(self):
        '''Plots the graph on the axes'''
        ax = self._graph_axes

        # f(x)
        ax.plot(self.x_plots, self.y_plots,
                color='blue',
                label=self.graph_label)

        # -f(x)
        # Need to make this conditional on choice of flag.  Move these y-plot calcs to a seperate
        # property / method.  Need to make this calcualtion / display conditional on an init
        # parameter
        minus = [-x for x in self.y_plots]
        ax.plot(self.x_plots, minus,
                color='red',
                label='TBA')

    def _apply_axis_formatting(self):
        '''Applies axes formatting'''
        ax = self._graph_axes
        ax.xaxis.set_major_formatter(
            plt.FuncFormatter(self._format_x_tick_mark))
        ax.yaxis.set_major_formatter(
            plt.FuncFormatter(self._format_y_tick_mark))
        # ax.plot(self.x_plots, self.y_plots ,
        #         color = 'blue',
        #         label = self.graph_label)
        ax.legend(loc='upper right', frameon=False, fontsize='x-large')
        ax.set(
            xlim=self._x_limits(),
            ylim=self._y_limits(),
            xticks=self.x_ticks_floats,
            yticks=self.y_ticks_floats
        )
        self._AddlegendInBbox(ax, borderaxespad=5)

    def display(self):
        '''Displays the graph'''
        self._plot_graphs()
        self._apply_axis_formatting()
        self._graph_figure.set_visible(True)


class graph_function():

    def __init__(self,
                 fn,  # where fn is a sympy expression
                 # Sympy set for example an interval
                 domain_set=sp.Interval(-10, 10),
                 points_to_plot=1000, fig_width=10, fig_height=10, set_ticks_equal_intercepts=True,
                 x_tick_mark_type='standard', y_tick_mark_type='standard', graph_buffer_over_domain=0.1, graph_label=None):
        '''Graph function inits with the same parameters as graph with the addition of the function parameter'''

        self.fn = fn
        self.x = sp.Symbol('x', real=True)
        self.y = sp.Symbol('y', real=True)

        if graph_label is None:
            graph_label = '$ f(x) = ' + sp.latex(self.fn) + '$'
            # use dfrac rather than frac to ensure raction characters are full size
            graph_label = graph_label.replace('\frac', '\dfrac')

        self._graph = _GraphCore(
            domain_set=domain_set,
            points_to_plot=points_to_plot,
            fig_width=fig_width,
            fig_height=fig_height,
            x_tick_mark_type=x_tick_mark_type,
            y_tick_mark_type=y_tick_mark_type,
            graph_buffer_over_domain=graph_buffer_over_domain,
            graph_label=graph_label)

        self._graph.set_x_plots(self._calc_x_plots())
        self._graph.set_y_plots(self._calc_y_plots(points_to_plot))

        # Get intercepts in sympy numeric format
        intercepts = graph_axes_intercepts(fn, domain_set)
        self.x_intercepts = intercepts.x_intercepts
        self.y_intercepts = intercepts.y_intercepts

        if set_ticks_equal_intercepts:
            self._graph.set_x_ticks(self.x_intercepts)
            self._graph.set_y_ticks(self.y_intercepts)

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
