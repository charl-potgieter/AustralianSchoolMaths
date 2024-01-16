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
{{< tabs "95a095ef-e48b-4416-a713-2f8fed0b46f2" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_8cb45 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8cb45 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_8cb45">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8cb45_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_8cb45_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_8cb45_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_8cb45_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_8cb45_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_8cb45_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_8cb45_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_8cb45_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_8cb45_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_8cb45_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_8cb45_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_8cb45_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_8cb45_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_c8071 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c8071 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c8071_row0_col0, #T_c8071_row3_col0, #T_c8071_row5_col0, #T_c8071_row6_col0, #T_c8071_row8_col0, #T_c8071_row10_col0, #T_c8071_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_c8071_row1_col0, #T_c8071_row2_col0, #T_c8071_row4_col0, #T_c8071_row7_col0, #T_c8071_row9_col0, #T_c8071_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_c8071">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c8071_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_c8071_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_c8071_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_c8071_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_c8071_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_c8071_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_c8071_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_c8071_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_c8071_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_c8071_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_c8071_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_c8071_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_c8071_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_5c33b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5c33b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_5c33b_row0_col0, #T_5c33b_row2_col0, #T_5c33b_row4_col0, #T_5c33b_row5_col0, #T_5c33b_row6_col0, #T_5c33b_row7_col0, #T_5c33b_row8_col0, #T_5c33b_row9_col0, #T_5c33b_row10_col0, #T_5c33b_row11_col0, #T_5c33b_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_5c33b_row1_col0, #T_5c33b_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_5c33b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5c33b_row0_col0" class="data row0 col0" >$ P(E) = \dfrac{n(E)}{n(S)} $</td>
    </tr>
    <tr>
      <td id="T_5c33b_row1_col0" class="data row1 col0" >$P(A \cup B) = P(A) + P(B) - P(A \cap B) $</td>
    </tr>
    <tr>
      <td id="T_5c33b_row2_col0" class="data row2 col0" >$P(A \cap B)  = P(A)P(B)$</td>
    </tr>
    <tr>
      <td id="T_5c33b_row3_col0" class="data row3 col0" >$P(\overline{E}) = 1 - P(E)$</td>
    </tr>
    <tr>
      <td id="T_5c33b_row4_col0" class="data row4 col0" >$ P(A|B) = \dfrac{P(A \cap B)}{P(B)} \text{, where } P(B) \neq 0 $</td>
    </tr>
    <tr>
      <td id="T_5c33b_row5_col0" class="data row5 col0" >$ P(X=x) =  \dfrac{1}{n} 
\text {applies only to uniform proability distributions with n values} $</td>
    </tr>
    <tr>
      <td id="T_5c33b_row6_col0" class="data row6 col0" >$ E(X) =\sum xp(x)$</td>
    </tr>
    <tr>
      <td id="T_5c33b_row7_col0" class="data row7 col0" >$ E(X) = \mu $</td>
    </tr>
    <tr>
      <td id="T_5c33b_row8_col0" class="data row8 col0" >$ \sigma^{2} = Var(X) = \sum(x-\mu)^{2}p(x)$</td>
    </tr>
    <tr>
      <td id="T_5c33b_row9_col0" class="data row9 col0" >$ Var(X) = E[(x-\mu)^2]$</td>
    </tr>
    <tr>
      <td id="T_5c33b_row10_col0" class="data row10 col0" >$ Var(X) = \sum[x^2p(x)] - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_5c33b_row11_col0" class="data row11 col0" >$ Var(X) = E(X^2) - \mu^2$</td>
    </tr>
    <tr>
      <td id="T_5c33b_row12_col0" class="data row12 col0" >$ \sigma = \sqrt{Var(X)}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}