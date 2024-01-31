---
weight: 3
---

## <span style="color:RGB(0,32,96"> Introduction to Complex Numbers </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - Argand diagram
 - argument
 - Complex numbers
 - Cartesian or rectangular form
 - complex conjugate
 - complex plane
 - exponential form
 - Euler's formula
 - imaginary number
 - imaginary part
 - modulus
 - polar or modulus-argument form
 - real part
 - vector



### <span style="color:RGB(139,69,19)">  Notes </span>

 - Equivalence of complex numbers

 - Realising the denominator

 - Calculating the square of a complex number

 - Vectors of a complex number and its conjugate are reflections in  the real axis on an Argand diagram.

 - Add and subtract complex numbers utilising vector parallelogram rule

 - Multiply complex numbers by a constant

 - Tip: If a question provides 2 complex roots of a quadratic, it is simpler to substitute symbols for the roots such as a and b e.g. $(x-a)(x-b)  = 0$ and then multiply out before inserting the complex numbers

 - Be able to factorise a quadratic as a difference of squares by adding an $i^2$ to one of the sides in place of a minus one.  The real part of the square may need to be obtained by completing the square.

 - Complex numbers can be written in :
    * cartesian or rectangular form
    * polar of modulus-argument form
    * exponential form
 
 - Writing complex numbers in exponential form enables the use of index laws that can simplify calculations
