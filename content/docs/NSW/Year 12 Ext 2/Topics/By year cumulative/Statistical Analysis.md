---
weight: 5
---

## <span style="color:RGB(0,32,96"> Probability and Discrete Probability Distributions </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "abef0e26-4ef2-4f3d-a9cb-c3d696e930b7" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_c10c6 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c10c6 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_c10c6">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c10c6_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_c10c6_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_c10c6_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_c10c6_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_c10c6_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_c10c6_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_c10c6_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_c10c6_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_c10c6_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_c10c6_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_c10c6_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_c10c6_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_c10c6_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_a2417 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_a2417 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_a2417_row0_col0, #T_a2417_row3_col0, #T_a2417_row5_col0, #T_a2417_row6_col0, #T_a2417_row8_col0, #T_a2417_row10_col0, #T_a2417_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_a2417_row1_col0, #T_a2417_row2_col0, #T_a2417_row4_col0, #T_a2417_row7_col0, #T_a2417_row9_col0, #T_a2417_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_a2417">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_a2417_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_a2417_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_a2417_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_a2417_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_a2417_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_a2417_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_a2417_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_a2417_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_a2417_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_a2417_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_a2417_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_a2417_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_a2417_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_8c5a1 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8c5a1 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_8c5a1_row0_col0, #T_8c5a1_row2_col0, #T_8c5a1_row4_col0, #T_8c5a1_row5_col0, #T_8c5a1_row6_col0, #T_8c5a1_row7_col0, #T_8c5a1_row8_col0, #T_8c5a1_row9_col0, #T_8c5a1_row10_col0, #T_8c5a1_row11_col0, #T_8c5a1_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_8c5a1_row1_col0, #T_8c5a1_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_8c5a1">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8c5a1_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_8c5a1_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Descriptive Statistics and Bivariate Data Analysis </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "f8d084ab-4094-41dc-970f-047bd615b23e" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_3d9e3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3d9e3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_3d9e3">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_3d9e3_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_3d9e3_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_3d9e3_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_3d9e3_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_3d9e3_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_3d9e3_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_16e83 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_16e83 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_16e83_row0_col0, #T_16e83_row1_col0, #T_16e83_row2_col0, #T_16e83_row3_col0, #T_16e83_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_16e83_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_16e83">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_16e83_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_16e83_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_16e83_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_16e83_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_16e83_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_16e83_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Random Variables </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "4392e782-7d7e-4232-bc25-40b76067ef7d" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_5e49e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5e49e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_5e49e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5e49e_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_5e49e_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_5e49e_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_5e49e_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_5e49e_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_5e49e_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_af31b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_af31b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_af31b_row0_col0, #T_af31b_row1_col0, #T_af31b_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_af31b_row2_col0, #T_af31b_row3_col0, #T_af31b_row5_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_af31b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_af31b_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_af31b_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_af31b_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_af31b_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_af31b_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_af31b_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

### <span style="color:RGB(139,69,19)"> Spreadsheets  </span>


Click on below to open spreadsheet examples

[RandomVariables](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/RandomVariables.xlsx)


## <span style="color:RGB(0,32,96"> The Binomial Distribution </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "7a7fa363-c674-4a3f-8af1-5d946031df46" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_d9d08 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d9d08 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_d9d08">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d9d08_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_d9d08_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_d9d08_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_d9d08_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_d9d08_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_d9d08_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_d9d08_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_d9d08_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_d9d08_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_a143a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_a143a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_a143a_row0_col0, #T_a143a_row1_col0, #T_a143a_row7_col0, #T_a143a_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_a143a_row2_col0, #T_a143a_row3_col0, #T_a143a_row4_col0, #T_a143a_row5_col0, #T_a143a_row6_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_a143a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_a143a_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_a143a_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_a143a_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_a143a_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_a143a_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_a143a_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_a143a_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_a143a_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_a143a_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

### <span style="color:RGB(139,69,19)"> Spreadsheets  </span>


Click on below to open spreadsheet examples

[BinomialDistributions](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/BinomialDistributions.xlsx)
