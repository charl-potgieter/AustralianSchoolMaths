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
{{< tabs "11fb434e-cbd6-475a-aa9c-e72ccd643f2b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_3a64c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3a64c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_3a64c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_3a64c_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_3a64c_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_3a64c_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_fab84 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fab84 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_fab84_row0_col0, #T_fab84_row1_col0, #T_fab84_row2_col0, #T_fab84_row3_col0, #T_fab84_row4_col0, #T_fab84_row5_col0, #T_fab84_row6_col0, #T_fab84_row7_col0 {
  background-color: rgba(0,0,0,0);
}
#T_fab84_row8_col0, #T_fab84_row9_col0, #T_fab84_row10_col0, #T_fab84_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_fab84">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fab84_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_fab84_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_fab84_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
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

 -  The graphs are similar to those of $N(t) = P + Ae^{kt}$ with the excpetion of the different initial quantity

<br>

*Rate of change is directly proportional to the difference between the current amount of the quantity and a fixed quantity*
- That is... $\dfrac{dN}{dt} = k(N-p)$

- $N(t) = P + Ae^{kt}$ satisfies the above relationship (be able to prove)

-  Initial quantity  = P+A

- when $k<0$, then ${N \to P} \text { as } {t \to \infty} $

<br>

 <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/ME_C1_ExpGrowthProportionToNLessConstant.jpg" />

<br>

 <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/ME_C1_ExpDecayProportionToNLessConstant.jpg" />


<br>

#### Related rates of change
If y is related to x, and x is related to time t, then the instantaneous rate of change of y with respect to time t utilises the chain rule: <br>
$\dfrac{dy}{dt} = \dfrac{dy}{dx} \times \dfrac{dx}{dt}$


<BR><BR>

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "0f102c81-4f88-4634-8bfe-58302afaf13f" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_e1d97 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e1d97 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_e1d97">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e1d97_row0_col0" class="data row0 col0" >$v = \dot x = \dfrac{dx}{dt}$</td>
    </tr>
    <tr>
      <td id="T_e1d97_row1_col0" class="data row1 col0" >$a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$</td>
    </tr>
    <tr>
      <td id="T_e1d97_row2_col0" class="data row2 col0" >$\dfrac{dN}{dt} = kn \text{ is satisfied by } N(t) = Ae^{kt}$</td>
    </tr>
    <tr>
      <td id="T_e1d97_row3_col0" class="data row3 col0" >$\dfrac{dN}{dt} = k(N-p) \text{ is satisfied by } N(t) = P + Ae^{kt}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_ab2c0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ab2c0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_ab2c0_row0_col0, #T_ab2c0_row1_col0 {
  background-color: rgba(0,0,0,0);
}
#T_ab2c0_row2_col0, #T_ab2c0_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_ab2c0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ab2c0_row0_col0" class="data row0 col0" >$v = \dot x = \dfrac{dx}{dt}$</td>
    </tr>
    <tr>
      <td id="T_ab2c0_row1_col0" class="data row1 col0" >$a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$</td>
    </tr>
    <tr>
      <td id="T_ab2c0_row2_col0" class="data row2 col0" >$\dfrac{dN}{dt} = kn \text{ is satisfied by } N(t) = Ae^{kt}$</td>
    </tr>
    <tr>
      <td id="T_ab2c0_row3_col0" class="data row3 col0" >$\dfrac{dN}{dt} = k(N-p) \text{ is satisfied by } N(t) = P + Ae^{kt}$</td>
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

In particular note that $\tan x$ can be converted to $\dfrac{sin x}{cos x}$ and the quotient rule can then be applied.

