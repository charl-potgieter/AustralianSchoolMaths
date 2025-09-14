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
      <td id="T_NONE45ae7519723ffe7c_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col2" class="data row0 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col3" class="data row0 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col4" class="data row0 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col5" class="data row0 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col10" class="data row0 col10" >$\sin A=\dfrac{opp}{hyp}$</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col11" class="data row0 col11" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col12" class="data row0 col12" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col2" class="data row1 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col3" class="data row1 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col4" class="data row1 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col5" class="data row1 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col10" class="data row1 col10" >$\cos A=\dfrac{adj}{hyp}$</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col11" class="data row1 col11" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col12" class="data row1 col12" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col2" class="data row2 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col3" class="data row2 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col4" class="data row2 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col5" class="data row2 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col10" class="data row2 col10" >$\tan A=\dfrac{opp}{adj}$</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col11" class="data row2 col11" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col12" class="data row2 col12" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col2" class="data row3 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col3" class="data row3 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col4" class="data row3 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col5" class="data row3 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col10" class="data row3 col10" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col11" class="data row3 col11" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col12" class="data row3 col12" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col2" class="data row4 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col3" class="data row4 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col4" class="data row4 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col5" class="data row4 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col10" class="data row4 col10" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col11" class="data row4 col11" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col12" class="data row4 col12" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col2" class="data row5 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col3" class="data row5 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col4" class="data row5 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col5" class="data row5 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col10" class="data row5 col10" >$A = \dfrac{1}{2} ab \sin C$</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col11" class="data row5 col11" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col12" class="data row5 col12" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col2" class="data row6 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col3" class="data row6 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col4" class="data row6 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col5" class="data row6 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col10" class="data row6 col10" >$\sin (180^\circ - \theta) = \sin \theta $</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col11" class="data row6 col11" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col12" class="data row6 col12" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col2" class="data row7 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col3" class="data row7 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col4" class="data row7 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col5" class="data row7 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col10" class="data row7 col10" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col11" class="data row7 col11" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col12" class="data row7 col12" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col2" class="data row8 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col3" class="data row8 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col4" class="data row8 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col5" class="data row8 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col10" class="data row8 col10" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col11" class="data row8 col11" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col12" class="data row8 col12" >False</td>
      <td id="T_NONE45ae7519723ffe7c_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col2" class="data row9 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col3" class="data row9 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col4" class="data row9 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col5" class="data row9 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col10" class="data row9 col10" >$l=r\theta$</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col11" class="data row9 col11" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col12" class="data row9 col12" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_NONE45ae7519723ffe7c_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col2" class="data row10 col2" >Trigonometric Functions</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col3" class="data row10 col3" >MA-T1</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col4" class="data row10 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col5" class="data row10 col5" >Trigonometry</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col10" class="data row10 col10" >$A=\dfrac{1}{2}r^2 \theta$</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col11" class="data row10 col11" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col12" class="data row10 col12" >True</td>
      <td id="T_NONE45ae7519723ffe7c_row10_col13" class="data row10 col13" >nan</td>
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
#T_FORMULA_SHEET45ae7519723ffe7c_row0_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row0_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row6_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row7_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row8_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col13, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col0, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col1, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col2, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col3, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col4, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col5, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col6, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col7, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col8, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col9, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col11, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col12, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col13 {
  background-color: rgba(0,0,0,0);
}
#T_FORMULA_SHEET45ae7519723ffe7c_row0_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row1_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row2_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row3_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row4_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row5_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row9_col10, #T_FORMULA_SHEET45ae7519723ffe7c_row10_col10 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_FORMULA_SHEET45ae7519723ffe7c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col2" class="data row0 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col3" class="data row0 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col4" class="data row0 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col5" class="data row0 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col10" class="data row0 col10" >$\sin A=\dfrac{opp}{hyp}$</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col11" class="data row0 col11" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col12" class="data row0 col12" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col2" class="data row1 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col3" class="data row1 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col4" class="data row1 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col5" class="data row1 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col10" class="data row1 col10" >$\cos A=\dfrac{adj}{hyp}$</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col11" class="data row1 col11" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col12" class="data row1 col12" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col2" class="data row2 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col3" class="data row2 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col4" class="data row2 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col5" class="data row2 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col10" class="data row2 col10" >$\tan A=\dfrac{opp}{adj}$</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col11" class="data row2 col11" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col12" class="data row2 col12" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col2" class="data row3 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col3" class="data row3 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col4" class="data row3 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col5" class="data row3 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col10" class="data row3 col10" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col11" class="data row3 col11" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col12" class="data row3 col12" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col2" class="data row4 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col3" class="data row4 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col4" class="data row4 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col5" class="data row4 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col10" class="data row4 col10" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col11" class="data row4 col11" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col12" class="data row4 col12" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col2" class="data row5 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col3" class="data row5 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col4" class="data row5 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col5" class="data row5 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col10" class="data row5 col10" >$A = \dfrac{1}{2} ab \sin C$</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col11" class="data row5 col11" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col12" class="data row5 col12" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col2" class="data row6 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col3" class="data row6 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col4" class="data row6 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col5" class="data row6 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col10" class="data row6 col10" >$\sin (180^\circ - \theta) = \sin \theta $</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col11" class="data row6 col11" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col12" class="data row6 col12" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col2" class="data row7 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col3" class="data row7 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col4" class="data row7 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col5" class="data row7 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col10" class="data row7 col10" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col11" class="data row7 col11" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col12" class="data row7 col12" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col2" class="data row8 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col3" class="data row8 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col4" class="data row8 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col5" class="data row8 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col10" class="data row8 col10" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col11" class="data row8 col11" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col12" class="data row8 col12" >False</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col2" class="data row9 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col3" class="data row9 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col4" class="data row9 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col5" class="data row9 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col10" class="data row9 col10" >$l=r\theta$</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col11" class="data row9 col11" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col12" class="data row9 col12" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col2" class="data row10 col2" >Trigonometric Functions</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col3" class="data row10 col3" >MA-T1</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col4" class="data row10 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col5" class="data row10 col5" >Trigonometry</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col10" class="data row10 col10" >$A=\dfrac{1}{2}r^2 \theta$</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col11" class="data row10 col11" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col12" class="data row10 col12" >True</td>
      <td id="T_FORMULA_SHEET45ae7519723ffe7c_row10_col13" class="data row10 col13" >nan</td>
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
#T_PROOF_REQUIRED45ae7519723ffe7c_row0_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row0_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row1_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row2_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row3_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row6_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row7_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row8_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col13, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col0, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col1, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col2, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col3, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col4, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col5, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col6, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col7, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col8, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col9, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col11, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col12, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col13 {
  background-color: rgba(0,0,0,0);
}
#T_PROOF_REQUIRED45ae7519723ffe7c_row3_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row4_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row5_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row9_col10, #T_PROOF_REQUIRED45ae7519723ffe7c_row10_col10 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_PROOF_REQUIRED45ae7519723ffe7c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col0" class="data row0 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col1" class="data row0 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col2" class="data row0 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col3" class="data row0 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col4" class="data row0 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col5" class="data row0 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col6" class="data row0 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col7" class="data row0 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col8" class="data row0 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col9" class="data row0 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col10" class="data row0 col10" >$\sin A=\dfrac{opp}{hyp}$</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col11" class="data row0 col11" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col12" class="data row0 col12" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row0_col13" class="data row0 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col0" class="data row1 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col1" class="data row1 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col2" class="data row1 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col3" class="data row1 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col4" class="data row1 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col5" class="data row1 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col6" class="data row1 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col7" class="data row1 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col8" class="data row1 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col9" class="data row1 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col10" class="data row1 col10" >$\cos A=\dfrac{adj}{hyp}$</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col11" class="data row1 col11" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col12" class="data row1 col12" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row1_col13" class="data row1 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col0" class="data row2 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col1" class="data row2 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col2" class="data row2 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col3" class="data row2 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col4" class="data row2 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col5" class="data row2 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col6" class="data row2 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col7" class="data row2 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col8" class="data row2 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col9" class="data row2 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col10" class="data row2 col10" >$\tan A=\dfrac{opp}{adj}$</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col11" class="data row2 col11" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col12" class="data row2 col12" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row2_col13" class="data row2 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col0" class="data row3 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col1" class="data row3 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col2" class="data row3 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col3" class="data row3 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col4" class="data row3 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col5" class="data row3 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col6" class="data row3 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col7" class="data row3 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col8" class="data row3 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col9" class="data row3 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col10" class="data row3 col10" >$\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C} $</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col11" class="data row3 col11" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col12" class="data row3 col12" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row3_col13" class="data row3 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col0" class="data row4 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col1" class="data row4 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col2" class="data row4 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col3" class="data row4 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col4" class="data row4 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col5" class="data row4 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col6" class="data row4 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col7" class="data row4 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col8" class="data row4 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col9" class="data row4 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col10" class="data row4 col10" >$c^2 = a^2 + b^2 - 2ab \cos C$</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col11" class="data row4 col11" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col12" class="data row4 col12" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row4_col13" class="data row4 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col0" class="data row5 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col1" class="data row5 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col2" class="data row5 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col3" class="data row5 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col4" class="data row5 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col5" class="data row5 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col6" class="data row5 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col7" class="data row5 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col8" class="data row5 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col9" class="data row5 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col10" class="data row5 col10" >$A = \dfrac{1}{2} ab \sin C$</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col11" class="data row5 col11" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col12" class="data row5 col12" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row5_col13" class="data row5 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col0" class="data row6 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col1" class="data row6 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col2" class="data row6 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col3" class="data row6 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col4" class="data row6 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col5" class="data row6 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col6" class="data row6 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col7" class="data row6 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col8" class="data row6 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col9" class="data row6 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col10" class="data row6 col10" >$\sin (180^\circ - \theta) = \sin \theta $</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col11" class="data row6 col11" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col12" class="data row6 col12" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row6_col13" class="data row6 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col0" class="data row7 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col1" class="data row7 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col2" class="data row7 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col3" class="data row7 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col4" class="data row7 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col5" class="data row7 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col6" class="data row7 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col7" class="data row7 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col8" class="data row7 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col9" class="data row7 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col10" class="data row7 col10" >$\cos (180 ^\circ - \theta) = - \cos \theta $</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col11" class="data row7 col11" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col12" class="data row7 col12" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row7_col13" class="data row7 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col0" class="data row8 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col1" class="data row8 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col2" class="data row8 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col3" class="data row8 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col4" class="data row8 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col5" class="data row8 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col6" class="data row8 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col7" class="data row8 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col8" class="data row8 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col9" class="data row8 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col10" class="data row8 col10" >$\tan (180 ^\circ - \theta) = - \tan \theta $</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col11" class="data row8 col11" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col12" class="data row8 col12" >False</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row8_col13" class="data row8 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col0" class="data row9 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col1" class="data row9 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col2" class="data row9 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col3" class="data row9 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col4" class="data row9 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col5" class="data row9 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col6" class="data row9 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col7" class="data row9 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col8" class="data row9 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col9" class="data row9 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col10" class="data row9 col10" >$l=r\theta$</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col11" class="data row9 col11" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col12" class="data row9 col12" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row9_col13" class="data row9 col13" >nan</td>
    </tr>
    <tr>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col0" class="data row10 col0" >NSW</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col1" class="data row10 col1" >Year 11 Adv</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col2" class="data row10 col2" >Trigonometric Functions</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col3" class="data row10 col3" >MA-T1</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col4" class="data row10 col4" >Trigonometry and Measure of Angles</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col5" class="data row10 col5" >Trigonometry</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col6" class="data row10 col6" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col7" class="data row10 col7" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col8" class="data row10 col8" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col9" class="data row10 col9" >nan</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col10" class="data row10 col10" >$A=\dfrac{1}{2}r^2 \theta$</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col11" class="data row10 col11" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col12" class="data row10 col12" >True</td>
      <td id="T_PROOF_REQUIRED45ae7519723ffe7c_row10_col13" class="data row10 col13" >nan</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}
