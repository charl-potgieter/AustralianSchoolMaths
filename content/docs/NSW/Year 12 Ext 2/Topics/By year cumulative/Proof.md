---
weight: 7
---

## <span style="color:RGB(0,32,96"> Proof by Mathematical Induction </span> 
<br>

### <span style="color:RGB(139,69,19)">  Notes </span>


* Can be utilised to prove a statement true for all positive integers, n
<BR><BR>
* Step 1: Show that the statement is true for n=1
<BR><BR>
* Step 2: Assume that the statement is true for some positive integer n = k
<BR><BR>
* Step 3: Using the assumption prove that the statement is also true for the next integer n=k+1
<BR><BR>
* Conclusion: State why the statement is true for all positive integers $n \ge 1$  Don't forget this!
<BR><BR>
* The conclusion can look like this :
    * The statement is true for n=k+1
    * The statement is true for n=1
    * Therefore by mathematical induction it is true for all integers $n \ge 1$
<BR><BR>


## <span style="color:RGB(0,32,96"> The Nature of Proof </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* contrapositive
* converse
* counterexample
* equivalence
* implication statement
* negation
* proof by contradiction - don’t confuse with counterexample
* QED
* statement / propisition / premise
* triangle of inequality


### <span style="color:RGB(139,69,19)">  Notes </span>


* $ P \implies Q \text { : P implies Q}$
<BR><BR>
* $ \neg P \text{ or } P' \text{ or }  \overline P \text { : not P}$
<BR><BR>
* $ P \iff Q \text { or } P \text { iff } Q { : equivalence}$
<BR><BR>
* $ \forall \text{ : For all}$
<BR><BR>
* $ \exists \text{ : There exists}$
<BR><BR>
* $ \mathbb{N} \text { The set of natural numbers}$
<BR><BR>
* $ \mathbb{Z}  \text { The set of integers (includes natural numbers)}$
<BR><BR>
* $ \mathbb{Q}  \text { The set of rational numbers (includes integers)}$
<BR><BR>
* $ \mathbb{R}  \text { The set of real numbers (includes rational numbers)}$
<BR><BR>
* $ \mathbb{C}  \text { The set of complex numbers (includes real numbers)}$
<BR><BR>
* $ \in  \text { is an element of or belongs to}$
<BR><BR>
* $ :  \text { such that}$
<BR><BR>
* Note that in general concepts such as even numbers, odd numbers etc are taken to refer to positive integers only
<BR><BR>
* $ \text {The inequality definition: for } a, b \in \mathbb{R}, a > b \text{ if } a-b > 0$
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "6d81f127-0dff-43cd-bd70-19ff7cdaf386" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_5e669 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5e669 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_5e669">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5e669_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_5e669_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_e9185 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e9185 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_e9185_row0_col0, #T_e9185_row1_col0, #T_e9185_row2_col0, #T_e9185_row3_col0, #T_e9185_row4_col0, #T_e9185_row6_col0, #T_e9185_row7_col0, #T_e9185_row8_col0, #T_e9185_row9_col0 {
  background-color: rgba(0,0,0,0);
}
#T_e9185_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_e9185">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e9185_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e9185_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Proof by Mathematical Induction </span> 
<br>