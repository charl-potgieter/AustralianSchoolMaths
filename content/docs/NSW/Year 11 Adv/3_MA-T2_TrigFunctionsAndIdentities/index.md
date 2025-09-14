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
      <td id="T_NONE2b44b809099ca740_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row0_col2" class="data row0 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row0_col3" class="data row0 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row0_col4" class="data row0 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row0_col5" class="data row0 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row0_col10" class="data row0 col10" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
      <td id="T_NONE2b44b809099ca740_row0_col11" class="data row0 col11" >True</td>
      <td id="T_NONE2b44b809099ca740_row0_col12" class="data row0 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row1_col2" class="data row1 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row1_col3" class="data row1 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row1_col4" class="data row1 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row1_col5" class="data row1 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row1_col10" class="data row1 col10" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
      <td id="T_NONE2b44b809099ca740_row1_col11" class="data row1 col11" >True</td>
      <td id="T_NONE2b44b809099ca740_row1_col12" class="data row1 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row2_col2" class="data row2 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row2_col3" class="data row2 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row2_col4" class="data row2 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row2_col5" class="data row2 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row2_col10" class="data row2 col10" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
      <td id="T_NONE2b44b809099ca740_row2_col11" class="data row2 col11" >True</td>
      <td id="T_NONE2b44b809099ca740_row2_col12" class="data row2 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row3_col2" class="data row3 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row3_col3" class="data row3 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row3_col4" class="data row3 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row3_col5" class="data row3 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row3_col10" class="data row3 col10" >$\cos^2 x+\sin^2 x = 1$</td>
      <td id="T_NONE2b44b809099ca740_row3_col11" class="data row3 col11" >True</td>
      <td id="T_NONE2b44b809099ca740_row3_col12" class="data row3 col12" >True</td>
      <td id="T_NONE2b44b809099ca740_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row4_col2" class="data row4 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row4_col3" class="data row4 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row4_col4" class="data row4 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row4_col5" class="data row4 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row4_col10" class="data row4 col10" >$1+\tan^2 x = \sec^2 x$</td>
      <td id="T_NONE2b44b809099ca740_row4_col11" class="data row4 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row4_col12" class="data row4 col12" >True</td>
      <td id="T_NONE2b44b809099ca740_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row5_col2" class="data row5 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row5_col3" class="data row5 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row5_col4" class="data row5 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row5_col5" class="data row5 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row5_col10" class="data row5 col10" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
      <td id="T_NONE2b44b809099ca740_row5_col11" class="data row5 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row5_col12" class="data row5 col12" >True</td>
      <td id="T_NONE2b44b809099ca740_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row6_col2" class="data row6 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row6_col3" class="data row6 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row6_col4" class="data row6 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row6_col5" class="data row6 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row6_col10" class="data row6 col10" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
      <td id="T_NONE2b44b809099ca740_row6_col11" class="data row6 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row6_col12" class="data row6 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row7_col2" class="data row7 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row7_col3" class="data row7 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row7_col4" class="data row7 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row7_col5" class="data row7 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row7_col10" class="data row7 col10" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
      <td id="T_NONE2b44b809099ca740_row7_col11" class="data row7 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row7_col12" class="data row7 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row8_col2" class="data row8 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row8_col3" class="data row8 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row8_col4" class="data row8 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row8_col5" class="data row8 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row8_col10" class="data row8 col10" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
      <td id="T_NONE2b44b809099ca740_row8_col11" class="data row8 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row8_col12" class="data row8 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row9_col2" class="data row9 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row9_col3" class="data row9 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row9_col4" class="data row9 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row9_col5" class="data row9 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row9_col10" class="data row9 col10" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
      <td id="T_NONE2b44b809099ca740_row9_col11" class="data row9 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row9_col12" class="data row9 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row10_col2" class="data row10 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row10_col3" class="data row10 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row10_col4" class="data row10 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row10_col5" class="data row10 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row10_col10" class="data row10 col10" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
      <td id="T_NONE2b44b809099ca740_row10_col11" class="data row10 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row10_col12" class="data row10 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row10_col13" class="data row10 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row11_col0" class="data row11 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row11_col1" class="data row11 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row11_col2" class="data row11 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row11_col3" class="data row11 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row11_col4" class="data row11 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row11_col5" class="data row11 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row11_col6" class="data row11 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row11_col7" class="data row11 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row11_col8" class="data row11 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row11_col9" class="data row11 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row11_col10" class="data row11 col10" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
      <td id="T_NONE2b44b809099ca740_row11_col11" class="data row11 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row11_col12" class="data row11 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row11_col13" class="data row11 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE2b44b809099ca740_row12_col0" class="data row12 col0" >NSW</td>
      <td id="T_NONE2b44b809099ca740_row12_col1" class="data row12 col1" >Year 11 Adv</td>
      <td id="T_NONE2b44b809099ca740_row12_col2" class="data row12 col2" >Trigonometric Functions</td>
      <td id="T_NONE2b44b809099ca740_row12_col3" class="data row12 col3" >MA-T2</td>
      <td id="T_NONE2b44b809099ca740_row12_col4" class="data row12 col4" >Trigonometric Functions and Identities</td>
      <td id="T_NONE2b44b809099ca740_row12_col5" class="data row12 col5" >Trigonometry</td>
      <td id="T_NONE2b44b809099ca740_row12_col6" class="data row12 col6" >nan</td>
      <td id="T_NONE2b44b809099ca740_row12_col7" class="data row12 col7" >nan</td>
      <td id="T_NONE2b44b809099ca740_row12_col8" class="data row12 col8" >nan</td>
      <td id="T_NONE2b44b809099ca740_row12_col9" class="data row12 col9" >nan</td>
      <td id="T_NONE2b44b809099ca740_row12_col10" class="data row12 col10" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
      <td id="T_NONE2b44b809099ca740_row12_col11" class="data row12 col11" >False</td>
      <td id="T_NONE2b44b809099ca740_row12_col12" class="data row12 col12" >False</td>
      <td id="T_NONE2b44b809099ca740_row12_col13" class="data row12 col13" >nan</td>
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
#T_FORMULA_SHEET2b44b809099ca740_row0_col0, #T_FORMULA_SHEET2b44b809099ca740_row0_col1, #T_FORMULA_SHEET2b44b809099ca740_row0_col2, #T_FORMULA_SHEET2b44b809099ca740_row0_col3, #T_FORMULA_SHEET2b44b809099ca740_row0_col4, #T_FORMULA_SHEET2b44b809099ca740_row0_col5, #T_FORMULA_SHEET2b44b809099ca740_row0_col6, #T_FORMULA_SHEET2b44b809099ca740_row0_col7, #T_FORMULA_SHEET2b44b809099ca740_row0_col8, #T_FORMULA_SHEET2b44b809099ca740_row0_col9, #T_FORMULA_SHEET2b44b809099ca740_row0_col11, #T_FORMULA_SHEET2b44b809099ca740_row0_col12, #T_FORMULA_SHEET2b44b809099ca740_row0_col13, #T_FORMULA_SHEET2b44b809099ca740_row1_col0, #T_FORMULA_SHEET2b44b809099ca740_row1_col1, #T_FORMULA_SHEET2b44b809099ca740_row1_col2, #T_FORMULA_SHEET2b44b809099ca740_row1_col3, #T_FORMULA_SHEET2b44b809099ca740_row1_col4, #T_FORMULA_SHEET2b44b809099ca740_row1_col5, #T_FORMULA_SHEET2b44b809099ca740_row1_col6, #T_FORMULA_SHEET2b44b809099ca740_row1_col7, #T_FORMULA_SHEET2b44b809099ca740_row1_col8, #T_FORMULA_SHEET2b44b809099ca740_row1_col9, #T_FORMULA_SHEET2b44b809099ca740_row1_col11, #T_FORMULA_SHEET2b44b809099ca740_row1_col12, #T_FORMULA_SHEET2b44b809099ca740_row1_col13, #T_FORMULA_SHEET2b44b809099ca740_row2_col0, #T_FORMULA_SHEET2b44b809099ca740_row2_col1, #T_FORMULA_SHEET2b44b809099ca740_row2_col2, #T_FORMULA_SHEET2b44b809099ca740_row2_col3, #T_FORMULA_SHEET2b44b809099ca740_row2_col4, #T_FORMULA_SHEET2b44b809099ca740_row2_col5, #T_FORMULA_SHEET2b44b809099ca740_row2_col6, #T_FORMULA_SHEET2b44b809099ca740_row2_col7, #T_FORMULA_SHEET2b44b809099ca740_row2_col8, #T_FORMULA_SHEET2b44b809099ca740_row2_col9, #T_FORMULA_SHEET2b44b809099ca740_row2_col11, #T_FORMULA_SHEET2b44b809099ca740_row2_col12, #T_FORMULA_SHEET2b44b809099ca740_row2_col13, #T_FORMULA_SHEET2b44b809099ca740_row3_col0, #T_FORMULA_SHEET2b44b809099ca740_row3_col1, #T_FORMULA_SHEET2b44b809099ca740_row3_col2, #T_FORMULA_SHEET2b44b809099ca740_row3_col3, #T_FORMULA_SHEET2b44b809099ca740_row3_col4, #T_FORMULA_SHEET2b44b809099ca740_row3_col5, #T_FORMULA_SHEET2b44b809099ca740_row3_col6, #T_FORMULA_SHEET2b44b809099ca740_row3_col7, #T_FORMULA_SHEET2b44b809099ca740_row3_col8, #T_FORMULA_SHEET2b44b809099ca740_row3_col9, #T_FORMULA_SHEET2b44b809099ca740_row3_col11, #T_FORMULA_SHEET2b44b809099ca740_row3_col12, #T_FORMULA_SHEET2b44b809099ca740_row3_col13, #T_FORMULA_SHEET2b44b809099ca740_row4_col0, #T_FORMULA_SHEET2b44b809099ca740_row4_col1, #T_FORMULA_SHEET2b44b809099ca740_row4_col2, #T_FORMULA_SHEET2b44b809099ca740_row4_col3, #T_FORMULA_SHEET2b44b809099ca740_row4_col4, #T_FORMULA_SHEET2b44b809099ca740_row4_col5, #T_FORMULA_SHEET2b44b809099ca740_row4_col6, #T_FORMULA_SHEET2b44b809099ca740_row4_col7, #T_FORMULA_SHEET2b44b809099ca740_row4_col8, #T_FORMULA_SHEET2b44b809099ca740_row4_col9, #T_FORMULA_SHEET2b44b809099ca740_row4_col10, #T_FORMULA_SHEET2b44b809099ca740_row4_col11, #T_FORMULA_SHEET2b44b809099ca740_row4_col12, #T_FORMULA_SHEET2b44b809099ca740_row4_col13, #T_FORMULA_SHEET2b44b809099ca740_row5_col0, #T_FORMULA_SHEET2b44b809099ca740_row5_col1, #T_FORMULA_SHEET2b44b809099ca740_row5_col2, #T_FORMULA_SHEET2b44b809099ca740_row5_col3, #T_FORMULA_SHEET2b44b809099ca740_row5_col4, #T_FORMULA_SHEET2b44b809099ca740_row5_col5, #T_FORMULA_SHEET2b44b809099ca740_row5_col6, #T_FORMULA_SHEET2b44b809099ca740_row5_col7, #T_FORMULA_SHEET2b44b809099ca740_row5_col8, #T_FORMULA_SHEET2b44b809099ca740_row5_col9, #T_FORMULA_SHEET2b44b809099ca740_row5_col10, #T_FORMULA_SHEET2b44b809099ca740_row5_col11, #T_FORMULA_SHEET2b44b809099ca740_row5_col12, #T_FORMULA_SHEET2b44b809099ca740_row5_col13, #T_FORMULA_SHEET2b44b809099ca740_row6_col0, #T_FORMULA_SHEET2b44b809099ca740_row6_col1, #T_FORMULA_SHEET2b44b809099ca740_row6_col2, #T_FORMULA_SHEET2b44b809099ca740_row6_col3, #T_FORMULA_SHEET2b44b809099ca740_row6_col4, #T_FORMULA_SHEET2b44b809099ca740_row6_col5, #T_FORMULA_SHEET2b44b809099ca740_row6_col6, #T_FORMULA_SHEET2b44b809099ca740_row6_col7, #T_FORMULA_SHEET2b44b809099ca740_row6_col8, #T_FORMULA_SHEET2b44b809099ca740_row6_col9, #T_FORMULA_SHEET2b44b809099ca740_row6_col10, #T_FORMULA_SHEET2b44b809099ca740_row6_col11, #T_FORMULA_SHEET2b44b809099ca740_row6_col12, #T_FORMULA_SHEET2b44b809099ca740_row6_col13, #T_FORMULA_SHEET2b44b809099ca740_row7_col0, #T_FORMULA_SHEET2b44b809099ca740_row7_col1, #T_FORMULA_SHEET2b44b809099ca740_row7_col2, #T_FORMULA_SHEET2b44b809099ca740_row7_col3, #T_FORMULA_SHEET2b44b809099ca740_row7_col4, #T_FORMULA_SHEET2b44b809099ca740_row7_col5, #T_FORMULA_SHEET2b44b809099ca740_row7_col6, #T_FORMULA_SHEET2b44b809099ca740_row7_col7, #T_FORMULA_SHEET2b44b809099ca740_row7_col8, #T_FORMULA_SHEET2b44b809099ca740_row7_col9, #T_FORMULA_SHEET2b44b809099ca740_row7_col10, #T_FORMULA_SHEET2b44b809099ca740_row7_col11, #T_FORMULA_SHEET2b44b809099ca740_row7_col12, #T_FORMULA_SHEET2b44b809099ca740_row7_col13, #T_FORMULA_SHEET2b44b809099ca740_row8_col0, #T_FORMULA_SHEET2b44b809099ca740_row8_col1, #T_FORMULA_SHEET2b44b809099ca740_row8_col2, #T_FORMULA_SHEET2b44b809099ca740_row8_col3, #T_FORMULA_SHEET2b44b809099ca740_row8_col4, #T_FORMULA_SHEET2b44b809099ca740_row8_col5, #T_FORMULA_SHEET2b44b809099ca740_row8_col6, #T_FORMULA_SHEET2b44b809099ca740_row8_col7, #T_FORMULA_SHEET2b44b809099ca740_row8_col8, #T_FORMULA_SHEET2b44b809099ca740_row8_col9, #T_FORMULA_SHEET2b44b809099ca740_row8_col10, #T_FORMULA_SHEET2b44b809099ca740_row8_col11, #T_FORMULA_SHEET2b44b809099ca740_row8_col12, #T_FORMULA_SHEET2b44b809099ca740_row8_col13, #T_FORMULA_SHEET2b44b809099ca740_row9_col0, #T_FORMULA_SHEET2b44b809099ca740_row9_col1, #T_FORMULA_SHEET2b44b809099ca740_row9_col2, #T_FORMULA_SHEET2b44b809099ca740_row9_col3, #T_FORMULA_SHEET2b44b809099ca740_row9_col4, #T_FORMULA_SHEET2b44b809099ca740_row9_col5, #T_FORMULA_SHEET2b44b809099ca740_row9_col6, #T_FORMULA_SHEET2b44b809099ca740_row9_col7, #T_FORMULA_SHEET2b44b809099ca740_row9_col8, #T_FORMULA_SHEET2b44b809099ca740_row9_col9, #T_FORMULA_SHEET2b44b809099ca740_row9_col10, #T_FORMULA_SHEET2b44b809099ca740_row9_col11, #T_FORMULA_SHEET2b44b809099ca740_row9_col12, #T_FORMULA_SHEET2b44b809099ca740_row9_col13, #T_FORMULA_SHEET2b44b809099ca740_row10_col0, #T_FORMULA_SHEET2b44b809099ca740_row10_col1, #T_FORMULA_SHEET2b44b809099ca740_row10_col2, #T_FORMULA_SHEET2b44b809099ca740_row10_col3, #T_FORMULA_SHEET2b44b809099ca740_row10_col4, #T_FORMULA_SHEET2b44b809099ca740_row10_col5, #T_FORMULA_SHEET2b44b809099ca740_row10_col6, #T_FORMULA_SHEET2b44b809099ca740_row10_col7, #T_FORMULA_SHEET2b44b809099ca740_row10_col8, #T_FORMULA_SHEET2b44b809099ca740_row10_col9, #T_FORMULA_SHEET2b44b809099ca740_row10_col10, #T_FORMULA_SHEET2b44b809099ca740_row10_col11, #T_FORMULA_SHEET2b44b809099ca740_row10_col12, #T_FORMULA_SHEET2b44b809099ca740_row10_col13, #T_FORMULA_SHEET2b44b809099ca740_row11_col0, #T_FORMULA_SHEET2b44b809099ca740_row11_col1, #T_FORMULA_SHEET2b44b809099ca740_row11_col2, #T_FORMULA_SHEET2b44b809099ca740_row11_col3, #T_FORMULA_SHEET2b44b809099ca740_row11_col4, #T_FORMULA_SHEET2b44b809099ca740_row11_col5, #T_FORMULA_SHEET2b44b809099ca740_row11_col6, #T_FORMULA_SHEET2b44b809099ca740_row11_col7, #T_FORMULA_SHEET2b44b809099ca740_row11_col8, #T_FORMULA_SHEET2b44b809099ca740_row11_col9, #T_FORMULA_SHEET2b44b809099ca740_row11_col10, #T_FORMULA_SHEET2b44b809099ca740_row11_col11, #T_FORMULA_SHEET2b44b809099ca740_row11_col12, #T_FORMULA_SHEET2b44b809099ca740_row11_col13, #T_FORMULA_SHEET2b44b809099ca740_row12_col0, #T_FORMULA_SHEET2b44b809099ca740_row12_col1, #T_FORMULA_SHEET2b44b809099ca740_row12_col2, #T_FORMULA_SHEET2b44b809099ca740_row12_col3, #T_FORMULA_SHEET2b44b809099ca740_row12_col4, #T_FORMULA_SHEET2b44b809099ca740_row12_col5, #T_FORMULA_SHEET2b44b809099ca740_row12_col6, #T_FORMULA_SHEET2b44b809099ca740_row12_col7, #T_FORMULA_SHEET2b44b809099ca740_row12_col8, #T_FORMULA_SHEET2b44b809099ca740_row12_col9, #T_FORMULA_SHEET2b44b809099ca740_row12_col10, #T_FORMULA_SHEET2b44b809099ca740_row12_col11, #T_FORMULA_SHEET2b44b809099ca740_row12_col12, #T_FORMULA_SHEET2b44b809099ca740_row12_col13 {
  background-color: rgba(0,0,0,0);
}
#T_FORMULA_SHEET2b44b809099ca740_row0_col10, #T_FORMULA_SHEET2b44b809099ca740_row1_col10, #T_FORMULA_SHEET2b44b809099ca740_row2_col10, #T_FORMULA_SHEET2b44b809099ca740_row3_col10 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_FORMULA_SHEET2b44b809099ca740">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col2" class="data row0 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col3" class="data row0 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col4" class="data row0 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col5" class="data row0 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col10" class="data row0 col10" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col11" class="data row0 col11" >True</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col12" class="data row0 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col2" class="data row1 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col3" class="data row1 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col4" class="data row1 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col5" class="data row1 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col10" class="data row1 col10" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col11" class="data row1 col11" >True</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col12" class="data row1 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col2" class="data row2 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col3" class="data row2 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col4" class="data row2 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col5" class="data row2 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col10" class="data row2 col10" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col11" class="data row2 col11" >True</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col12" class="data row2 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col2" class="data row3 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col3" class="data row3 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col4" class="data row3 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col5" class="data row3 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col10" class="data row3 col10" >$\cos^2 x+\sin^2 x = 1$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col11" class="data row3 col11" >True</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col12" class="data row3 col12" >True</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col2" class="data row4 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col3" class="data row4 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col4" class="data row4 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col5" class="data row4 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col10" class="data row4 col10" >$1+\tan^2 x = \sec^2 x$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col11" class="data row4 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col12" class="data row4 col12" >True</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col2" class="data row5 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col3" class="data row5 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col4" class="data row5 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col5" class="data row5 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col10" class="data row5 col10" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col11" class="data row5 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col12" class="data row5 col12" >True</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col2" class="data row6 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col3" class="data row6 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col4" class="data row6 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col5" class="data row6 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col10" class="data row6 col10" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col11" class="data row6 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col12" class="data row6 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col2" class="data row7 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col3" class="data row7 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col4" class="data row7 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col5" class="data row7 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col10" class="data row7 col10" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col11" class="data row7 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col12" class="data row7 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col2" class="data row8 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col3" class="data row8 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col4" class="data row8 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col5" class="data row8 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col10" class="data row8 col10" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col11" class="data row8 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col12" class="data row8 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col2" class="data row9 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col3" class="data row9 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col4" class="data row9 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col5" class="data row9 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col10" class="data row9 col10" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col11" class="data row9 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col12" class="data row9 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col2" class="data row10 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col3" class="data row10 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col4" class="data row10 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col5" class="data row10 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col10" class="data row10 col10" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col11" class="data row10 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col12" class="data row10 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row10_col13" class="data row10 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col0" class="data row11 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col1" class="data row11 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col2" class="data row11 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col3" class="data row11 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col4" class="data row11 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col5" class="data row11 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col6" class="data row11 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col7" class="data row11 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col8" class="data row11 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col9" class="data row11 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col10" class="data row11 col10" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col11" class="data row11 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col12" class="data row11 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row11_col13" class="data row11 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col0" class="data row12 col0" >NSW</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col1" class="data row12 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col2" class="data row12 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col3" class="data row12 col3" >MA-T2</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col4" class="data row12 col4" >Trigonometric Functions and Identities</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col5" class="data row12 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col6" class="data row12 col6" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col7" class="data row12 col7" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col8" class="data row12 col8" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col9" class="data row12 col9" >nan</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col10" class="data row12 col10" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col11" class="data row12 col11" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col12" class="data row12 col12" >False</td>
      <td id="T_FORMULA_SHEET2b44b809099ca740_row12_col13" class="data row12 col13" >nan</td>
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
#T_PROOF_REQUIRED2b44b809099ca740_row0_col0, #T_PROOF_REQUIRED2b44b809099ca740_row0_col1, #T_PROOF_REQUIRED2b44b809099ca740_row0_col2, #T_PROOF_REQUIRED2b44b809099ca740_row0_col3, #T_PROOF_REQUIRED2b44b809099ca740_row0_col4, #T_PROOF_REQUIRED2b44b809099ca740_row0_col5, #T_PROOF_REQUIRED2b44b809099ca740_row0_col6, #T_PROOF_REQUIRED2b44b809099ca740_row0_col7, #T_PROOF_REQUIRED2b44b809099ca740_row0_col8, #T_PROOF_REQUIRED2b44b809099ca740_row0_col9, #T_PROOF_REQUIRED2b44b809099ca740_row0_col10, #T_PROOF_REQUIRED2b44b809099ca740_row0_col11, #T_PROOF_REQUIRED2b44b809099ca740_row0_col12, #T_PROOF_REQUIRED2b44b809099ca740_row0_col13, #T_PROOF_REQUIRED2b44b809099ca740_row1_col0, #T_PROOF_REQUIRED2b44b809099ca740_row1_col1, #T_PROOF_REQUIRED2b44b809099ca740_row1_col2, #T_PROOF_REQUIRED2b44b809099ca740_row1_col3, #T_PROOF_REQUIRED2b44b809099ca740_row1_col4, #T_PROOF_REQUIRED2b44b809099ca740_row1_col5, #T_PROOF_REQUIRED2b44b809099ca740_row1_col6, #T_PROOF_REQUIRED2b44b809099ca740_row1_col7, #T_PROOF_REQUIRED2b44b809099ca740_row1_col8, #T_PROOF_REQUIRED2b44b809099ca740_row1_col9, #T_PROOF_REQUIRED2b44b809099ca740_row1_col10, #T_PROOF_REQUIRED2b44b809099ca740_row1_col11, #T_PROOF_REQUIRED2b44b809099ca740_row1_col12, #T_PROOF_REQUIRED2b44b809099ca740_row1_col13, #T_PROOF_REQUIRED2b44b809099ca740_row2_col0, #T_PROOF_REQUIRED2b44b809099ca740_row2_col1, #T_PROOF_REQUIRED2b44b809099ca740_row2_col2, #T_PROOF_REQUIRED2b44b809099ca740_row2_col3, #T_PROOF_REQUIRED2b44b809099ca740_row2_col4, #T_PROOF_REQUIRED2b44b809099ca740_row2_col5, #T_PROOF_REQUIRED2b44b809099ca740_row2_col6, #T_PROOF_REQUIRED2b44b809099ca740_row2_col7, #T_PROOF_REQUIRED2b44b809099ca740_row2_col8, #T_PROOF_REQUIRED2b44b809099ca740_row2_col9, #T_PROOF_REQUIRED2b44b809099ca740_row2_col10, #T_PROOF_REQUIRED2b44b809099ca740_row2_col11, #T_PROOF_REQUIRED2b44b809099ca740_row2_col12, #T_PROOF_REQUIRED2b44b809099ca740_row2_col13, #T_PROOF_REQUIRED2b44b809099ca740_row3_col0, #T_PROOF_REQUIRED2b44b809099ca740_row3_col1, #T_PROOF_REQUIRED2b44b809099ca740_row3_col2, #T_PROOF_REQUIRED2b44b809099ca740_row3_col3, #T_PROOF_REQUIRED2b44b809099ca740_row3_col4, #T_PROOF_REQUIRED2b44b809099ca740_row3_col5, #T_PROOF_REQUIRED2b44b809099ca740_row3_col6, #T_PROOF_REQUIRED2b44b809099ca740_row3_col7, #T_PROOF_REQUIRED2b44b809099ca740_row3_col8, #T_PROOF_REQUIRED2b44b809099ca740_row3_col9, #T_PROOF_REQUIRED2b44b809099ca740_row3_col11, #T_PROOF_REQUIRED2b44b809099ca740_row3_col12, #T_PROOF_REQUIRED2b44b809099ca740_row3_col13, #T_PROOF_REQUIRED2b44b809099ca740_row4_col0, #T_PROOF_REQUIRED2b44b809099ca740_row4_col1, #T_PROOF_REQUIRED2b44b809099ca740_row4_col2, #T_PROOF_REQUIRED2b44b809099ca740_row4_col3, #T_PROOF_REQUIRED2b44b809099ca740_row4_col4, #T_PROOF_REQUIRED2b44b809099ca740_row4_col5, #T_PROOF_REQUIRED2b44b809099ca740_row4_col6, #T_PROOF_REQUIRED2b44b809099ca740_row4_col7, #T_PROOF_REQUIRED2b44b809099ca740_row4_col8, #T_PROOF_REQUIRED2b44b809099ca740_row4_col9, #T_PROOF_REQUIRED2b44b809099ca740_row4_col11, #T_PROOF_REQUIRED2b44b809099ca740_row4_col12, #T_PROOF_REQUIRED2b44b809099ca740_row4_col13, #T_PROOF_REQUIRED2b44b809099ca740_row5_col0, #T_PROOF_REQUIRED2b44b809099ca740_row5_col1, #T_PROOF_REQUIRED2b44b809099ca740_row5_col2, #T_PROOF_REQUIRED2b44b809099ca740_row5_col3, #T_PROOF_REQUIRED2b44b809099ca740_row5_col4, #T_PROOF_REQUIRED2b44b809099ca740_row5_col5, #T_PROOF_REQUIRED2b44b809099ca740_row5_col6, #T_PROOF_REQUIRED2b44b809099ca740_row5_col7, #T_PROOF_REQUIRED2b44b809099ca740_row5_col8, #T_PROOF_REQUIRED2b44b809099ca740_row5_col9, #T_PROOF_REQUIRED2b44b809099ca740_row5_col11, #T_PROOF_REQUIRED2b44b809099ca740_row5_col12, #T_PROOF_REQUIRED2b44b809099ca740_row5_col13, #T_PROOF_REQUIRED2b44b809099ca740_row6_col0, #T_PROOF_REQUIRED2b44b809099ca740_row6_col1, #T_PROOF_REQUIRED2b44b809099ca740_row6_col2, #T_PROOF_REQUIRED2b44b809099ca740_row6_col3, #T_PROOF_REQUIRED2b44b809099ca740_row6_col4, #T_PROOF_REQUIRED2b44b809099ca740_row6_col5, #T_PROOF_REQUIRED2b44b809099ca740_row6_col6, #T_PROOF_REQUIRED2b44b809099ca740_row6_col7, #T_PROOF_REQUIRED2b44b809099ca740_row6_col8, #T_PROOF_REQUIRED2b44b809099ca740_row6_col9, #T_PROOF_REQUIRED2b44b809099ca740_row6_col10, #T_PROOF_REQUIRED2b44b809099ca740_row6_col11, #T_PROOF_REQUIRED2b44b809099ca740_row6_col12, #T_PROOF_REQUIRED2b44b809099ca740_row6_col13, #T_PROOF_REQUIRED2b44b809099ca740_row7_col0, #T_PROOF_REQUIRED2b44b809099ca740_row7_col1, #T_PROOF_REQUIRED2b44b809099ca740_row7_col2, #T_PROOF_REQUIRED2b44b809099ca740_row7_col3, #T_PROOF_REQUIRED2b44b809099ca740_row7_col4, #T_PROOF_REQUIRED2b44b809099ca740_row7_col5, #T_PROOF_REQUIRED2b44b809099ca740_row7_col6, #T_PROOF_REQUIRED2b44b809099ca740_row7_col7, #T_PROOF_REQUIRED2b44b809099ca740_row7_col8, #T_PROOF_REQUIRED2b44b809099ca740_row7_col9, #T_PROOF_REQUIRED2b44b809099ca740_row7_col10, #T_PROOF_REQUIRED2b44b809099ca740_row7_col11, #T_PROOF_REQUIRED2b44b809099ca740_row7_col12, #T_PROOF_REQUIRED2b44b809099ca740_row7_col13, #T_PROOF_REQUIRED2b44b809099ca740_row8_col0, #T_PROOF_REQUIRED2b44b809099ca740_row8_col1, #T_PROOF_REQUIRED2b44b809099ca740_row8_col2, #T_PROOF_REQUIRED2b44b809099ca740_row8_col3, #T_PROOF_REQUIRED2b44b809099ca740_row8_col4, #T_PROOF_REQUIRED2b44b809099ca740_row8_col5, #T_PROOF_REQUIRED2b44b809099ca740_row8_col6, #T_PROOF_REQUIRED2b44b809099ca740_row8_col7, #T_PROOF_REQUIRED2b44b809099ca740_row8_col8, #T_PROOF_REQUIRED2b44b809099ca740_row8_col9, #T_PROOF_REQUIRED2b44b809099ca740_row8_col10, #T_PROOF_REQUIRED2b44b809099ca740_row8_col11, #T_PROOF_REQUIRED2b44b809099ca740_row8_col12, #T_PROOF_REQUIRED2b44b809099ca740_row8_col13, #T_PROOF_REQUIRED2b44b809099ca740_row9_col0, #T_PROOF_REQUIRED2b44b809099ca740_row9_col1, #T_PROOF_REQUIRED2b44b809099ca740_row9_col2, #T_PROOF_REQUIRED2b44b809099ca740_row9_col3, #T_PROOF_REQUIRED2b44b809099ca740_row9_col4, #T_PROOF_REQUIRED2b44b809099ca740_row9_col5, #T_PROOF_REQUIRED2b44b809099ca740_row9_col6, #T_PROOF_REQUIRED2b44b809099ca740_row9_col7, #T_PROOF_REQUIRED2b44b809099ca740_row9_col8, #T_PROOF_REQUIRED2b44b809099ca740_row9_col9, #T_PROOF_REQUIRED2b44b809099ca740_row9_col10, #T_PROOF_REQUIRED2b44b809099ca740_row9_col11, #T_PROOF_REQUIRED2b44b809099ca740_row9_col12, #T_PROOF_REQUIRED2b44b809099ca740_row9_col13, #T_PROOF_REQUIRED2b44b809099ca740_row10_col0, #T_PROOF_REQUIRED2b44b809099ca740_row10_col1, #T_PROOF_REQUIRED2b44b809099ca740_row10_col2, #T_PROOF_REQUIRED2b44b809099ca740_row10_col3, #T_PROOF_REQUIRED2b44b809099ca740_row10_col4, #T_PROOF_REQUIRED2b44b809099ca740_row10_col5, #T_PROOF_REQUIRED2b44b809099ca740_row10_col6, #T_PROOF_REQUIRED2b44b809099ca740_row10_col7, #T_PROOF_REQUIRED2b44b809099ca740_row10_col8, #T_PROOF_REQUIRED2b44b809099ca740_row10_col9, #T_PROOF_REQUIRED2b44b809099ca740_row10_col10, #T_PROOF_REQUIRED2b44b809099ca740_row10_col11, #T_PROOF_REQUIRED2b44b809099ca740_row10_col12, #T_PROOF_REQUIRED2b44b809099ca740_row10_col13, #T_PROOF_REQUIRED2b44b809099ca740_row11_col0, #T_PROOF_REQUIRED2b44b809099ca740_row11_col1, #T_PROOF_REQUIRED2b44b809099ca740_row11_col2, #T_PROOF_REQUIRED2b44b809099ca740_row11_col3, #T_PROOF_REQUIRED2b44b809099ca740_row11_col4, #T_PROOF_REQUIRED2b44b809099ca740_row11_col5, #T_PROOF_REQUIRED2b44b809099ca740_row11_col6, #T_PROOF_REQUIRED2b44b809099ca740_row11_col7, #T_PROOF_REQUIRED2b44b809099ca740_row11_col8, #T_PROOF_REQUIRED2b44b809099ca740_row11_col9, #T_PROOF_REQUIRED2b44b809099ca740_row11_col10, #T_PROOF_REQUIRED2b44b809099ca740_row11_col11, #T_PROOF_REQUIRED2b44b809099ca740_row11_col12, #T_PROOF_REQUIRED2b44b809099ca740_row11_col13, #T_PROOF_REQUIRED2b44b809099ca740_row12_col0, #T_PROOF_REQUIRED2b44b809099ca740_row12_col1, #T_PROOF_REQUIRED2b44b809099ca740_row12_col2, #T_PROOF_REQUIRED2b44b809099ca740_row12_col3, #T_PROOF_REQUIRED2b44b809099ca740_row12_col4, #T_PROOF_REQUIRED2b44b809099ca740_row12_col5, #T_PROOF_REQUIRED2b44b809099ca740_row12_col6, #T_PROOF_REQUIRED2b44b809099ca740_row12_col7, #T_PROOF_REQUIRED2b44b809099ca740_row12_col8, #T_PROOF_REQUIRED2b44b809099ca740_row12_col9, #T_PROOF_REQUIRED2b44b809099ca740_row12_col10, #T_PROOF_REQUIRED2b44b809099ca740_row12_col11, #T_PROOF_REQUIRED2b44b809099ca740_row12_col12, #T_PROOF_REQUIRED2b44b809099ca740_row12_col13 {
  background-color: rgba(0,0,0,0);
}
#T_PROOF_REQUIRED2b44b809099ca740_row3_col10, #T_PROOF_REQUIRED2b44b809099ca740_row4_col10, #T_PROOF_REQUIRED2b44b809099ca740_row5_col10 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_PROOF_REQUIRED2b44b809099ca740">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col2" class="data row0 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col3" class="data row0 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col4" class="data row0 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col5" class="data row0 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col10" class="data row0 col10" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col11" class="data row0 col11" >True</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col12" class="data row0 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col2" class="data row1 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col3" class="data row1 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col4" class="data row1 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col5" class="data row1 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col10" class="data row1 col10" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col11" class="data row1 col11" >True</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col12" class="data row1 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col2" class="data row2 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col3" class="data row2 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col4" class="data row2 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col5" class="data row2 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col10" class="data row2 col10" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col11" class="data row2 col11" >True</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col12" class="data row2 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col2" class="data row3 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col3" class="data row3 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col4" class="data row3 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col5" class="data row3 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col10" class="data row3 col10" >$\cos^2 x+\sin^2 x = 1$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col11" class="data row3 col11" >True</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col12" class="data row3 col12" >True</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col2" class="data row4 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col3" class="data row4 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col4" class="data row4 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col5" class="data row4 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col10" class="data row4 col10" >$1+\tan^2 x = \sec^2 x$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col11" class="data row4 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col12" class="data row4 col12" >True</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col2" class="data row5 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col3" class="data row5 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col4" class="data row5 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col5" class="data row5 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col10" class="data row5 col10" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col11" class="data row5 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col12" class="data row5 col12" >True</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col2" class="data row6 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col3" class="data row6 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col4" class="data row6 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col5" class="data row6 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col10" class="data row6 col10" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col11" class="data row6 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col12" class="data row6 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col2" class="data row7 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col3" class="data row7 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col4" class="data row7 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col5" class="data row7 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col10" class="data row7 col10" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col11" class="data row7 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col12" class="data row7 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col2" class="data row8 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col3" class="data row8 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col4" class="data row8 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col5" class="data row8 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col10" class="data row8 col10" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col11" class="data row8 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col12" class="data row8 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col2" class="data row9 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col3" class="data row9 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col4" class="data row9 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col5" class="data row9 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col10" class="data row9 col10" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col11" class="data row9 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col12" class="data row9 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col2" class="data row10 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col3" class="data row10 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col4" class="data row10 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col5" class="data row10 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col10" class="data row10 col10" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col11" class="data row10 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col12" class="data row10 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row10_col13" class="data row10 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col0" class="data row11 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col1" class="data row11 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col2" class="data row11 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col3" class="data row11 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col4" class="data row11 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col5" class="data row11 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col6" class="data row11 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col7" class="data row11 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col8" class="data row11 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col9" class="data row11 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col10" class="data row11 col10" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col11" class="data row11 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col12" class="data row11 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row11_col13" class="data row11 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col0" class="data row12 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col1" class="data row12 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col2" class="data row12 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col3" class="data row12 col3" >MA-T2</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col4" class="data row12 col4" >Trigonometric Functions and Identities</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col5" class="data row12 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col6" class="data row12 col6" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col7" class="data row12 col7" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col8" class="data row12 col8" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col9" class="data row12 col9" >nan</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col10" class="data row12 col10" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col11" class="data row12 col11" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col12" class="data row12 col12" >False</td>
      <td id="T_PROOF_REQUIRED2b44b809099ca740_row12_col13" class="data row12 col13" >nan</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
