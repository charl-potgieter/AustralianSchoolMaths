---
weight: 4
---

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

A proper fraction can be decomposed into simpler partial fractions.

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

Uses below formula which appears on the formula sheet: <br>
$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$

<br>

#### Recurrence relations



<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "2d5a1f62-cb58-498a-b5b1-d225231ec8a8" >}}

{{< tab "Standard view" >}}

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
</style>
<table id="T_0181f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_0181f_row0_col0" class="data row0 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_23d4c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_23d4c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_23d4c_row0_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_23d4c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_23d4c_row0_col0" class="data row0 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}