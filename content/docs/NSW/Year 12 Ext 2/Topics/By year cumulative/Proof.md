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
{{< tabs "03d4b9a2-0500-4d5b-bea2-2f79c8e45626" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_eca17 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_eca17 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_eca17">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_eca17_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_eca17_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_72587 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_72587 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_72587_row0_col0, #T_72587_row1_col0, #T_72587_row2_col0, #T_72587_row3_col0, #T_72587_row4_col0, #T_72587_row6_col0, #T_72587_row7_col0, #T_72587_row8_col0, #T_72587_row9_col0 {
  background-color: rgba(0,0,0,0);
}
#T_72587_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_72587">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_72587_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_72587_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_72587_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_72587_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_72587_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_72587_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_72587_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_72587_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_72587_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_72587_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Proof by Mathematical Induction </span> 
<br>