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
{{< tabs "d0aa438e-3de4-414f-867d-d572e68f557b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_d2543 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d2543 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_d2543">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d2543_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_d2543_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_d2543_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_ec380 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ec380 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_ec380_row0_col0, #T_ec380_row1_col0, #T_ec380_row2_col0, #T_ec380_row3_col0, #T_ec380_row4_col0, #T_ec380_row5_col0, #T_ec380_row6_col0, #T_ec380_row7_col0 {
  background-color: rgba(0,0,0,0);
}
#T_ec380_row8_col0, #T_ec380_row9_col0, #T_ec380_row10_col0, #T_ec380_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_ec380">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ec380_row0_col0" class="data row0 col0" >$\text{gradient} = m = \dfrac{rise}{run} = \dfrac{y_2-y_1}{x_2-x_1}$</td>
    </tr>
    <tr>
      <td id="T_ec380_row1_col0" class="data row1 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row2_col0" class="data row2 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row3_col0" class="data row3 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row4_col0" class="data row4 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row5_col0" class="data row5 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row6_col0" class="data row6 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row7_col0" class="data row7 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row8_col0" class="data row8 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row9_col0" class="data row9 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row10_col0" class="data row10 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_ec380_row11_col0" class="data row11 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx} \text { (the chain rule)}$ </td>
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
{{< tabs "4ffb00a4-3348-4936-94c2-cba29c3794c8" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_4a0a0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4a0a0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_4a0a0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4a0a0_row0_col0" class="data row0 col0" >$v = \dot x = \dfrac{dx}{dt}$</td>
    </tr>
    <tr>
      <td id="T_4a0a0_row1_col0" class="data row1 col0" >$a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$</td>
    </tr>
    <tr>
      <td id="T_4a0a0_row2_col0" class="data row2 col0" >$\dfrac{dN}{dt} = kn \text{ is satisfied by } N(t) = Ae^{kt}$</td>
    </tr>
    <tr>
      <td id="T_4a0a0_row3_col0" class="data row3 col0" >$\dfrac{dN}{dt} = k(N-p) \text{ is satisfied by } N(t) = P + Ae^{kt}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_245a3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_245a3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_245a3_row0_col0, #T_245a3_row1_col0 {
  background-color: rgba(0,0,0,0);
}
#T_245a3_row2_col0, #T_245a3_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_245a3">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_245a3_row0_col0" class="data row0 col0" >$v = \dot x = \dfrac{dx}{dt}$</td>
    </tr>
    <tr>
      <td id="T_245a3_row1_col0" class="data row1 col0" >$a = \ddot x = \dfrac{dv}{dt} = \dfrac{d^{2}x}{dt^2}$</td>
    </tr>
    <tr>
      <td id="T_245a3_row2_col0" class="data row2 col0" >$\dfrac{dN}{dt} = kn \text{ is satisfied by } N(t) = Ae^{kt}$</td>
    </tr>
    <tr>
      <td id="T_245a3_row3_col0" class="data row3 col0" >$\dfrac{dN}{dt} = k(N-p) \text{ is satisfied by } N(t) = P + Ae^{kt}$</td>
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
{{< tabs "83a6eaab-8049-41c1-a517-a6ebac24be84" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_77f26 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_77f26 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_77f26">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_77f26_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_77f26_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_77f26_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_77f26_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_77f26_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_77f26_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_77f26_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_77f26_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_77f26_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_77f26_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_77f26_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_77f26_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_3f2b2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3f2b2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_3f2b2_row0_col0, #T_3f2b2_row1_col0, #T_3f2b2_row2_col0, #T_3f2b2_row3_col0, #T_3f2b2_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_3f2b2_row5_col0, #T_3f2b2_row6_col0, #T_3f2b2_row7_col0, #T_3f2b2_row8_col0, #T_3f2b2_row9_col0, #T_3f2b2_row10_col0, #T_3f2b2_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_3f2b2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_3f2b2_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_3f2b2_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_3f2b2_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_3f2b2_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_3f2b2_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_3f2b2_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_3f2b2_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_3f2b2_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_3f2b2_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_3f2b2_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_3f2b2_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_3f2b2_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_f3bf2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f3bf2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_f3bf2_row0_col0, #T_f3bf2_row1_col0, #T_f3bf2_row2_col0, #T_f3bf2_row3_col0, #T_f3bf2_row4_col0, #T_f3bf2_row5_col0, #T_f3bf2_row6_col0, #T_f3bf2_row7_col0, #T_f3bf2_row8_col0, #T_f3bf2_row9_col0, #T_f3bf2_row10_col0, #T_f3bf2_row11_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_f3bf2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f3bf2_row0_col0" class="data row0 col0" >$y=\sin (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \cos (x)$</td>
    </tr>
    <tr>
      <td id="T_f3bf2_row1_col0" class="data row1 col0" >$y=\cos (x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = -\sin (x)$</td>
    </tr>
    <tr>
      <td id="T_f3bf2_row2_col0" class="data row2 col0" >$y=a^x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = (\ln a)a^x$</td>
    </tr>
    <tr>
      <td id="T_f3bf2_row3_col0" class="data row3 col0" >$y=\ln x \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x}$</td>
    </tr>
    <tr>
      <td id="T_f3bf2_row4_col0" class="data row4 col0" >$y=log_a {x} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = \dfrac{1}{x \ln a}$</td>
    </tr>
    <tr>
      <td id="T_f3bf2_row5_col0" class="data row5 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bf2_row6_col0" class="data row6 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bf2_row7_col0" class="data row7 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bf2_row8_col0" class="data row8 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bf2_row9_col0" class="data row9 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bf2_row10_col0" class="data row10 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_f3bf2_row11_col0" class="data row11 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
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
{{< tabs "748fdb79-78eb-4798-a497-7d30c6e3f9e1" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_f6fc4 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f6fc4 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_f6fc4">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f6fc4_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_f6fc4_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_e312a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e312a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_e312a_row0_col0, #T_e312a_row1_col0, #T_e312a_row2_col0, #T_e312a_row3_col0, #T_e312a_row4_col0, #T_e312a_row5_col0, #T_e312a_row6_col0, #T_e312a_row7_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_e312a_row8_col0, #T_e312a_row9_col0, #T_e312a_row10_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_e312a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e312a_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_e312a_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_e312a_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_e312a_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_e312a_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_e312a_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_e312a_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_e312a_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_e312a_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_e312a_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_e312a_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_32da4 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_32da4 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_32da4_row0_col0, #T_32da4_row2_col0, #T_32da4_row3_col0, #T_32da4_row5_col0, #T_32da4_row6_col0, #T_32da4_row9_col0, #T_32da4_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_32da4_row1_col0, #T_32da4_row4_col0, #T_32da4_row7_col0, #T_32da4_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_32da4">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_32da4_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_32da4_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_32da4_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_32da4_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_32da4_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_32da4_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_32da4_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_32da4_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_32da4_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_32da4_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_32da4_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
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

With an equation  like $\frac{du}{dx}=3$, while $\frac{du}{dx}$ is not a true fraction, certain fraction-like operations do apply and therefore above can be rewritten as $dx = \frac{1}{3}du$

General approach:
- Identify a portion of the equation that needs to be integrated and set equal to u
- Differentiate above to obtain an equation in the format $\frac{du}{dx}$ = something
- Solve for dx (make dx subject of equation) so that the dx in the original integral can be replaced with an expression in terms of du.
- In some cases it may be convenvient to substitute with x as the subject of the equation rather than u, for example $x = u^2-1$, in this case calculate $\frac{dx}{du}$ rather than $\frac{du}{dx}$
- substitute the x's and dx in the original equation with u's and du
- calculate the integral in terms of u
- for indefinite integrals replace the u's with expression in terms of x in the final step
- for definite integrals recalculate the lower and upper limits by substituting the original integral lower and upper limits into x in the formula for u as a function of x.  That way when the integral is calculated in terms of u, there is no need to rework back to x.
 - My undesrtanding is that HSC answers follow a simplified approach for convenience with relation to square roots arising from integration by susbstitution.  For example if substituting with  $x=u^2$, then u is simply taken as $\sqrt{x}$, rather than $\pm \sqrt{x}$

 

#### Integrals in the form $\sin^2nx$ and $\cos^2ns$
Prove and use the below 2 identities in order to solve integrals in the form of $\sin^2nx$ and $\cos^2ns$:
 
 - $\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$
 
 - $\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$
 




#### Derivatives of inverse functions
Derivatives of inverse functions can be calculated by swapping x and y variables, making the "new" y the subject of the equation and then calculating the derivative.  It is however sometimes difficult to change the subject of the equation, in which case the derivatives of inverse functions can be found using the below formula: <br>

  $\frac{dy}{dx} = \dfrac{1}{\frac{dx}{dy}} $

When using the above equation, simply swap the x and the y variables of the original function to obtain the inverse function, but keep x as the subject and then calculate $\frac{dx}{dy}$.  Sometimes question states to leave the answer in terms of y, as reworking back to x may be difficult.  (The inverse trig derivatives need to be reworked back to x though.)  If the derivative is in terms of y and asked to find the gradient at a certain x value, first calculate the y-value at this point and then substitute this into the derivative equation which is in terms of y.

#### Derivatives of inverse trigonometric functions
Be able to prove the derivatives of the inverse trigonometric functions (See derivatives vs integrals summary beloe)

Note that the derivative and integrals of the inverse trigonometric functions can be presented in three forms:
Derivative of 
 - x

 - f(x)
 
 - $\frac{f(x)}{a}$, which results in a simplified chain rule equation

The formula sheet presents the derivative of f(x) for inverse sin, cos and tan, and an integral equations with an answer in the format of $\frac{f(x)}{a}$ for inverse sin and tan.  If a question requires a derivative of $\frac{f(x)}{a}$ style format one can easily work backward from the integral formula on the formula sheet to get the answer and vice versa for an integral in f(x) style format.  Note that no inverse cos integral is provided on the formula sheet.  See comments on the dervivatives vs integrals formula summary which lays this out in an easier to understand layout.


It is recommended to view the inverse trigonometric derivatives and corresponding integrals on the derivatives vs integrals summary below which presents a more intuitive layout than the simple list of formulas.
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "d5cb52d3-78b8-4272-a00e-2e18e85fc883" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_89db3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_89db3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_89db3">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_89db3_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_89db3_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_89db3_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_89db3_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_89db3_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_89db3_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_89db3_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_89db3_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_89db3_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_89db3_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_89db3_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_89db3_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_89db3_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_89db3_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_89db3_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_ac262 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ac262 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_ac262_row0_col0, #T_ac262_row3_col0, #T_ac262_row4_col0, #T_ac262_row8_col0, #T_ac262_row11_col0, #T_ac262_row13_col0, #T_ac262_row14_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_ac262_row1_col0, #T_ac262_row2_col0, #T_ac262_row5_col0, #T_ac262_row6_col0, #T_ac262_row7_col0, #T_ac262_row9_col0, #T_ac262_row10_col0, #T_ac262_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_ac262">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ac262_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ac262_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_ac262_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_ac262_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_ac262_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ac262_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_ac262_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ac262_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_ac262_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_ac262_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_ac262_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_ac262_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_ac262_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_ac262_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_ac262_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_0181f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_0181f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_0181f_row0_col0, #T_0181f_row1_col0, #T_0181f_row2_col0, #T_0181f_row3_col0, #T_0181f_row4_col0, #T_0181f_row5_col0, #T_0181f_row6_col0, #T_0181f_row7_col0, #T_0181f_row8_col0, #T_0181f_row9_col0, #T_0181f_row10_col0, #T_0181f_row11_col0, #T_0181f_row13_col0, #T_0181f_row14_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_0181f_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_0181f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_0181f_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_0181f_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_0181f_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_0181f_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_0181f_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_0181f_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_0181f_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_0181f_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_0181f_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_0181f_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_0181f_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_0181f_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_0181f_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_0181f_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_0181f_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}


<br>


###  <span style="color:RGB(139,69,19)"> Derivatives vs integrals  </span>
<br>
{{< tabs "8895e233-e51e-4cca-bfe1-48fc8da836f5" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_49e15 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_49e15 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_49e15">
  <thead>
    <tr>
      <th id="T_49e15_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_49e15_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_49e15_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_49e15_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_49e15_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_49e15_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_49e15_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_49e15_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_49e15_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_49e15_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_49e15_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_49e15_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_49e15_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_49e15_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_49e15_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_49e15_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_49e15_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_49e15_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_49e15_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_49e15_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_49e15_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_23700 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_23700 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_23700_row0_col0, #T_23700_row1_col1, #T_23700_row2_col0, #T_23700_row4_col0, #T_23700_row5_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_23700_row0_col1, #T_23700_row1_col0, #T_23700_row2_col1, #T_23700_row3_col0, #T_23700_row3_col1, #T_23700_row4_col1, #T_23700_row5_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_23700">
  <thead>
    <tr>
      <th id="T_23700_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_23700_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_23700_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_23700_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_23700_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_23700_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_23700_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_23700_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_23700_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_23700_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_23700_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_23700_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_23700_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_23700_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_23700_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_23700_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_23700_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_23700_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_23700_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_23700_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_23700_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_60878 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_60878 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_60878_row0_col0, #T_60878_row0_col1, #T_60878_row1_col0, #T_60878_row1_col1, #T_60878_row2_col0, #T_60878_row2_col1, #T_60878_row3_col0, #T_60878_row3_col1, #T_60878_row4_col0, #T_60878_row4_col1, #T_60878_row5_col0, #T_60878_row5_col1 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_60878">
  <thead>
    <tr>
      <th id="T_60878_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_60878_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_60878_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_60878_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_60878_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_60878_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_60878_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_60878_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_60878_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_60878_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_60878_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_60878_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_60878_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_60878_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_60878_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_60878_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_60878_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_60878_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_60878_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_60878_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_60878_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Applications of Calculus </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - Intergrand
 - solid of revolution
 - differential equation
 - direction field or slope field
 - first-order differential equation
 - logistic equation


### <span style="color:RGB(139,69,19)">  Notes </span>

#### Further area and volumes of solids of revolution
 
Volumes formed by rotation about the x-axis = $V=\pi \int_a^b y^2 dx$
 - The volume calculated is between the curves and point a and b on the x-axis, as the curve is rotated around the x-axis


Volumes formed by rotation about the y-axis = $V=\pi \int_a^b x^2 dy$
- The volume calculated is between the curves and point a and b on the y-axis, as the curve is rotated around the y-axis
 - If a question provides 2 points on the x-axis, the a and b values on the y-axis need to be calculated by using the original function formula.

 <span style="color:RGB(255,0,0)">  Can above formulas be used directly in questions or do they need to be derived.  They do not appear on the formula sheet or in the syllabus  </span>

 Remember to specify $\text{units}^3$ when providing a volume answer if no other specific measure e.g. cm is provided in the question.


 #### Differential equations

 Be able to sketch direction fields / slope fields

 **Solving differential equations in the form $\frac{dy}{dx}=f(x)$**
 - The solution is an equation on the format of y=f(x)
 
 - This involves finding the integral (anti-derivative)

<br>
 
 **Solving differential equations in the form $\frac{dy}{dx}=g(y)$**
 - Note how the derivative "denominator" is x but function g is defined in terms of y.

 - This equation can be interpreted as "the gradient of y=f(x) is a function of it's y-value, that is the gradient can be determined if a y-value is provided"

 - The same as above, these problems involve finding a solution equation on the format of y=f(x)

 - Need to use the fact that $\frac{dy}{dx} = \dfrac{1}{\frac{dx}{dy}}$, that is invert g(y) and calculate $\frac{dx}{dy}$ which will provide an equation in the format x=f(y)

 - As a final step make y the subject of the above equation.

 - Be on on the lookout for derivative "denominators" that don't match the variable in the equation.


<br>

 **Solving differential equations in the form $\frac{dy}{dx}=f(x)g(y)$**

 - This equation can be interpreted as "the gradient of y=f(x) is a function of both it's x and y-value"

 - These equations can sometimes be solved by the separation of variables which places the y's on the left and x's on the right, that is: $\dfrac{1}{g(y)}dy = f(x)dx$

- Both sides can then be integrated

- Not all differential equations are separable.

<br>

**Exponential Growth and Decay**

 - Exponential growth and decay equations covered in Year 11, ext 1 are first-order linear differential equations, effectively in the format $\frac{dy}{dx}=g(y)$



**Logistic Equation**

This is a more realistic model than the exponential growth and decay which restricts the population to a maximum level.

Population is a function of time, that is P(t) and $\frac{dP}{dt}$ represents the instantaneous rate of change of the population at a specific time

Option 1: $\frac{dP}{dt} = kP(N-P)$ <br><br>
Option 2: $\frac{dP}{dt} = kP(1-\frac{P}{N})$, where 
 - t is time
 - k is the growth rate
 - P is population
 - N is the limiting condition or carrying capacity (defined to be the maximum population of that organism that the environment can sustain indefinitely)

Note that the first part of above equations, $\frac{dP}{dt} = kP$, is the simple expononential growth and decay equation (although the later tends to use the symbol N instead of P).  In both options above kP is then multiplied by a factor which results in the rate of change ceasing once a limit  is reached.


<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "17a6b74a-a9a8-4215-b0ff-2efd0bd9d6b9" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_ebeb2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ebeb2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_ebeb2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ebeb2_row0_col0" class="data row0 col0" >Volumes formed by rotation about the x-axis = $V=\pi \int_a^b y^2 dx$</td>
    </tr>
    <tr>
      <td id="T_ebeb2_row1_col0" class="data row1 col0" >Volumes formed by rotation about the y-axis = $V=\pi \int_a^b x^2 dy$</td>
    </tr>
    <tr>
      <td id="T_ebeb2_row2_col0" class="data row2 col0" >Logistic equation option 1: $\frac{dP}{dt} = kP(N-P)$ <br><br></td>
    </tr>
    <tr>
      <td id="T_ebeb2_row3_col0" class="data row3 col0" >Logistic equation option 2:$\frac{dP}{dt} = kP(1-\frac{P}{N})$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_bc06a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bc06a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_bc06a_row0_col0, #T_bc06a_row1_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_bc06a_row2_col0, #T_bc06a_row3_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_bc06a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_bc06a_row0_col0" class="data row0 col0" >Volumes formed by rotation about the x-axis = $V=\pi \int_a^b y^2 dx$</td>
    </tr>
    <tr>
      <td id="T_bc06a_row1_col0" class="data row1 col0" >Volumes formed by rotation about the y-axis = $V=\pi \int_a^b x^2 dy$</td>
    </tr>
    <tr>
      <td id="T_bc06a_row2_col0" class="data row2 col0" >Logistic equation option 1: $\frac{dP}{dt} = kP(N-P)$ <br><br></td>
    </tr>
    <tr>
      <td id="T_bc06a_row3_col0" class="data row3 col0" >Logistic equation option 2:$\frac{dP}{dt} = kP(1-\frac{P}{N})$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Integration </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>





### <span style="color:RGB(139,69,19)">  Notes </span>

#### Integration by substitution

This is an extension of this topic as covered in Year 12 Ext 1.


Hints:
 - When substituting with say $u=\sqrt{x}$ it is not necessary to replace every single $\sqrt{x}$ with u.  One of the cases can be left as $\sqrt{x}$ to cross cancel with value in the "derivative" portion of the equation, for exmple where $dx = 5 \sqrt{x}$  
 
 - Before jumping into substitution (or another integation method) consider any other simplifications that can be made to the expression requiring integration for example
    - factorising and simplifing fractions, e.g. via difference of squares
    - trig identities e.g. $\sin^2 nx = \frac{1}{2}(1-\cos 2nx)$ and $\cos^2 nx = \frac{1}{2}(1+\cos 2nx)$

 - When using the t-formula subsitutions $t = \tan \frac{x}{2}$ as per patterns below it is worthwhile remembering that when calculating dx it needs to equal $\dfrac{2dt}{1+t^2}$



Examples of substition "patterns" are included in the table below:

 
|Integral                                       | Substitution                                      | <div style="width:300px">Comment</div>    |
| --------                                      | -------                                           |---------                                  |
| $ \int f'(x)f(x)^n dx $                       | $u= f(x)$                                         |                                           |
| $ \int \dfrac{f'(x)}{f(x)^n} dx $             | $u= f(x)$                                         | Look for potential pattern of a function and its derivative.  n may be a fraction, that is f(x) may be inside a root     |
| $\int \dfrac{1}{a \cos x + b \sin x} dx$      | $t = \tan \frac{x}{2}$                            | $\frac{dt}{dx}$ is a function of sec but can be restated in terms of tan and then t using the trig Pythagorean identities yielding $dx=\frac{2dt}{1+t^2}$|
| $\int \dfrac{1}{a \cos x + b} dx$             | $t = \tan \frac{x}{2}$                            |                                           |
| $\int \dfrac{1}{a + b \sin x} dx$             | $t = \tan \frac{x}{2}$                            |                                           |
| $ \int \dfrac{1}{\sqrt{a^2+x^2}} dx $         | $x=a \tan \theta$                                 | Note how x is the subject of the substition here, as well as in the below few cases.  Be careful when calculating bounds of definite integrals.                                          |
| $ \int \dfrac{1}{\sqrt{a^2-x^2}} dx $         | $x=a \sin \theta \text{ or } x=a \cos \theta$     |                                           |
| $ \int \dfrac{x}{\sqrt{x+a}} dx $             | $x= u^2 -a$                                       | This enables removing the square root     |


<br>

#### Integration of rational functions involving a quadratic denominator

 Rational functions are functions where both the numerator and denominator are polynomials.
 
 Possible approaches:
  - Dont overlook simple options such as factorising and simplifying fractions that may remove the quadratic denominator.

  - If the integrand can be restated as $\dfrac{1}{(x+a)^2}$ the result of the integral calculation is simply $- \dfrac{1}{x+a}$
  
 - If the integrand can be transformed into one of the below forms, for examply by completing the square, the inverse sin and inverse tan integration rules can be applied respectively:
   - $\dfrac{f'(x)}{\sqrt{a^2-[f(x)]^2}}$
   
   
   - $\dfrac{f'(x)}{a^2+[f(x)]^2}$

 - Look for integrands in the form of $\dfrac{f'(x)}{f{x}}$ that when integrated yield $ln|f(x)| + c$

 - if the numerator consists of 2 terms, the fraction may be able to be split into 2 fractions which may match one of the patterns above.

 - As an extension of above step, sometimes additional values can be added to and then subtracted from the numerator to enable the single fraction to be split into two that intergtate more easily, for exmple $\dfrac {x^2}{x^2+1} = \dfrac{x^2+1-1}{x^2+1} = 1 - \dfrac{1}{x^2+1}$


 


<br>

#### Integration using partial fractions

The degree of a polynomial expression in x is the highest power of x appearing in the expression. An algebraic fraction where the degree of the numerator is less than the degree of the denominator is called a proper fraction (and vice versa for improper fractions)

A proper fraction can be decomposed into simpler partial fractions which are easier to integrate.

Ensure that denominator is factorised as far as possible before applying the below:

**Linear factors in the denominator with no repetition** <br>
$\dfrac{k}{(a_1x+b_1)(a_2x+b_2)...(a_nx+b_n)} = \dfrac{A_1}{a_1x+b_1} + \dfrac{A_2}{a_2 x+b_2}+...\dfrac{A_n}{a_n x+b_n} $

<br>

**Linear factors in the denominator with repetition** <br>
$\dfrac{k}{(ax+b)^n} = \dfrac{A_1}{ax+b} + \dfrac{A_2}{(ax+b)^2} +...+\dfrac{A_n}{(ax+b)^n}  $

<br>

**Irreducible quadratic factors in the denominator with no repetition** <br>
$\dfrac{kx +l}{(a_1x^2+b_1x+c_1)(a_2x^2+b_2 x + c_2)...(a_n x^2+b_n x +c_n)} = \dfrac{A_1x + B_1}{a_1x^2+b_1x+c_1} + \dfrac{A_2x+B_2}{a_2x^2+b_2 x + c_2}+...\dfrac{A_n x + B_n}{a_n x^2+b_n x +c_n} $

<br>

**Repeated irreducible quadratic factors in the denominator with repetition** <br>
$\dfrac{kx + l}{(ax^2+bx + c)^n} = \dfrac{A_1x + B_1}{ax^2+bx+c} + \dfrac{A_2x+B_2}{(ax^2+bx+c)^2} +...+\dfrac{A_nx+B_n}{(ax^2+bx+c)^n}  $

<br>

**Combination of above** <br>

For example the denominator may contain a combination or linear, quadratic, unique and repeating factors.

<br>

**Solving for the numerators:**

 - Multiply the equation by the denominator of the LHS to get rid of all fractions.

 - Option 1 Quicker method but not always possible
    - After first step above, assume equation is as follows 6=A(x+1)(x+2)+B(X-1)(x+2)
    - Equation needs to hold for all values of x
    - By setting x=-1 we can solve for B (as A gets zero'd out)
    - By setting x=1 we can solve for A (as B gets zero'd out)

 - Option 2 Simultaneous equations:
    - multiply out the RHS
    - group by powers of X
    - Arrive at a set of simultaneous equations by setting each coeficient of x or constsnt on LHS with corresponding expression on the RHS

#### Integration by parts

This technique is useful for integrating expressions such as:
 - $\ln x$
 - $ \tan^{-1} x$
 - $ xe^x$

Uses below formula which appears on the formula sheet: <br>
$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$

<br>
When calculating a definite integral the "bounds" need to be applied to both the uv and the integral portion for example:
<br>

$ {\Large\int}_a^b u \dfrac{dv}{dx} dx= {\Large[} uv {\Large]}_a^b-{\Large\int}_a^bv \dfrac {du}{dx}dx$




Integration by parts can also be applied when it looks as if there is only one expression, for example $ {\Large\int} \ln  x dx$ can be written as $ {\Large\int} (1) (\ln  x) dx$ and then we can assign u=ln x and v'=1.

<br>

When integrating by parts use the LIATE rule in order to decide which expression to allocate to u to differentiate.  Assign in the below order:

 - Logarithmic functions e.g $\ln x$, $\log x$
 - Inverse trig functions
 - Algabraic functions e.g. $1$, $x$, $3x^2$
 - Trigonometric functions (excluding inverse included above)
 - Exponential functions e.g. $3^x$, $e^x$

It is possible that multiple applications of integration by parts need to be performed in oder to arrive at a solution. 

It is possible for integration by parts to form a "loop" for example: <br>
$ {\Large\int} \text{<expression 1>} = \text{expression 2 } - {\Large\int} \text{<expression 1>} $, <br>
then <br>
$ {\Large\int} \text{<expression 1>} = \dfrac{1}{2} (\text{expression 2 })$

Above 2 cases tie into recurrence relations as below.
<br>

#### Recurrence relations

A recurrence relation is a recursive formula that expresses an integral in terms of a similiar integral with a smaller power.

For example <br>

$ {\Large\int} x^ne^{ax}dx = \dfrac{1}{a}(x^ne^{ax}-n {\Large\int} x^{n-1}e^{ax}dx) $

Hints
 - An integral such as $ {\Large\int} \cos^nx $ can be restated as $ {\Large\int} \cos^{n-1} x \cos x dx$ and integration by parts can then be applied.  In these cases set u equal to the expression with the power.
  - Not all recurrence relation questions rely on integration by parts

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "a8958868-ba27-4870-b42b-63692f61abd0" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_077e4 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_077e4 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_077e4">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_077e4_row0_col0" class="data row0 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_cd3da th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_cd3da td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_cd3da_row0_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_cd3da">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_cd3da_row0_col0" class="data row0 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}