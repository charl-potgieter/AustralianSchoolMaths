---
weight: 7
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
 - f'(x) is positive when f(x) has an increasing gradient
 - f'(x) is negative when f(x) has a decreasing gradient

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
{{< tabs "c9c58cad-a7da-463f-94ae-ae8bf822e89f" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_8377b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8377b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_8377b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8377b_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_8377b_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_8377b_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_5efff th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5efff td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_5efff_row0_col0, #T_5efff_row1_col0, #T_5efff_row2_col0, #T_5efff_row3_col0, #T_5efff_row4_col0, #T_5efff_row5_col0, #T_5efff_row6_col0, #T_5efff_row7_col0 {
  background-color: rgba(0,0,0,0);
}
#T_5efff_row8_col0, #T_5efff_row9_col0, #T_5efff_row10_col0, #T_5efff_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_5efff">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5efff_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_5efff_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_5efff_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
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


*Zero displacement*, when a particle is at the origin that is x = 0<br><br>
*Velocity*
 - rate of change of displacement, $v = \dot x = \dfrac{dx}{dt}$

 - If a particle is moving to the right then velocity is positive, to the left velocity is negative

 - Zero velocity = when a particle is not moving
 <br><br>

*Accelaration*
 - $a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$

 - Acceleration to the right is positive, to the left is negative. 

 - If acceleration is in the same direction as velocity then the particle is speeding up (accelerating) and vice versa.

 - Zero acceleration  = the particle is not accelerating or deccelerating, that is it has a constant velocity.

<br><br>

#### Exponential growth and decay

*Rate of change is directly proportional to the current amount of the quantity*
 - That is... $\dfrac{dN}{dt} = kN$
 
 - $N(t) = Ae^{kt}$ satisfies the above relationship (be able to prove)

 - k is the growth (positive) of decay (negative) constant 

 - N = quantity

 - t = time

 - Initial quantity = A

 -  when $k<0$, then ${N \to 0} \text { as } {t \to \infty} $

 - <span style="color:RGB(255,0,0)"> Insert graph for both positive and negative values of k </span>

<br>

*Rate of change is directly proportional to the difference between the current amount of the quantity and a fixed quantity*
- That is... $\dfrac{dN}{dt} = k(N-p)$

- $N(t) = P + Ae^{kt}$ satisfies the above relationship (be able to prove)

-  Initial quantity  = P+A

- when $k<0$, then ${N \to P} \text { as } {t \to \infty} $

- <span style="color:RGB(255,0,0)"> Insert graph for both positive and negative values of k </span>

<br>

#### Related rates of change
If y is related to x, and x is related to time t, then the instantaneous rate of change of y with respect to time t utilises the chain rule: <br>
$\dfrac{dy}{dt} = \dfrac{dy}{dx} \times \dfrac{dx}{dt}$


<BR><BR>

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "cb6c36f7-b66d-4534-8ee9-23eef246b7ea" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_6f93a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_6f93a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_6f93a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_6f93a_row0_col0" class="data row0 col0" >$v = \dot x = \dfrac{dx}{dt}$</td>
    </tr>
    <tr>
      <td id="T_6f93a_row1_col0" class="data row1 col0" >$a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$</td>
    </tr>
    <tr>
      <td id="T_6f93a_row2_col0" class="data row2 col0" >$\dfrac{dN}{dt} = kn \text{ is satisfied by } N(t) = Ae^{kt}$</td>
    </tr>
    <tr>
      <td id="T_6f93a_row3_col0" class="data row3 col0" >$\dfrac{dN}{dt} = k(N-p) \text{ is satisfied by } N(t) = P + Ae^{kt}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_bae05 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bae05 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_bae05_row0_col0, #T_bae05_row1_col0 {
  background-color: rgba(0,0,0,0);
}
#T_bae05_row2_col0, #T_bae05_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_bae05">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_bae05_row0_col0" class="data row0 col0" >$v = \dot x = \dfrac{dx}{dt}$</td>
    </tr>
    <tr>
      <td id="T_bae05_row1_col0" class="data row1 col0" >$a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$</td>
    </tr>
    <tr>
      <td id="T_bae05_row2_col0" class="data row2 col0" >$\dfrac{dN}{dt} = kn \text{ is satisfied by } N(t) = Ae^{kt}$</td>
    </tr>
    <tr>
      <td id="T_bae05_row3_col0" class="data row3 col0" >$\dfrac{dN}{dt} = k(N-p) \text{ is satisfied by } N(t) = P + Ae^{kt}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Differential Calculus </span> 
