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

<span style="color:RGB(255,0,0)"> Need to insert  graphs, most likely draw with matplotlib.  Excel trig doees not seem feasible </span>



<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "f16d572f-5a77-4b7f-8d27-135e7bb6c6c7" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_f778e th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f778e td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_f778e">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f778e_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_f778e_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_f778e_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_f778e_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_f778e_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_f778e_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_f778e_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_f778e_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_f778e_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_f778e_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_f778e_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_370da th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_370da td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_370da_row0_col0, #T_370da_row1_col0, #T_370da_row2_col0, #T_370da_row3_col0, #T_370da_row4_col0, #T_370da_row5_col0, #T_370da_row9_col0, #T_370da_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_370da_row6_col0, #T_370da_row7_col0, #T_370da_row8_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_370da">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_370da_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_370da_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_370da_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_370da_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_370da_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_370da_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_370da_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_370da_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_370da_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_370da_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_370da_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_6fa40 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_6fa40 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_6fa40_row0_col0, #T_6fa40_row1_col0, #T_6fa40_row2_col0, #T_6fa40_row6_col0, #T_6fa40_row7_col0, #T_6fa40_row8_col0 {
  background-color: rgba(0,0,0,0);
}
#T_6fa40_row3_col0, #T_6fa40_row4_col0, #T_6fa40_row5_col0, #T_6fa40_row9_col0, #T_6fa40_row10_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_6fa40">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_6fa40_row0_col0" class="data row0 col0" >$\sin A=\dfrac{opp}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_6fa40_row1_col0" class="data row1 col0" >$\cos A=\dfrac{adj}{hyp}$</td>
    </tr>
    <tr>
      <td id="T_6fa40_row2_col0" class="data row2 col0" >$\tan A=\dfrac{opp}{adj}$</td>
    </tr>
    <tr>
      <td id="T_6fa40_row3_col0" class="data row3 col0" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
    </tr>
    <tr>
      <td id="T_6fa40_row4_col0" class="data row4 col0" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
    </tr>
    <tr>
      <td id="T_6fa40_row5_col0" class="data row5 col0" >$A = \dfrac{1}{2} ab \sin C$</td>
    </tr>
    <tr>
      <td id="T_6fa40_row6_col0" class="data row6 col0" >$\sin (180^\circ - \theta) = \sin \theta $</td>
    </tr>
    <tr>
      <td id="T_6fa40_row7_col0" class="data row7 col0" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
    </tr>
    <tr>
      <td id="T_6fa40_row8_col0" class="data row8 col0" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
    </tr>
    <tr>
      <td id="T_6fa40_row9_col0" class="data row9 col0" >$l=r\theta$</td>
    </tr>
    <tr>
      <td id="T_6fa40_row10_col0" class="data row10 col0" >$A=\dfrac{1}{2}r^2 \theta$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Trigonometric Functions and Identities </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>


<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "1b6a55b1-65f9-4495-92e2-e4de51186eb4" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_3f80c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3f80c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_3f80c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_3f80c_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_3f80c_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_3f80c_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_3f80c_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_3f80c_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_3f80c_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_3f80c_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_59b25 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_59b25 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_59b25_row0_col0, #T_59b25_row1_col0, #T_59b25_row2_col0, #T_59b25_row3_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_59b25_row4_col0, #T_59b25_row5_col0, #T_59b25_row6_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_59b25">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_59b25_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_59b25_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_59b25_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_59b25_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_59b25_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_59b25_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_59b25_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_bd4da th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bd4da td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_bd4da_row0_col0, #T_bd4da_row1_col0, #T_bd4da_row2_col0, #T_bd4da_row6_col0 {
  background-color: rgba(0,0,0,0);
}
#T_bd4da_row3_col0, #T_bd4da_row4_col0, #T_bd4da_row5_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_bd4da">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_bd4da_row0_col0" class="data row0 col0" >$\sec A = \dfrac{1}{\cos A}, \cos A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_bd4da_row1_col0" class="data row1 col0" >$\text{cosec } A = \dfrac{1}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_bd4da_row2_col0" class="data row2 col0" >$\cot A = \dfrac{\cos A}{\sin A}, \sin A \ne 0$</td>
    </tr>
    <tr>
      <td id="T_bd4da_row3_col0" class="data row3 col0" >$\cos^2 x+\sin^2 x = 1$</td>
    </tr>
    <tr>
      <td id="T_bd4da_row4_col0" class="data row4 col0" >$1+\tan^2 x = \sec^2 x$</td>
    </tr>
    <tr>
      <td id="T_bd4da_row5_col0" class="data row5 col0" >$\cot^2 x+1 = \text{cosec }^2 x$</td>
    </tr>
    <tr>
      <td id="T_bd4da_row6_col0" class="data row6 col0" >$\tan x = \dfrac{\sin x}{\cos x}, cos x \ne 0$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Inverse Trigonometric Functions </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>


## <span style="color:RGB(0,32,96"> Further Trigonometric Identities </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>
<BR><BR>