<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "db28e2a6-1279-49f2-933d-7457924b9816" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_853ce th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_853ce td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_853ce">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_853ce_row0_col0" class="data row0 col0" >$ i = \sqrt{-1}$</td>
    </tr>
    <tr>
      <td id="T_853ce_row1_col0" class="data row1 col0" >$ z = a + ib$</td>
    </tr>
    <tr>
      <td id="T_853ce_row2_col0" class="data row2 col0" >$\text{ mod z} =|z| = \sqrt{a^2+b^2} $</td>
    </tr>
    <tr>
      <td id="T_853ce_row3_col0" class="data row3 col0" >$\tan \theta = \dfrac{b}{a} \text{ where } \theta \text{ equals arg z in interval } (-\pi, \pi]  \text{Don’t confuse with angle of a position vector which ranges from 0 to 360 degrees}$</td>
    </tr>
    <tr>
      <td id="T_853ce_row4_col0" class="data row4 col0" >$z = r (\cos \theta + i \sin \theta)$</td>
    </tr>
    <tr>
      <td id="T_853ce_row5_col0" class="data row5 col0" >$ z_1z_2  = r_1 r_2[\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)]$</td>
    </tr>
    <tr>
      <td id="T_853ce_row6_col0" class="data row6 col0" >$ \dfrac{z_1}{z_2}  = \dfrac{r_1}{ r_2}[\cos(\theta_1 - \theta_2) + i \sin(\theta_1 - \theta_2)], z_2 \ne 0$</td>
    </tr>
    <tr>
      <td id="T_853ce_row7_col0" class="data row7 col0" > $ z^n = r^n(\cos n \theta + i \sin n \theta)$</td>
    </tr>
    <tr>
      <td id="T_853ce_row8_col0" class="data row8 col0" >$ z^{-1} = r^{-1}(\cos \theta - i \sin \theta), z \ne 0$</td>
    </tr>
    <tr>
      <td id="T_853ce_row9_col0" class="data row9 col0" > $ z^{-n} = r^{-n}(\cos -n \theta + i \sin -n \theta), z \ne 0, n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_853ce_row10_col0" class="data row10 col0" >$ z_1z_2...z_n = r_1r_2...r_n[\cos(\theta_1+\theta_2+...\theta_n) + i\sin(\theta_1+\theta_2+...\theta_n)]$</td>
    </tr>
    <tr>
      <td id="T_853ce_row11_col0" class="data row11 col0" >$ |z_1||z_2| = |z_1z_2| \text{ and arg } z_1z_2 = { arg } z_1 + { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_853ce_row12_col0" class="data row12 col0" >$ \dfrac{|z_1|}{|z_2|} = \bigg| \dfrac{z_1}{z_2} \bigg| \text{ and arg } \dfrac{z_1}{z_2} = { arg } z_1 - { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_853ce_row13_col0" class="data row13 col0" >$ |z|^n = |z^n| \text{ and arg } z^n = n \times \text{arg z for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_853ce_row14_col0" class="data row14 col0" >$ |z^{-1}| = \dfrac{1}{|z|} \text { and arg } z^{-1} = -\text {arg z}, z\ne 0$</td>
    </tr>
    <tr>
      <td id="T_853ce_row15_col0" class="data row15 col0" >$ |z^{-n}| = \dfrac{1}{|z|^n} \text { and arg } z^{-n} = \text {-n arg z}, z\ne 0 \text { for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_853ce_row16_col0" class="data row16 col0" >$ |z_1||z_2||z_3|...|z_n| = |z_1z_2z_3...z_n| \text { and arg } z_1z_2z_3...z_n = { arg } z_1 + { arg } z_2 + ...+ { arg } z_n \text { where } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_853ce_row17_col0" class="data row17 col0" >$ \text{ If } z = \cos \theta + i\sin \theta \text{, then } z^{-1} = \overline{z} \text{ (only applies when modulus = 1)} $</td>
    </tr>
    <tr>
      <td id="T_853ce_row18_col0" class="data row18 col0" >$ z\overline{z} = |z|^2 \text{ and arg } z\overline{z} = 0  $</td>
    </tr>
    <tr>
      <td id="T_853ce_row19_col0" class="data row19 col0" >$ |\overline{z}| = |z| \text{ and arg } \overline{z} = -{arg } z $</td>
    </tr>
    <tr>
      <td id="T_853ce_row20_col0" class="data row20 col0" >$ \overline{z_1} + \overline{z_2} = \overline{z_1 + z_2}  $</td>
    </tr>
    <tr>
      <td id="T_853ce_row21_col0" class="data row21 col0" >$ \overline{z_1} \,\, \overline{z_2} = \overline{z_1 z_2}  $</td>
    </tr>
    <tr>
      <td id="T_853ce_row22_col0" class="data row22 col0" >$ z + \overline{z} = 2Re(z)  $</td>
    </tr>
    <tr>
      <td id="T_853ce_row23_col0" class="data row23 col0" >$ z - \overline{z} = 2Im(z)  $</td>
    </tr>
    <tr>
      <td id="T_853ce_row24_col0" class="data row24 col0" >$ {|z+w| \le |z| + |w|} \text{ (the triangle inequality where z and w are complex numbers)}  $</td>
    </tr>
    <tr>
      <td id="T_853ce_row25_col0" class="data row25 col0" >$ e^{i\theta} = \cos \theta + i \sin \theta, \text{ where  }\theta \in \mathbb{R}  \text{ (This is Euler's formula and represents the exponential form of a complex number)}$</td>
    </tr>
    <tr>
      <td id="T_853ce_row26_col0" class="data row26 col0" >$ e^{i\pi} = -1  $</td>
    </tr>
    <tr>
      <td id="T_853ce_row27_col0" class="data row27 col0" >$ z = a+ib = r(\cos \theta + i \sin \theta) = re^{i \theta}$</td>
    </tr>
    <tr>
      <td id="T_853ce_row28_col0" class="data row28 col0" >$ [r(\cos \theta + i \sin \theta)]^n = r^n(\cos n\theta + i\sin n\theta) =  r^ne^{in \theta}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_cc8cc th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_cc8cc td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_cc8cc_row0_col0, #T_cc8cc_row1_col0, #T_cc8cc_row2_col0, #T_cc8cc_row3_col0, #T_cc8cc_row4_col0, #T_cc8cc_row5_col0, #T_cc8cc_row6_col0, #T_cc8cc_row7_col0, #T_cc8cc_row8_col0, #T_cc8cc_row9_col0, #T_cc8cc_row10_col0, #T_cc8cc_row11_col0, #T_cc8cc_row12_col0, #T_cc8cc_row13_col0, #T_cc8cc_row14_col0, #T_cc8cc_row15_col0, #T_cc8cc_row16_col0, #T_cc8cc_row17_col0, #T_cc8cc_row18_col0, #T_cc8cc_row19_col0, #T_cc8cc_row20_col0, #T_cc8cc_row21_col0, #T_cc8cc_row22_col0, #T_cc8cc_row23_col0, #T_cc8cc_row24_col0, #T_cc8cc_row25_col0, #T_cc8cc_row26_col0 {
  background-color: rgba(0,0,0,0);
}
#T_cc8cc_row27_col0, #T_cc8cc_row28_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_cc8cc">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_cc8cc_row0_col0" class="data row0 col0" >$ i = \sqrt{-1}$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row1_col0" class="data row1 col0" >$ z = a + ib$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row2_col0" class="data row2 col0" >$\text{ mod z} =|z| = \sqrt{a^2+b^2} $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row3_col0" class="data row3 col0" >$\tan \theta = \dfrac{b}{a} \text{ where } \theta \text{ equals arg z in interval } (-\pi, \pi]  \text{Don’t confuse with angle of a position vector which ranges from 0 to 360 degrees}$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row4_col0" class="data row4 col0" >$z = r (\cos \theta + i \sin \theta)$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row5_col0" class="data row5 col0" >$ z_1z_2  = r_1 r_2[\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)]$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row6_col0" class="data row6 col0" >$ \dfrac{z_1}{z_2}  = \dfrac{r_1}{ r_2}[\cos(\theta_1 - \theta_2) + i \sin(\theta_1 - \theta_2)], z_2 \ne 0$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row7_col0" class="data row7 col0" > $ z^n = r^n(\cos n \theta + i \sin n \theta)$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row8_col0" class="data row8 col0" >$ z^{-1} = r^{-1}(\cos \theta - i \sin \theta), z \ne 0$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row9_col0" class="data row9 col0" > $ z^{-n} = r^{-n}(\cos -n \theta + i \sin -n \theta), z \ne 0, n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row10_col0" class="data row10 col0" >$ z_1z_2...z_n = r_1r_2...r_n[\cos(\theta_1+\theta_2+...\theta_n) + i\sin(\theta_1+\theta_2+...\theta_n)]$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row11_col0" class="data row11 col0" >$ |z_1||z_2| = |z_1z_2| \text{ and arg } z_1z_2 = { arg } z_1 + { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row12_col0" class="data row12 col0" >$ \dfrac{|z_1|}{|z_2|} = \bigg| \dfrac{z_1}{z_2} \bigg| \text{ and arg } \dfrac{z_1}{z_2} = { arg } z_1 - { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row13_col0" class="data row13 col0" >$ |z|^n = |z^n| \text{ and arg } z^n = n \times \text{arg z for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row14_col0" class="data row14 col0" >$ |z^{-1}| = \dfrac{1}{|z|} \text { and arg } z^{-1} = -\text {arg z}, z\ne 0$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row15_col0" class="data row15 col0" >$ |z^{-n}| = \dfrac{1}{|z|^n} \text { and arg } z^{-n} = \text {-n arg z}, z\ne 0 \text { for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row16_col0" class="data row16 col0" >$ |z_1||z_2||z_3|...|z_n| = |z_1z_2z_3...z_n| \text { and arg } z_1z_2z_3...z_n = { arg } z_1 + { arg } z_2 + ...+ { arg } z_n \text { where } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row17_col0" class="data row17 col0" >$ \text{ If } z = \cos \theta + i\sin \theta \text{, then } z^{-1} = \overline{z} \text{ (only applies when modulus = 1)} $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row18_col0" class="data row18 col0" >$ z\overline{z} = |z|^2 \text{ and arg } z\overline{z} = 0  $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row19_col0" class="data row19 col0" >$ |\overline{z}| = |z| \text{ and arg } \overline{z} = -{arg } z $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row20_col0" class="data row20 col0" >$ \overline{z_1} + \overline{z_2} = \overline{z_1 + z_2}  $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row21_col0" class="data row21 col0" >$ \overline{z_1} \,\, \overline{z_2} = \overline{z_1 z_2}  $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row22_col0" class="data row22 col0" >$ z + \overline{z} = 2Re(z)  $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row23_col0" class="data row23 col0" >$ z - \overline{z} = 2Im(z)  $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row24_col0" class="data row24 col0" >$ {|z+w| \le |z| + |w|} \text{ (the triangle inequality where z and w are complex numbers)}  $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row25_col0" class="data row25 col0" >$ e^{i\theta} = \cos \theta + i \sin \theta, \text{ where  }\theta \in \mathbb{R}  \text{ (This is Euler's formula and represents the exponential form of a complex number)}$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row26_col0" class="data row26 col0" >$ e^{i\pi} = -1  $</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row27_col0" class="data row27 col0" >$ z = a+ib = r(\cos \theta + i \sin \theta) = re^{i \theta}$</td>
    </tr>
    <tr>
      <td id="T_cc8cc_row28_col0" class="data row28 col0" >$ [r(\cos \theta + i \sin \theta)]^n = r^n(\cos n\theta + i\sin n\theta) =  r^ne^{in \theta}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_40b6b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_40b6b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_40b6b_row0_col0, #T_40b6b_row1_col0, #T_40b6b_row2_col0, #T_40b6b_row3_col0, #T_40b6b_row25_col0, #T_40b6b_row26_col0, #T_40b6b_row27_col0, #T_40b6b_row28_col0 {
  background-color: rgba(0,0,0,0);
}
#T_40b6b_row4_col0, #T_40b6b_row5_col0, #T_40b6b_row6_col0, #T_40b6b_row7_col0, #T_40b6b_row8_col0, #T_40b6b_row9_col0, #T_40b6b_row10_col0, #T_40b6b_row11_col0, #T_40b6b_row12_col0, #T_40b6b_row13_col0, #T_40b6b_row14_col0, #T_40b6b_row15_col0, #T_40b6b_row16_col0, #T_40b6b_row17_col0, #T_40b6b_row18_col0, #T_40b6b_row19_col0, #T_40b6b_row20_col0, #T_40b6b_row21_col0, #T_40b6b_row22_col0, #T_40b6b_row23_col0, #T_40b6b_row24_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_40b6b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_40b6b_row0_col0" class="data row0 col0" >$ i = \sqrt{-1}$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row1_col0" class="data row1 col0" >$ z = a + ib$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row2_col0" class="data row2 col0" >$\text{ mod z} =|z| = \sqrt{a^2+b^2} $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row3_col0" class="data row3 col0" >$\tan \theta = \dfrac{b}{a} \text{ where } \theta \text{ equals arg z in interval } (-\pi, \pi]  \text{Don’t confuse with angle of a position vector which ranges from 0 to 360 degrees}$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row4_col0" class="data row4 col0" >$z = r (\cos \theta + i \sin \theta)$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row5_col0" class="data row5 col0" >$ z_1z_2  = r_1 r_2[\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)]$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row6_col0" class="data row6 col0" >$ \dfrac{z_1}{z_2}  = \dfrac{r_1}{ r_2}[\cos(\theta_1 - \theta_2) + i \sin(\theta_1 - \theta_2)], z_2 \ne 0$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row7_col0" class="data row7 col0" > $ z^n = r^n(\cos n \theta + i \sin n \theta)$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row8_col0" class="data row8 col0" >$ z^{-1} = r^{-1}(\cos \theta - i \sin \theta), z \ne 0$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row9_col0" class="data row9 col0" > $ z^{-n} = r^{-n}(\cos -n \theta + i \sin -n \theta), z \ne 0, n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row10_col0" class="data row10 col0" >$ z_1z_2...z_n = r_1r_2...r_n[\cos(\theta_1+\theta_2+...\theta_n) + i\sin(\theta_1+\theta_2+...\theta_n)]$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row11_col0" class="data row11 col0" >$ |z_1||z_2| = |z_1z_2| \text{ and arg } z_1z_2 = { arg } z_1 + { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row12_col0" class="data row12 col0" >$ \dfrac{|z_1|}{|z_2|} = \bigg| \dfrac{z_1}{z_2} \bigg| \text{ and arg } \dfrac{z_1}{z_2} = { arg } z_1 - { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row13_col0" class="data row13 col0" >$ |z|^n = |z^n| \text{ and arg } z^n = n \times \text{arg z for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row14_col0" class="data row14 col0" >$ |z^{-1}| = \dfrac{1}{|z|} \text { and arg } z^{-1} = -\text {arg z}, z\ne 0$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row15_col0" class="data row15 col0" >$ |z^{-n}| = \dfrac{1}{|z|^n} \text { and arg } z^{-n} = \text {-n arg z}, z\ne 0 \text { for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row16_col0" class="data row16 col0" >$ |z_1||z_2||z_3|...|z_n| = |z_1z_2z_3...z_n| \text { and arg } z_1z_2z_3...z_n = { arg } z_1 + { arg } z_2 + ...+ { arg } z_n \text { where } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row17_col0" class="data row17 col0" >$ \text{ If } z = \cos \theta + i\sin \theta \text{, then } z^{-1} = \overline{z} \text{ (only applies when modulus = 1)} $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row18_col0" class="data row18 col0" >$ z\overline{z} = |z|^2 \text{ and arg } z\overline{z} = 0  $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row19_col0" class="data row19 col0" >$ |\overline{z}| = |z| \text{ and arg } \overline{z} = -{arg } z $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row20_col0" class="data row20 col0" >$ \overline{z_1} + \overline{z_2} = \overline{z_1 + z_2}  $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row21_col0" class="data row21 col0" >$ \overline{z_1} \,\, \overline{z_2} = \overline{z_1 z_2}  $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row22_col0" class="data row22 col0" >$ z + \overline{z} = 2Re(z)  $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row23_col0" class="data row23 col0" >$ z - \overline{z} = 2Im(z)  $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row24_col0" class="data row24 col0" >$ {|z+w| \le |z| + |w|} \text{ (the triangle inequality where z and w are complex numbers)}  $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row25_col0" class="data row25 col0" >$ e^{i\theta} = \cos \theta + i \sin \theta, \text{ where  }\theta \in \mathbb{R}  \text{ (This is Euler's formula and represents the exponential form of a complex number)}$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row26_col0" class="data row26 col0" >$ e^{i\pi} = -1  $</td>
    </tr>
    <tr>
      <td id="T_40b6b_row27_col0" class="data row27 col0" >$ z = a+ib = r(\cos \theta + i \sin \theta) = re^{i \theta}$</td>
    </tr>
    <tr>
      <td id="T_40b6b_row28_col0" class="data row28 col0" >$ [r(\cos \theta + i \sin \theta)]^n = r^n(\cos n\theta + i\sin n\theta) =  r^ne^{in \theta}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Using Complex Numbers </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - De Moivre's therom
 - locus
 - roots of unity


<BR><BR>

### <span style="color:RGB(139,69,19)">  Notes </span>

#### De Moivre's therom
 - For any non-zero complex number $z = \cos \theta + i \sin \theta = e^{i\theta}$

 - Polar form:  $(\cos \theta + i \sin \theta)^n = \cos n \theta + i \sin n \theta = e^{in \theta}, \forall n \in \mathbb{Q}$ 

 - Exponential form: $(e ^ {i \theta})^n = e ^ {in \theta},  \forall  n \in \mathbb{Q}$ 

 - Be able to prove the above (note that above formulas also hold for real values of n but this is outside the scope of Year 12 Ext 2)

  - Tip: if the equation is in the format $\cos \theta + i \sin \theta $, then it needs to be converted into polar format before De Moivre's therom can be applied that is, $ \cos (-\theta) + i \sin (-\theta) $

 - Be able to use De Moivre's therom to derive trig identities

 - Below 2 formula are not listed in the syllabus but can easily be derived using De Moivre's therom:
     - $z^n + \dfrac{1}{z^n} = 2 \cos n \theta $
     
     - $z^n - \dfrac{1}{z^n} = 2i \sin n \theta $


<BR><BR>

#### Quadratic equations with complex coefficients

 - Quadratic equations
     - if coefficients are real then the complex roots are always in conjugate pairs
     - if the coefficients are complex the roots will not be conjugate pairs

<BR><BR>

#### Polynomial equations

**Complex conjugate root therom** <br>
If a polynomial equation P(z) = 0 has real coefficients and if $\alpha = ai + b, a,b \in \mathbb{R} $   is a root of P(z) = 0 then $ \overline{\alpha}  = a - ib $ is also a root of P(z) = 0

**Real and complex roots** <br>
Given a polynomial equation P(z) = 0 with *real* coefficients and a degree of n:
 - If n is odd then P(z) = 0 
     - has at least one real root
    - the complex roots come in conjugate pairs (if they exist)
 
 - If n is even then P(z) = 0 has 
      - no real roots or an even number of real roots
      - the complex roots come in conjugate pairs (if they exist)
 
 - if P(z) = 0 has complex roots $\alpha = a+ib$ and $\overline{\alpha} = a - ib$, <br>
 then P(z) = 0 will have a quadratic factor of the form <br>
 $(x-\alpha)(x-\overline{\alpha}) = [x^2 - (\alpha + \overline{\alpha})x +\alpha \overline{\alpha}]$


<BR><BR>
#### Operations on the complex plane

**Multiplying complex numbers**

 - $z_1 z_2 = r_1 r_2 [\cos (\theta_1 + \theta_2) = i \sin (\theta_1 + \theta_2)] $

  - *Geometrically* this means that the product of vectors $\underset{\sim}{z}$ and $\underset{\sim}{w}$ : 
     - will have a length of $|\underset{\sim}{z}||\underset{\sim}{w}|$
     - will have an argument of arg $\underset{\sim}{z}$ + arg $\underset{\sim}{w}$, that is the argument of $\underset{\sim}{z}$ is rotated anti-clockwise by the argument of $\underset{\sim}{w}$

**Dividing complex numbers**

 - $\dfrac{z_1}{z_2} = \dfrac{r_1}{r_2} [\cos (\theta_1 - \theta_2) = i \sin (\theta_1 - \theta_2)] $

  - *Geometrically* this means that the product of vectors $\underset{\sim}{z}$ and $\underset{\sim}{w}$ : 
     - will have a length of $\dfrac{|\underset{\sim}{z}|}{|\underset{\sim}{w}|}$
     - will have an argument of arg $\underset{\sim}{z}$ - arg $\underset{\sim}{w}$, that is the argument of $\underset{\sim}{z}$ is rotated clockwise by the argument of $\underset{\sim}{w}$

**Multiplying and dividing by i**

Given that $ i = 1(\cos \dfrac{\pi}{2} + i \sin \dfrac{\pi}{2})$:
 - Multiplying $\underset{\sim}{z}$ by i rotates $\underset{\sim}{z}$  anti-clockwise by $ \dfrac{\pi}{2}$
 - Dividing $\underset{\sim}{z}$ by i rotates $\underset{\sim}{z} $ clockwise by $ \dfrac{\pi}{2}$
 - The modulus remains unchanged
 - Division by i is the same as  multiplication by -i
 - Multiplication by i is the same as division by -i
<BR><BR>

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
<style type="text/css">
#T_72275 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_72275 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_72275">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_72275_row0_col0" class="data row0 col0" >$(e ^ {i \theta})^n = e ^ {in \theta} $</td>
    </tr>
    <tr>
      <td id="T_72275_row1_col0" class="data row1 col0" >$z^n + \dfrac{1}{z^n} = 2 \cos n \theta $</td>
    </tr>
    <tr>
      <td id="T_72275_row2_col0" class="data row2 col0" >$z^n - \dfrac{1}{z^n} = 2i \sin n \theta $</td>
    </tr>
    <tr>
      <td id="T_72275_row3_col0" class="data row3 col0" >$ i = 1(\cos \dfrac{\pi}{2} + i \sin \dfrac{\pi}{2})$</td>
    </tr>
  </tbody>
</table>
