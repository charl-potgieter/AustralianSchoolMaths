---
weight: 8
title: 'Random variables'
---


###   Concepts 

 - random variable
 - continuous random variable
 - continuous probability distribution
 - uniform probability distribution
 - probability density function (pdf)
 - cumulative distribution function (cdf)
 - empirical rule
 - normal distribution
 - z-score



###   Notes 

 - The cumulative distribution function is the integral of the probability density function

 - A continuous probability distribution is reported by a probability density function

 - The probability of a single outcome of a continuous probability distribution cannot be calculated, in other words $P(X=x) = 0$.  The probability can only be calculated for a range

 - Given $P(X=a) = 0$ and $P(X=b) = 0$, therefore $P(a < X < b) = P(a \leq X \leq b)$

 - The area under a probability density function is 1 : $ {\Large\int}^\infty_{-\infty} f(x)dx = 1$

 - Given probability density function $f(x)$ over domain [a,b] and cumulative distribution function $F(x)$ $F(a) = 0$ and $F(b) = 1$

 - The median lies at point x where ${\Large\int}^x_a f(x)dx = \dfrac{1}{2}$ where $f(x)$ is a pdf defined on domain [a,b].  Alternatively $F(x)-F(a) = \dfrac{1}{2}$ Similiar rules apply to other quantiles.

 - The mean, mode, and median are equal for a normal distribution
 
 - Finding probability by integration in a normal distribution is complex, therefore use tables where $\mu = 0$ and $\sigma = 1$


###  Spreadsheets  


Click on below to open spreadsheet examples

[RandomVariables](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/RandomVariables.xlsx)

### Formulas
{{< tabs "tab8c4d7589351ba739" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONE8c4d7589351ba739 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONE8c4d7589351ba739 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONE8c4d7589351ba739">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONE8c4d7589351ba739_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_NONE8c4d7589351ba739_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_NONE8c4d7589351ba739_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_NONE8c4d7589351ba739_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_NONE8c4d7589351ba739_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_NONE8c4d7589351ba739_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEET8c4d7589351ba739 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEET8c4d7589351ba739 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEET8c4d7589351ba739_row0_col0, #T_FORMULA_SHEET8c4d7589351ba739_row1_col0, #T_FORMULA_SHEET8c4d7589351ba739_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_FORMULA_SHEET8c4d7589351ba739_row2_col0, #T_FORMULA_SHEET8c4d7589351ba739_row3_col0, #T_FORMULA_SHEET8c4d7589351ba739_row5_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_FORMULA_SHEET8c4d7589351ba739">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET8c4d7589351ba739_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET8c4d7589351ba739_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET8c4d7589351ba739_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET8c4d7589351ba739_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET8c4d7589351ba739_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET8c4d7589351ba739_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
