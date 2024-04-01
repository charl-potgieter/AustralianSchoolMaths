---
weight: 10
---

## <span style="color:RGB(0,32,96"> Introduction to Differentiation </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

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


### <span style="color:RGB(139,69,19)">  Notes </span>

#### Differentiability

A function y=f(x) is differentiable at a point x= a if its graph is
 - continuous, and
 - smooth 

at x=a


#### Differentiation from 1st principles

When 2 points are taken very close together on a curve, the gradient of the secant of these 2 points is very close to the gradient of the tangent at one of these points, which is called the instantaneous rate of change.

$f'(x) =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $

#### Short methods of differentiation
See formulas below<br>

Tip: If two lines with gradients $m_1 \text{ and } m_2$ are perpendicular then $m_1 m_2 = -1$

#### The chain rule
If a function can be written as a composite function where $y = f(u(x))$ then $\dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx}$

#### Other rules
See formulas listed below

#### Rates of change

*Average rate of change* of quantity Q with respect to time t = $\dfrac{Q_2-Q_1}{t_2-t_1}$ 
<br><br>
*Instantaneous rate of change* of quantity Q with respect to time t = $\dfrac{dQ}{dt}$ 
<br><br>
*Displacement* measures the distance of an object from a fixed point or origin. Usually positive to the right of the point and negative to the left.
<br><br>
*Velocity* is the instantaneous rate of change of displacement x over time t = $v = \dfrac{dx}{dt}$, for example measured in km/h or $km^{-1}$
<br><br>
*Acceleration* is the instantaneous rate of change of velocity v over time t = $ a = \dfrac{dv}{dt}$, for example measured in km/h/h or $km h^{-2}$
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "67a4bfbf-6299-42d4-abfe-50f72fd6af32" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_2ef62 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2ef62 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_2ef62">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2ef62_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_2ef62_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_2ef62_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_fb0d5 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fb0d5 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_fb0d5_row0_col0, #T_fb0d5_row1_col0, #T_fb0d5_row2_col0, #T_fb0d5_row3_col0, #T_fb0d5_row4_col0, #T_fb0d5_row5_col0, #T_fb0d5_row6_col0, #T_fb0d5_row7_col0 {
  background-color: rgba(0,0,0,0);
}
#T_fb0d5_row8_col0, #T_fb0d5_row9_col0, #T_fb0d5_row10_col0, #T_fb0d5_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_fb0d5">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fb0d5_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_fb0d5_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_fb0d5_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Rates of Change </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>

#### Rates of change with respect to time



#### Exponential growth and decay



#### Related rates of change
If y is related to x, and x is related to time t, then the instantaneous rate of change of y with respect to time t utilises the chain rule: <br>
$\dfrac{dy}{dt} = \dfrac{dy}{dx} \times \dfrac{dx}{dt}$

#### Motion in a straight line
**Zero displacement**, when a particle is at the origin that is x = 0<br><br>
**Velocity** = rate of change of displacement, $v = \dot x = \dfrac{dx}{dt}$<br>
If a particle is moving to the right then velocity is positive, to the left velocity is negative<br>
Zero velocity = when a particle is not moving<br><br>
**Accelaration** = $a = \ddot x = \dfrac{dv}{dt}$<br>
Acceleration to the right is positive, to the left is negative. <br>
If acceleration is in the same direction as velocity then the particle is speeding up (accelerating) and vice versa.<br>
Zero acceleration  = the particle is not accelerating of deccelerating, that is it has a constant velocity.


<BR><BR>


## <span style="color:RGB(0,32,96"> Differential Calculus </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "26e0d25b-b3dc-428e-a3a8-f70e259927cd" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_4aad3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4aad3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_4aad3">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4aad3_row0_col0" class="data row0 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_4aad3_row1_col0" class="data row1 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_4aad3_row2_col0" class="data row2 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_4aad3_row3_col0" class="data row3 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_4aad3_row4_col0" class="data row4 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_4aad3_row5_col0" class="data row5 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_4aad3_row6_col0" class="data row6 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_65b31 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_65b31 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_65b31_row0_col0, #T_65b31_row1_col0, #T_65b31_row2_col0, #T_65b31_row3_col0, #T_65b31_row4_col0, #T_65b31_row5_col0, #T_65b31_row6_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_65b31">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_65b31_row0_col0" class="data row0 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_65b31_row1_col0" class="data row1 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_65b31_row2_col0" class="data row2 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_65b31_row3_col0" class="data row3 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_65b31_row4_col0" class="data row4 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_65b31_row5_col0" class="data row5 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_65b31_row6_col0" class="data row6 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Applications of Differentiation </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>


