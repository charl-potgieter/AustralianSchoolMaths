---
weight: 4
---

## <span style="color:RGB(0,32,96"> Further Integration </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>





### <span style="color:RGB(139,69,19)">  Notes </span>

#### Integration by substitution

This is an extension of this topic as covered in Year 12 Ext 1.

Examples of substition "patterns" are included in the table below:

 
|Integral                                       | Substitution                                      | <div style="width:300px">Comment</div>    |
| --------                                      | -------                                           |---------                                  |
| $ \int f'(x)f(x)^n dx $                       | $u= f(x)$                                         |                                           |
| $ \int \dfrac{f'(x)}{f(x)^n} dx $             | $u= f(x)$                                         | Look for potential pattern of a function and its derivative.  n may be a fraction, that is f(x) may be inside a root     |
| $\int \dfrac{1}{a \cos x + b \sin x} dx$      | $t = \tan \frac{x}{2}$                            | $\frac{dt}{dx}$ is a function of sec but can be restated in terms of tan and then t using the trig Pythagorean identities|
| $\int \dfrac{1}{a \cos x + b} dx$             | $t = \tan \frac{x}{2}$                            |                                           |
| $\int \dfrac{1}{a + b \sin x} dx$             | $t = \tan \frac{x}{2}$                            |                                           |
| $ \int \dfrac{1}{\sqrt{a^2+x^2}} dx $         | $x=a \tan \theta$                                 |                                           |
| $ \int \dfrac{1}{\sqrt{a^2-x^2}} dx $         | $x=a \sin \theta \text{ or } x=a \cos \theta$     |                                           |
| $ \int \dfrac{1}{\sqrt{x^2-a^2}} dx $         | $x=a \sec \theta$                                 |                                           |
| $ \int \dfrac{x}{\sqrt{x+a}} dx $             | $x= u^2 -a$                                       | This enables removing the square root     |



#### Integration of rational functions

 - Rational functions are functions where both the numerator and denominator are fractions.
 - completing the square
 - **Other methods?**

#### Integration using partial fractions


#### Integration by parts

Uses below formula which appears on the formula sheet: <br>
$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$


#### Recurrence relations



<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "3cfb3d85-e7c6-48e9-b11e-b3304a64929b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_2b0e5 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2b0e5 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_2b0e5">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2b0e5_row0_col0" class="data row0 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_17ac7 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_17ac7 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_17ac7_row0_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_17ac7">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_17ac7_row0_col0" class="data row0 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}