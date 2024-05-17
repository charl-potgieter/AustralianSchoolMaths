---
weight: 4
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
{{< tabs "d953d88f-e2b5-480d-8c92-5d508fd5a351" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_faab7 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_faab7 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_faab7">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_faab7_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_faab7_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_faab7_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_faab7_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_faab7_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_faab7_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_faab7_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_faab7_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_faab7_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_faab7_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_faab7_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_8c306 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8c306 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_8c306_row0_col0, #T_8c306_row1_col0, #T_8c306_row2_col0, #T_8c306_row3_col0, #T_8c306_row4_col0, #T_8c306_row5_col0, #T_8c306_row9_col0, #T_8c306_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_8c306_row6_col0, #T_8c306_row7_col0, #T_8c306_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_8c306">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_8c306_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_8c306_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_8c306_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_8c306_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_8c306_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_8c306_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_8c306_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_8c306_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_8c306_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_8c306_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_8c306_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_773c2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_773c2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_773c2_row0_col0, #T_773c2_row1_col0, #T_773c2_row2_col0, #T_773c2_row6_col0, #T_773c2_row7_col0, #T_773c2_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_773c2_row3_col0, #T_773c2_row4_col0, #T_773c2_row5_col0, #T_773c2_row9_col0, #T_773c2_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_773c2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_773c2_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_773c2_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_773c2_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_773c2_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_773c2_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_773c2_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_773c2_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_773c2_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_773c2_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_773c2_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_773c2_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
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
{{< tabs "a56d2ffa-af98-4afa-85e2-e1653de9f2fe" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_14cfd th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_14cfd td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_14cfd">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_14cfd_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_14cfd_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_4bff7 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4bff7 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_4bff7_row0_col0, #T_4bff7_row1_col0, #T_4bff7_row2_col0, #T_4bff7_row3_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_4bff7_row4_col0, #T_4bff7_row5_col0, #T_4bff7_row6_col0, #T_4bff7_row7_col0, #T_4bff7_row8_col0, #T_4bff7_row9_col0, #T_4bff7_row10_col0, #T_4bff7_row11_col0, #T_4bff7_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_4bff7">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4bff7_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_4bff7_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_73179 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_73179 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_73179_row0_col0, #T_73179_row1_col0, #T_73179_row2_col0, #T_73179_row6_col0, #T_73179_row7_col0, #T_73179_row8_col0, #T_73179_row9_col0, #T_73179_row10_col0, #T_73179_row11_col0, #T_73179_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_73179_row3_col0, #T_73179_row4_col0, #T_73179_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_73179">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_73179_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_73179_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_73179_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_73179_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_73179_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_73179_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_73179_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_73179_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_73179_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_73179_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_73179_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_73179_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_73179_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Inverse Trigonometric Functions </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>

The graph of an inverse function is a reflection of the original function in the line y=x.  (the y-value and x-values of the origianl graph are switched to obtain the inverse graph)

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


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "56e2a615-5fe2-45a4-8cc7-c9064268d710" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_bdfd2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bdfd2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_bdfd2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_bdfd2_row0_col0" class="data row0 col0" >$\sin(\sin^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row1_col0" class="data row1 col0" >$\sin^{-1}(\sin x) = x \text{, for } -\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row2_col0" class="data row2 col0" >$\cos(\cos^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row3_col0" class="data row3 col0" >$\cos^{-1}(\cos x) = x \text{, for } 0 \le x \le \pi$</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row4_col0" class="data row4 col0" >$\tan(\tan^{-1} x) = x \text{, for } -\infty < x < \infty$</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row5_col0" class="data row5 col0" >$\tan^{-1}(\tan x) = x \text{, for } -\dfrac{\pi}{2} < x < \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row6_col0" class="data row6 col0" >$\sin^{-1}(-x) = -\sin^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row7_col0" class="data row7 col0" >$\cos^{-1}(-x) = \pi -\cos^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row8_col0" class="data row8 col0" >$\tan^{-1}(-x) = -\tan^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_bdfd2_row9_col0" class="data row9 col0" >$\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_ce9c8 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ce9c8 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_ce9c8_row0_col0, #T_ce9c8_row1_col0, #T_ce9c8_row2_col0, #T_ce9c8_row3_col0, #T_ce9c8_row4_col0, #T_ce9c8_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_ce9c8_row6_col0, #T_ce9c8_row7_col0, #T_ce9c8_row8_col0, #T_ce9c8_row9_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_ce9c8">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ce9c8_row0_col0" class="data row0 col0" >$\sin(\sin^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row1_col0" class="data row1 col0" >$\sin^{-1}(\sin x) = x \text{, for } -\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row2_col0" class="data row2 col0" >$\cos(\cos^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row3_col0" class="data row3 col0" >$\cos^{-1}(\cos x) = x \text{, for } 0 \le x \le \pi$</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row4_col0" class="data row4 col0" >$\tan(\tan^{-1} x) = x \text{, for } -\infty < x < \infty$</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row5_col0" class="data row5 col0" >$\tan^{-1}(\tan x) = x \text{, for } -\dfrac{\pi}{2} < x < \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row6_col0" class="data row6 col0" >$\sin^{-1}(-x) = -\sin^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row7_col0" class="data row7 col0" >$\cos^{-1}(-x) = \pi -\cos^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row8_col0" class="data row8 col0" >$\tan^{-1}(-x) = -\tan^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_ce9c8_row9_col0" class="data row9 col0" >$\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Trigonometric Identities </span> 
<br>

### <span style="color:RGB(139,69,19)">  Notes </span>

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


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "8fabaf70-63cf-4f91-aa8d-245a575abf49" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_12883 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_12883 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_12883">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_12883_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_12883_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_12883_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_12883_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_12883_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_12883_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_12883_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_12883_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_12883_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_12883_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_12883_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_12883_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_12883_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_12883_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_12883_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_12883_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_12883_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_12883_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_25a76 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_25a76 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_25a76_row0_col0, #T_25a76_row2_col0, #T_25a76_row4_col0, #T_25a76_row11_col0, #T_25a76_row12_col0, #T_25a76_row13_col0, #T_25a76_row14_col0, #T_25a76_row15_col0, #T_25a76_row16_col0, #T_25a76_row17_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_25a76_row1_col0, #T_25a76_row3_col0, #T_25a76_row5_col0, #T_25a76_row6_col0, #T_25a76_row7_col0, #T_25a76_row8_col0, #T_25a76_row9_col0, #T_25a76_row10_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_25a76">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_25a76_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_25a76_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_25a76_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_25a76_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_25a76_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_25a76_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_25a76_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_25a76_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_25a76_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_25a76_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_25a76_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_25a76_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_25a76_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_25a76_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_25a76_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_25a76_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_25a76_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_25a76_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_95a22 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_95a22 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_95a22_row0_col0, #T_95a22_row1_col0, #T_95a22_row2_col0, #T_95a22_row3_col0, #T_95a22_row4_col0, #T_95a22_row5_col0, #T_95a22_row6_col0, #T_95a22_row7_col0, #T_95a22_row8_col0, #T_95a22_row9_col0, #T_95a22_row10_col0, #T_95a22_row11_col0, #T_95a22_row12_col0, #T_95a22_row13_col0, #T_95a22_row14_col0, #T_95a22_row15_col0, #T_95a22_row16_col0, #T_95a22_row17_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_95a22">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_95a22_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_95a22_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_95a22_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_95a22_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_95a22_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_95a22_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_95a22_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_95a22_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_95a22_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_95a22_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_95a22_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_95a22_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_95a22_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_95a22_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_95a22_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_95a22_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_95a22_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_95a22_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Trigonometric Functions and Graphs </span> 
<br>

### <span style="color:RGB(139,69,19)">  Notes </span>

 - Understand the transformation of functions in the form y=kf(a(x+b))+c, where f(x) is a trigonometric function such as sin x, cos x etc.
 - Be able to determine the domain and range of the transformed function
 - The impact of the transforation on amplitude, phase and center are set out in Year 11 Advanced, Trigonometric Functions.
 - Note that amplitude is a measure from centre to top (or bottom) of graph.  NOT top to bottom.
 - Note that domain refers to the values that can be allocated to $x$.  For example if $y=\sin 3x$ has a domain of $[0, \pi]$ tht means that $3x$ will have values between $0$ and $3\pi$
<BR><BR>


## <span style="color:RGB(0,32,96"> Trigonometric Equations </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>

**Auxiliary angles**
If required to draw a sketch of say $10 \sin x - 13 \cos x$, first convert to format $r\sin(x-\alpha)$ using the auxiliary angle formulas.


$a \sin x + b \cos x = r \sin(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$

$a \sin x - b \cos x = r \sin(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$

$a \cos x + b \sin x = r \cos(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$

$a \cos x - b \sin x = r \cos(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "51fcb6ef-3bb2-4b51-926d-6b0a6be57c73" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_a9fe7 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_a9fe7 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_a9fe7">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_a9fe7_row0_col0" class="data row0 col0" >$a \sin x + b \cos x = r \sin(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_a9fe7_row1_col0" class="data row1 col0" >$a \sin x - b \cos x = r \sin(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_a9fe7_row2_col0" class="data row2 col0" >$a \cos x + b \sin x = r \cos(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_a9fe7_row3_col0" class="data row3 col0" >$a \cos x - b \sin x = r \cos(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_95e8c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_95e8c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_95e8c_row0_col0, #T_95e8c_row1_col0, #T_95e8c_row2_col0, #T_95e8c_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_95e8c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_95e8c_row0_col0" class="data row0 col0" >$a \sin x + b \cos x = r \sin(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_95e8c_row1_col0" class="data row1 col0" >$a \sin x - b \cos x = r \sin(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_95e8c_row2_col0" class="data row2 col0" >$a \cos x + b \sin x = r \cos(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_95e8c_row3_col0" class="data row3 col0" >$a \cos x - b \sin x = r \cos(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}