## <span style="color:RGB(0,32,96"> Integral Calculus </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "a19d67e7-1f31-41d7-bf2b-22a58cbe5e08" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_afc33 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_afc33 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_afc33">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_afc33_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_afc33_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_afc33_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_afc33_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_afc33_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_afc33_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_afc33_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_afc33_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_afc33_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_afc33_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_25959 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_25959 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_25959_row0_col0, #T_25959_row1_col0, #T_25959_row2_col0, #T_25959_row3_col0, #T_25959_row4_col0, #T_25959_row5_col0, #T_25959_row6_col0, #T_25959_row7_col0, #T_25959_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_25959_row9_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_25959">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_25959_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_25959_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_25959_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_25959_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_25959_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_25959_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_25959_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_25959_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_25959_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_25959_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Calculus Skills </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "2f6d500f-7b7b-4a59-8f62-13f19ccdf213" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_28e35 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_28e35 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_28e35">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_28e35_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_28e35_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_28e35_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_28e35_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_28e35_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_28e35_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_28e35_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_28e35_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_28e35_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_28e35_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_28e35_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_28e35_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_28e35_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_14561 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_14561 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_14561_row0_col0, #T_14561_row3_col0, #T_14561_row4_col0, #T_14561_row8_col0, #T_14561_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_14561_row1_col0, #T_14561_row2_col0, #T_14561_row5_col0, #T_14561_row6_col0, #T_14561_row7_col0, #T_14561_row9_col0, #T_14561_row10_col0, #T_14561_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_14561">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_14561_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_14561_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_14561_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_14561_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_14561_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_14561_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_14561_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_14561_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_14561_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_14561_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_14561_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_14561_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_14561_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}


<br>


###  <span style="color:RGB(139,69,19)"> Derivatives vs integrals  </span>
<br>
{{< tabs "657b969d-5338-4efb-b7ef-085137cd6f65" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_302ff th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_302ff td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_302ff">
  <thead>
    <tr>
      <th id="T_302ff_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_302ff_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_302ff_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_302ff_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_302ff_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_302ff_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_302ff_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_302ff_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_302ff_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_302ff_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_302ff_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_302ff_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_302ff_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_302ff_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_302ff_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_302ff_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_302ff_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_302ff_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_302ff_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_302ff_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_302ff_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_302ff_row6_col0" class="data row6 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
      <td id="T_302ff_row6_col1" class="data row6 col1" ></td>
      <td id="T_302ff_row6_col2" class="data row6 col2" >Formula can be utilised to calculate otherwise hard to differentiate inverse functions</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_f1c0e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f1c0e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_f1c0e_row0_col0, #T_f1c0e_row1_col1, #T_f1c0e_row2_col0, #T_f1c0e_row4_col0, #T_f1c0e_row5_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_f1c0e_row0_col1, #T_f1c0e_row1_col0, #T_f1c0e_row2_col1, #T_f1c0e_row3_col0, #T_f1c0e_row3_col1, #T_f1c0e_row4_col1, #T_f1c0e_row5_col0, #T_f1c0e_row6_col0, #T_f1c0e_row6_col1 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_f1c0e">
  <thead>
    <tr>
      <th id="T_f1c0e_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_f1c0e_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_f1c0e_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_f1c0e_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_f1c0e_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_f1c0e_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_f1c0e_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_f1c0e_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_f1c0e_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_f1c0e_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_f1c0e_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_f1c0e_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_f1c0e_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_f1c0e_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_f1c0e_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_f1c0e_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_f1c0e_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_f1c0e_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_f1c0e_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_f1c0e_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_f1c0e_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_f1c0e_row6_col0" class="data row6 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
      <td id="T_f1c0e_row6_col1" class="data row6 col1" ></td>
      <td id="T_f1c0e_row6_col2" class="data row6 col2" >Formula can be utilised to calculate otherwise hard to differentiate inverse functions</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Applications of Calculus </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>


## <span style="color:RGB(0,32,96"> Further Integration </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>
