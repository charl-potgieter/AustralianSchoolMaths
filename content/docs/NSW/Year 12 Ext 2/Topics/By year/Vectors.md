---
weight: 2
---

## <span style="color:RGB(0,32,96"> Further Work with Vectors </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - cartesian equations
 - parametric equations
 - perpendicular vectors
  - $\underset{\sim}{\hat{v}}$ is the unit vector of $\underset{\sim}{v}$ 

 Note that concepts covered in Year 12 Ext 1 are not repeated above

 


### <span style="color:RGB(139,69,19)">  Notes </span>

**General**
 - Unit vectors *i, j,* and  *k* represent directions x, y, and z respectively
 
 - The vector from $A(x_1, y_1, z_1)$ to $B(x_12 y_2, z_2)$ <br>
 $= \vec{AB} $ <br>
 $= (x_2-x_1)i + (y_2-y1)j+(z_2-z1)k$

 **Geometry proofs using vectors**
 - parallel vectors in the same direction $\underset{\sim}{u} . \underset{\sim}{v} = |\underset{\sim}{u}|\underset{\sim}{v}|$ 
 - parallel vectors in the opposite direction $\underset{\sim}{u} . \underset{\sim}{v} = |\underset{\sim}{u}|\underset{\sim}{v}|$ 
  - Below 2 vectors are parallel if $x_2,y_2,z_2$ are in same ratio (fixed multiple) as $x_1,y_1,z_1$ <br>

  
    <div>
    $\begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}a \\ b \\ c\end{pmatrix} + \begin{pmatrix}x_1 \\ y_1 \\ z_1\end{pmatrix}$ 
    </div>
    <br>
    <div>$\begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}d \\ e \\ f\end{pmatrix} + \begin{pmatrix}x_2 \\ y_2 \\ z_2\end{pmatrix}$</div>
  - perpendicular vectors $\underset{\sim}{u} . \underset{\sim}{v} =0$
  - single vector midpoint $\dfrac{\underset{\sim}{u}}{2}$
  - sum of vector midpoint $\dfrac{\underset{\sim}{u} + \underset{\sim}{v}}{2}$
  - vector from $\underset{\sim}{u}$ to the midpoint between vectors $\underset{\sim}{u}$ and $\underset{\sim}{v} = \dfrac {\underset{\sim}{u} - \underset{\sim}{v}}{2}$

 **Vector equation of a curve**
  - Parametric equations can be used to represent a line in 3D space using vectors
  - The equation is a function of parameter t (note: not a function of x like "standard" graphs)
  - vector equation format <br>
  
   <div>
   $\begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}a \\ b \\ c\end{pmatrix} + t \begin{pmatrix}x_1 \\ y_1 \\ z_1\end{pmatrix}$
   </div> 
   <br> or <br>
   <div>
   $\begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}f(t) \\ g(t) \\ h(t)\end{pmatrix}$
   </div>
 - The above vector equation can be represented by below parametric equations:
    - $ x = a + tx_1$
    - $ y = b + ty_1$
    - $ x = c + tz_1$ <br>
    Note that there is no reference to i, j and k in the parametric equations
 - example = cartesian equation of a sphere with centre (a,b,c) and radius r <br>
    $ = (x-a)^2 + (y-b)^2 +(z-c)^2 = r^2$

 **Vector equation of a straight line**
<br> 
A line through points A and B can be represented as $r = \underset{\sim}{a} + \lambda \underset{\sim}{b}$, <br>
where, <br>
 - $\underset{\sim}{a}= \vec{OB}$, a vector from the origin
 - $\underset{\sim}{b}= \vec{AB}$, the direction of the required line
 - $ \lambda $ is a parameter

The below parametric equations:
 - $ x = a_1 + \lambda b_1 $
 - $ y = a_2 + \lambda b_2 $
 - $ z = a_3 + \lambda b_3 $<br> 
 
 can be written in cartesian format as below
$ \lambda = \dfrac{x - a_1}{b_1} = \dfrac{y - a_2}{b_2} = \dfrac{z - a_3}{b_3} $ <br>
(Equations are simply reworked with the parameter lambda as the subject of the equation)


