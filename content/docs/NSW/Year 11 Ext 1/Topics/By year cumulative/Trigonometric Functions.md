---
weight: 2
---

## Trigonometry and Measure of Angles
<br>

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

<BR><BR>



<br>


### Formulas
<br>
{{< tabs "d655911b" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_standard_57ca761f2a5bfb17 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_standard_57ca761f2a5bfb17 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_standard_57ca761f2a5bfb17">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_standard_57ca761f2a5bfb17_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_formula_sheet_1be88186f97400e9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_formula_sheet_1be88186f97400e9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_formula_sheet_1be88186f97400e9_row0_col0, #T_formula_sheet_1be88186f97400e9_row1_col0, #T_formula_sheet_1be88186f97400e9_row2_col0, #T_formula_sheet_1be88186f97400e9_row3_col0, #T_formula_sheet_1be88186f97400e9_row4_col0, #T_formula_sheet_1be88186f97400e9_row5_col0, #T_formula_sheet_1be88186f97400e9_row9_col0, #T_formula_sheet_1be88186f97400e9_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_formula_sheet_1be88186f97400e9_row6_col0, #T_formula_sheet_1be88186f97400e9_row7_col0, #T_formula_sheet_1be88186f97400e9_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_formula_sheet_1be88186f97400e9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_1be88186f97400e9_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_proof_required_7fb5bcf10195bff4 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_proof_required_7fb5bcf10195bff4 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_proof_required_7fb5bcf10195bff4_row0_col0, #T_proof_required_7fb5bcf10195bff4_row1_col0, #T_proof_required_7fb5bcf10195bff4_row2_col0, #T_proof_required_7fb5bcf10195bff4_row6_col0, #T_proof_required_7fb5bcf10195bff4_row7_col0, #T_proof_required_7fb5bcf10195bff4_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_proof_required_7fb5bcf10195bff4_row3_col0, #T_proof_required_7fb5bcf10195bff4_row4_col0, #T_proof_required_7fb5bcf10195bff4_row5_col0, #T_proof_required_7fb5bcf10195bff4_row9_col0, #T_proof_required_7fb5bcf10195bff4_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_proof_required_7fb5bcf10195bff4">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_proof_required_7fb5bcf10195bff4_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## Trigonometric Functions and Identities
<br>

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

<BR><BR>



<br>


### Formulas
<br>
{{< tabs "2755f25a" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_standard_3ca8b040b596f74e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_standard_3ca8b040b596f74e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_standard_3ca8b040b596f74e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_standard_3ca8b040b596f74e_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_formula_sheet_473130789760db88 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_formula_sheet_473130789760db88 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_formula_sheet_473130789760db88_row0_col0, #T_formula_sheet_473130789760db88_row1_col0, #T_formula_sheet_473130789760db88_row2_col0, #T_formula_sheet_473130789760db88_row3_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_formula_sheet_473130789760db88_row4_col0, #T_formula_sheet_473130789760db88_row5_col0, #T_formula_sheet_473130789760db88_row6_col0, #T_formula_sheet_473130789760db88_row7_col0, #T_formula_sheet_473130789760db88_row8_col0, #T_formula_sheet_473130789760db88_row9_col0, #T_formula_sheet_473130789760db88_row10_col0, #T_formula_sheet_473130789760db88_row11_col0, #T_formula_sheet_473130789760db88_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_formula_sheet_473130789760db88">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_formula_sheet_473130789760db88_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Proofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_proof_required_77eb1bd41e7e915b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_proof_required_77eb1bd41e7e915b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_proof_required_77eb1bd41e7e915b_row0_col0, #T_proof_required_77eb1bd41e7e915b_row1_col0, #T_proof_required_77eb1bd41e7e915b_row2_col0, #T_proof_required_77eb1bd41e7e915b_row6_col0, #T_proof_required_77eb1bd41e7e915b_row7_col0, #T_proof_required_77eb1bd41e7e915b_row8_col0, #T_proof_required_77eb1bd41e7e915b_row9_col0, #T_proof_required_77eb1bd41e7e915b_row10_col0, #T_proof_required_77eb1bd41e7e915b_row11_col0, #T_proof_required_77eb1bd41e7e915b_row12_col0 {
  background-color: rgba(0,0,0,0);
}
#T_proof_required_77eb1bd41e7e915b_row3_col0, #T_proof_required_77eb1bd41e7e915b_row4_col0, #T_proof_required_77eb1bd41e7e915b_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_proof_required_77eb1bd41e7e915b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row7_col0" class="data row7 col0" >$\sin \theta = \cos (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row8_col0" class="data row8 col0" >$\cos \theta = \sin (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row9_col0" class="data row9 col0" >$\tan \theta = \cot (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row10_col0" class="data row10 col0" >$\cot \theta = \tan (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row11_col0" class="data row11 col0" >$\sec \theta = \text{cosec } (90^{\circ} - \theta)$</td>
    </tr>
    <tr>
      <td id="T_proof_required_77eb1bd41e7e915b_row12_col0" class="data row12 col0" >$\text{cosec } \theta = \sec (90^{\circ} - \theta)$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

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