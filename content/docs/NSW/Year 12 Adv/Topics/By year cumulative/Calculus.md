---
weight: 4
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


<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "8cfd91fb-88b1-4851-828c-58f19792c726" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_f1ff5 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f1ff5 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_f1ff5">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f1ff5_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_f1ff5_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_f1ff5_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_3c3da th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3c3da td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_3c3da_row0_col0, #T_3c3da_row1_col0, #T_3c3da_row2_col0, #T_3c3da_row3_col0, #T_3c3da_row4_col0, #T_3c3da_row5_col0, #T_3c3da_row6_col0, #T_3c3da_row7_col0 {
  background-color: rgba(0,0,0,0);
}
#T_3c3da_row8_col0, #T_3c3da_row9_col0, #T_3c3da_row10_col0, #T_3c3da_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_3c3da">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_3c3da_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_3c3da_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_3c3da_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Differential Calculus </span> 
<br>

### <span style="color:RGB(139,69,19)">  Notes </span>



#### Differentiation of trigonometric, exponential and logarithmic functions

Refer formulas below (the non-chain rule versions).  Note cases requiring proof.

**NB** The trig derivative rules work on radians, not degrees.  If a question is in degrees it first needs to be converted into radians.  Convert back to degrees in final step if required.

#### Rules of differentiation

Apply product, quotient and chain rules to differentiate the "simpler" versions of the function.

In particular note that $\tan x$ can be converted to $\dfrac{sin x}{cos x}$ and the quotient rule can then be applied.  Similiarly the quotient rule can be used to calculate $\sec x$ and $\cosec x$ by converting these into $\frac{1}{cos x}$ and $\frac{1}{sin x}$ respectively.

Use log laws to simplify expressions before differentiating.

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "f41b372a-b3d6-466d-aae9-3be097ff8ac8" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_01bd2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_01bd2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_01bd2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_01bd2_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_01bd2_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_01bd2_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_01bd2_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_01bd2_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_01bd2_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_01bd2_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_01bd2_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_01bd2_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_01bd2_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_01bd2_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_01bd2_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_c046e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c046e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c046e_row0_col0, #T_c046e_row1_col0, #T_c046e_row2_col0, #T_c046e_row3_col0, #T_c046e_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_c046e_row5_col0, #T_c046e_row6_col0, #T_c046e_row7_col0, #T_c046e_row8_col0, #T_c046e_row9_col0, #T_c046e_row10_col0, #T_c046e_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_c046e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c046e_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_c046e_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_c046e_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_c046e_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_c046e_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_c046e_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_c046e_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_c046e_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_c046e_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_c046e_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_c046e_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_c046e_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_d3951 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d3951 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_d3951_row0_col0, #T_d3951_row1_col0, #T_d3951_row2_col0, #T_d3951_row3_col0, #T_d3951_row4_col0, #T_d3951_row5_col0, #T_d3951_row6_col0, #T_d3951_row7_col0, #T_d3951_row8_col0, #T_d3951_row9_col0, #T_d3951_row10_col0, #T_d3951_row11_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_d3951">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d3951_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_d3951_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_d3951_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_d3951_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_d3951_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_d3951_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_d3951_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_d3951_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_d3951_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_d3951_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_d3951_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_d3951_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Applications of Differentiation </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>
 - concatvity
 - local min or max
 - global min or max
 - point of inflection
 - horizontal point of inflection
 - monotonic increasing or decreasing


### <span style="color:RGB(139,69,19)">  Notes </span>

#### The first and second derivatives

**The second derivative** = $f''(x)$ or $\dfrac{d^{2}y}{dx^2}$
 
**Sign of the first derivative**
 - if f'(x)>0 then the graph y=f(x) is increasing
 - if f'(x)<0 then the graph y=f(x) is decreasing
 - if f'(x)=0 then the graph y=f(x) has a stationary point
 - if f'(x)>0 for all values of x then the curve is monotonic increasing
 - if f'(x)<0 for all values of x then the curve is monotonic decreasing

**Sign of the second derivative**
 - if f''(x)>0 
    - then f'(x) is increasing
    - the gradient of the tangent of f(x) is increasing (a greater upward slope or lesser downward slope)
    - f(x) is concave upwards
    - if f'(x)=0 this is a mimimum turning point
 - if f''(x)<0 
    - then f'(x) is decreasing
    - the gradient of the tangent of f(x) is decreasing (a lesser upward slope or greater downnward slope)
    - f(x) is concave downwards
    - if f'(x)=0 this is a maximum turning point
 - if f''(x) = 0
     - f'(x) is a constant
     - the tangent is neither increasing nor decreasing
     - if concavity changes it is a point of inflection
     - if concavity changes and f'(x)=0 it is a horizontal point of inflection

To test whether concavity changes test f''(x) just to the left and the right of the point being investigated.


**Stationary points**
 - Local minimum point
    - f'(x) = 0 at point
    - f'(x)<0 LHS of the point
    - f'(x)>0 RHS of the point
    - Or f'(x)=0 and f''(x)>0 
 - Local maximum point
    -  f'(x) = 0 at point
     - f'(x)>0 LHS of the point
     - f'(x)<0 RHS of the point
     - Or f'(x)=0 and f''(x)<0

