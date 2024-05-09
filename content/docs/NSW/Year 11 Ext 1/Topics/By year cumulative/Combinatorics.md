---
weight: 4
---

## <span style="color:RGB(0,32,96"> Working with Combinatorics </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - arrangements
 - fundamental counting principle, also known as the multiplication principle
 - pigeonhole principle
 - generalised pigeonhole principle
 - ordered selections
 - unordered selections
 - factorial
 - permutations
 - combinations
 - binomial expansion
 - Pascal's triangle and binomial coefficients
 - Pascal's triangle identity


### <span style="color:RGB(139,69,19)">  Notes </span>

 - $ n!$ is the number of ways of selecting n objects with no replacement or repetition.  Order is important.

 - Permutations = ordered

 - $^nP_r$ is the number of ways of making an ordered selection or r objects from a total of n objects.

 - Combinations = unordered.  Given the order is not important, therefore will be a smaller number than the equivalent permutation.

 - $^nC_r = (^n_r)$ is the number of ways of making an unordered selection or r objects from a total of n objects.

 - When calculating how many ways items can be arranged in a circle e.g. table, necklace:
    * questions assume position of items in a circle is irrelevant
    * item appearing at the top of the circle vs the bottom of the circle is the same thing for example
    * Therefore n items can be arranged around a circle in (n-1)! ways, as the positioning of the first item is irrelevant

 - When x items in an arrangement need to be together / consecutive, treat these as one item, and make the corresponding reduction to n.
     * For example when 5 different colour balls need to be arranged but red and yellow need to be next to each other than the number of arrangements is 4! treating the red and yellow as one.
     * But these x objects can be arranged in x! ways, in above case 2!
    * Therefore total arrangements  = 4! x 2!

 - Be on the lookout for the options in the "other" part of the arrangement.
    * For example if questions asks how many ways can 3 people sit next to each other at a table of 7 people:
    * The 3 people can sit next to each other in 3! ways  - where they sit on round table is irrelevant
    * Don’t forget that the other 4 people can sit next to each other in 4! different ways
    * Therefore 3! x 4!

 - Each item in Pascals triangle can be written as $^{\text{row index}}C_{\text{column index}}$ where both the indices start from zero.
 
 - To satisfy oneself as to workings of binomial expansion it can be quickly tested with something simple like $(a+b)^2$



<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "d9a16a0a-8403-4911-90ba-5e34d82276e9" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_fdebd th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fdebd td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_fdebd">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fdebd_row0_col0" class="data row0 col0" >$P(E) = \dfrac{\text{Number of ways an event can occur}}{\text{Total number of possible outcomes}}$</td>
    </tr>
    <tr>
      <td id="T_fdebd_row1_col0" class="data row1 col0" >$^n P_r = \dfrac{n!}{(n-r)!}$</td>
    </tr>
    <tr>
      <td id="T_fdebd_row2_col0" class="data row2 col0" >$0! = 1$</td>
    </tr>
    <tr>
      <td id="T_fdebd_row3_col0" class="data row3 col0" >$^n P_n = n!$</td>
    </tr>
    <tr>
      <td id="T_fdebd_row4_col0" class="data row4 col0" >$^n P_0 = 1$</td>
    </tr>
    <tr>
      <td id="T_fdebd_row5_col0" class="data row5 col0" >Permutations with repeated objects: $\dfrac{n!}{a!b!c!}$ where $a+b+c+... \leq n$</td>
    </tr>
    <tr>
      <td id="T_fdebd_row6_col0" class="data row6 col0" >$^nC_r = \dfrac{^n P_r}{r!}$</td>
    </tr>
    <tr>
      <td id="T_fdebd_row7_col0" class="data row7 col0" >$(^n_r) = ^n C _r = \dfrac{n!}{r!(n-r)!}$</td>
    </tr>
    <tr>
      <td id="T_fdebd_row8_col0" class="data row8 col0" >$ ^n C _0 = (^n_0) = 1 $</td>
    </tr>
    <tr>
      <td id="T_fdebd_row9_col0" class="data row9 col0" >$ ^n C _n = (^n_n) = 1 $</td>
    </tr>
    <tr>
      <td id="T_fdebd_row10_col0" class="data row10 col0" >$ ^n C _r = ^nC_{n-r} $</td>
    </tr>
    <tr>
      <td id="T_fdebd_row11_col0" class="data row11 col0" >$ (x+a)^n = x^n + (^n_1)x^{n-1}a+...+(^n_r)x^{n-r}a^r+...a^n    $</td>
    </tr>
    <tr>
      <td id="T_fdebd_row12_col0" class="data row12 col0" >$ (x+a)^n = (^n_0)x^n + (^n_1)x^{n-1}a + (^n_2)x^{n-2}a^2 + (^n_3)x^{n-3}a^3+...+(^n_k)x^{n-k}a^k+...+(^n_n)a^n $</td>
    </tr>
    <tr>
      <td id="T_fdebd_row13_col0" class="data row13 col0" >$ ^n C _k = ^{n-1}C_{k-1} + ^{n-1}C_k $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_f1aaf th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f1aaf td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_f1aaf_row0_col0, #T_f1aaf_row1_col0, #T_f1aaf_row3_col0, #T_f1aaf_row4_col0, #T_f1aaf_row5_col0, #T_f1aaf_row6_col0, #T_f1aaf_row8_col0, #T_f1aaf_row9_col0, #T_f1aaf_row10_col0, #T_f1aaf_row12_col0, #T_f1aaf_row13_col0 {
  background-color: rgba(0,0,0,0);
}
#T_f1aaf_row2_col0, #T_f1aaf_row7_col0, #T_f1aaf_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_f1aaf">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f1aaf_row0_col0" class="data row0 col0" >$P(E) = \dfrac{\text{Number of ways an event can occur}}{\text{Total number of possible outcomes}}$</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row1_col0" class="data row1 col0" >$^n P_r = \dfrac{n!}{(n-r)!}$</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row2_col0" class="data row2 col0" >$0! = 1$</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row3_col0" class="data row3 col0" >$^n P_n = n!$</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row4_col0" class="data row4 col0" >$^n P_0 = 1$</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row5_col0" class="data row5 col0" >Permutations with repeated objects: $\dfrac{n!}{a!b!c!}$ where $a+b+c+... \leq n$</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row6_col0" class="data row6 col0" >$^nC_r = \dfrac{^n P_r}{r!}$</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row7_col0" class="data row7 col0" >$(^n_r) = ^n C _r = \dfrac{n!}{r!(n-r)!}$</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row8_col0" class="data row8 col0" >$ ^n C _0 = (^n_0) = 1 $</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row9_col0" class="data row9 col0" >$ ^n C _n = (^n_n) = 1 $</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row10_col0" class="data row10 col0" >$ ^n C _r = ^nC_{n-r} $</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row11_col0" class="data row11 col0" >$ (x+a)^n = x^n + (^n_1)x^{n-1}a+...+(^n_r)x^{n-r}a^r+...a^n    $</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row12_col0" class="data row12 col0" >$ (x+a)^n = (^n_0)x^n + (^n_1)x^{n-1}a + (^n_2)x^{n-2}a^2 + (^n_3)x^{n-3}a^3+...+(^n_k)x^{n-k}a^k+...+(^n_n)a^n $</td>
    </tr>
    <tr>
      <td id="T_f1aaf_row13_col0" class="data row13 col0" >$ ^n C _k = ^{n-1}C_{k-1} + ^{n-1}C_k $</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}