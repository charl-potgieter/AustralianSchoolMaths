---
weight: 4
---

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
{{< tabs "abfc27b3-bb30-458c-989e-e7b17ba19bb2" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_253a8 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_253a8 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_253a8">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_253a8_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_253a8_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_253a8_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_253a8_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_253a8_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_253a8_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_253a8_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_253a8_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_253a8_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_253a8_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_253a8_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_253a8_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_253a8_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_253a8_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_253a8_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_19491 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_19491 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_19491_row0_col0, #T_19491_row3_col0, #T_19491_row4_col0, #T_19491_row8_col0, #T_19491_row11_col0, #T_19491_row13_col0, #T_19491_row14_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_19491_row1_col0, #T_19491_row2_col0, #T_19491_row5_col0, #T_19491_row6_col0, #T_19491_row7_col0, #T_19491_row9_col0, #T_19491_row10_col0, #T_19491_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_19491">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_19491_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_19491_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_19491_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_19491_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_19491_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_19491_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_19491_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_19491_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_19491_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_19491_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_19491_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_19491_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_19491_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_19491_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_19491_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_42468 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_42468 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_42468_row0_col0, #T_42468_row1_col0, #T_42468_row2_col0, #T_42468_row3_col0, #T_42468_row4_col0, #T_42468_row5_col0, #T_42468_row6_col0, #T_42468_row7_col0, #T_42468_row8_col0, #T_42468_row9_col0, #T_42468_row10_col0, #T_42468_row11_col0, #T_42468_row13_col0, #T_42468_row14_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_42468_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_42468">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_42468_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_42468_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_42468_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_42468_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_42468_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_42468_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_42468_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_42468_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_42468_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_42468_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_42468_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_42468_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_42468_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_42468_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_42468_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}


<br>


###  <span style="color:RGB(139,69,19)"> Derivatives vs integrals  </span>
<br>
{{< tabs "8adfcd47-a80a-48d9-b25d-fb022e19d5ef" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_bb89a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bb89a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_bb89a">
  <thead>
    <tr>
      <th id="T_bb89a_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_bb89a_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_bb89a_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_bb89a_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_bb89a_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_bb89a_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_bb89a_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_bb89a_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_bb89a_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_bb89a_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_bb89a_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_bb89a_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_bb89a_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_bb89a_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_bb89a_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_bb89a_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_bb89a_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_bb89a_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_bb89a_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_bb89a_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_bb89a_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_3dcc6 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3dcc6 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_3dcc6_row0_col0, #T_3dcc6_row1_col1, #T_3dcc6_row2_col0, #T_3dcc6_row4_col0, #T_3dcc6_row5_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_3dcc6_row0_col1, #T_3dcc6_row1_col0, #T_3dcc6_row2_col1, #T_3dcc6_row3_col0, #T_3dcc6_row3_col1, #T_3dcc6_row4_col1, #T_3dcc6_row5_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_3dcc6">
  <thead>
    <tr>
      <th id="T_3dcc6_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_3dcc6_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_3dcc6_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_3dcc6_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_3dcc6_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_3dcc6_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_3dcc6_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_3dcc6_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_3dcc6_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_3dcc6_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_3dcc6_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_3dcc6_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_3dcc6_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_3dcc6_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_3dcc6_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_3dcc6_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_3dcc6_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_3dcc6_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_3dcc6_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_3dcc6_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_3dcc6_row5_col2" class="data row5 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_8b086 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8b086 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_8b086_row0_col0, #T_8b086_row0_col1, #T_8b086_row1_col0, #T_8b086_row1_col1, #T_8b086_row2_col0, #T_8b086_row2_col1, #T_8b086_row3_col0, #T_8b086_row3_col1, #T_8b086_row4_col0, #T_8b086_row4_col1, #T_8b086_row5_col0, #T_8b086_row5_col1 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_8b086">
  <thead>
    <tr>
      <th id="T_8b086_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_8b086_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_8b086_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_8b086_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_8b086_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_8b086_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_8b086_row1_col0" class="data row1 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_8b086_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_8b086_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_8b086_row2_col0" class="data row2 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_8b086_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_8b086_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_8b086_row3_col0" class="data row3 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_8b086_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_8b086_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_8b086_row4_col0" class="data row4 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_8b086_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_8b086_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_8b086_row5_col0" class="data row5 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_8b086_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_8b086_row5_col2" class="data row5 col2" ></td>
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
{{< tabs "3e5543a1-72e8-49bc-a7e8-8f6c265931f8" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_ecfc7 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ecfc7 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_ecfc7">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ecfc7_row0_col0" class="data row0 col0" >Volumes formed by rotation about the x-axis = $V=\pi \int_a^b y^2 dx$</td>
    </tr>
    <tr>
      <td id="T_ecfc7_row1_col0" class="data row1 col0" >Volumes formed by rotation about the y-axis = $V=\pi \int_a^b x^2 dy$</td>
    </tr>
    <tr>
      <td id="T_ecfc7_row2_col0" class="data row2 col0" >Logistic equation option 1: $\frac{dP}{dt} = kP(N-P)$ <br><br></td>
    </tr>
    <tr>
      <td id="T_ecfc7_row3_col0" class="data row3 col0" >Logistic equation option 2:$\frac{dP}{dt} = kP(1-\frac{P}{N})$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_000f3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_000f3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_000f3_row0_col0, #T_000f3_row1_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_000f3_row2_col0, #T_000f3_row3_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_000f3">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_000f3_row0_col0" class="data row0 col0" >Volumes formed by rotation about the x-axis = $V=\pi \int_a^b y^2 dx$</td>
    </tr>
    <tr>
      <td id="T_000f3_row1_col0" class="data row1 col0" >Volumes formed by rotation about the y-axis = $V=\pi \int_a^b x^2 dy$</td>
    </tr>
    <tr>
      <td id="T_000f3_row2_col0" class="data row2 col0" >Logistic equation option 1: $\frac{dP}{dt} = kP(N-P)$ <br><br></td>
    </tr>
    <tr>
      <td id="T_000f3_row3_col0" class="data row3 col0" >Logistic equation option 2:$\frac{dP}{dt} = kP(1-\frac{P}{N})$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}