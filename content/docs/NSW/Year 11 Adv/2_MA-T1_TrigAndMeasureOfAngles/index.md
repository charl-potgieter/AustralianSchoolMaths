---
weight: 2
title: 'Trigonometry and Measure of Angles'
---

## Trigonometry and Measure of Angles

### Concepts

- angle of elevation
- angle of depression
- true bearing (sometimes written as $x^\circ T$, representing $x$ degrees true
bearing)
- compass bearing
- amplitude
- period
- phase
- supplementary angles
- complementary angles
- similiar triangles

###   Notes 


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
 - Find and angle given 3 sides (SSS)

No need to use sine or cosine rule in right angled triangles - problems can
generally be solved by simply using the definitions of the trig ratios.

When using the sine formula for calculating the area of a triangle note that the
angle utilised in the formula is the angle between the 2 sides whose lengths are
utilsed in the formula

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

Understand the reason why $\pi \text{ radians}  = 180^{\circ}$ based on
 - the definition of 1 radian being the angle subtended by an arc with length of 1 in a unit circle (with radius of 1)
 - fact that circumference of a circle = $2 \pi r$

**NB** Generally most trig questions will be in radians.  The smaller number generally gives a clue that amount is in radians.  Carefully check for abscence / presence of the degree symbol


<br>

**Triangles utilised for calculation of exact ratios**

 <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_T1_StandardTriangle.jpg" />

<br>


"Standard triangles" are provided in degrees as above on the formula sheet.  Converting to radians:

 - $30^{\circ} = \dfrac{\pi}{6}$ radians

 -  $45^{\circ} = \dfrac{\pi}{4}$ radians

 -  $60^{\circ} = \dfrac{\pi}{3}$ radians


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

### Formulas
{{< tabs "tab45ae7519723ffe7c" >}}

{{< tab "Standard View" >}}

<style type="text/css">
#T_NONE45ae7519723ffe7c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_NONE45ae7519723ffe7c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_NONE45ae7519723ffe7c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

<style type="text/css">
#T_FORMULA_SHEET45ae7519723ffe7c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_FORMULA_SHEET45ae7519723ffe7c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_FORMULA_SHEET45ae7519723ffe7c_row0_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_FORMULA_SHEET45ae7519723ffe7c_row6_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_FORMULA_SHEET45ae7519723ffe7c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proof Required" >}}

<style type="text/css">
#T_PROOF_REQUIRED45ae7519723ffe7c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_PROOF_REQUIRED45ae7519723ffe7c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_PROOF_REQUIRED45ae7519723ffe7c_row0_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_PROOF_REQUIRED45ae7519723ffe7c_row3_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_PROOF_REQUIRED45ae7519723ffe7c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
