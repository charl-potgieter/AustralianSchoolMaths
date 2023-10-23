---
weight: 9
---

## <span style="color:RGB(0,32,96"> Introduction to Complex Numbers </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "69cbc307-b5e6-45f9-8d0f-153a5a55a662" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_4bcc4 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4bcc4 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_4bcc4">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4bcc4_row0_col0" class="data row0 col0" >$ i = \sqrt{-1}$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row1_col0" class="data row1 col0" >$ z = a + ib$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row2_col0" class="data row2 col0" >$\text{ mod z} =|z| = \sqrt{a^2+b^2} $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row3_col0" class="data row3 col0" >$tan \theta = \dfrac{b}{a} \text{ where } \theta \text{ equals arg z in interval } (-\pi, \pi]$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row4_col0" class="data row4 col0" >$z = r (cos \theta + i sin \theta)$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row5_col0" class="data row5 col0" >$ z_1z_2  = r_1 r_2[cos(\theta_1 + \theta_2) + i sin(\theta_1 + \theta_2)]$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row6_col0" class="data row6 col0" >$ \dfrac{z_1}{z_2}  = \dfrac{r_1}{ r_2}[cos(\theta_1 - \theta_2) + i sin(\theta_1 - \theta_2)], z_2 \ne 0$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row7_col0" class="data row7 col0" > $ z^n = r^n[cos (n \theta) + i sin (n \theta)]$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row8_col0" class="data row8 col0" >$ z^{-1} = r^{-1}(cos \theta - i sin \theta), z \ne 0$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row9_col0" class="data row9 col0" > $ z^{-n} = r^{-n}[cos (-n \theta) + i sin (-n \theta)], z \ne 0, n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row10_col0" class="data row10 col0" >$ z_1z_2...z_n = r_1r_2...r_n[cos(\theta_1+\theta_2+...\theta_n) + isin(\theta_1+\theta_2+...\theta_n)]$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row11_col0" class="data row11 col0" >$ |z_1||z_2| = |z_1z_2| \text{ and arg } z_1z_2 = { arg } z_1 + { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row12_col0" class="data row12 col0" >$ \dfrac{|z_1|}{|z_2|} = \bigg| \dfrac{z_1}{z_2} \bigg| \text{ and arg } \dfrac{z_1}{z_2} = { arg } z_1 - { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row13_col0" class="data row13 col0" >$ |z|^n = |z^n| \text{ and arg } z^n = n \times \text{arg z for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row14_col0" class="data row14 col0" >$ |z^{-1}| = \dfrac{1}{|z|} \text { and arg } z^{-1} = -\text {arg z}, z\ne 0$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row15_col0" class="data row15 col0" >$ |z^{-n}| = \dfrac{1}{|z|^n} \text { and arg } z^{-n} = \text {-n arg z}, z\ne 0 \text { for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row16_col0" class="data row16 col0" >$ |z_1||z_2||z_3|...|z_n| = |z_1z_2z_3...z_n| \text { and arg } z_1z_2z_3...z_n = { arg } z_1 + { arg } z_2 + ...+ { arg } z_n \text { where } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row17_col0" class="data row17 col0" >$ \text{ If } z = cos \theta + isin \theta \text{, then } z^{-1} = \overline{z} \text{ (only applies when modulus = 1)} $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row18_col0" class="data row18 col0" >$ z\overline{z} = |z|^2 \text{ and arg } z\overline{z} = 0  $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row19_col0" class="data row19 col0" >$ |\overline{z}| = |z| \text{ and arg } |\overline{z}| = -{arg } z $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row20_col0" class="data row20 col0" >$ \overline{z_1} + \overline{z_2} = \overline{z_1 + z_2}  $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row21_col0" class="data row21 col0" >$ \overline{z_1} \,\, \overline{z_2} = \overline{z_1 z_2}  $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row22_col0" class="data row22 col0" >$ z + \overline{z} = 2Re(z)  $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row23_col0" class="data row23 col0" >$ z - \overline{z} = 2Im(z)  $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row24_col0" class="data row24 col0" >$ {|z+w| \le |z| + |w|} \text{ (the triangle inequality where z and w are complex numbers)}  $</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row25_col0" class="data row25 col0" >$ e^{i\theta} = cos \theta + i sin \theta, \text{ where  }\theta \in \mathbb{R}  \text{ (This is Euler's formula and represents the exponential form of a complex number)}$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row26_col0" class="data row26 col0" >$ z = a+ib = r(cos \theta + i sin \theta) = re^{i \theta}$</td>
    </tr>
    <tr>
      <td id="T_4bcc4_row27_col0" class="data row27 col0" >$ [r(cos \theta + i sin \theta)]^n = r^n[cos(n\theta) + isin(n\theta)] =  r^ne^{in \theta}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_c64d5 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c64d5 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_c64d5_row0_col0, #T_c64d5_row1_col0, #T_c64d5_row2_col0, #T_c64d5_row3_col0, #T_c64d5_row4_col0, #T_c64d5_row5_col0, #T_c64d5_row6_col0, #T_c64d5_row7_col0, #T_c64d5_row8_col0, #T_c64d5_row9_col0, #T_c64d5_row10_col0, #T_c64d5_row11_col0, #T_c64d5_row12_col0, #T_c64d5_row13_col0, #T_c64d5_row14_col0, #T_c64d5_row15_col0, #T_c64d5_row16_col0, #T_c64d5_row17_col0, #T_c64d5_row18_col0, #T_c64d5_row19_col0, #T_c64d5_row20_col0, #T_c64d5_row21_col0, #T_c64d5_row22_col0, #T_c64d5_row23_col0, #T_c64d5_row24_col0, #T_c64d5_row25_col0 {
  background-color: rgba(0,0,0,0);
}
#T_c64d5_row26_col0, #T_c64d5_row27_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_c64d5">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c64d5_row0_col0" class="data row0 col0" >$ i = \sqrt{-1}$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row1_col0" class="data row1 col0" >$ z = a + ib$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row2_col0" class="data row2 col0" >$\text{ mod z} =|z| = \sqrt{a^2+b^2} $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row3_col0" class="data row3 col0" >$tan \theta = \dfrac{b}{a} \text{ where } \theta \text{ equals arg z in interval } (-\pi, \pi]$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row4_col0" class="data row4 col0" >$z = r (cos \theta + i sin \theta)$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row5_col0" class="data row5 col0" >$ z_1z_2  = r_1 r_2[cos(\theta_1 + \theta_2) + i sin(\theta_1 + \theta_2)]$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row6_col0" class="data row6 col0" >$ \dfrac{z_1}{z_2}  = \dfrac{r_1}{ r_2}[cos(\theta_1 - \theta_2) + i sin(\theta_1 - \theta_2)], z_2 \ne 0$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row7_col0" class="data row7 col0" > $ z^n = r^n[cos (n \theta) + i sin (n \theta)]$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row8_col0" class="data row8 col0" >$ z^{-1} = r^{-1}(cos \theta - i sin \theta), z \ne 0$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row9_col0" class="data row9 col0" > $ z^{-n} = r^{-n}[cos (-n \theta) + i sin (-n \theta)], z \ne 0, n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row10_col0" class="data row10 col0" >$ z_1z_2...z_n = r_1r_2...r_n[cos(\theta_1+\theta_2+...\theta_n) + isin(\theta_1+\theta_2+...\theta_n)]$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row11_col0" class="data row11 col0" >$ |z_1||z_2| = |z_1z_2| \text{ and arg } z_1z_2 = { arg } z_1 + { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row12_col0" class="data row12 col0" >$ \dfrac{|z_1|}{|z_2|} = \bigg| \dfrac{z_1}{z_2} \bigg| \text{ and arg } \dfrac{z_1}{z_2} = { arg } z_1 - { arg } z_2$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row13_col0" class="data row13 col0" >$ |z|^n = |z^n| \text{ and arg } z^n = n \times \text{arg z for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row14_col0" class="data row14 col0" >$ |z^{-1}| = \dfrac{1}{|z|} \text { and arg } z^{-1} = -\text {arg z}, z\ne 0$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row15_col0" class="data row15 col0" >$ |z^{-n}| = \dfrac{1}{|z|^n} \text { and arg } z^{-n} = \text {-n arg z}, z\ne 0 \text { for } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row16_col0" class="data row16 col0" >$ |z_1||z_2||z_3|...|z_n| = |z_1z_2z_3...z_n| \text { and arg } z_1z_2z_3...z_n = { arg } z_1 + { arg } z_2 + ...+ { arg } z_n \text { where } n \in \mathbb{Z}$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row17_col0" class="data row17 col0" >$ \text{ If } z = cos \theta + isin \theta \text{, then } z^{-1} = \overline{z} \text{ (only applies when modulus = 1)} $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row18_col0" class="data row18 col0" >$ z\overline{z} = |z|^2 \text{ and arg } z\overline{z} = 0  $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row19_col0" class="data row19 col0" >$ |\overline{z}| = |z| \text{ and arg } |\overline{z}| = -{arg } z $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row20_col0" class="data row20 col0" >$ \overline{z_1} + \overline{z_2} = \overline{z_1 + z_2}  $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row21_col0" class="data row21 col0" >$ \overline{z_1} \,\, \overline{z_2} = \overline{z_1 z_2}  $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row22_col0" class="data row22 col0" >$ z + \overline{z} = 2Re(z)  $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row23_col0" class="data row23 col0" >$ z - \overline{z} = 2Im(z)  $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row24_col0" class="data row24 col0" >$ {|z+w| \le |z| + |w|} \text{ (the triangle inequality where z and w are complex numbers)}  $</td>
    </tr>
    <tr>
      <td id="T_c64d5_row25_col0" class="data row25 col0" >$ e^{i\theta} = cos \theta + i sin \theta, \text{ where  }\theta \in \mathbb{R}  \text{ (This is Euler's formula and represents the exponential form of a complex number)}$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row26_col0" class="data row26 col0" >$ z = a+ib = r(cos \theta + i sin \theta) = re^{i \theta}$</td>
    </tr>
    <tr>
      <td id="T_c64d5_row27_col0" class="data row27 col0" >$ [r(cos \theta + i sin \theta)]^n = r^n[cos(n\theta) + isin(n\theta)] =  r^ne^{in \theta}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Using Complex Numbers </span> 
<br>