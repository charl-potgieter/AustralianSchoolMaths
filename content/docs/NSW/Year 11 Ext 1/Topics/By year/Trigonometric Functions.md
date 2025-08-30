---
weight: 2
---

## Inverse Trigonometric Functions
<br>

###   Concepts 




###   Notes 

The graph of an inverse function is a reflection of the original function in the line y=x.  (the y-value and x-values of the original graph are switched to obtain the inverse graph)

The domain of the original function needs to be restricted before converting into the inverse fucntion to ensure that the result is a function, that is one value of y for each value of x.  This means that a horizontal line can cross the original function at only one point so that the inverse funciton passes a similar test with a vertical line.

The domain of the orignal function becomes the range of the inverse and vice-versa.

**arcsin**
 - $y=sin^{-1}(x)$
 - domain = [-1,1]
 - range = $[-\frac{\pi}{2}, \frac{\pi}{2}]$
 - Note no arrows at end of grpah as range is finite
 - It is an odd function, -f(x) = f(-x)

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/ME_T1_Arcsin.jpg" />

**arccos**
 - $y=cos^{-1}(x)$
 - domain = [-1,1]
 - range = $[0, \pi]$
 - Note no arrows at end of grpah as range is finite
 - It is neither odd nor even
 - The y-intercept of arccos is the x-intercept of cos = $\frac{\pi}{2}$

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/ME_T1_Arccos.jpg" />

**arctan**
 - $y=tan^{-1}(x)$
 - domain = $(-\infty , \infty )$
 - range = $(-\frac{\pi}{2} , \frac{\pi}{2})$
 - infinite range, therefore arrows at end of graph
 - It is an odd function, -f(x) = f(-x)

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/ME_T1_Arctan.jpg" />


<br>

Included in the formulas below requiring proof are the below 2 formulas.  Note that this reflects the fact that they are odd functions.
 - $\sin^{-1}(-x) = -\sin^{-1}x $
 - $\tan^{-1}(-x) = -\tan^{-1}x $





<BR><BR>



<br>