**Inflection**
 - Point of inflection
   - f''(x) = 0,
   - and concavity changes at that point
 - Horizontal point of inflection
   - f''(x) = 0,
   - and concavity changes at that point,
   - and f'(x)=0

 <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_C3_CurveGraphSummary.jpg" />


#### Applications of the derivative

**Curve sketching techniques**
 - find stationary points where f'(x)=0
 - find points of inflection where f''(x)=0 and concavity changes
 - find x and y intercepts
 - find domain and range
 - identify any asymptotes or disontinuities
 - identify limiting behaviour of the function
 - Use symmetry where possible
    - even function f(-x) = f(x)  (graph is symmetrical in y-axis)
    - odd function f(-x) = -f(x)  (graph has rotational symmetry with respect to the origin,that is it remains unchanged after rotation of 180 degrees about the origin)
 - If the 2nd derivative is hard to calculate, the first derivative can be calculated to the left and right of the point being investigated to determine whether the curve is increasing or decreasing
  - Rembember to restrict domains when there is a square root involved.  The expression inside the square root must be greater than zero.

  **Global maxima and minima**
  
  Need to check turning points as well as endpoints in the domain for potential candidates.

  **Optimisation problems**
   - Find formula for quantity that is being maximised or minimised
   - Find min/max values using derivatives
   - Always check if an answer for f'(x)=0 is yielding a min or max with either
       - a second derivative calculation
       - calculating the first derivative at points just before and after the point being investigated.
<BR><BR>


## <span style="color:RGB(0,32,96"> Integral Calculus </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - anti-derivative / indefinate integral / pimitive
  - definite integral
 - area under a curve
 


### <span style="color:RGB(139,69,19)">  Notes </span>

When sketching a derivative graph:
 - the x-intercepts are where the original function has a stationary point
 - Where the derivative graph is above the x-axis, the original graph has a positive gradient and vice versa.
 - The anti-derivative represents a family of curves unless a point on the curve is specified.

 When solving integration questions be on the lookout for equations in the below formats or or equations that can be factored into these patterns:
  -  $f'(x)[f(x)]^n$ 
  
  - $\dfrac{f'(x)}{f((x))}$

  **NB** The trig integral rules work on radians, not degrees. If a question is in degrees it first needs to be converted into radians.  Convert back to degrees in final step if required.

  Capital letters are often used as convention for the integral / anti-derivatve function, for example if f(x) is the function F(x) is the anti-derivative.

  The area enclosed by a curve y=f(x), the x-axis and lines x=a and x=b is given by $\int_a^b f(x)dx = F(b)-F(a)$

  When calculating the area between a curve and the x-axis:
   - best to first sketch the curve and deterimine the x-intercepts
   - areas above and below the x-axis need to be calculated seperately, and there absolute values summed.

When a question asks to calculate the area bounded by a curve and either x or y axis, it is the area between the curve and the axis intercepts.  For example it could be something like the shaded sections below.

<!-- Parameter SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_C4_BoundedByCurve.jpg" />
 


**Even functions**
 - f(-x) = f(x)

- $ \int_{-a}^a dx = 2 \int_0^a dx $ 

- area under curve between -a and a  =  $ 2 \int_{0}^a dx$ 

<!-- Parameter SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_C4_EvenFunction.jpg" />


**Odd functions**
 - $f(-x) = -f(x)$

 - $ \int_{-a}^a dx=0$ 

 - area under curve between -a and a  =  $ 2 \int_{0}^a dx$ 
 
<!-- Parameter SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_C4_OddFunction.jpg" />



**Areas enclosed by the y-axis**
 - Can be calculated by rewriting the equation in the form x=f(y) and then calculting the absolute value of each portion of the integral to left or right of y=axis, that is $\int_a^b f(y) dy$

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "0bbbe06e-8d0b-4637-a9cb-f4622fd122f2" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_2da75 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2da75 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_2da75">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2da75_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_2da75_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_2da75_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_2da75_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_2da75_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_2da75_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_2da75_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_2da75_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_2da75_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_2da75_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_2da75_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_f1e22 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f1e22 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_f1e22_row0_col0, #T_f1e22_row1_col0, #T_f1e22_row2_col0, #T_f1e22_row3_col0, #T_f1e22_row4_col0, #T_f1e22_row5_col0, #T_f1e22_row6_col0, #T_f1e22_row7_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_f1e22_row8_col0, #T_f1e22_row9_col0, #T_f1e22_row10_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_f1e22">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f1e22_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_f1e22_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_f1e22_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_f1e22_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_f1e22_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_f1e22_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_f1e22_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_f1e22_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_f1e22_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_f1e22_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_f1e22_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_75ebc th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_75ebc td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_75ebc_row0_col0, #T_75ebc_row2_col0, #T_75ebc_row3_col0, #T_75ebc_row5_col0, #T_75ebc_row6_col0, #T_75ebc_row9_col0, #T_75ebc_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_75ebc_row1_col0, #T_75ebc_row4_col0, #T_75ebc_row7_col0, #T_75ebc_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_75ebc">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_75ebc_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_75ebc_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_75ebc_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_75ebc_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_75ebc_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_75ebc_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_75ebc_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_75ebc_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_75ebc_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_75ebc_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_75ebc_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}