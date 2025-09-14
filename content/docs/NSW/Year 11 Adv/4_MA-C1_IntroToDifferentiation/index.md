---
weight: 4
title: 'Introduction to Differentiation'
---

## Introduction to Differentiation

###   Concepts 

- acceleration
- average rate of change
- chain rule
- derivative function
- differentiability
- differentiation
- differentiation from first principles
- displacement
- gradient of a secant
- gradient of a tangent
- instantaneous rate of change
- limit
- normal
- product rule
- quotient rule
- secant
- stationary point
- tangent
- turning point
- velocity


###   Notes 


#### Gradients and tangents

A function y=f(x) is differentiable at a point x= a if its graph is
 - continuous, and
 - smooth 
at x=a

The gradient of a secant drawn through 2 points on a curve approximates the gradient of a tangent where accuaracy improves as the distance between the point decreases

$\tan \theta = \text{ the gradient m}$

#### Difference quotients

Average rate of change of f(x) = gradient of chord of a secant $= \dfrac{f(x+h) - f(x)}{h}  $

#### The derivative function and its graph

$\dfrac{dy}{dx} = y' = f'(x) =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $

Graphing a derivative funcion f'(x):
 - f'(x) is zero at a stationary point of f(x)
 - f'(x) is positive when f(x) has a positive gradient
 - f'(x) is negative when f(x) has a negative gradient

The derivative at a point represents the instantaneous rate of change


#### Calculating with derivatives

See formulas below<br>

*Average rate of change* of quantity Q with respect to time t = $\dfrac{Q_2-Q_1}{t_2-t_1}$ 
<br><br>
*Instantaneous rate of change* of quantity Q with respect to time t = $\dfrac{dQ}{dt}$ 
<br><br>
*Displacement* measures the distance of an object from a fixed point or origin. Usually positive to the right of the point and negative to the left.
<br><br>
*Velocity* is the instantaneous rate of change of displacement x over time t = $v = \dfrac{dx}{dt}$, for example measured in km/h or $km^{-1}$
<br><br>
*Acceleration* is the instantaneous rate of change of velocity v over time t = $ a = \dfrac{dv}{dt}$, for example measured in km/h/h or $km h^{-2}$


#### Other notes

If two lines with gradients $m_1 \text{ and } m_2$ are perpendicular then $m_1 m_2 = -1$