### Formulas
<br>
{{< tabs "2c47d067" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_standard_996d4055a963f5d4 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_standard_996d4055a963f5d4 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_standard_996d4055a963f5d4">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row0_col0" class="data row0 col0" >$\sin(\sin^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row1_col0" class="data row1 col0" >$\sin^{-1}(\sin x) = x \text{, for } -\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row2_col0" class="data row2 col0" >$\cos(\cos^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row3_col0" class="data row3 col0" >$\cos^{-1}(\cos x) = x \text{, for } 0 \le x \le \pi$</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row4_col0" class="data row4 col0" >$\tan(\tan^{-1} x) = x \text{, for } -\infty < x < \infty$</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row5_col0" class="data row5 col0" >$\tan^{-1}(\tan x) = x \text{, for } -\dfrac{\pi}{2} < x < \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row6_col0" class="data row6 col0" >$\sin^{-1}(-x) = -\sin^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row7_col0" class="data row7 col0" >$\cos^{-1}(-x) = \pi -\cos^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row8_col0" class="data row8 col0" >$\tan^{-1}(-x) = -\tan^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_standard_996d4055a963f5d4_row9_col0" class="data row9 col0" >$\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_proof_required_fe942a24f10ee5f0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_proof_required_fe942a24f10ee5f0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_proof_required_fe942a24f10ee5f0_row0_col0, #T_proof_required_fe942a24f10ee5f0_row1_col0, #T_proof_required_fe942a24f10ee5f0_row2_col0, #T_proof_required_fe942a24f10ee5f0_row3_col0, #T_proof_required_fe942a24f10ee5f0_row4_col0, #T_proof_required_fe942a24f10ee5f0_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_proof_required_fe942a24f10ee5f0_row6_col0, #T_proof_required_fe942a24f10ee5f0_row7_col0, #T_proof_required_fe942a24f10ee5f0_row8_col0, #T_proof_required_fe942a24f10ee5f0_row9_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_proof_required_fe942a24f10ee5f0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row0_col0" class="data row0 col0" >$\sin(\sin^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row1_col0" class="data row1 col0" >$\sin^{-1}(\sin x) = x \text{, for } -\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row2_col0" class="data row2 col0" >$\cos(\cos^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row3_col0" class="data row3 col0" >$\cos^{-1}(\cos x) = x \text{, for } 0 \le x \le \pi$</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row4_col0" class="data row4 col0" >$\tan(\tan^{-1} x) = x \text{, for } -\infty < x < \infty$</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row5_col0" class="data row5 col0" >$\tan^{-1}(\tan x) = x \text{, for } -\dfrac{\pi}{2} < x < \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row6_col0" class="data row6 col0" >$\sin^{-1}(-x) = -\sin^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row7_col0" class="data row7 col0" >$\cos^{-1}(-x) = \pi -\cos^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row8_col0" class="data row8 col0" >$\tan^{-1}(-x) = -\tan^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_proof_required_fe942a24f10ee5f0_row9_col0" class="data row9 col0" >$\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## Further Trigonometric Identities
<br>

###   Notes 

**Sum and difference expansions and double angles** <br>
The proofs of the sum and difference of angles such as $\sin(A+B)$ and $\tan(A-B)$ and following on that the double angles such as $\sin 2A$  etc all flow from the proof of $cos(A-B)$ which is proved via the unit circle and the cosine rule.

**t-formulas**<br>
The t-formulas express sin A, cos A, tan A in terms of t, where $t=\tan \frac{A}{2}$

Uses
 - a fraction in relevant format in terms of tan(the right hand side of a t-formula equation) can be converted into a simple sin, cos or tan function.
 - t-formulas can be utilised in integration (Year 12 Ext 2)

**Trigonometric products**
 - such as $\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$

 - They are simple to prove by expanding the right hand side of the equation using the sum and difference expansions.
 
 - Note that the below 2 equations on the formula sheet are essentially the same, given the last portion of the second equation could be rewritten as  $+\sin(B-A)$.
    - $\sin A \cos B = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$
    - $\cos A \sin B = \frac{1}{2}[\sin(A+B) - \sin(A-B)]$
 
<BR><BR>



<br>


### Formulas
<br>
{{< tabs "a1c3a337" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_standard_ba8fdd11758eeb0b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_standard_ba8fdd11758eeb0b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_standard_ba8fdd11758eeb0b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_standard_ba8fdd11758eeb0b_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_formula_sheet_77c88d24d5951dbb th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_formula_sheet_77c88d24d5951dbb td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_formula_sheet_77c88d24d5951dbb_row0_col0, #T_formula_sheet_77c88d24d5951dbb_row2_col0, #T_formula_sheet_77c88d24d5951dbb_row4_col0, #T_formula_sheet_77c88d24d5951dbb_row11_col0, #T_formula_sheet_77c88d24d5951dbb_row12_col0, #T_formula_sheet_77c88d24d5951dbb_row13_col0, #T_formula_sheet_77c88d24d5951dbb_row14_col0, #T_formula_sheet_77c88d24d5951dbb_row15_col0, #T_formula_sheet_77c88d24d5951dbb_row16_col0, #T_formula_sheet_77c88d24d5951dbb_row17_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_formula_sheet_77c88d24d5951dbb_row1_col0, #T_formula_sheet_77c88d24d5951dbb_row3_col0, #T_formula_sheet_77c88d24d5951dbb_row5_col0, #T_formula_sheet_77c88d24d5951dbb_row6_col0, #T_formula_sheet_77c88d24d5951dbb_row7_col0, #T_formula_sheet_77c88d24d5951dbb_row8_col0, #T_formula_sheet_77c88d24d5951dbb_row9_col0, #T_formula_sheet_77c88d24d5951dbb_row10_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_formula_sheet_77c88d24d5951dbb">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_77c88d24d5951dbb_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_proof_required_0f6ca0f8c050b896 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_proof_required_0f6ca0f8c050b896 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_proof_required_0f6ca0f8c050b896_row0_col0, #T_proof_required_0f6ca0f8c050b896_row1_col0, #T_proof_required_0f6ca0f8c050b896_row2_col0, #T_proof_required_0f6ca0f8c050b896_row3_col0, #T_proof_required_0f6ca0f8c050b896_row4_col0, #T_proof_required_0f6ca0f8c050b896_row5_col0, #T_proof_required_0f6ca0f8c050b896_row6_col0, #T_proof_required_0f6ca0f8c050b896_row7_col0, #T_proof_required_0f6ca0f8c050b896_row8_col0, #T_proof_required_0f6ca0f8c050b896_row9_col0, #T_proof_required_0f6ca0f8c050b896_row10_col0, #T_proof_required_0f6ca0f8c050b896_row11_col0, #T_proof_required_0f6ca0f8c050b896_row12_col0, #T_proof_required_0f6ca0f8c050b896_row13_col0, #T_proof_required_0f6ca0f8c050b896_row14_col0, #T_proof_required_0f6ca0f8c050b896_row15_col0, #T_proof_required_0f6ca0f8c050b896_row16_col0, #T_proof_required_0f6ca0f8c050b896_row17_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_proof_required_0f6ca0f8c050b896">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_proof_required_0f6ca0f8c050b896_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}