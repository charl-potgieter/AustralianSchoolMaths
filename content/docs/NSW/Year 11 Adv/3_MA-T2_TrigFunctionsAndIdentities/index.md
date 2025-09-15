---
weight: 3
title: 'Trigonometric Functions and Identities'
---

## Trigonometric Functions and Identities

###   Concepts 

 - identity


###   Notes 


**Reciprocal trigonometric functions**
Refer formulas below for cosececant (cosec or csc), secant(sec) and cotangent(cot).

Note how $\cot A = \frac{\cos A}{\sin A}, \sin A \ne 0$, which is effectively $\frac{\text{adjacent}}{\text{opposite}}$ **not** $\frac{1}{\tan A}$.  This is important as tan A is undefined at odd multiples of $\frac{\pi}{2}$ while cot A is zero.  This concept must also be understood when graphing cot A given that cot A has different assymptotes to tan A.


**Pythagorean identities**
<br>
An identity is true for all values of the variable, as opposed to an equation which is only true for a certain number(s).
 - $\cos^2 x+\sin^2 x = 1$
 - $1+\tan^2 x = \sec^2 x$
 - $\cot^2 x+1 = \text{cosec }^2 x$

Note only the first identity appears on the formula sheet.  As alternative to memorising the 2nd and 3rd identity above they can be derived by dividing the first indentity by $\cos^2 x$ and $sin^2 x$ respectively.

**Complementary angles**
<br>
Complementary angles add up to 90 degrees (vs supsupplementary angles which add up to 180 degrees) <br>
Formulas such as $\sin \theta = \cos (90^{\circ} - \theta)$ are included in formulas below. <br>

As an alternative to memorising the complementary angle identities can be derived from a triangle such as below.  Worthwhile memorising the sin and cos related formulas at a minimum though.

<!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T2_ComplementaryAngles.jpg" />


**y=cosec(x)**
 - domain = $(-\infty , \infty )$, except for multiples of $\pi$
 - range = $(-\infty , -1] \cup  [1, \infty) $
 - It is an odd function, -f(x) = f(-x)

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T2_cosec.jpg" />


**y=sec(x)**
 - domain = $(-\infty , \infty)$, except for odd multiples of $\frac{\pi}{2}$
 - range = $(-\infty , -1] \cup  [1, \infty) $
 - It is an even function, f(x) = f(-x)

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T2_sec.jpg" />


**y=cot(x)**
 - domain = $(-\infty , \infty )$, except for multiples of $\pi$ (asymptotes exist at these x-values)
 - range = $(-\infty , \infty )$
 - It is an odd function, f(x) = f(-x)

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T2_cot.jpg" />

When solving trigonometric expressions within a domain remember that domain
refers to the domain of the x values, therefore if solving something like
$\sin 2x = \frac{1}{2}$ for a range of $[0^\circ, 360^\circ]$ solutions first need to
be found for $2x$ within the range of $[0^\circ, 720^\circ]$

### Formulas
{{< tabs "tab2b44b809099ca740" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONE2b44b809099ca740 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONE2b44b809099ca740 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONE2b44b809099ca740">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONE2b44b809099ca740_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEET2b44b809099ca740 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEET2b44b809099ca740 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEET2b44b809099ca740_row0_col0, #T_FORMULA_SHEET2b44b809099ca740_row1_col0, #T_FORMULA_SHEET2b44b809099ca740_row2_col0, #T_FORMULA_SHEET2b44b809099ca740_row3_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_FORMULA_SHEET2b44b809099ca740_row4_col0, #T_FORMULA_SHEET2b44b809099ca740_row5_col0, #T_FORMULA_SHEET2b44b809099ca740_row6_col0, #T_FORMULA_SHEET2b44b809099ca740_row7_col0, #T_FORMULA_SHEET2b44b809099ca740_row8_col0, #T_FORMULA_SHEET2b44b809099ca740_row9_col0, #T_FORMULA_SHEET2b44b809099ca740_row10_col0, #T_FORMULA_SHEET2b44b809099ca740_row11_col0, #T_FORMULA_SHEET2b44b809099ca740_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_FORMULA_SHEET2b44b809099ca740">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proof Required" >}}

<style type="text/css">
#T_PROOF_REQUIRED2b44b809099ca740 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_PROOF_REQUIRED2b44b809099ca740 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_PROOF_REQUIRED2b44b809099ca740_row0_col0, #T_PROOF_REQUIRED2b44b809099ca740_row1_col0, #T_PROOF_REQUIRED2b44b809099ca740_row2_col0, #T_PROOF_REQUIRED2b44b809099ca740_row6_col0, #T_PROOF_REQUIRED2b44b809099ca740_row7_col0, #T_PROOF_REQUIRED2b44b809099ca740_row8_col0, #T_PROOF_REQUIRED2b44b809099ca740_row9_col0, #T_PROOF_REQUIRED2b44b809099ca740_row10_col0, #T_PROOF_REQUIRED2b44b809099ca740_row11_col0, #T_PROOF_REQUIRED2b44b809099ca740_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_PROOF_REQUIRED2b44b809099ca740_row3_col0, #T_PROOF_REQUIRED2b44b809099ca740_row4_col0, #T_PROOF_REQUIRED2b44b809099ca740_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_PROOF_REQUIRED2b44b809099ca740">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