<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "18cdc9d9-e9be-42bc-ac9b-57d053a3af41" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_952fc th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_952fc td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_952fc">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_952fc_row0_col0" class="data row0 col0" >$\underset{\sim}{u} + \underset{\sim}{v} = \underset{\sim}{v} + \underset{\sim}{u}$ </td>
    </tr>
    <tr>
      <td id="T_952fc_row1_col0" class="data row1 col0" >$(\underset{\sim}{u} + \underset{\sim}{v}) + \underset{\sim}{w} = \underset{\sim}{u} + (\underset{\sim}{v} + \underset{\sim}{w} )$ </td>
    </tr>
    <tr>
      <td id="T_952fc_row2_col0" class="data row2 col0" >$\underset{\sim}{u} + 0 = \underset{\sim}{u}$ </td>
    </tr>
    <tr>
      <td id="T_952fc_row3_col0" class="data row3 col0" >$|\underset{\sim}{u} + \underset{\sim}{v}| \le |\underset{\sim}{u}| + |\underset{\sim}{v}|$ </td>
    </tr>
    <tr>
      <td id="T_952fc_row4_col0" class="data row4 col0" >$|r| = \sqrt{x^2+y^2+z^2}$</td>
    </tr>
    <tr>
      <td id="T_952fc_row5_col0" class="data row5 col0" >$\underset{\sim}{u} . \underset{\sim}{v} = x_1x_2 + y_1y_2 + z_1z_2 = |\underset{\sim}{u}|\underset{\sim}{v}| \cos \theta$</td>
    </tr>
    <tr>
      <td id="T_952fc_row6_col0" class="data row6 col0" >$\underset{\sim}{u} . \underset{\sim}{v}  = \underset{\sim}{v} . \underset{\sim}{u}$</td>
    </tr>
    <tr>
      <td id="T_952fc_row7_col0" class="data row7 col0" >$\underset{\sim}{u} . (\underset{\sim}{v} +\underset{\sim}{w})   = \underset{\sim}{u} . \underset{\sim}{v} + \underset{\sim}{u} . \underset{\sim}{w}$</td>
    </tr>
    <tr>
      <td id="T_952fc_row8_col0" class="data row8 col0" >$r = \underset{\sim}{a} + \lambda \underset{\sim}{b}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_b1201 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_b1201 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_b1201_row0_col0, #T_b1201_row1_col0, #T_b1201_row2_col0, #T_b1201_row3_col0, #T_b1201_row4_col0, #T_b1201_row5_col0, #T_b1201_row6_col0, #T_b1201_row7_col0 {
  background-color: rgba(0,0,0,0);
}
#T_b1201_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_b1201">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_b1201_row0_col0" class="data row0 col0" >$\underset{\sim}{u} + \underset{\sim}{v} = \underset{\sim}{v} + \underset{\sim}{u}$ </td>
    </tr>
    <tr>
      <td id="T_b1201_row1_col0" class="data row1 col0" >$(\underset{\sim}{u} + \underset{\sim}{v}) + \underset{\sim}{w} = \underset{\sim}{u} + (\underset{\sim}{v} + \underset{\sim}{w} )$ </td>
    </tr>
    <tr>
      <td id="T_b1201_row2_col0" class="data row2 col0" >$\underset{\sim}{u} + 0 = \underset{\sim}{u}$ </td>
    </tr>
    <tr>
      <td id="T_b1201_row3_col0" class="data row3 col0" >$|\underset{\sim}{u} + \underset{\sim}{v}| \le |\underset{\sim}{u}| + |\underset{\sim}{v}|$ </td>
    </tr>
    <tr>
      <td id="T_b1201_row4_col0" class="data row4 col0" >$|r| = \sqrt{x^2+y^2+z^2}$</td>
    </tr>
    <tr>
      <td id="T_b1201_row5_col0" class="data row5 col0" >$\underset{\sim}{u} . \underset{\sim}{v} = x_1x_2 + y_1y_2 + z_1z_2 = |\underset{\sim}{u}|\underset{\sim}{v}| \cos \theta$</td>
    </tr>
    <tr>
      <td id="T_b1201_row6_col0" class="data row6 col0" >$\underset{\sim}{u} . \underset{\sim}{v}  = \underset{\sim}{v} . \underset{\sim}{u}$</td>
    </tr>
    <tr>
      <td id="T_b1201_row7_col0" class="data row7 col0" >$\underset{\sim}{u} . (\underset{\sim}{v} +\underset{\sim}{w})   = \underset{\sim}{u} . \underset{\sim}{v} + \underset{\sim}{u} . \underset{\sim}{w}$</td>
    </tr>
    <tr>
      <td id="T_b1201_row8_col0" class="data row8 col0" >$r = \underset{\sim}{a} + \lambda \underset{\sim}{b}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}