<br>

### <span style="color:RGB(139,69,19)">  Notes </span>



#### Differentiation of trigonometric, exponential and logarithmic functions


#### Rules of differentiation



<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "197a632e-19a9-4bbb-9aa3-2cbc03cee4aa" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_c620a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c620a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_c620a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c620a_row0_col0" class="data row0 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_c620a_row1_col0" class="data row1 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_c620a_row2_col0" class="data row2 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_c620a_row3_col0" class="data row3 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_c620a_row4_col0" class="data row4 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_c620a_row5_col0" class="data row5 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_c620a_row6_col0" class="data row6 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_5bd96 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5bd96 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_5bd96_row0_col0, #T_5bd96_row1_col0, #T_5bd96_row2_col0, #T_5bd96_row3_col0, #T_5bd96_row4_col0, #T_5bd96_row5_col0, #T_5bd96_row6_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_5bd96">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5bd96_row0_col0" class="data row0 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_5bd96_row1_col0" class="data row1 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_5bd96_row2_col0" class="data row2 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_5bd96_row3_col0" class="data row3 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_5bd96_row4_col0" class="data row4 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_5bd96_row5_col0" class="data row5 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_5bd96_row6_col0" class="data row6 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
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
{{< tabs "6edbd862-cb4c-43c6-8058-37137233969d" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_9f17b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_9f17b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_9f17b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_9f17b_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_9f17b_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_9f17b_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_9f17b_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_9f17b_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_9f17b_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_9f17b_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_9f17b_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_9f17b_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_9f17b_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_8d04f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8d04f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_8d04f_row0_col0, #T_8d04f_row1_col0, #T_8d04f_row2_col0, #T_8d04f_row3_col0, #T_8d04f_row4_col0, #T_8d04f_row5_col0, #T_8d04f_row6_col0, #T_8d04f_row7_col0, #T_8d04f_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_8d04f_row9_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_8d04f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8d04f_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_8d04f_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_8d04f_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_8d04f_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_8d04f_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_8d04f_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_8d04f_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_8d04f_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_8d04f_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_8d04f_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
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
{{< tabs "b44d6473-32c8-4be9-8f97-c310de71bb75" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_4326e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4326e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_4326e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4326e_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_4326e_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_4326e_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_4326e_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_4326e_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_4326e_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_4326e_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_4326e_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_4326e_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_4326e_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_4326e_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_4326e_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_4326e_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_019e9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_019e9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_019e9_row0_col0, #T_019e9_row3_col0, #T_019e9_row4_col0, #T_019e9_row8_col0, #T_019e9_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_019e9_row1_col0, #T_019e9_row2_col0, #T_019e9_row5_col0, #T_019e9_row6_col0, #T_019e9_row7_col0, #T_019e9_row9_col0, #T_019e9_row10_col0, #T_019e9_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_019e9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_019e9_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_019e9_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_019e9_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_019e9_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_019e9_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_019e9_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_019e9_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_019e9_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_019e9_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_019e9_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_019e9_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_019e9_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_019e9_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}


<br>


###  <span style="color:RGB(139,69,19)"> Derivatives vs integrals  </span>
<br>
{{< tabs "1ff063f0-0056-4c50-a2c0-3648c7fae5f9" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_76c5a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_76c5a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_76c5a">
  <thead>
    <tr>
      <th id="T_76c5a_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_76c5a_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_76c5a_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_76c5a_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_76c5a_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_76c5a_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_76c5a_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_76c5a_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_76c5a_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_76c5a_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_76c5a_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_76c5a_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_76c5a_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_76c5a_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_76c5a_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_76c5a_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_76c5a_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_76c5a_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_76c5a_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_76c5a_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_76c5a_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_944b1 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_944b1 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_944b1_row0_col0, #T_944b1_row1_col1, #T_944b1_row2_col0, #T_944b1_row4_col0, #T_944b1_row5_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_944b1_row0_col1, #T_944b1_row1_col0, #T_944b1_row2_col1, #T_944b1_row3_col0, #T_944b1_row3_col1, #T_944b1_row4_col1, #T_944b1_row5_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_944b1">
  <thead>
    <tr>
      <th id="T_944b1_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_944b1_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_944b1_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_944b1_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_944b1_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_944b1_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_944b1_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_944b1_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_944b1_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_944b1_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_944b1_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_944b1_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_944b1_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_944b1_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_944b1_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_944b1_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_944b1_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_944b1_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_944b1_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_944b1_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_944b1_row5_col2" class="data row5 col2" ></td>
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
