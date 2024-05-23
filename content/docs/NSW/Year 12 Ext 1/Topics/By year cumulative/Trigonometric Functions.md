---
weight: 6
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
{{< tabs "27fba55f-8d41-4fc2-a874-891f84d5b0bb" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_deb13 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_deb13 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_deb13">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_deb13_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_deb13_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_deb13_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_deb13_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_deb13_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_deb13_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_deb13_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_deb13_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_deb13_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_deb13_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_deb13_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_bb28d th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bb28d td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_bb28d_row0_col0, #T_bb28d_row1_col0, #T_bb28d_row2_col0, #T_bb28d_row3_col0, #T_bb28d_row4_col0, #T_bb28d_row5_col0, #T_bb28d_row9_col0, #T_bb28d_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_bb28d_row6_col0, #T_bb28d_row7_col0, #T_bb28d_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_bb28d">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_bb28d_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_bb28d_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_bb28d_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_bb28d_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_bb28d_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_bb28d_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_bb28d_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_bb28d_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_bb28d_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_bb28d_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_bb28d_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_671f0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_671f0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_671f0_row0_col0, #T_671f0_row1_col0, #T_671f0_row2_col0, #T_671f0_row6_col0, #T_671f0_row7_col0, #T_671f0_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_671f0_row3_col0, #T_671f0_row4_col0, #T_671f0_row5_col0, #T_671f0_row9_col0, #T_671f0_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_671f0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_671f0_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_671f0_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_671f0_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_671f0_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_671f0_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_671f0_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_671f0_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_671f0_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_671f0_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_671f0_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_671f0_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
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
{{< tabs "9e46ce2f-f539-45e4-908b-d687d4684b70" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_eace6 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_eace6 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_eace6">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_eace6_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_eace6_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_eace6_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_eace6_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_eace6_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_eace6_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_eace6_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_eace6_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_eace6_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_eace6_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_eace6_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_eace6_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_eace6_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_2ecd3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2ecd3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_2ecd3_row0_col0, #T_2ecd3_row1_col0, #T_2ecd3_row2_col0, #T_2ecd3_row3_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_2ecd3_row4_col0, #T_2ecd3_row5_col0, #T_2ecd3_row6_col0, #T_2ecd3_row7_col0, #T_2ecd3_row8_col0, #T_2ecd3_row9_col0, #T_2ecd3_row10_col0, #T_2ecd3_row11_col0, #T_2ecd3_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_2ecd3">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2ecd3_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_2ecd3_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_9c9fa th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_9c9fa td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_9c9fa_row0_col0, #T_9c9fa_row1_col0, #T_9c9fa_row2_col0, #T_9c9fa_row6_col0, #T_9c9fa_row7_col0, #T_9c9fa_row8_col0, #T_9c9fa_row9_col0, #T_9c9fa_row10_col0, #T_9c9fa_row11_col0, #T_9c9fa_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_9c9fa_row3_col0, #T_9c9fa_row4_col0, #T_9c9fa_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_9c9fa">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_9c9fa_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_9c9fa_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
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
{{< tabs "48ac17a4-a2a2-4787-9e66-f97ce2fb4d55" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_553ac th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_553ac td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_553ac">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_553ac_row0_col0" class="data row0 col0" >$\sin(\sin^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_553ac_row1_col0" class="data row1 col0" >$\sin^{-1}(\sin x) = x \text{, for } -\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_553ac_row2_col0" class="data row2 col0" >$\cos(\cos^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_553ac_row3_col0" class="data row3 col0" >$\cos^{-1}(\cos x) = x \text{, for } 0 \le x \le \pi$</td>
    </tr>
    <tr>
      <td id="T_553ac_row4_col0" class="data row4 col0" >$\tan(\tan^{-1} x) = x \text{, for } -\infty < x < \infty$</td>
    </tr>
    <tr>
      <td id="T_553ac_row5_col0" class="data row5 col0" >$\tan^{-1}(\tan x) = x \text{, for } -\dfrac{\pi}{2} < x < \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_553ac_row6_col0" class="data row6 col0" >$\sin^{-1}(-x) = -\sin^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_553ac_row7_col0" class="data row7 col0" >$\cos^{-1}(-x) = \pi -\cos^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_553ac_row8_col0" class="data row8 col0" >$\tan^{-1}(-x) = -\tan^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_553ac_row9_col0" class="data row9 col0" >$\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_c9f58 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c9f58 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c9f58_row0_col0, #T_c9f58_row1_col0, #T_c9f58_row2_col0, #T_c9f58_row3_col0, #T_c9f58_row4_col0, #T_c9f58_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_c9f58_row6_col0, #T_c9f58_row7_col0, #T_c9f58_row8_col0, #T_c9f58_row9_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_c9f58">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c9f58_row0_col0" class="data row0 col0" >$\sin(\sin^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_c9f58_row1_col0" class="data row1 col0" >$\sin^{-1}(\sin x) = x \text{, for } -\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_c9f58_row2_col0" class="data row2 col0" >$\cos(\cos^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_c9f58_row3_col0" class="data row3 col0" >$\cos^{-1}(\cos x) = x \text{, for } 0 \le x \le \pi$</td>
    </tr>
    <tr>
      <td id="T_c9f58_row4_col0" class="data row4 col0" >$\tan(\tan^{-1} x) = x \text{, for } -\infty < x < \infty$</td>
    </tr>
    <tr>
      <td id="T_c9f58_row5_col0" class="data row5 col0" >$\tan^{-1}(\tan x) = x \text{, for } -\dfrac{\pi}{2} < x < \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_c9f58_row6_col0" class="data row6 col0" >$\sin^{-1}(-x) = -\sin^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_c9f58_row7_col0" class="data row7 col0" >$\cos^{-1}(-x) = \pi -\cos^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_c9f58_row8_col0" class="data row8 col0" >$\tan^{-1}(-x) = -\tan^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_c9f58_row9_col0" class="data row9 col0" >$\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$</td>
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
{{< tabs "e99ea7ff-ecac-4a59-b522-4c98cd3e6040" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_10eb9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_10eb9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_10eb9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_10eb9_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_10eb9_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_22eab th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_22eab td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_22eab_row0_col0, #T_22eab_row2_col0, #T_22eab_row4_col0, #T_22eab_row11_col0, #T_22eab_row12_col0, #T_22eab_row13_col0, #T_22eab_row14_col0, #T_22eab_row15_col0, #T_22eab_row16_col0, #T_22eab_row17_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_22eab_row1_col0, #T_22eab_row3_col0, #T_22eab_row5_col0, #T_22eab_row6_col0, #T_22eab_row7_col0, #T_22eab_row8_col0, #T_22eab_row9_col0, #T_22eab_row10_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_22eab">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_22eab_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_22eab_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_22eab_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_22eab_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_22eab_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_22eab_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_22eab_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_22eab_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_22eab_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_22eab_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_22eab_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_22eab_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_22eab_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_22eab_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_22eab_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_22eab_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_22eab_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_22eab_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_a9e70 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_a9e70 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_a9e70_row0_col0, #T_a9e70_row1_col0, #T_a9e70_row2_col0, #T_a9e70_row3_col0, #T_a9e70_row4_col0, #T_a9e70_row5_col0, #T_a9e70_row6_col0, #T_a9e70_row7_col0, #T_a9e70_row8_col0, #T_a9e70_row9_col0, #T_a9e70_row10_col0, #T_a9e70_row11_col0, #T_a9e70_row12_col0, #T_a9e70_row13_col0, #T_a9e70_row14_col0, #T_a9e70_row15_col0, #T_a9e70_row16_col0, #T_a9e70_row17_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_a9e70">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_a9e70_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_a9e70_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
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

The auxiliary angle method can be utilsed to reduce an expression in the format $\pm a\cos x \pm b \sin x $ into $r \cos (x \pm \alpha)$ or $r \sin (x \pm \alpha)$.  In these scenarios, $\alpha$ is known as the auxiliary angle.

The above simpliciation can be useful in solving equations or sketching graphs.

Examples of auxiliary angles are incuded in the formulas below for example:<br>
$a \sin x + b \cos x = r \sin(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$

None of the auxiliary angles appear on the formula sheet so rather than attemping to memorise the below approach is recommended when say trying to solve a formula such as the above:
 - Expand the RHS of the equation using the compound angle rules that appear on the formula sheet, for example the $\sin (A+B)$ formula
 - The expanded right hand side will then equal something like $r\sin x \cos \alpha  + r \cos x \sin \alpha$
 - Comparing to LHS we can deduce that:
    - $r\cos \alpha  = a \therefore cos \alpha  =\frac{a}{r}$, and
    - $r\sin \alpha = b \therefore sin \alpha  =\frac{b}{r}$
 - sketching a right angled triangle:
   - r can be solved using the pythagoras theorem
   - $\alpha$ can be solved using $\tan \alpha = \frac{b}{a}$




<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "4c77ce31-fa47-4095-8b1b-967320267c59" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_d1363 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d1363 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_d1363">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d1363_row0_col0" class="data row0 col0" >$a \sin x + b \cos x = r \sin(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_d1363_row1_col0" class="data row1 col0" >$a \sin x - b \cos x = r \sin(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_d1363_row2_col0" class="data row2 col0" >$a \cos x + b \sin x = r \cos(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_d1363_row3_col0" class="data row3 col0" >$a \cos x - b \sin x = r \cos(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_d729f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d729f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_d729f_row0_col0, #T_d729f_row1_col0, #T_d729f_row2_col0, #T_d729f_row3_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_d729f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d729f_row0_col0" class="data row0 col0" >$a \sin x + b \cos x = r \sin(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_d729f_row1_col0" class="data row1 col0" >$a \sin x - b \cos x = r \sin(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_d729f_row2_col0" class="data row2 col0" >$a \cos x + b \sin x = r \cos(x - \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
    <tr>
      <td id="T_d729f_row3_col0" class="data row3 col0" >$a \cos x - b \sin x = r \cos(x + \alpha) \text{, where } r=\sqrt{a^2+b^2} \text { and } \tan \alpha = \dfrac{b}{a}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}