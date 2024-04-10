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
{{< tabs "4a4f794f-ef25-4e47-bb15-a96e6f31f329" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_96112 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_96112 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_96112">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_96112_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_96112_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_96112_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_c1360 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c1360 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c1360_row0_col0, #T_c1360_row1_col0, #T_c1360_row2_col0, #T_c1360_row3_col0, #T_c1360_row4_col0, #T_c1360_row5_col0, #T_c1360_row6_col0, #T_c1360_row7_col0 {
  background-color: rgba(0,0,0,0);
}
#T_c1360_row8_col0, #T_c1360_row9_col0, #T_c1360_row10_col0, #T_c1360_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_c1360">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c1360_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_c1360_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_c1360_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
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
{{< tabs "78b4c3ab-44f2-4558-ad7f-be0baebc1baa" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_48b63 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_48b63 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_48b63">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_48b63_row0_col0" class="data row0 col0" >$v = \dot x = \dfrac{dx}{dt}$</td>
    </tr>
    <tr>
      <td id="T_48b63_row1_col0" class="data row1 col0" >$a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$</td>
    </tr>
    <tr>
      <td id="T_48b63_row2_col0" class="data row2 col0" >$\dfrac{dN}{dt} = kn \text{ is satisfied by } N(t) = Ae^{kt}$</td>
    </tr>
    <tr>
      <td id="T_48b63_row3_col0" class="data row3 col0" >$\dfrac{dN}{dt} = k(N-p) \text{ is satisfied by } N(t) = P + Ae^{kt}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_aa0fe th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_aa0fe td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_aa0fe_row0_col0, #T_aa0fe_row1_col0 {
  background-color: rgba(0,0,0,0);
}
#T_aa0fe_row2_col0, #T_aa0fe_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_aa0fe">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_aa0fe_row0_col0" class="data row0 col0" >$v = \dot x = \dfrac{dx}{dt}$</td>
    </tr>
    <tr>
      <td id="T_aa0fe_row1_col0" class="data row1 col0" >$a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$</td>
    </tr>
    <tr>
      <td id="T_aa0fe_row2_col0" class="data row2 col0" >$\dfrac{dN}{dt} = kn \text{ is satisfied by } N(t) = Ae^{kt}$</td>
    </tr>
    <tr>
      <td id="T_aa0fe_row3_col0" class="data row3 col0" >$\dfrac{dN}{dt} = k(N-p) \text{ is satisfied by } N(t) = P + Ae^{kt}$</td>
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

#### Rules of differentiation

Apply product, quotient and chain rules to differentiate the "simpler" versions of the function.

In particular note that $\tan x$ can be converted to $\dfrac{sin x}{cos x}$ and the quotient rule can then be applied.

Use log laws to simplify expressions before differentiating.

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "a10aeaca-5754-4d85-8fdc-c2e5fd9595da" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_809ee th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_809ee td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_809ee">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_809ee_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_809ee_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_809ee_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_809ee_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_809ee_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_809ee_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_809ee_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_809ee_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_809ee_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_809ee_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_809ee_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_809ee_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_19b3e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_19b3e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_19b3e_row0_col0, #T_19b3e_row1_col0, #T_19b3e_row2_col0, #T_19b3e_row3_col0, #T_19b3e_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_19b3e_row5_col0, #T_19b3e_row6_col0, #T_19b3e_row7_col0, #T_19b3e_row8_col0, #T_19b3e_row9_col0, #T_19b3e_row10_col0, #T_19b3e_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_19b3e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_19b3e_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_19b3e_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_19b3e_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_19b3e_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_19b3e_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_19b3e_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_19b3e_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_19b3e_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_19b3e_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_19b3e_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_19b3e_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_19b3e_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_bb4c0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bb4c0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_bb4c0_row0_col0, #T_bb4c0_row1_col0, #T_bb4c0_row2_col0, #T_bb4c0_row3_col0, #T_bb4c0_row4_col0, #T_bb4c0_row5_col0, #T_bb4c0_row6_col0, #T_bb4c0_row7_col0, #T_bb4c0_row8_col0, #T_bb4c0_row9_col0, #T_bb4c0_row10_col0, #T_bb4c0_row11_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_bb4c0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_bb4c0_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_bb4c0_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_bb4c0_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_bb4c0_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_bb4c0_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_bb4c0_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_bb4c0_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_bb4c0_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_bb4c0_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_bb4c0_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_bb4c0_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_bb4c0_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
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
{{< tabs "5bfb44a5-2fce-4316-a82c-ba92b3e051b1" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_06b04 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_06b04 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_06b04">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_06b04_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_06b04_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_06b04_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_06b04_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_06b04_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_06b04_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_06b04_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_06b04_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_06b04_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_06b04_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_79d24 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_79d24 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_79d24_row0_col0, #T_79d24_row1_col0, #T_79d24_row2_col0, #T_79d24_row3_col0, #T_79d24_row4_col0, #T_79d24_row5_col0, #T_79d24_row6_col0, #T_79d24_row7_col0, #T_79d24_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_79d24_row9_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_79d24">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_79d24_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_79d24_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_79d24_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_79d24_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_79d24_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_79d24_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_79d24_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_79d24_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_79d24_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_79d24_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
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
{{< tabs "e44f7341-4b44-4a98-b1a3-356f6c4fffc3" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_02cbd th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_02cbd td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_02cbd">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_02cbd_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_02cbd_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_02cbd_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_02cbd_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_02cbd_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_02cbd_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_02cbd_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_02cbd_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_02cbd_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_02cbd_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_02cbd_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_02cbd_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_02cbd_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_fb099 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fb099 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_fb099_row0_col0, #T_fb099_row3_col0, #T_fb099_row4_col0, #T_fb099_row8_col0, #T_fb099_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_fb099_row1_col0, #T_fb099_row2_col0, #T_fb099_row5_col0, #T_fb099_row6_col0, #T_fb099_row7_col0, #T_fb099_row9_col0, #T_fb099_row10_col0, #T_fb099_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_fb099">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fb099_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_fb099_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_fb099_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_fb099_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_fb099_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_fb099_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_fb099_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_fb099_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_fb099_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_fb099_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_fb099_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_fb099_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_fb099_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}


<br>


###  <span style="color:RGB(139,69,19)"> Derivatives vs integrals  </span>
<br>
{{< tabs "07bc17bc-4cc5-47dd-b485-cf7d135ef6d5" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_54ca3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_54ca3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_54ca3">
  <thead>
    <tr>
      <th id="T_54ca3_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_54ca3_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_54ca3_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_54ca3_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_54ca3_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_54ca3_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_54ca3_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_54ca3_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_54ca3_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_54ca3_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_54ca3_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_54ca3_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_54ca3_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_54ca3_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_54ca3_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_54ca3_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_54ca3_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_54ca3_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_54ca3_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_54ca3_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_54ca3_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_5f258 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5f258 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_5f258_row0_col0, #T_5f258_row1_col1, #T_5f258_row2_col0, #T_5f258_row4_col0, #T_5f258_row5_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_5f258_row0_col1, #T_5f258_row1_col0, #T_5f258_row2_col1, #T_5f258_row3_col0, #T_5f258_row3_col1, #T_5f258_row4_col1, #T_5f258_row5_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_5f258">
  <thead>
    <tr>
      <th id="T_5f258_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_5f258_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_5f258_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_5f258_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_5f258_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_5f258_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_5f258_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_5f258_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_5f258_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_5f258_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_5f258_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_5f258_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_5f258_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_5f258_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_5f258_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_5f258_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_5f258_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_5f258_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_5f258_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_5f258_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_5f258_row5_col2" class="data row5 col2" ></td>
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
