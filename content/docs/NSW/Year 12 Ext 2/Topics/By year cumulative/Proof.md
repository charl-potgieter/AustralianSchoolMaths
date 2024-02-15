---
weight: 7
---

## <span style="color:RGB(0,32,96"> Proof by Mathematical Induction </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - contrapositive
 - converse
 - counterexample
 - equivalence
 - implication statement
 - negation
 - proof by contradiction - don’t confuse with counterexample
 - QED
 - statement / propisition / premise
 - triangle of inequality



### <span style="color:RGB(139,69,19)">  Notes </span>

 - Can be utilised to prove a statement true for all positive integers, n

 - Step 1: Show that the statement is true for n=1

 - Step 2: Assume that the statement is true for some positive integer n = k

 - Step 3: Using the assumption prove that the statement is also true for the next integer n=k+1

 - Conclusion: State why the statement is true for all positive integers $n \ge 1$  Don't forget this!

 - The conclusion can look like this :
    * The statement is true for n=k+1
    * The statement is true for n=1
    * Therefore by mathematical induction it is true for all integers $n \ge 1$

<BR><BR>


## <span style="color:RGB(0,32,96"> The Nature of Proof </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - contrapositive
 - converse
 - counterexample
 - equivalence
 - implication statement
 - negation
 - proof by contradiction - don’t confuse with counterexample
 - QED
 - statement / propisition / premise
 - triangle of inequality



### <span style="color:RGB(139,69,19)">  Notes </span>

 - $ P \implies Q \text { : P implies Q}$

 - $ \neg P \text{ or } P' \text{ or }  \overline P \text { : not P}$

 - $ P \iff Q \text { or } P \text { iff } Q { : equivalence}$

 - $ \forall \text{ : For all}$

 - $ \exists \text{ : There exists}$

 - $ \mathbb{N} \text { The set of natural numbers}$

 - $ \mathbb{Z}  \text { The set of integers (includes natural numbers)}$

 - $ \mathbb{Q}  \text { The set of rational numbers (includes integers)}$

 - $ \mathbb{R}  \text { The set of real numbers (includes rational numbers)}$

 - $ \mathbb{C}  \text { The set of complex numbers (includes real numbers)}$

 - $ \in  \text { is an element of or belongs to}$

 - $ :  \text { such that}$

 - Note that in general concepts such as even numbers, odd numbers etc are taken to refer to positive integers only
 
 - $ \text {The inequality definition: for } a, b \in \mathbb{R}, a > b \text{ if } a-b > 0$

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "a17a7d5a-e572-4335-a198-5594a434bbcd" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_e1052 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e1052 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_e1052">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e1052_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e1052_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_c37d9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c37d9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c37d9_row0_col0, #T_c37d9_row1_col0, #T_c37d9_row2_col0, #T_c37d9_row3_col0, #T_c37d9_row4_col0, #T_c37d9_row6_col0, #T_c37d9_row7_col0, #T_c37d9_row8_col0, #T_c37d9_row9_col0 {
  background-color: rgba(0,0,0,0);
}
#T_c37d9_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_c37d9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c37d9_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_c37d9_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Proof by Mathematical Induction </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>
