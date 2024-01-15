---
weight: 7
---

## <span style="color:RGB(0,32,96"> Proof by Mathematical Induction </span> 
<br>

## <span style="color:RGB(0,32,96"> The Nature of Proof </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "5546d40a-f866-42dd-afa6-6d236ff919d3" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_1f44f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_1f44f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_1f44f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_1f44f_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_1f44f_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_3e30e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3e30e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_3e30e_row0_col0, #T_3e30e_row1_col0, #T_3e30e_row2_col0, #T_3e30e_row3_col0, #T_3e30e_row4_col0, #T_3e30e_row6_col0, #T_3e30e_row7_col0, #T_3e30e_row8_col0, #T_3e30e_row9_col0 {
  background-color: rgba(0,0,0,0);
}
#T_3e30e_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_3e30e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_3e30e_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_3e30e_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Proof by Mathematical Induction </span> 
<br>