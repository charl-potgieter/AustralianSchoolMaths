---
weight: 2
---

## <span style="color:RGB(0,32,96"> Trigonometry and Measure of Angles </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - angle of elevation
 - angle of depression
 - true bearing
 - compass bearing
 - amplitude
 - period
 - phase


### <span style="color:RGB(139,69,19)">  Notes </span>


#### Trigonometry

Naming convention uses upper case letter for angle and equivalent lower case letter for the side opposite the angle.

Use sine rule
 - to find a side given 2 angles and one side (AAS)
 - To find an angle given 2 sides and a non included angle (SSA)
     - This is the ambiguous case (there are 2 possible solutions, one accute and one obtuse angle)
     - SSA is not a proof of congruence given the potential for an ambiguous solution
     - In questions check that the obtuse solution does not result in the known angle + the calculated angle exceding 180 degrees.  In this case the obtuse angle is not a valid solution

Use the cosine rule
 - Find a side given 2 sides and an included angle (SAS)
 - Find and angle given 2 sides (SSS)
 
Degrees, minutes and seconds 
- 60 minutes = 1 degree
- 60 seconds = 1 minute
- Be careful rounding minutes or seconds.  Round minutes over 30 to the next degree up etc.
- Be able to convert between degrees (as decimal) and degrees+minutes+seconds on a calculator

Trig ratios are positive in "**A**ll **S**tations **T**o **C**entral" that is
 - **A**ll are positive in quadrant 1
 - **S**in is positive in quadrant 2
 - **T**an is positive in quadrant 3
 - **C**os is positive in quadrant 4

#### Radians  

Understand the reason why $  \pi \text{ radians}  = 180^{\circ}$ based on
 - the definition of 1 radian being the angle subtended by an arc with length of 1 in a unit circle (with radius of 1)
 - fact that circumference of a circle = $2 \pi r$

**NB** Generally most trig questions will be in radians.  The smaller number generally gives a clue that amount is in radians.  Carefully check for abscence / presence of the degree symbol


<br>

**Triangles utilised for calculation of exact ratios**

 <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T1_StandardTriangle.jpg" />

<br>


"Standard triangles" are provided in degrees as above on the formula sheet.  Converting to radians:

 - $30^{\circ} = \dfrac{\pi}{6} $ radians

 -  $45^{\circ} = \dfrac{\pi}{4} $ radians

 -  $60^{\circ} = \dfrac{\pi}{3} $ radians


<br>

**y=sin(x)**
 - domain = $(-\infty , \infty )$
 - range = [-1, 1]
 - It is an odd function, -f(x) = f(-x)

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T1_sin.jpg" />


**y=cos(x)**
 - domain = $(-\infty , \infty )$
 - range = [-1, 1]
 - It is an even function, f(x) = f(-x)

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T1_cos.jpg" />


**y=tan(x)**
 - domain = $(-\infty , \infty )$, except for odd multiples of $\frac{\pi}{2}$ (asymptotes exist at these x-values)
 - range = $(-\infty , \infty )$
 - It is an odd function, f(x) = f(-x)

  <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T1_tan.jpg" />



**Amplitude, period, phase and centre**
- $y = k \sin[a(x+b)] + c$
    - amplitude = k
    - period = $\frac{2\pi}{a}$
    - phase: if b >0, shift to left, if b <0 shift to right
    - centre = c (shift up if c>0, down if c<0)

- $y = k \cos[a(x+b)] + c$
    - amplitude = k
    - period = $\frac{2\pi}{a}$
    - phase: if b >0, shift to left, if b <0 shift to right
    - centre = c (shift up if c>0, down if c<0)

- $y = k \tan[a(x+b)] + c$
    - tan has no amplitude
    - period = $\frac{\pi}{a}$
    - phase: if b >0, shift to left, if b <0 shift to right
    - centre = c (shift up if c>0, down if c<0)


Note that in the above formulas the "a" needs to multiply not just the x but the (x+b), assuming b iz not zero.
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "b8168cd4-7a8e-4c53-8003-d10c336026cc" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_f267b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f267b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_f267b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f267b_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_f267b_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_f267b_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_f267b_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_f267b_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_f267b_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_f267b_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_f267b_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_f267b_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_f267b_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_f267b_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_d8822 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d8822 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_d8822_row0_col0, #T_d8822_row1_col0, #T_d8822_row2_col0, #T_d8822_row3_col0, #T_d8822_row4_col0, #T_d8822_row5_col0, #T_d8822_row9_col0, #T_d8822_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_d8822_row6_col0, #T_d8822_row7_col0, #T_d8822_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_d8822">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d8822_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_d8822_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_d8822_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_d8822_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_d8822_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_d8822_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_d8822_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_d8822_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_d8822_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_d8822_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_d8822_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_d71e4 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d71e4 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_d71e4_row0_col0, #T_d71e4_row1_col0, #T_d71e4_row2_col0, #T_d71e4_row6_col0, #T_d71e4_row7_col0, #T_d71e4_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_d71e4_row3_col0, #T_d71e4_row4_col0, #T_d71e4_row5_col0, #T_d71e4_row9_col0, #T_d71e4_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_d71e4">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d71e4_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_d71e4_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_d71e4_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_d71e4_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_d71e4_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_d71e4_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_d71e4_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_d71e4_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_d71e4_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_d71e4_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_d71e4_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Trigonometric Functions and Identities </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - identity


### <span style="color:RGB(139,69,19)">  Notes </span>


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

As an alternative to memorising the complementary angle identities can be derived from a triangle such as below.

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

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "c198d9ae-f141-44d3-894b-ac04d7608aca" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_2951f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2951f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_2951f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2951f_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_2951f_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_2951f_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_2951f_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_2951f_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_2951f_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_2951f_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_2951f_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2951f_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2951f_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2951f_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2951f_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2951f_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_66c30 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_66c30 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_66c30_row0_col0, #T_66c30_row1_col0, #T_66c30_row2_col0, #T_66c30_row3_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_66c30_row4_col0, #T_66c30_row5_col0, #T_66c30_row6_col0, #T_66c30_row7_col0, #T_66c30_row8_col0, #T_66c30_row9_col0, #T_66c30_row10_col0, #T_66c30_row11_col0, #T_66c30_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_66c30">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_66c30_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_66c30_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_66c30_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_66c30_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_66c30_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_66c30_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_66c30_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_66c30_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_66c30_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_66c30_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_66c30_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_66c30_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_66c30_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_a3506 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_a3506 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_a3506_row0_col0, #T_a3506_row1_col0, #T_a3506_row2_col0, #T_a3506_row6_col0, #T_a3506_row7_col0, #T_a3506_row8_col0, #T_a3506_row9_col0, #T_a3506_row10_col0, #T_a3506_row11_col0, #T_a3506_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_a3506_row3_col0, #T_a3506_row4_col0, #T_a3506_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_a3506">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_a3506_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_a3506_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_a3506_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_a3506_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_a3506_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_a3506_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_a3506_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_a3506_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_a3506_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_a3506_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_a3506_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_a3506_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_a3506_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}