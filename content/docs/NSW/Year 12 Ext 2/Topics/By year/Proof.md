---
weight: 1
---

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
{{< tabs "fadfffe5-e973-477e-8153-8b99d948411b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_e8325 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e8325 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_e8325">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e8325_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_e8325_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_2802a th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2802a td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_2802a_row0_col0, #T_2802a_row1_col0, #T_2802a_row2_col0, #T_2802a_row3_col0, #T_2802a_row4_col0, #T_2802a_row6_col0, #T_2802a_row7_col0, #T_2802a_row8_col0, #T_2802a_row9_col0 {
  background-color: rgba(0,0,0,0);
}
#T_2802a_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_2802a">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2802a_row0_col0" class="data row0 col0" >$ |a| \ge a,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row1_col0" class="data row1 col0" >$ |a||b| = |ab|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row2_col0" class="data row2 col0" >$ |a|^2 = a^2,  \forall \: a \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row3_col0" class="data row3 col0" >$ |ab| \ge ab,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row4_col0" class="data row4 col0" >$ a^2 \ge b^2 \iff |a| \ge |b|,  \forall \: a,b \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row5_col0" class="data row5 col0" >$ |x| + |y| \ge |x+y|, \forall \; x, y \in \mathbb{R}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row6_col0" class="data row6 col0" >$ \text {even number } 2n, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row7_col0" class="data row7 col0" >$ \text {odd number } 2n-1, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row8_col0" class="data row8 col0" >$ \text {square number } n^2, \forall \: n \in \mathbb{N}$</td>
    </tr>
    <tr>
      <td id="T_2802a_row9_col0" class="data row9 col0" >$ \text {X is divisible by p when there exists another number, } p, p \in \mathbb{N}, \text{ if } \exists \; Y, Y \in \mathbb{N} \text { such that } X=pY$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Proof by Mathematical Induction </span> 
<br>

 
 ### <span style="color:RGB(139,69,19)">  Concepts </span>

 - divisibility
 - induction
 - recursive formula
 - series
 - sigma notation





### <span style="color:RGB(139,69,19)">  Notes </span>


#### Proof of divisibility
If X is divisible by Y then X = pY for some $P \in \mathbb{N}$

#### Further mathematical induction
Proving propositions that are only true for a subset of integer values n such as 
 - $ n \ge \text {some value}$
 - odd integers
 - even integers

#### Series and sigma notation

$\displaystyle \sum_{n=1}^n T_r - T_1 + T_2 + T_3+...+T_n$

RTP = required to prove

Tip: Sequences that alternate between positive and negative can be prefixed by $(-1)^r$

#### Applications of mathematical induction

Below are examples of results that can be ussed in inequality proofs:
 
 - if a>b then a-b >0

 - if a>b and b>c then a>c

 - if a>b and c>d then a+c>b+d

 - if a,b,c > 0  and a>b then ac>bc
 
 - if a>b>0 then $\dfrac{1}{a}<\dfrac{1}{b}$


#### Recursive proofs
 - Recursive formulas: An item  in a sequence is defined in terms of the precvious item in the sequence.

 - Induction can be utilised to prove a recursive formula in terms of n (without referencing the previous term in the sequence)

 - Tip: When assuming  P(k) is true, it is also assumed that P(k-1), P(k-2) and earlier are true.  It is only the next item that needs to be proven, e.g P(k+1) or say P(k+2) for odd or even numbers



#### Proofs involving inequalities and graphs
Graphs can be utlised when inequalities are difficult to solve  algebraically. 

<BR><BR>