### Formulas
{{< tabs "tab693fae173570f292" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONE693fae173570f292 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONE693fae173570f292 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONE693fae173570f292">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONE693fae173570f292_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row0_col2" class="data row0 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row0_col3" class="data row0 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row0_col4" class="data row0 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row0_col5" class="data row0 col5" >nan</td>
      <td id="T_NONE693fae173570f292_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row0_col10" class="data row0 col10" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
      <td id="T_NONE693fae173570f292_row0_col11" class="data row0 col11" >False</td>
      <td id="T_NONE693fae173570f292_row0_col12" class="data row0 col12" >False</td>
      <td id="T_NONE693fae173570f292_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row1_col2" class="data row1 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row1_col3" class="data row1 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row1_col4" class="data row1 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row1_col5" class="data row1 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row1_col10" class="data row1 col10" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
      <td id="T_NONE693fae173570f292_row1_col11" class="data row1 col11" >False</td>
      <td id="T_NONE693fae173570f292_row1_col12" class="data row1 col12" >False</td>
      <td id="T_NONE693fae173570f292_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row2_col2" class="data row2 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row2_col3" class="data row2 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row2_col4" class="data row2 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row2_col5" class="data row2 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row2_col10" class="data row2 col10" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
      <td id="T_NONE693fae173570f292_row2_col11" class="data row2 col11" >False</td>
      <td id="T_NONE693fae173570f292_row2_col12" class="data row2 col12" >False</td>
      <td id="T_NONE693fae173570f292_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row3_col2" class="data row3 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row3_col3" class="data row3 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row3_col4" class="data row3 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row3_col5" class="data row3 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row3_col10" class="data row3 col10" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
      <td id="T_NONE693fae173570f292_row3_col11" class="data row3 col11" >False</td>
      <td id="T_NONE693fae173570f292_row3_col12" class="data row3 col12" >False</td>
      <td id="T_NONE693fae173570f292_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row4_col2" class="data row4 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row4_col3" class="data row4 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row4_col4" class="data row4 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row4_col5" class="data row4 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row4_col10" class="data row4 col10" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
      <td id="T_NONE693fae173570f292_row4_col11" class="data row4 col11" >False</td>
      <td id="T_NONE693fae173570f292_row4_col12" class="data row4 col12" >False</td>
      <td id="T_NONE693fae173570f292_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row5_col2" class="data row5 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row5_col3" class="data row5 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row5_col4" class="data row5 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row5_col5" class="data row5 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row5_col10" class="data row5 col10" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
      <td id="T_NONE693fae173570f292_row5_col11" class="data row5 col11" >False</td>
      <td id="T_NONE693fae173570f292_row5_col12" class="data row5 col12" >False</td>
      <td id="T_NONE693fae173570f292_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row6_col2" class="data row6 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row6_col3" class="data row6 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row6_col4" class="data row6 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row6_col5" class="data row6 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row6_col10" class="data row6 col10" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
      <td id="T_NONE693fae173570f292_row6_col11" class="data row6 col11" >False</td>
      <td id="T_NONE693fae173570f292_row6_col12" class="data row6 col12" >False</td>
      <td id="T_NONE693fae173570f292_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row7_col2" class="data row7 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row7_col3" class="data row7 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row7_col4" class="data row7 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row7_col5" class="data row7 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row7_col10" class="data row7 col10" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
      <td id="T_NONE693fae173570f292_row7_col11" class="data row7 col11" >False</td>
      <td id="T_NONE693fae173570f292_row7_col12" class="data row7 col12" >False</td>
      <td id="T_NONE693fae173570f292_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row8_col2" class="data row8 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row8_col3" class="data row8 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row8_col4" class="data row8 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row8_col5" class="data row8 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row8_col9" class="data row8 col9" >1.000000</td>
      <td id="T_NONE693fae173570f292_row8_col10" class="data row8 col10" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
      <td id="T_NONE693fae173570f292_row8_col11" class="data row8 col11" >True</td>
      <td id="T_NONE693fae173570f292_row8_col12" class="data row8 col12" >False</td>
      <td id="T_NONE693fae173570f292_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row9_col2" class="data row9 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row9_col3" class="data row9 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row9_col4" class="data row9 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row9_col5" class="data row9 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row9_col9" class="data row9 col9" >2.000000</td>
      <td id="T_NONE693fae173570f292_row9_col10" class="data row9 col10" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
      <td id="T_NONE693fae173570f292_row9_col11" class="data row9 col11" >True</td>
      <td id="T_NONE693fae173570f292_row9_col12" class="data row9 col12" >False</td>
      <td id="T_NONE693fae173570f292_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row10_col2" class="data row10 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row10_col3" class="data row10 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row10_col4" class="data row10 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row10_col5" class="data row10 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row10_col9" class="data row10 col9" >3.000000</td>
      <td id="T_NONE693fae173570f292_row10_col10" class="data row10 col10" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
      <td id="T_NONE693fae173570f292_row10_col11" class="data row10 col11" >True</td>
      <td id="T_NONE693fae173570f292_row10_col12" class="data row10 col12" >False</td>
      <td id="T_NONE693fae173570f292_row10_col13" class="data row10 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE693fae173570f292_row11_col0" class="data row11 col0" >NSW</td>
      <td id="T_NONE693fae173570f292_row11_col1" class="data row11 col1" >Year 11 Adv</td>
      <td id="T_NONE693fae173570f292_row11_col2" class="data row11 col2" >Calculus</td>
      <td id="T_NONE693fae173570f292_row11_col3" class="data row11 col3" >MA-C1</td>
      <td id="T_NONE693fae173570f292_row11_col4" class="data row11 col4" >Introduction to Differentiation</td>
      <td id="T_NONE693fae173570f292_row11_col5" class="data row11 col5" >Differentiation</td>
      <td id="T_NONE693fae173570f292_row11_col6" class="data row11 col6" >nan</td>
      <td id="T_NONE693fae173570f292_row11_col7" class="data row11 col7" >nan</td>
      <td id="T_NONE693fae173570f292_row11_col8" class="data row11 col8" >nan</td>
      <td id="T_NONE693fae173570f292_row11_col9" class="data row11 col9" >nan</td>
      <td id="T_NONE693fae173570f292_row11_col10" class="data row11 col10" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
      <td id="T_NONE693fae173570f292_row11_col11" class="data row11 col11" >True</td>
      <td id="T_NONE693fae173570f292_row11_col12" class="data row11 col12" >False</td>
      <td id="T_NONE693fae173570f292_row11_col13" class="data row11 col13" >nan</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEET693fae173570f292 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEET693fae173570f292 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEET693fae173570f292_row0_col0, #T_FORMULA_SHEET693fae173570f292_row0_col1, #T_FORMULA_SHEET693fae173570f292_row0_col2, #T_FORMULA_SHEET693fae173570f292_row0_col3, #T_FORMULA_SHEET693fae173570f292_row0_col4, #T_FORMULA_SHEET693fae173570f292_row0_col5, #T_FORMULA_SHEET693fae173570f292_row0_col6, #T_FORMULA_SHEET693fae173570f292_row0_col7, #T_FORMULA_SHEET693fae173570f292_row0_col8, #T_FORMULA_SHEET693fae173570f292_row0_col9, #T_FORMULA_SHEET693fae173570f292_row0_col10, #T_FORMULA_SHEET693fae173570f292_row0_col11, #T_FORMULA_SHEET693fae173570f292_row0_col12, #T_FORMULA_SHEET693fae173570f292_row0_col13, #T_FORMULA_SHEET693fae173570f292_row1_col0, #T_FORMULA_SHEET693fae173570f292_row1_col1, #T_FORMULA_SHEET693fae173570f292_row1_col2, #T_FORMULA_SHEET693fae173570f292_row1_col3, #T_FORMULA_SHEET693fae173570f292_row1_col4, #T_FORMULA_SHEET693fae173570f292_row1_col5, #T_FORMULA_SHEET693fae173570f292_row1_col6, #T_FORMULA_SHEET693fae173570f292_row1_col7, #T_FORMULA_SHEET693fae173570f292_row1_col8, #T_FORMULA_SHEET693fae173570f292_row1_col9, #T_FORMULA_SHEET693fae173570f292_row1_col10, #T_FORMULA_SHEET693fae173570f292_row1_col11, #T_FORMULA_SHEET693fae173570f292_row1_col12, #T_FORMULA_SHEET693fae173570f292_row1_col13, #T_FORMULA_SHEET693fae173570f292_row2_col0, #T_FORMULA_SHEET693fae173570f292_row2_col1, #T_FORMULA_SHEET693fae173570f292_row2_col2, #T_FORMULA_SHEET693fae173570f292_row2_col3, #T_FORMULA_SHEET693fae173570f292_row2_col4, #T_FORMULA_SHEET693fae173570f292_row2_col5, #T_FORMULA_SHEET693fae173570f292_row2_col6, #T_FORMULA_SHEET693fae173570f292_row2_col7, #T_FORMULA_SHEET693fae173570f292_row2_col8, #T_FORMULA_SHEET693fae173570f292_row2_col9, #T_FORMULA_SHEET693fae173570f292_row2_col10, #T_FORMULA_SHEET693fae173570f292_row2_col11, #T_FORMULA_SHEET693fae173570f292_row2_col12, #T_FORMULA_SHEET693fae173570f292_row2_col13, #T_FORMULA_SHEET693fae173570f292_row3_col0, #T_FORMULA_SHEET693fae173570f292_row3_col1, #T_FORMULA_SHEET693fae173570f292_row3_col2, #T_FORMULA_SHEET693fae173570f292_row3_col3, #T_FORMULA_SHEET693fae173570f292_row3_col4, #T_FORMULA_SHEET693fae173570f292_row3_col5, #T_FORMULA_SHEET693fae173570f292_row3_col6, #T_FORMULA_SHEET693fae173570f292_row3_col7, #T_FORMULA_SHEET693fae173570f292_row3_col8, #T_FORMULA_SHEET693fae173570f292_row3_col9, #T_FORMULA_SHEET693fae173570f292_row3_col10, #T_FORMULA_SHEET693fae173570f292_row3_col11, #T_FORMULA_SHEET693fae173570f292_row3_col12, #T_FORMULA_SHEET693fae173570f292_row3_col13, #T_FORMULA_SHEET693fae173570f292_row4_col0, #T_FORMULA_SHEET693fae173570f292_row4_col1, #T_FORMULA_SHEET693fae173570f292_row4_col2, #T_FORMULA_SHEET693fae173570f292_row4_col3, #T_FORMULA_SHEET693fae173570f292_row4_col4, #T_FORMULA_SHEET693fae173570f292_row4_col5, #T_FORMULA_SHEET693fae173570f292_row4_col6, #T_FORMULA_SHEET693fae173570f292_row4_col7, #T_FORMULA_SHEET693fae173570f292_row4_col8, #T_FORMULA_SHEET693fae173570f292_row4_col9, #T_FORMULA_SHEET693fae173570f292_row4_col10, #T_FORMULA_SHEET693fae173570f292_row4_col11, #T_FORMULA_SHEET693fae173570f292_row4_col12, #T_FORMULA_SHEET693fae173570f292_row4_col13, #T_FORMULA_SHEET693fae173570f292_row5_col0, #T_FORMULA_SHEET693fae173570f292_row5_col1, #T_FORMULA_SHEET693fae173570f292_row5_col2, #T_FORMULA_SHEET693fae173570f292_row5_col3, #T_FORMULA_SHEET693fae173570f292_row5_col4, #T_FORMULA_SHEET693fae173570f292_row5_col5, #T_FORMULA_SHEET693fae173570f292_row5_col6, #T_FORMULA_SHEET693fae173570f292_row5_col7, #T_FORMULA_SHEET693fae173570f292_row5_col8, #T_FORMULA_SHEET693fae173570f292_row5_col9, #T_FORMULA_SHEET693fae173570f292_row5_col10, #T_FORMULA_SHEET693fae173570f292_row5_col11, #T_FORMULA_SHEET693fae173570f292_row5_col12, #T_FORMULA_SHEET693fae173570f292_row5_col13, #T_FORMULA_SHEET693fae173570f292_row6_col0, #T_FORMULA_SHEET693fae173570f292_row6_col1, #T_FORMULA_SHEET693fae173570f292_row6_col2, #T_FORMULA_SHEET693fae173570f292_row6_col3, #T_FORMULA_SHEET693fae173570f292_row6_col4, #T_FORMULA_SHEET693fae173570f292_row6_col5, #T_FORMULA_SHEET693fae173570f292_row6_col6, #T_FORMULA_SHEET693fae173570f292_row6_col7, #T_FORMULA_SHEET693fae173570f292_row6_col8, #T_FORMULA_SHEET693fae173570f292_row6_col9, #T_FORMULA_SHEET693fae173570f292_row6_col10, #T_FORMULA_SHEET693fae173570f292_row6_col11, #T_FORMULA_SHEET693fae173570f292_row6_col12, #T_FORMULA_SHEET693fae173570f292_row6_col13, #T_FORMULA_SHEET693fae173570f292_row7_col0, #T_FORMULA_SHEET693fae173570f292_row7_col1, #T_FORMULA_SHEET693fae173570f292_row7_col2, #T_FORMULA_SHEET693fae173570f292_row7_col3, #T_FORMULA_SHEET693fae173570f292_row7_col4, #T_FORMULA_SHEET693fae173570f292_row7_col5, #T_FORMULA_SHEET693fae173570f292_row7_col6, #T_FORMULA_SHEET693fae173570f292_row7_col7, #T_FORMULA_SHEET693fae173570f292_row7_col8, #T_FORMULA_SHEET693fae173570f292_row7_col9, #T_FORMULA_SHEET693fae173570f292_row7_col10, #T_FORMULA_SHEET693fae173570f292_row7_col11, #T_FORMULA_SHEET693fae173570f292_row7_col12, #T_FORMULA_SHEET693fae173570f292_row7_col13, #T_FORMULA_SHEET693fae173570f292_row8_col0, #T_FORMULA_SHEET693fae173570f292_row8_col1, #T_FORMULA_SHEET693fae173570f292_row8_col2, #T_FORMULA_SHEET693fae173570f292_row8_col3, #T_FORMULA_SHEET693fae173570f292_row8_col4, #T_FORMULA_SHEET693fae173570f292_row8_col5, #T_FORMULA_SHEET693fae173570f292_row8_col6, #T_FORMULA_SHEET693fae173570f292_row8_col7, #T_FORMULA_SHEET693fae173570f292_row8_col8, #T_FORMULA_SHEET693fae173570f292_row8_col9, #T_FORMULA_SHEET693fae173570f292_row8_col11, #T_FORMULA_SHEET693fae173570f292_row8_col12, #T_FORMULA_SHEET693fae173570f292_row8_col13, #T_FORMULA_SHEET693fae173570f292_row9_col0, #T_FORMULA_SHEET693fae173570f292_row9_col1, #T_FORMULA_SHEET693fae173570f292_row9_col2, #T_FORMULA_SHEET693fae173570f292_row9_col3, #T_FORMULA_SHEET693fae173570f292_row9_col4, #T_FORMULA_SHEET693fae173570f292_row9_col5, #T_FORMULA_SHEET693fae173570f292_row9_col6, #T_FORMULA_SHEET693fae173570f292_row9_col7, #T_FORMULA_SHEET693fae173570f292_row9_col8, #T_FORMULA_SHEET693fae173570f292_row9_col9, #T_FORMULA_SHEET693fae173570f292_row9_col11, #T_FORMULA_SHEET693fae173570f292_row9_col12, #T_FORMULA_SHEET693fae173570f292_row9_col13, #T_FORMULA_SHEET693fae173570f292_row10_col0, #T_FORMULA_SHEET693fae173570f292_row10_col1, #T_FORMULA_SHEET693fae173570f292_row10_col2, #T_FORMULA_SHEET693fae173570f292_row10_col3, #T_FORMULA_SHEET693fae173570f292_row10_col4, #T_FORMULA_SHEET693fae173570f292_row10_col5, #T_FORMULA_SHEET693fae173570f292_row10_col6, #T_FORMULA_SHEET693fae173570f292_row10_col7, #T_FORMULA_SHEET693fae173570f292_row10_col8, #T_FORMULA_SHEET693fae173570f292_row10_col9, #T_FORMULA_SHEET693fae173570f292_row10_col11, #T_FORMULA_SHEET693fae173570f292_row10_col12, #T_FORMULA_SHEET693fae173570f292_row10_col13, #T_FORMULA_SHEET693fae173570f292_row11_col0, #T_FORMULA_SHEET693fae173570f292_row11_col1, #T_FORMULA_SHEET693fae173570f292_row11_col2, #T_FORMULA_SHEET693fae173570f292_row11_col3, #T_FORMULA_SHEET693fae173570f292_row11_col4, #T_FORMULA_SHEET693fae173570f292_row11_col5, #T_FORMULA_SHEET693fae173570f292_row11_col6, #T_FORMULA_SHEET693fae173570f292_row11_col7, #T_FORMULA_SHEET693fae173570f292_row11_col8, #T_FORMULA_SHEET693fae173570f292_row11_col9, #T_FORMULA_SHEET693fae173570f292_row11_col11, #T_FORMULA_SHEET693fae173570f292_row11_col12, #T_FORMULA_SHEET693fae173570f292_row11_col13 {
  background-color: rgba(0,0,0,0);
}
#T_FORMULA_SHEET693fae173570f292_row8_col10, #T_FORMULA_SHEET693fae173570f292_row9_col10, #T_FORMULA_SHEET693fae173570f292_row10_col10, #T_FORMULA_SHEET693fae173570f292_row11_col10 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_FORMULA_SHEET693fae173570f292">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col2" class="data row0 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col3" class="data row0 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col4" class="data row0 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col5" class="data row0 col5" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col10" class="data row0 col10" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col11" class="data row0 col11" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col12" class="data row0 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col2" class="data row1 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col3" class="data row1 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col4" class="data row1 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col5" class="data row1 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col10" class="data row1 col10" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col11" class="data row1 col11" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col12" class="data row1 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col2" class="data row2 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col3" class="data row2 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col4" class="data row2 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col5" class="data row2 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col10" class="data row2 col10" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col11" class="data row2 col11" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col12" class="data row2 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col2" class="data row3 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col3" class="data row3 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col4" class="data row3 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col5" class="data row3 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col10" class="data row3 col10" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col11" class="data row3 col11" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col12" class="data row3 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col2" class="data row4 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col3" class="data row4 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col4" class="data row4 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col5" class="data row4 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col10" class="data row4 col10" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col11" class="data row4 col11" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col12" class="data row4 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col2" class="data row5 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col3" class="data row5 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col4" class="data row5 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col5" class="data row5 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col10" class="data row5 col10" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col11" class="data row5 col11" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col12" class="data row5 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col2" class="data row6 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col3" class="data row6 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col4" class="data row6 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col5" class="data row6 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col10" class="data row6 col10" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col11" class="data row6 col11" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col12" class="data row6 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col2" class="data row7 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col3" class="data row7 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col4" class="data row7 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col5" class="data row7 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col10" class="data row7 col10" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col11" class="data row7 col11" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col12" class="data row7 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col2" class="data row8 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col3" class="data row8 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col4" class="data row8 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col5" class="data row8 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col9" class="data row8 col9" >1.000000</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col10" class="data row8 col10" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col11" class="data row8 col11" >True</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col12" class="data row8 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col2" class="data row9 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col3" class="data row9 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col4" class="data row9 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col5" class="data row9 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col9" class="data row9 col9" >2.000000</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col10" class="data row9 col10" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col11" class="data row9 col11" >True</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col12" class="data row9 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col2" class="data row10 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col3" class="data row10 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col4" class="data row10 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col5" class="data row10 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col9" class="data row10 col9" >3.000000</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col10" class="data row10 col10" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col11" class="data row10 col11" >True</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col12" class="data row10 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row10_col13" class="data row10 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col0" class="data row11 col0" >NSW</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col1" class="data row11 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col2" class="data row11 col2" >Calculus</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col3" class="data row11 col3" >MA-C1</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col4" class="data row11 col4" >Introduction to Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col5" class="data row11 col5" >Differentiation</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col6" class="data row11 col6" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col7" class="data row11 col7" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col8" class="data row11 col8" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col9" class="data row11 col9" >nan</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col10" class="data row11 col10" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col11" class="data row11 col11" >True</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col12" class="data row11 col12" >False</td>
      <td id="T_FORMULA_SHEET693fae173570f292_row11_col13" class="data row11 col13" >nan</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