Use log laws to simplify expressions before differentiating.

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "78e9a124-701a-4cf7-bc5a-484ec5232c28" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_158a9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_158a9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_158a9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_158a9_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_158a9_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_158a9_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_158a9_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_158a9_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_158a9_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_158a9_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_158a9_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_158a9_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_158a9_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_158a9_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_158a9_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_04d00 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_04d00 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_04d00_row0_col0, #T_04d00_row1_col0, #T_04d00_row2_col0, #T_04d00_row3_col0, #T_04d00_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_04d00_row5_col0, #T_04d00_row6_col0, #T_04d00_row7_col0, #T_04d00_row8_col0, #T_04d00_row9_col0, #T_04d00_row10_col0, #T_04d00_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_04d00">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_04d00_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_04d00_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_04d00_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_04d00_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_04d00_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_04d00_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_04d00_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_04d00_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_04d00_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_04d00_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_04d00_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_04d00_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_b6d53 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_b6d53 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_b6d53_row0_col0, #T_b6d53_row1_col0, #T_b6d53_row2_col0, #T_b6d53_row3_col0, #T_b6d53_row4_col0, #T_b6d53_row5_col0, #T_b6d53_row6_col0, #T_b6d53_row7_col0, #T_b6d53_row8_col0, #T_b6d53_row9_col0, #T_b6d53_row10_col0, #T_b6d53_row11_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_b6d53">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_b6d53_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_b6d53_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_b6d53_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_b6d53_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_b6d53_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_b6d53_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_b6d53_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_b6d53_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_b6d53_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_b6d53_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_b6d53_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_b6d53_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
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
{{< tabs "59267809-f935-4234-b697-26d29c3fdee3" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_97c3c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_97c3c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_97c3c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_97c3c_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_97c3c_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_97c3c_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row10_col0" class="data row10 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_97c3c_row11_col0" class="data row11 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_23f1d th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_23f1d td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_23f1d_row0_col0, #T_23f1d_row1_col0, #T_23f1d_row2_col0, #T_23f1d_row3_col0, #T_23f1d_row4_col0, #T_23f1d_row5_col0, #T_23f1d_row6_col0, #T_23f1d_row7_col0, #T_23f1d_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_23f1d_row9_col0, #T_23f1d_row10_col0, #T_23f1d_row11_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_23f1d">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_23f1d_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_23f1d_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_23f1d_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row10_col0" class="data row10 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_23f1d_row11_col0" class="data row11 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_e7944 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e7944 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_e7944_row0_col0, #T_e7944_row3_col0, #T_e7944_row4_col0, #T_e7944_row6_col0, #T_e7944_row7_col0, #T_e7944_row10_col0, #T_e7944_row11_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_e7944_row1_col0, #T_e7944_row2_col0, #T_e7944_row5_col0, #T_e7944_row8_col0, #T_e7944_row9_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_e7944">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e7944_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_e7944_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_e7944_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_e7944_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_e7944_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_e7944_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_e7944_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_e7944_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_e7944_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_e7944_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_e7944_row10_col0" class="data row10 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_e7944_row11_col0" class="data row11 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Calculus Skills </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>





### <span style="color:RGB(139,69,19)">  Notes </span>

#### Integration by substitution
This can be useful when integrals don't follow any of the other standard rules.<br>

With an equation  like $\frac{du}{dx}=3$, while $\frac{du}{dx}$ is not a true fraction, certain fraction-like operations do apply and therefore above can be rewritten as $du=3dx$

General approach:
- Identify a portion of the equation that needs to be integrated and set equal to u
- Differentiate above to obtain an equation in the format $\frac{du}{dx}$ = something
- multiply out to get du = something times dx
- attempt to substitute the x's and dx in the original equation with u's and du
- calculate the integral in terms of u
- for indefinite integrals replace the u's with expression in terms of x in the final step
- for definite integrals recalculate the lower and upper limits by substituting the original integral lower and upper limits into x in the formula for u as a function of x.  That way when the integral is calculated in terms of u, there is no need to rework back to x.
 


#### Derivatives of inverse functions
Derivatives of inverse functions can be calculated by swapping x and y variables, making the "new" y the subject of the equation and then calculating the derivative.  It is however sometimes difficult to change the subject of the equation, in which case the derivatives of inverse functions can be found using the below formula: <br>

  $\frac{dy}{dx} = \dfrac{1}{\frac{dx}{dy}} $

When using the above equation, simply swap the x and the y variables of the original function to obtain the inverse function, but keep x as the subject and then calculate $\frac{dx}{dy}$.  Sometimes question states to leave the answer in terms of y, as reworking back to x may be difficult.  (The inverse trig derivatives need to be reworked back to x though.)  If the derivative is in terms of y and asked to find the gradient at a certain x value, first calculate the y-value at this point and then substitute this into the derivative equation which is in terms of y.

#### Derivatives of inverse trigonometric functions
Be able to prove the derivatives of the inverse trigonometric functions (see formulas on Calculus formula page)

Note that the derivative and integrals of the inverse trigonometric functions can be presented in three forms:
Derivative of 
 - x

 - f(x)
 
 - $\frac{f(x)}{a}$, which results in a simplified chain rule equation

The formula sheet presents the derivative of f(x) for inverse sin, cos and tan, and an integral equation with an answer in the format of $\frac{f(x)}{a}$ for inverse sin and tan.  If a question requires a derivative of $\frac{f(x)}{a}$ style format one can easily work backward from the integral formula on the formula sheet to get the answer and vice versa for an integral in f(x) style format.  Note that no inverse cos integral is provided on the formula sheet.  See comments on the calculus formula summary which lays this out in an easier to understand layout.


It is recommended to view the inverse trigonometric derivatives and corresponding integrals on the Formula Summaries / Calculus page of this site which presents a more intuitive layout than the simple list of formulas below.
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "53546a23-4790-46dc-982e-de856c2a53a0" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_4bb1e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4bb1e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_4bb1e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4bb1e_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_4bb1e_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_4bb1e_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_4bb1e_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_4bb1e_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_4bb1e_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_4bb1e_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_4bb1e_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_4bb1e_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_4bb1e_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_4bb1e_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_4bb1e_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_4bb1e_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_4bb1e_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_4bb1e_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_ebaaf th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ebaaf td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_ebaaf_row0_col0, #T_ebaaf_row3_col0, #T_ebaaf_row4_col0, #T_ebaaf_row8_col0, #T_ebaaf_row11_col0, #T_ebaaf_row13_col0, #T_ebaaf_row14_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_ebaaf_row1_col0, #T_ebaaf_row2_col0, #T_ebaaf_row5_col0, #T_ebaaf_row6_col0, #T_ebaaf_row7_col0, #T_ebaaf_row9_col0, #T_ebaaf_row10_col0, #T_ebaaf_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_ebaaf">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ebaaf_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ebaaf_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_ebaaf_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_ebaaf_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_ebaaf_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ebaaf_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_ebaaf_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ebaaf_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_ebaaf_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_ebaaf_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_ebaaf_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_ebaaf_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_ebaaf_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_ebaaf_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_ebaaf_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_44936 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_44936 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_44936_row0_col0, #T_44936_row1_col0, #T_44936_row2_col0, #T_44936_row3_col0, #T_44936_row4_col0, #T_44936_row5_col0, #T_44936_row6_col0, #T_44936_row7_col0, #T_44936_row8_col0, #T_44936_row9_col0, #T_44936_row10_col0, #T_44936_row11_col0, #T_44936_row13_col0, #T_44936_row14_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_44936_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_44936">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_44936_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_44936_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_44936_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_44936_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_44936_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_44936_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_44936_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_44936_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_44936_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_44936_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_44936_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_44936_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_44936_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_44936_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_44936_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}


<br>


###  <span style="color:RGB(139,69,19)"> Derivatives vs integrals  </span>
<br>
{{< tabs "e98e27da-1a03-400b-85ee-4928427ccd4c" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_9897f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_9897f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_9897f">
  <thead>
    <tr>
      <th id="T_9897f_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_9897f_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_9897f_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_9897f_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_9897f_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_9897f_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_9897f_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_9897f_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_9897f_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_9897f_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_9897f_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_9897f_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_9897f_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_9897f_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_9897f_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_9897f_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_9897f_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_9897f_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_9897f_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_9897f_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_9897f_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_c81bb th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c81bb td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c81bb_row0_col0, #T_c81bb_row1_col1, #T_c81bb_row2_col0, #T_c81bb_row4_col0, #T_c81bb_row5_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_c81bb_row0_col1, #T_c81bb_row1_col0, #T_c81bb_row2_col1, #T_c81bb_row3_col0, #T_c81bb_row3_col1, #T_c81bb_row4_col1, #T_c81bb_row5_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_c81bb">
  <thead>
    <tr>
      <th id="T_c81bb_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_c81bb_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_c81bb_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_c81bb_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_c81bb_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_c81bb_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_c81bb_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_c81bb_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_c81bb_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_c81bb_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_c81bb_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_c81bb_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_c81bb_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_c81bb_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_c81bb_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_c81bb_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_c81bb_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_c81bb_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_c81bb_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_c81bb_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_c81bb_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_725ee th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_725ee td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_725ee_row0_col0, #T_725ee_row0_col1, #T_725ee_row1_col0, #T_725ee_row1_col1, #T_725ee_row2_col0, #T_725ee_row2_col1, #T_725ee_row3_col0, #T_725ee_row3_col1, #T_725ee_row4_col0, #T_725ee_row4_col1, #T_725ee_row5_col0, #T_725ee_row5_col1 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_725ee">
  <thead>
    <tr>
      <th id="T_725ee_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_725ee_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_725ee_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_725ee_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_725ee_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_725ee_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_725ee_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_725ee_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_725ee_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_725ee_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_725ee_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_725ee_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_725ee_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_725ee_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_725ee_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_725ee_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_725ee_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_725ee_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_725ee_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_725ee_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_725ee_row5_col2" class="data row5 col2" ></td>
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
