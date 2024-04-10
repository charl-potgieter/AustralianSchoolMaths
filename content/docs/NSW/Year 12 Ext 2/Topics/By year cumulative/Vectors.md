---
weight: 8
---

## <span style="color:RGB(0,32,96"> Introduction to Vectors </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>

 - column vector notation
 - component form
 - displacement vector
 - equal vectors
 - magnitude or modulus of a vector
 - negative vector
 - parallel vectors
 - position vector
 - scalar
 - unit vector
 - vector
 - scalar multiplication
 - dot product or scalar product
 - projectile
 - projectile motion
 - projection of a vector


### <span style="color:RGB(139,69,19)">  Notes </span>

 - Vectors vs scalars

 - Triangle law of addition

 - Parallelogram law of addition

 - Subtracting vectors using the triangle rule

 - Subtracting vectors using the parallelogram rule

 - Adding and subtracting vectors numerically

 - Scalar multiplication

 - Magnitude of a position vector

 - Magnitude of a displacement vector

 - Direction of a position vector

 - Direction of a displacement vector

 - Don't confuse dot product $\underset{\sim}{u}.\underset{\sim}{v}$ and product of vector magnitudes $|\underset{\sim}{u}||\underset{\sim}{v}|$

 - Geometric proofs using vector examples

 - See formulas below for vectors parallel in like and unlike directions.  Also note vectors are parallel if one is a scalar multiple of another.

 - Length of vector x unit vector = the vector itself

 - Equal vectors have the same magnitude and direction but don’t need to have the same position on the cartesian plane

 - Tip-to-tail addition of vectors can be applied to more than 2 vectors

 - Bearing is measured clockwise from north

 - Direction is measured anti-clockwise from  Easterly horizon

 - The path of projectile motion is a parabola

 - Acceleration due to gravity is the only acceleration that a projectile undergoes.  It can be subject to other velocity vectors though.

 - Note that it is useful to know below formulas but they cannot be used directly in any answers, they need to be derived from the gravity acceleration formula and the initial velocity formula

 - Projectile acceleration vector = $0\underset{\sim}{i}  +  -g\underset{\sim}{j}$

 - Projectile velocity vector = $v\cos\theta \underset{\sim}{i}  + (-gt + V \sin \theta) \underset{\sim}{j}$

 - Projectile displacement vector = $vt\cos\theta \underset{\sim}{i}  + (\dfrac{-gt^2}{2} + Vt \sin \theta) \underset{\sim}{j}$

 - Note from above that the horizontal component of the velocity vector is independent of time t, whereas the horizontal component of the displacement vector is dependent on t.

 - In order to calculate the velocity vector of a projectile :
    * Calculate the integral of the acceleration vector which includes a constant, say C
    * Get the initial velocity of the vector using $ v\cos\theta \underset{\sim}{i}  + v \sin \theta \underset{\sim}{j} $
    * Substitute above into the gravity velocity vector at time zero to solve for C

 - In order to calculate the displacement vector of a projectile :
    * Calculate the integral of the velocity vector which includes a constant, say D.  The velocity vector is as calculated above.
    * Get the displacement vector at time zero assuming horizontal component  = 0 = the start point and vertical component  = distance from vertical end point
    *  Substitute the above equations into one another to solve for the constant D

 - Projectile calculation notes :
    * Measure vertical displacement vector from where an object lands  - it should make no difference if measured from starting vertical point but ending vertical point is generally used if it is known
    * Measure horizontal displacement vector from starting point that is starting point =  zero horizontal displacement.  This is done as we generally dont know the ending point but in theory doesnt make a difference and end point may have to be used depending on question.
    * Speed  = magnitude of velocity vector at a specific time = $| \underset{\sim}{v} |$
    * Max height occurs when the vertical component of the velocity vector is zero
    * Max height is the vertical component of the displacement vector when the vertical component of the velocity vector is zero
    * Time of flight occurs when the vertical component of the displacement vector is zero
    * range of flight or horizontal range is the horizontal component of the displacement vector at the time that the vertical component of the displacement vector is zero

