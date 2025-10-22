---
weight: 4
title: 'Further calculus skills'
---


###   Concepts 





###   Notes 

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

### Formulas
{{< tabs "tab1510825f7d8e9942" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONE1510825f7d8e9942 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONE1510825f7d8e9942 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONE1510825f7d8e9942">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_NONE1510825f7d8e9942_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEET1510825f7d8e9942 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEET1510825f7d8e9942 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEET1510825f7d8e9942_row0_col0, #T_FORMULA_SHEET1510825f7d8e9942_row3_col0, #T_FORMULA_SHEET1510825f7d8e9942_row4_col0, #T_FORMULA_SHEET1510825f7d8e9942_row8_col0, #T_FORMULA_SHEET1510825f7d8e9942_row11_col0, #T_FORMULA_SHEET1510825f7d8e9942_row13_col0, #T_FORMULA_SHEET1510825f7d8e9942_row14_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_FORMULA_SHEET1510825f7d8e9942_row1_col0, #T_FORMULA_SHEET1510825f7d8e9942_row2_col0, #T_FORMULA_SHEET1510825f7d8e9942_row5_col0, #T_FORMULA_SHEET1510825f7d8e9942_row6_col0, #T_FORMULA_SHEET1510825f7d8e9942_row7_col0, #T_FORMULA_SHEET1510825f7d8e9942_row9_col0, #T_FORMULA_SHEET1510825f7d8e9942_row10_col0, #T_FORMULA_SHEET1510825f7d8e9942_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_FORMULA_SHEET1510825f7d8e9942">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET1510825f7d8e9942_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proof Required" >}}

<style type="text/css">
#T_PROOF_REQUIRED1510825f7d8e9942 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_PROOF_REQUIRED1510825f7d8e9942 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_PROOF_REQUIRED1510825f7d8e9942_row0_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row1_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row2_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row3_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row4_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row5_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row6_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row7_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row8_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row9_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row10_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row11_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row13_col0, #T_PROOF_REQUIRED1510825f7d8e9942_row14_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_PROOF_REQUIRED1510825f7d8e9942_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_PROOF_REQUIRED1510825f7d8e9942">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row0_col0" class="data row0 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row2_col0" class="data row2 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row4_col0" class="data row4 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row6_col0" class="data row6 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row8_col0" class="data row8 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row10_col0" class="data row10 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row13_col0" class="data row13 col0" >$\sin^2nx = \dfrac{1}{2}(1-\cos 2nx)$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED1510825f7d8e9942_row14_col0" class="data row14 col0" >$\cos^2nx = \dfrac{1}{2}(1+\cos 2nx)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
