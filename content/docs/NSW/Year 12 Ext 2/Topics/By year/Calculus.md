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

#### Integration of rational functions

 Rational functions are functions where both the numerator and denominator are polynomials.
 
 Possible approches:
  - Dont overlook simple options such as factorising and simplifying fractions that may remove the quadratic denominator.

  - If the integrand can be restated as $\dfrac{1}{(x+a)^2}$ the result of the integral calculation is simply $- \dfrac{1}{x+a}$
  
 - If the integrand can be transformed into one of the below forms, for examply by completing the square, the inverse sin and inverse tan integration rules can be applied respectively:
   - $\dfrac{f'(x)}{\sqrt{a^2-[f(x)]^2}}$
   
   
   - $\dfrac{f'(x)}{a^2+[f(x)]^2}$



 - **Other methods?**

<br>

#### Integration using partial fractions

<br>

#### Integration by parts

Uses below formula which appears on the formula sheet: <br>
$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$

<br>

#### Recurrence relations



<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "a1607d07-bc66-4bc2-9dc3-5757c5bf61e1" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_102e9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_102e9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_102e9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_102e9_row0_col0" class="data row0 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_25804 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_25804 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_25804_row0_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_25804">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_25804_row0_col0" class="data row0 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}