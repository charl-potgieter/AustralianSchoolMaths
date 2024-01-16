---
weight: 6
---

## <span style="color:RGB(0,32,96"> Probability and Discrete Probability Distributions </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "7db61aeb-16cc-4b74-81ff-486c2a1c293c" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_b8a27 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_b8a27 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_b8a27">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_b8a27_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_b8a27_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_b8a27_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_b8a27_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_b8a27_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_b8a27_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_b8a27_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_b8a27_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_b8a27_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_b8a27_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_b8a27_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_b8a27_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_b8a27_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_7db17 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_7db17 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_7db17_row0_col0, #T_7db17_row3_col0, #T_7db17_row5_col0, #T_7db17_row6_col0, #T_7db17_row8_col0, #T_7db17_row10_col0, #T_7db17_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_7db17_row1_col0, #T_7db17_row2_col0, #T_7db17_row4_col0, #T_7db17_row7_col0, #T_7db17_row9_col0, #T_7db17_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_7db17">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_7db17_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_7db17_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_7db17_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_7db17_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_7db17_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_7db17_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_7db17_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_7db17_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_7db17_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_7db17_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_7db17_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_7db17_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_7db17_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_5daef th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5daef td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_5daef_row0_col0, #T_5daef_row2_col0, #T_5daef_row4_col0, #T_5daef_row5_col0, #T_5daef_row6_col0, #T_5daef_row7_col0, #T_5daef_row8_col0, #T_5daef_row9_col0, #T_5daef_row10_col0, #T_5daef_row11_col0, #T_5daef_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_5daef_row1_col0, #T_5daef_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_5daef">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5daef_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_5daef_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_5daef_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_5daef_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_5daef_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_5daef_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_5daef_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_5daef_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_5daef_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_5daef_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_5daef_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_5daef_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_5daef_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
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
{{< tabs "efa08b3f-67df-456f-aec2-1573bdbb5128" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_7010a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_7010a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_7010a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_7010a_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_7010a_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_7010a_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_7010a_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_7010a_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_7010a_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_34dab th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_34dab td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_34dab_row0_col0, #T_34dab_row1_col0, #T_34dab_row2_col0, #T_34dab_row3_col0, #T_34dab_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_34dab_row4_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_34dab">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_34dab_row0_col0" class="data row0 col0" >$ \text{Mean} = \dfrac{\text{Sum of scores}}{\text{Total number of scores}} = \overline{x} = \dfrac{\sum{x}}{n} $</td>
    </tr>
    <tr>
      <td id="T_34dab_row1_col0" class="data row1 col0" >$ \text{The median of n scores is the } \dfrac{n+1}{2} \text{th score} $
$ \text{if n is even the median is the average of the two middle scores to the left and the right of }  \dfrac{n+1}{2} $</td>
    </tr>
    <tr>
      <td id="T_34dab_row2_col0" class="data row2 col0" >$ \text{Range = highest score - lowest score} $</td>
    </tr>
    <tr>
      <td id="T_34dab_row3_col0" class="data row3 col0" >$ \text{Interquartile range = Q3 - Q1} $</td>
    </tr>
    <tr>
      <td id="T_34dab_row4_col0" class="data row4 col0" >$\text{An outlier is a score with} $
$ \text {   less than } Q1 - 1.5  \times IQR $
$ \text {   or more than than } Q3 + 1.5  \times IQR $</td>
    </tr>
    <tr>
      <td id="T_34dab_row5_col0" class="data row5 col0" >$ \overline{x} = \dfrac{\sum fx}{\sum f} $</td>
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
{{< tabs "c05ac5ed-f01a-460a-9916-81e819b4a68b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_d8837 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d8837 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_d8837">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d8837_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_d8837_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_d8837_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_d8837_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_d8837_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_d8837_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_b42d7 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_b42d7 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_b42d7_row0_col0, #T_b42d7_row1_col0, #T_b42d7_row4_col0 {
  background-color: rgba(0,0,0,0);
}
#T_b42d7_row2_col0, #T_b42d7_row3_col0, #T_b42d7_row5_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_b42d7">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_b42d7_row0_col0" class="data row0 col0" >$P(a < X < b) = P(a \leq X \leq b) \text {(for continuous probability distributions})$</td>
    </tr>
    <tr>
      <td id="T_b42d7_row1_col0" class="data row1 col0" >$F(x) = P(X\leq x) = {\Large\int}^x_a f(x)dx \text { (for continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b] and F(x) is the cumulative density function})$</td>
    </tr>
    <tr>
      <td id="T_b42d7_row2_col0" class="data row2 col0" >$P(X \leq r) =  {\Large\int}_a^r f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_b42d7_row3_col0" class="data row3 col0" >$P(a \leq X \leq b) =  {\Large\int}_a^b f(x)dx$</td>
    </tr>
    <tr>
      <td id="T_b42d7_row4_col0" class="data row4 col0" >$f(x) = \dfrac{1}{b-a} \text{ for } a \leq x \leq b \text { (Uniform continuous probability distributions, where f(x) is a probability distribution function defined in the domain [a,b]})$</td>
    </tr>
    <tr>
      <td id="T_b42d7_row5_col0" class="data row5 col0" >$z = \dfrac{x-\mu}{\sigma} $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

### <span style="color:RGB(139,69,19)"> Spreadsheets  </span>


Click on below to open spreadsheet examples

[RandomVariables](https://github.com/charl-potgieter/AustralianSchoolMaths/raw/main/WebsiteCreator/spreadsheets/RandomVariables.xlsx)
