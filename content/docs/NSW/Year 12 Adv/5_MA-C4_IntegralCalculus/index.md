---
weight: 5
title: 'Integral calculus'
---

###   Concepts 

 - anti-derivative / indefinate integral / pimitive
  - definite integral
 - area under a curve
 


###   Notes 

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

### Formulas
{{< tabs "tab823133bb1f5f30d0" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONE823133bb1f5f30d0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONE823133bb1f5f30d0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONE823133bb1f5f30d0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_NONE823133bb1f5f30d0_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEET823133bb1f5f30d0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEET823133bb1f5f30d0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEET823133bb1f5f30d0_row0_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row1_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row2_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row3_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row4_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row5_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row6_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row7_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_FORMULA_SHEET823133bb1f5f30d0_row8_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row9_col0, #T_FORMULA_SHEET823133bb1f5f30d0_row10_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_FORMULA_SHEET823133bb1f5f30d0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET823133bb1f5f30d0_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proof Required" >}}

<style type="text/css">
#T_PROOF_REQUIRED823133bb1f5f30d0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_PROOF_REQUIRED823133bb1f5f30d0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_PROOF_REQUIRED823133bb1f5f30d0_row0_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row2_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row3_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row5_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row6_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row9_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
#T_PROOF_REQUIRED823133bb1f5f30d0_row1_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row4_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row7_col0, #T_PROOF_REQUIRED823133bb1f5f30d0_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_PROOF_REQUIRED823133bb1f5f30d0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row1_col0" class="data row1 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row2_col0" class="data row2 col0" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row6_col0" class="data row6 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row7_col0" class="data row7 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row8_col0" class="data row8 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row9_col0" class="data row9 col0" >$ {\Large\int}_b^a f(x)dx = F(b)-F(a) \text{, where F(x) is the anti-derivative of f(x)}$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED823133bb1f5f30d0_row10_col0" class="data row10 col0" >$F'(x) = \dfrac{d}{dx} {\Large\int}_a^x f(t)dt = f(x) \text{ (the Fundamental Therom of Calculus)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
