---
weight: 9
---

## <span style="color:RGB(0,32,96"> Introduction to Complex Numbers </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* Argand diagram
* argument
* Complex numbers
* Cartesian or rectangular form
* complex conjugate
* complex plane
* exponential form
* Euler's formula
* imaginary number
* imaginary part
* modulus
* polar or modulus-argument form
* real part
* vector


### <span style="color:RGB(139,69,19)">  Notes </span>


* Equivalence of complex numbers
<BR><BR>
* Realising the denominator
<BR><BR>
* Calculating the square of a complex number
<BR><BR>
* Vectors of a complex number and its conjugate are reflections in  the real axis on an Argand diagram.
<BR><BR>
* Add and subtract complex numbers utilising vector parallelogram rule
<BR><BR>
* Multiply complex numbers by a constant
<BR><BR>
* Tip: If a question provides 2 complex roots of a quadratic, it is simpler to substitute symbols for the roots such as a and b e.g. $(x-a)(x-b)  = 0$ and then multiply out before inserting the complex numbers
<BR><BR>
* Be able to factorise a quadratic as a difference of squares by adding an $i^2$ to one of the sides in place of a minus one.  The real part of the square may need to be obtained by completing the square.
<BR><BR>
* Complex numbers can be written in :
    * cartesian or rectangular form
    * polar of modulus-argument form
    * exponential form