<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "67412b52-efc5-46b5-a0a1-7353559f897a" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_5f9b9 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_5f9b9 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_5f9b9">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_5f9b9_row0_col0" class="data row0 col0" >$ \vec{AB} + \vec{BC} = \vec{AC} $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row1_col0" class="data row1 col0" >$ |\underset{\sim}{u}| = |x\underset{\sim}{i} + y\underset{\sim}{j}| = \sqrt{x^2+y^2}  $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row2_col0" class="data row2 col0" >$ \underset{\sim}{a} +  (-\underset{\sim}{a}) =0  $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row3_col0" class="data row3 col0" >$ \vec{AB} - \vec{AD} =  \vec{AB} + \vec{DA} =  \vec{DA} + \vec{AB} = \vec{DB}  $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row4_col0" class="data row4 col0" >$ \text{The unit vector parallel to } \underset{\sim}{v} =  \underset{\sim}{v} * \dfrac{1}{|\underset{\sim}{v}|} $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row5_col0" class="data row5 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} +  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  \begin{pmatrix} a_1 + a_2 \\b_1 + b_2 \end{pmatrix} $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row6_col0" class="data row6 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} -  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  \begin{pmatrix} a_1 - a_2 \\b_1 - b_2 \end{pmatrix} $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row7_col0" class="data row7 col0" >$\lambda \begin{pmatrix} a \\b \end{pmatrix} =  \begin{pmatrix} \lambda a \\ \lambda b \end{pmatrix}$</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row8_col0" class="data row8 col0" >$|\underset{\sim}{u}| = \sqrt{x^2 + y^2}$</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row9_col0" class="data row9 col0" >$|\vec{XY}|  =  \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row10_col0" class="data row10 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} +  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  (a_1 + a_2)\underset{\sim}{i} + (b_1+b_2)\underset{\sim}{j} $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row11_col0" class="data row11 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} -  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  (a_1 - a_2)\underset{\sim}{i} + (b_1-b_2)\underset{\sim}{j} $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row12_col0" class="data row12 col0" >$\underset{\sim}{u}.\underset{\sim}{v} = |\underset{\sim}{u}||\underset{\sim}{v}|\cos\theta = x_1x_2 + y_1y_2 $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row13_col0" class="data row13 col0" >$\underset{\sim}{v}.\underset{\sim}{v} = |\underset{\sim}{v}|^2 $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row14_col0" class="data row14 col0" >$ \text{perpendicular vectors: }\underset{\sim}{u}.\underset{\sim}{v} = 0 $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row15_col0" class="data row15 col0" >$ \text{parallel vectors like directions: }\underset{\sim}{u}.\underset{\sim}{v} = |\underset{\sim}{u}||\underset{\sim}{v}| $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row16_col0" class="data row16 col0" >$ \text{parallel vectors unlike directions: }\underset{\sim}{u}.\underset{\sim}{v} = -|\underset{\sim}{u}||\underset{\sim}{v}| $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row17_col0" class="data row17 col0" >$ P_{\underset{\sim}{u}}\underset{\sim}{v} = \dfrac{\underset{\sim}{u}.\underset{\sim}{v}}{|\underset{\sim}{u}|^2} \underset{\sim}{u} $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row18_col0" class="data row18 col0" >$ \underset{\sim}{u} = (r\cos\theta, r\sin\theta) = r\cos\theta \underset{\sim}{i} + r\sin\theta \underset{\sim}{j}  $</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row19_col0" class="data row19 col0" >$ \underset{\sim}{v}  =  \int \underset{\sim}{a} \; dt$</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row20_col0" class="data row20 col0" >$ \underset{\sim}{s}  =  \int \underset{\sim}{v} \; dt$</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row21_col0" class="data row21 col0" >$\text{Initial velocity of a vector } =  \underset{\sim}{v}  =  v\cos\theta \underset{\sim}{i}  + v \sin \theta \underset{\sim}{j} \text{ where v is the initial speed, a scalar}$</td>
    </tr>
    <tr>
      <td id="T_5f9b9_row22_col0" class="data row22 col0" >$\text{acceleration due to gravity } =  \underset{\sim}{a}  =  -g\underset{\sim}{j}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_93b2f th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_93b2f td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_93b2f_row0_col0, #T_93b2f_row2_col0, #T_93b2f_row3_col0, #T_93b2f_row4_col0, #T_93b2f_row5_col0, #T_93b2f_row6_col0, #T_93b2f_row7_col0, #T_93b2f_row8_col0, #T_93b2f_row9_col0, #T_93b2f_row10_col0, #T_93b2f_row11_col0, #T_93b2f_row13_col0, #T_93b2f_row14_col0, #T_93b2f_row15_col0, #T_93b2f_row16_col0, #T_93b2f_row17_col0, #T_93b2f_row18_col0, #T_93b2f_row19_col0, #T_93b2f_row20_col0, #T_93b2f_row21_col0, #T_93b2f_row22_col0 {
  background-color: rgba(0,0,0,0);
}
#T_93b2f_row1_col0, #T_93b2f_row12_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_93b2f">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_93b2f_row0_col0" class="data row0 col0" >$ \vec{AB} + \vec{BC} = \vec{AC} $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row1_col0" class="data row1 col0" >$ |\underset{\sim}{u}| = |x\underset{\sim}{i} + y\underset{\sim}{j}| = \sqrt{x^2+y^2}  $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row2_col0" class="data row2 col0" >$ \underset{\sim}{a} +  (-\underset{\sim}{a}) =0  $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row3_col0" class="data row3 col0" >$ \vec{AB} - \vec{AD} =  \vec{AB} + \vec{DA} =  \vec{DA} + \vec{AB} = \vec{DB}  $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row4_col0" class="data row4 col0" >$ \text{The unit vector parallel to } \underset{\sim}{v} =  \underset{\sim}{v} * \dfrac{1}{|\underset{\sim}{v}|} $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row5_col0" class="data row5 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} +  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  \begin{pmatrix} a_1 + a_2 \\b_1 + b_2 \end{pmatrix} $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row6_col0" class="data row6 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} -  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  \begin{pmatrix} a_1 - a_2 \\b_1 - b_2 \end{pmatrix} $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row7_col0" class="data row7 col0" >$\lambda \begin{pmatrix} a \\b \end{pmatrix} =  \begin{pmatrix} \lambda a \\ \lambda b \end{pmatrix}$</td>
    </tr>
    <tr>
      <td id="T_93b2f_row8_col0" class="data row8 col0" >$|\underset{\sim}{u}| = \sqrt{x^2 + y^2}$</td>
    </tr>
    <tr>
      <td id="T_93b2f_row9_col0" class="data row9 col0" >$|\vec{XY}|  =  \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$</td>
    </tr>
    <tr>
      <td id="T_93b2f_row10_col0" class="data row10 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} +  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  (a_1 + a_2)\underset{\sim}{i} + (b_1+b_2)\underset{\sim}{j} $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row11_col0" class="data row11 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} -  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  (a_1 - a_2)\underset{\sim}{i} + (b_1-b_2)\underset{\sim}{j} $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row12_col0" class="data row12 col0" >$\underset{\sim}{u}.\underset{\sim}{v} = |\underset{\sim}{u}||\underset{\sim}{v}|\cos\theta = x_1x_2 + y_1y_2 $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row13_col0" class="data row13 col0" >$\underset{\sim}{v}.\underset{\sim}{v} = |\underset{\sim}{v}|^2 $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row14_col0" class="data row14 col0" >$ \text{perpendicular vectors: }\underset{\sim}{u}.\underset{\sim}{v} = 0 $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row15_col0" class="data row15 col0" >$ \text{parallel vectors like directions: }\underset{\sim}{u}.\underset{\sim}{v} = |\underset{\sim}{u}||\underset{\sim}{v}| $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row16_col0" class="data row16 col0" >$ \text{parallel vectors unlike directions: }\underset{\sim}{u}.\underset{\sim}{v} = -|\underset{\sim}{u}||\underset{\sim}{v}| $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row17_col0" class="data row17 col0" >$ P_{\underset{\sim}{u}}\underset{\sim}{v} = \dfrac{\underset{\sim}{u}.\underset{\sim}{v}}{|\underset{\sim}{u}|^2} \underset{\sim}{u} $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row18_col0" class="data row18 col0" >$ \underset{\sim}{u} = (r\cos\theta, r\sin\theta) = r\cos\theta \underset{\sim}{i} + r\sin\theta \underset{\sim}{j}  $</td>
    </tr>
    <tr>
      <td id="T_93b2f_row19_col0" class="data row19 col0" >$ \underset{\sim}{v}  =  \int \underset{\sim}{a} \; dt$</td>
    </tr>
    <tr>
      <td id="T_93b2f_row20_col0" class="data row20 col0" >$ \underset{\sim}{s}  =  \int \underset{\sim}{v} \; dt$</td>
    </tr>
    <tr>
      <td id="T_93b2f_row21_col0" class="data row21 col0" >$\text{Initial velocity of a vector } =  \underset{\sim}{v}  =  v\cos\theta \underset{\sim}{i}  + v \sin \theta \underset{\sim}{j} \text{ where v is the initial speed, a scalar}$</td>
    </tr>
    <tr>
      <td id="T_93b2f_row22_col0" class="data row22 col0" >$\text{acceleration due to gravity } =  \underset{\sim}{a}  =  -g\underset{\sim}{j}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

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
{{< tabs "dbfab3c1-f3d3-4373-be3e-60ca0b545e1a" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_2156b th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2156b td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_2156b">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2156b_row0_col0" class="data row0 col0" >$\underset{\sim}{u} + \underset{\sim}{v} = \underset{\sim}{v} + \underset{\sim}{u}$ </td>
    </tr>
    <tr>
      <td id="T_2156b_row1_col0" class="data row1 col0" >$(\underset{\sim}{u} + \underset{\sim}{v}) + \underset{\sim}{w} = \underset{\sim}{u} + (\underset{\sim}{v} + \underset{\sim}{w} )$ </td>
    </tr>
    <tr>
      <td id="T_2156b_row2_col0" class="data row2 col0" >$\underset{\sim}{u} + 0 = \underset{\sim}{u}$ </td>
    </tr>
    <tr>
      <td id="T_2156b_row3_col0" class="data row3 col0" >$|\underset{\sim}{u} + \underset{\sim}{v}| \le |\underset{\sim}{u}| + |\underset{\sim}{v}|$ </td>
    </tr>
    <tr>
      <td id="T_2156b_row4_col0" class="data row4 col0" >$|r| = \sqrt{x^2+y^2+z^2}$</td>
    </tr>
    <tr>
      <td id="T_2156b_row5_col0" class="data row5 col0" >$\underset{\sim}{u} . \underset{\sim}{v} = x_1x_2 + y_1y_2 + z_1z_2 = |\underset{\sim}{u}|\underset{\sim}{v}| \cos \theta$</td>
    </tr>
    <tr>
      <td id="T_2156b_row6_col0" class="data row6 col0" >$\underset{\sim}{u} . \underset{\sim}{v}  = \underset{\sim}{v} . \underset{\sim}{u}$</td>
    </tr>
    <tr>
      <td id="T_2156b_row7_col0" class="data row7 col0" >$\underset{\sim}{u} . (\underset{\sim}{v} +\underset{\sim}{w})   = \underset{\sim}{u} . \underset{\sim}{v} + \underset{\sim}{u} . \underset{\sim}{w}$</td>
    </tr>
    <tr>
      <td id="T_2156b_row8_col0" class="data row8 col0" >$r = \underset{\sim}{a} + \lambda \underset{\sim}{b}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_67f83 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_67f83 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_67f83_row0_col0, #T_67f83_row1_col0, #T_67f83_row2_col0, #T_67f83_row3_col0, #T_67f83_row4_col0, #T_67f83_row5_col0, #T_67f83_row6_col0, #T_67f83_row7_col0 {
  background-color: rgba(0,0,0,0);
}
#T_67f83_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_67f83">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_67f83_row0_col0" class="data row0 col0" >$\underset{\sim}{u} + \underset{\sim}{v} = \underset{\sim}{v} + \underset{\sim}{u}$ </td>
    </tr>
    <tr>
      <td id="T_67f83_row1_col0" class="data row1 col0" >$(\underset{\sim}{u} + \underset{\sim}{v}) + \underset{\sim}{w} = \underset{\sim}{u} + (\underset{\sim}{v} + \underset{\sim}{w} )$ </td>
    </tr>
    <tr>
      <td id="T_67f83_row2_col0" class="data row2 col0" >$\underset{\sim}{u} + 0 = \underset{\sim}{u}$ </td>
    </tr>
    <tr>
      <td id="T_67f83_row3_col0" class="data row3 col0" >$|\underset{\sim}{u} + \underset{\sim}{v}| \le |\underset{\sim}{u}| + |\underset{\sim}{v}|$ </td>
    </tr>
    <tr>
      <td id="T_67f83_row4_col0" class="data row4 col0" >$|r| = \sqrt{x^2+y^2+z^2}$</td>
    </tr>
    <tr>
      <td id="T_67f83_row5_col0" class="data row5 col0" >$\underset{\sim}{u} . \underset{\sim}{v} = x_1x_2 + y_1y_2 + z_1z_2 = |\underset{\sim}{u}|\underset{\sim}{v}| \cos \theta$</td>
    </tr>
    <tr>
      <td id="T_67f83_row6_col0" class="data row6 col0" >$\underset{\sim}{u} . \underset{\sim}{v}  = \underset{\sim}{v} . \underset{\sim}{u}$</td>
    </tr>
    <tr>
      <td id="T_67f83_row7_col0" class="data row7 col0" >$\underset{\sim}{u} . (\underset{\sim}{v} +\underset{\sim}{w})   = \underset{\sim}{u} . \underset{\sim}{v} + \underset{\sim}{u} . \underset{\sim}{w}$</td>
    </tr>
    <tr>
      <td id="T_67f83_row8_col0" class="data row8 col0" >$r = \underset{\sim}{a} + \lambda \underset{\sim}{b}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}