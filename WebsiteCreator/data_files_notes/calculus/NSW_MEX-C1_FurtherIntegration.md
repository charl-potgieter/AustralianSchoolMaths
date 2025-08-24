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
