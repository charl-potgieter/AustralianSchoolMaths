---
weight: 8
---

## <span style="color:RGB(0,32,96"> Probability and Discrete Probability Distributions </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "c79817c3-c3b7-40ff-a5e7-9ce3b1f7166b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_fbfec th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fbfec td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_fbfec">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fbfec_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_fbfec_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_fbfec_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_fbfec_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_fbfec_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_fbfec_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_fbfec_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_fbfec_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_fbfec_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_fbfec_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_fbfec_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_fbfec_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_fbfec_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_8322a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8322a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_8322a_row0_col0, #T_8322a_row3_col0, #T_8322a_row5_col0, #T_8322a_row6_col0, #T_8322a_row8_col0, #T_8322a_row10_col0, #T_8322a_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_8322a_row1_col0, #T_8322a_row2_col0, #T_8322a_row4_col0, #T_8322a_row7_col0, #T_8322a_row9_col0, #T_8322a_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_8322a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8322a_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_8322a_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_8322a_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_8322a_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_8322a_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_8322a_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_8322a_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_8322a_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_8322a_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_8322a_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_8322a_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_8322a_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_8322a_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_89ae0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_89ae0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_89ae0_row0_col0, #T_89ae0_row2_col0, #T_89ae0_row4_col0, #T_89ae0_row5_col0, #T_89ae0_row6_col0, #T_89ae0_row7_col0, #T_89ae0_row8_col0, #T_89ae0_row9_col0, #T_89ae0_row10_col0, #T_89ae0_row11_col0, #T_89ae0_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_89ae0_row1_col0, #T_89ae0_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_89ae0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_89ae0_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_89ae0_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_89ae0_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_89ae0_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_89ae0_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_89ae0_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_89ae0_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_89ae0_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_89ae0_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_89ae0_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_89ae0_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_89ae0_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_89ae0_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
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
{{< tabs "8fd11288-e453-4513-8513-cc7fbe0d5d76" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_4f3ea th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4f3ea td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_4f3ea">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4f3ea_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_4f3ea_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_4f3ea_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_4f3ea_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_4f3ea_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_4f3ea_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_1841c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_1841c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_1841c_row0_col0, #T_1841c_row1_col0, #T_1841c_row2_col0, #T_1841c_row3_col0, #T_1841c_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_1841c_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_1841c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_1841c_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_1841c_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_1841c_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_1841c_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_1841c_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_1841c_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
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
{{< tabs "45626112-89a5-4a44-8509-65db4738b466" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_778bf th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_778bf td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_778bf">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_778bf_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_778bf_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_778bf_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_778bf_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_778bf_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_778bf_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_9fbb2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_9fbb2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_9fbb2_row0_col0, #T_9fbb2_row1_col0, #T_9fbb2_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_9fbb2_row2_col0, #T_9fbb2_row3_col0, #T_9fbb2_row5_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_9fbb2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_9fbb2_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_9fbb2_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_9fbb2_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_9fbb2_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_9fbb2_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_9fbb2_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
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
{{< tabs "9f3aaffb-ffef-4c7a-924f-df6266ea6945" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_39d88 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_39d88 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_39d88">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_39d88_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_39d88_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_39d88_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_39d88_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_39d88_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_39d88_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_39d88_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_39d88_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_39d88_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_5b3e7 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5b3e7 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_5b3e7_row0_col0, #T_5b3e7_row1_col0, #T_5b3e7_row7_col0, #T_5b3e7_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_5b3e7_row2_col0, #T_5b3e7_row3_col0, #T_5b3e7_row4_col0, #T_5b3e7_row5_col0, #T_5b3e7_row6_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_5b3e7">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5b3e7_row0_col0" class="data row0 col0" >$ \text{Bernoulli distribution: } E(X) = p $</td>
    </tr>
    <tr>
      <td id="T_5b3e7_row1_col0" class="data row1 col0" >$ \text{Bernoulli distribution: } VAR(X) = p(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_5b3e7_row2_col0" class="data row2 col0" >$\text{Binomial distribution}: P(X=r) = ^nC_rp^r(1-p)^{n-r}$</td>
    </tr>
    <tr>
      <td id="T_5b3e7_row3_col0" class="data row3 col0" >$\text{Binomial distribution}: X\sim Bin(n,p) $
$ \Rightarrow P(X=x) $
$ = \bigl({n \atop x} \bigr)p^x(1-p)^{n-x}, x=0,1,...,n$</td>
    </tr>
    <tr>
      <td id="T_5b3e7_row4_col0" class="data row4 col0" >$ \text{binomial distribution: } E(X) = np $</td>
    </tr>
    <tr>
      <td id="T_5b3e7_row5_col0" class="data row5 col0" >$ \text{binmomial distribution: } VAR(X) = np(1-p)  $</td>
    </tr>
    <tr>
      <td id="T_5b3e7_row6_col0" class="data row6 col0" >$ \hat{p} = \dfrac{x}{n} $</td>
    </tr>
    <tr>
      <td id="T_5b3e7_row7_col0" class="data row7 col0" >$ \text{sample proportions: } E(\hat{p}) = p $</td>
    </tr>
    <tr>
      <td id="T_5b3e7_row8_col0" class="data row8 col0" >$ \text{sample proportions: } \text{VAR} (\hat{p}) = \dfrac{p(1-p)}{n} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

### <span style="color:RGB(139,69,19)"> Spreadsheets  </span>


Click on below to open spreadsheet examples

[BinomialDistributions](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/BinomialDistributions.xlsx)