<BR><BR>
* Writing complex numbers in exponential form enables the use of index laws that can simplify calculations
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "dea89bdf-c7f2-47b0-a1de-af98c0b6f3c2" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_1dfff th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_1dfff td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_1dfff">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_1dfff_row0_col0" class="data row0 col0" >$ i = \sqrt{-1}$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row1_col0" class="data row1 col0" >$ z = a + ib$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row2_col0" class="data row2 col0" >$\text{ mod z} =|z| = \sqrt{a^2+b^2} $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row3_col0" class="data row3 col0" >$\tan \theta = \dfrac{b}{a} \text{ where } \theta \text{ equals arg z in interval } (-\pi, \pi]  \text{Don’t confuse with angle of a position vector which ranges from 0 to 360 degrees}$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row4_col0" class="data row4 col0" >$z = r (\cos \theta + i \sin \theta)$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row5_col0" class="data row5 col0" >$ z_1z_2  = r_1 r_2[\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)]$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row6_col0" class="data row6 col0" >$ \dfrac{z_1}{z_2}  = \dfrac{r_1}{ r_2}[\cos(\theta_1 - \theta_2) + i \sin(\theta_1 - \theta_2)], z_2 \ne 0$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row7_col0" class="data row7 col0" > $ z^n = r^n(\cos n \theta + i \sin n \theta)$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row8_col0" class="data row8 col0" >$ z^{-1} = r^{-1}(\cos \theta - i \sin \theta), z \ne 0$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row9_col0" class="data row9 col0" > $ z^{-n} = r^{-n}(\cos -n \theta + i \sin -n \theta), z \ne 0, n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row10_col0" class="data row10 col0" >$ z_1z_2...z_n = r_1r_2...r_n[\cos(\theta_1+\theta_2+...\theta_n) + i\sin(\theta_1+\theta_2+...\theta_n)]$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row11_col0" class="data row11 col0" >$ |z_1||z_2| = |z_1z_2| \text{ and arg } z_1z_2 = { arg } z_1 + { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row12_col0" class="data row12 col0" >$ \dfrac{|z_1|}{|z_2|} = \bigg| \dfrac{z_1}{z_2} \bigg| \text{ and arg } \dfrac{z_1}{z_2} = { arg } z_1 - { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row13_col0" class="data row13 col0" >$ |z|^n = |z^n| \text{ and arg } z^n = n \times \text{arg z for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row14_col0" class="data row14 col0" >$ |z^{-1}| = \dfrac{1}{|z|} \text { and arg } z^{-1} = -\text {arg z}, z\ne 0$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row15_col0" class="data row15 col0" >$ |z^{-n}| = \dfrac{1}{|z|^n} \text { and arg } z^{-n} = \text {-n arg z}, z\ne 0 \text { for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row16_col0" class="data row16 col0" >$ |z_1||z_2||z_3|...|z_n| = |z_1z_2z_3...z_n| \text { and arg } z_1z_2z_3...z_n = { arg } z_1 + { arg } z_2 + ...+ { arg } z_n \text { where } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row17_col0" class="data row17 col0" >$ \text{ If } z = \cos \theta + i\sin \theta \text{, then } z^{-1} = \overline{z} \text{ (only applies when modulus = 1)} $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row18_col0" class="data row18 col0" >$ z\overline{z} = |z|^2 \text{ and arg } z\overline{z} = 0  $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row19_col0" class="data row19 col0" >$ |\overline{z}| = |z| \text{ and arg } \overline{z} = -{arg } z $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row20_col0" class="data row20 col0" >$ \overline{z_1} + \overline{z_2} = \overline{z_1 + z_2}  $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row21_col0" class="data row21 col0" >$ \overline{z_1} \,\, \overline{z_2} = \overline{z_1 z_2}  $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row22_col0" class="data row22 col0" >$ z + \overline{z} = 2Re(z)  $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row23_col0" class="data row23 col0" >$ z - \overline{z} = 2Im(z)  $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row24_col0" class="data row24 col0" >$ {|z+w| \le |z| + |w|} \text{ (the triangle inequality where z and w are complex numbers)}  $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row25_col0" class="data row25 col0" >$ e^{i\theta} = \cos \theta + i \sin \theta, \text{ where  }\theta \in \mathbb{R}  \text{ (This is Euler's formula and represents the exponential form of a complex number)}$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row26_col0" class="data row26 col0" >$ e^{i\pi} = -1  $</td>
    </tr>
    <tr>
      <td id="T_1dfff_row27_col0" class="data row27 col0" >$ z = a+ib = r(\cos \theta + i \sin \theta) = re^{i \theta}$</td>
    </tr>
    <tr>
      <td id="T_1dfff_row28_col0" class="data row28 col0" >$ [r(\cos \theta + i \sin \theta)]^n = r^n(\cos n\theta + i\sin n\theta) =  r^ne^{in \theta}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_d23a9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_d23a9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_d23a9_row0_col0, #T_d23a9_row1_col0, #T_d23a9_row2_col0, #T_d23a9_row3_col0, #T_d23a9_row4_col0, #T_d23a9_row5_col0, #T_d23a9_row6_col0, #T_d23a9_row7_col0, #T_d23a9_row8_col0, #T_d23a9_row9_col0, #T_d23a9_row10_col0, #T_d23a9_row11_col0, #T_d23a9_row12_col0, #T_d23a9_row13_col0, #T_d23a9_row14_col0, #T_d23a9_row15_col0, #T_d23a9_row16_col0, #T_d23a9_row17_col0, #T_d23a9_row18_col0, #T_d23a9_row19_col0, #T_d23a9_row20_col0, #T_d23a9_row21_col0, #T_d23a9_row22_col0, #T_d23a9_row23_col0, #T_d23a9_row24_col0, #T_d23a9_row25_col0, #T_d23a9_row26_col0 {
  background-color: rgba(0,0,0,0);
}
#T_d23a9_row27_col0, #T_d23a9_row28_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_d23a9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_d23a9_row0_col0" class="data row0 col0" >$ i = \sqrt{-1}$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row1_col0" class="data row1 col0" >$ z = a + ib$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row2_col0" class="data row2 col0" >$\text{ mod z} =|z| = \sqrt{a^2+b^2} $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row3_col0" class="data row3 col0" >$\tan \theta = \dfrac{b}{a} \text{ where } \theta \text{ equals arg z in interval } (-\pi, \pi]  \text{Don’t confuse with angle of a position vector which ranges from 0 to 360 degrees}$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row4_col0" class="data row4 col0" >$z = r (\cos \theta + i \sin \theta)$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row5_col0" class="data row5 col0" >$ z_1z_2  = r_1 r_2[\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)]$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row6_col0" class="data row6 col0" >$ \dfrac{z_1}{z_2}  = \dfrac{r_1}{ r_2}[\cos(\theta_1 - \theta_2) + i \sin(\theta_1 - \theta_2)], z_2 \ne 0$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row7_col0" class="data row7 col0" > $ z^n = r^n(\cos n \theta + i \sin n \theta)$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row8_col0" class="data row8 col0" >$ z^{-1} = r^{-1}(\cos \theta - i \sin \theta), z \ne 0$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row9_col0" class="data row9 col0" > $ z^{-n} = r^{-n}(\cos -n \theta + i \sin -n \theta), z \ne 0, n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row10_col0" class="data row10 col0" >$ z_1z_2...z_n = r_1r_2...r_n[\cos(\theta_1+\theta_2+...\theta_n) + i\sin(\theta_1+\theta_2+...\theta_n)]$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row11_col0" class="data row11 col0" >$ |z_1||z_2| = |z_1z_2| \text{ and arg } z_1z_2 = { arg } z_1 + { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row12_col0" class="data row12 col0" >$ \dfrac{|z_1|}{|z_2|} = \bigg| \dfrac{z_1}{z_2} \bigg| \text{ and arg } \dfrac{z_1}{z_2} = { arg } z_1 - { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row13_col0" class="data row13 col0" >$ |z|^n = |z^n| \text{ and arg } z^n = n \times \text{arg z for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row14_col0" class="data row14 col0" >$ |z^{-1}| = \dfrac{1}{|z|} \text { and arg } z^{-1} = -\text {arg z}, z\ne 0$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row15_col0" class="data row15 col0" >$ |z^{-n}| = \dfrac{1}{|z|^n} \text { and arg } z^{-n} = \text {-n arg z}, z\ne 0 \text { for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row16_col0" class="data row16 col0" >$ |z_1||z_2||z_3|...|z_n| = |z_1z_2z_3...z_n| \text { and arg } z_1z_2z_3...z_n = { arg } z_1 + { arg } z_2 + ...+ { arg } z_n \text { where } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row17_col0" class="data row17 col0" >$ \text{ If } z = \cos \theta + i\sin \theta \text{, then } z^{-1} = \overline{z} \text{ (only applies when modulus = 1)} $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row18_col0" class="data row18 col0" >$ z\overline{z} = |z|^2 \text{ and arg } z\overline{z} = 0  $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row19_col0" class="data row19 col0" >$ |\overline{z}| = |z| \text{ and arg } \overline{z} = -{arg } z $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row20_col0" class="data row20 col0" >$ \overline{z_1} + \overline{z_2} = \overline{z_1 + z_2}  $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row21_col0" class="data row21 col0" >$ \overline{z_1} \,\, \overline{z_2} = \overline{z_1 z_2}  $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row22_col0" class="data row22 col0" >$ z + \overline{z} = 2Re(z)  $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row23_col0" class="data row23 col0" >$ z - \overline{z} = 2Im(z)  $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row24_col0" class="data row24 col0" >$ {|z+w| \le |z| + |w|} \text{ (the triangle inequality where z and w are complex numbers)}  $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row25_col0" class="data row25 col0" >$ e^{i\theta} = \cos \theta + i \sin \theta, \text{ where  }\theta \in \mathbb{R}  \text{ (This is Euler's formula and represents the exponential form of a complex number)}$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row26_col0" class="data row26 col0" >$ e^{i\pi} = -1  $</td>
    </tr>
    <tr>
      <td id="T_d23a9_row27_col0" class="data row27 col0" >$ z = a+ib = r(\cos \theta + i \sin \theta) = re^{i \theta}$</td>
    </tr>
    <tr>
      <td id="T_d23a9_row28_col0" class="data row28 col0" >$ [r(\cos \theta + i \sin \theta)]^n = r^n(\cos n\theta + i\sin n\theta) =  r^ne^{in \theta}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_3bff5 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_3bff5 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_3bff5_row0_col0, #T_3bff5_row1_col0, #T_3bff5_row2_col0, #T_3bff5_row3_col0, #T_3bff5_row25_col0, #T_3bff5_row26_col0, #T_3bff5_row27_col0, #T_3bff5_row28_col0 {
  background-color: rgba(0,0,0,0);
}
#T_3bff5_row4_col0, #T_3bff5_row5_col0, #T_3bff5_row6_col0, #T_3bff5_row7_col0, #T_3bff5_row8_col0, #T_3bff5_row9_col0, #T_3bff5_row10_col0, #T_3bff5_row11_col0, #T_3bff5_row12_col0, #T_3bff5_row13_col0, #T_3bff5_row14_col0, #T_3bff5_row15_col0, #T_3bff5_row16_col0, #T_3bff5_row17_col0, #T_3bff5_row18_col0, #T_3bff5_row19_col0, #T_3bff5_row20_col0, #T_3bff5_row21_col0, #T_3bff5_row22_col0, #T_3bff5_row23_col0, #T_3bff5_row24_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_3bff5">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_3bff5_row0_col0" class="data row0 col0" >$ i = \sqrt{-1}$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row1_col0" class="data row1 col0" >$ z = a + ib$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row2_col0" class="data row2 col0" >$\text{ mod z} =|z| = \sqrt{a^2+b^2} $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row3_col0" class="data row3 col0" >$\tan \theta = \dfrac{b}{a} \text{ where } \theta \text{ equals arg z in interval } (-\pi, \pi]  \text{Don’t confuse with angle of a position vector which ranges from 0 to 360 degrees}$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row4_col0" class="data row4 col0" >$z = r (\cos \theta + i \sin \theta)$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row5_col0" class="data row5 col0" >$ z_1z_2  = r_1 r_2[\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)]$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row6_col0" class="data row6 col0" >$ \dfrac{z_1}{z_2}  = \dfrac{r_1}{ r_2}[\cos(\theta_1 - \theta_2) + i \sin(\theta_1 - \theta_2)], z_2 \ne 0$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row7_col0" class="data row7 col0" > $ z^n = r^n(\cos n \theta + i \sin n \theta)$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row8_col0" class="data row8 col0" >$ z^{-1} = r^{-1}(\cos \theta - i \sin \theta), z \ne 0$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row9_col0" class="data row9 col0" > $ z^{-n} = r^{-n}(\cos -n \theta + i \sin -n \theta), z \ne 0, n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row10_col0" class="data row10 col0" >$ z_1z_2...z_n = r_1r_2...r_n[\cos(\theta_1+\theta_2+...\theta_n) + i\sin(\theta_1+\theta_2+...\theta_n)]$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row11_col0" class="data row11 col0" >$ |z_1||z_2| = |z_1z_2| \text{ and arg } z_1z_2 = { arg } z_1 + { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row12_col0" class="data row12 col0" >$ \dfrac{|z_1|}{|z_2|} = \bigg| \dfrac{z_1}{z_2} \bigg| \text{ and arg } \dfrac{z_1}{z_2} = { arg } z_1 - { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row13_col0" class="data row13 col0" >$ |z|^n = |z^n| \text{ and arg } z^n = n \times \text{arg z for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row14_col0" class="data row14 col0" >$ |z^{-1}| = \dfrac{1}{|z|} \text { and arg } z^{-1} = -\text {arg z}, z\ne 0$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row15_col0" class="data row15 col0" >$ |z^{-n}| = \dfrac{1}{|z|^n} \text { and arg } z^{-n} = \text {-n arg z}, z\ne 0 \text { for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row16_col0" class="data row16 col0" >$ |z_1||z_2||z_3|...|z_n| = |z_1z_2z_3...z_n| \text { and arg } z_1z_2z_3...z_n = { arg } z_1 + { arg } z_2 + ...+ { arg } z_n \text { where } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row17_col0" class="data row17 col0" >$ \text{ If } z = \cos \theta + i\sin \theta \text{, then } z^{-1} = \overline{z} \text{ (only applies when modulus = 1)} $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row18_col0" class="data row18 col0" >$ z\overline{z} = |z|^2 \text{ and arg } z\overline{z} = 0  $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row19_col0" class="data row19 col0" >$ |\overline{z}| = |z| \text{ and arg } \overline{z} = -{arg } z $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row20_col0" class="data row20 col0" >$ \overline{z_1} + \overline{z_2} = \overline{z_1 + z_2}  $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row21_col0" class="data row21 col0" >$ \overline{z_1} \,\, \overline{z_2} = \overline{z_1 z_2}  $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row22_col0" class="data row22 col0" >$ z + \overline{z} = 2Re(z)  $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row23_col0" class="data row23 col0" >$ z - \overline{z} = 2Im(z)  $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row24_col0" class="data row24 col0" >$ {|z+w| \le |z| + |w|} \text{ (the triangle inequality where z and w are complex numbers)}  $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row25_col0" class="data row25 col0" >$ e^{i\theta} = \cos \theta + i \sin \theta, \text{ where  }\theta \in \mathbb{R}  \text{ (This is Euler's formula and represents the exponential form of a complex number)}$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row26_col0" class="data row26 col0" >$ e^{i\pi} = -1  $</td>
    </tr>
    <tr>
      <td id="T_3bff5_row27_col0" class="data row27 col0" >$ z = a+ib = r(\cos \theta + i \sin \theta) = re^{i \theta}$</td>
    </tr>
    <tr>
      <td id="T_3bff5_row28_col0" class="data row28 col0" >$ [r(\cos \theta + i \sin \theta)]^n = r^n(\cos n\theta + i\sin n\theta) =  r^ne^{in \theta}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Using Complex Numbers </span> 
<br>