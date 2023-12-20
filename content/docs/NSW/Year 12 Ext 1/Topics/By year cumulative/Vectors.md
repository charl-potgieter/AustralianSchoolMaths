---
weight: 5
---

## <span style="color:RGB(0,32,96"> Introduction to Vectors </span> 
<br>

### <span style="color:RGB(139,69,19)"> Concepts  </span>


* column vector notation
* component form
* displacement vector
* equal vectors
* magnitude or modulus of a vector
* negative vector
* parallel vectors
* position vector
* scalar
* unit vector
* vector
* scalar multiplication
* dot product or scalar product
* projectile
* projectile motion
* projection of a vector


### <span style="color:RGB(139,69,19)">  Notes </span>


* Vectors vs scalars
<BR><BR>
* Triangle law of addition
<BR><BR>
* Parallelogram law of addition
<BR><BR>
* Subtracting vectors using the triangle rule
<BR><BR>
* Subtracting vectors using the parallelogram rule
<BR><BR>
* Adding and subtracting vectors numerically
<BR><BR>
* Scalar multiplication
<BR><BR>
* Magnitude of a position vector
<BR><BR>
* Magnitude of a displacement vector
<BR><BR>
* Direction of a position vector
<BR><BR>
* Direction of a displacement vector
<BR><BR>
* Don't confuse dot product $\underset{\sim}{u}.\underset{\sim}{v}$ and product of vector magnitudes $|\underset{\sim}{u}||\underset{\sim}{v}|$
<BR><BR>
* Geometric proofs using vector examples
<BR><BR>
* See formulas below for vectors parallel in like and unlike directions.  Also note vectors are parallel if one is a scalar multiple of another.
<BR><BR>
* Length of vector x unit vector = the vector itself
<BR><BR>
* Equal vectors have the same magnitude and direction but don’t need to have the same position on the cartesian plane
<BR><BR>
* Tip-to-tail addition of vectors can be applied to more than 2 vectors
<BR><BR>
* Bearing is measured clockwise from north
<BR><BR>
* Direction is measured anti-clockwise from  Easterly horizon
<BR><BR>
* The path of projectile motion is a parabola
<BR><BR>
* Acceleration due to gravity is the only acceleration that a projectile undergoes.  It can be subject to other velocity vectors though.
<BR><BR>
* Note that it is useful to know below formulas but they cannot be used directly in any answers, they need to be derived from the gravity acceleration formula and the initial velocity formula
<BR><BR>
* Projectile acceleration vector = $0\underset{\sim}{i}  +  -g\underset{\sim}{j}$
<BR><BR>
* Projectile velocity vector = $v\cos\theta \underset{\sim}{i}  + (-gt + V \sin \theta) \underset{\sim}{j}$
<BR><BR>
* Projectile displacement vector = $vt\cos\theta \underset{\sim}{i}  + (\dfrac{-gt^2}{2} + Vt \sin \theta) \underset{\sim}{j}$
<BR><BR>
* Note from above that the horizontal component of the velocity vector is independent of time t, whereas the horizontal component of the displacement vector is dependent on t.
<BR><BR>
* In order to calculate the velocity vector of a projectile :
    * Calculate the integral of the acceleration vector which includes a constant, say C
    * Get the initial velocity of the vector using $ v\cos\theta \underset{\sim}{i}  + v \sin \theta \underset{\sim}{j} $
    * Substitute above into the gravity velocity vector at time zero to solve for C
<BR><BR>
* In order to calculate the displacement vector of a projectile :
    * Calculate the integral of the velocity vector which includes a constant, say D.  The velocity vector is as calculated above.
    * Get the displacement vector at time zero assuming horizontal component  = 0 = the start point and vertical component  = distance from vertical end point
    *  Substitute the above equations into one another to solve for the constant D
<BR><BR>
* Projectile calculation notes :
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
{{< tabs "52fa044c-3a03-4659-aa25-af5673ac4e51" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_fa669 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fa669 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_fa669">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fa669_row0_col0" class="data row0 col0" >$ \vec{AB} + \vec{BC} = \vec{AC} $</td>
    </tr>
    <tr>
      <td id="T_fa669_row1_col0" class="data row1 col0" >$ |\underset{\sim}{u}| = |x\underset{\sim}{i} + y\underset{\sim}{j}| = \sqrt{x^2+y^2}  $</td>
    </tr>
    <tr>
      <td id="T_fa669_row2_col0" class="data row2 col0" >$ \underset{\sim}{a} +  (-\underset{\sim}{a}) =0  $</td>
    </tr>
    <tr>
      <td id="T_fa669_row3_col0" class="data row3 col0" >$ \vec{AB} - \vec{AD} =  \vec{AB} + \vec{DA} =  \vec{DA} + \vec{AB} = \vec{DB}  $</td>
    </tr>
    <tr>
      <td id="T_fa669_row4_col0" class="data row4 col0" >$ \text{The unit vector parallel to } \underset{\sim}{v} =  \underset{\sim}{v} * \dfrac{1}{|\underset{\sim}{v}|} $</td>
    </tr>
    <tr>
      <td id="T_fa669_row5_col0" class="data row5 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} +  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  \begin{pmatrix} a_1 + a_2 \\b_1 + b_2 \end{pmatrix} $</td>
    </tr>
    <tr>
      <td id="T_fa669_row6_col0" class="data row6 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} -  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  \begin{pmatrix} a_1 - a_2 \\b_1 - b_2 \end{pmatrix} $</td>
    </tr>
    <tr>
      <td id="T_fa669_row7_col0" class="data row7 col0" >$\lambda \begin{pmatrix} a \\b \end{pmatrix} =  \begin{pmatrix} \lambda a \\ \lambda b \end{pmatrix}$</td>
    </tr>
    <tr>
      <td id="T_fa669_row8_col0" class="data row8 col0" >$|\underset{\sim}{u}| = \sqrt{x^2 + y^2}$</td>
    </tr>
    <tr>
      <td id="T_fa669_row9_col0" class="data row9 col0" >$|\vec{XY}|  =  \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$</td>
    </tr>
    <tr>
      <td id="T_fa669_row10_col0" class="data row10 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} +  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  (a_1 + a_2)\underset{\sim}{i} + (b_1+b_2)\underset{\sim}{j} $</td>
    </tr>
    <tr>
      <td id="T_fa669_row11_col0" class="data row11 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} -  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  (a_1 - a_2)\underset{\sim}{i} + (b_1-b_2)\underset{\sim}{j} $</td>
    </tr>
    <tr>
      <td id="T_fa669_row12_col0" class="data row12 col0" >$\underset{\sim}{u}.\underset{\sim}{v} = |\underset{\sim}{u}||\underset{\sim}{v}|\cos\theta = x_1x_2 + y_1y_2 $</td>
    </tr>
    <tr>
      <td id="T_fa669_row13_col0" class="data row13 col0" >$\underset{\sim}{v}.\underset{\sim}{v} = |\underset{\sim}{v}|^2 $</td>
    </tr>
    <tr>
      <td id="T_fa669_row14_col0" class="data row14 col0" >$ \text{perpendicular vectors: }\underset{\sim}{u}.\underset{\sim}{v} = 0 $</td>
    </tr>
    <tr>
      <td id="T_fa669_row15_col0" class="data row15 col0" >$ \text{parallel vectors like directions: }\underset{\sim}{u}.\underset{\sim}{v} = |\underset{\sim}{u}||\underset{\sim}{v}| $</td>
    </tr>
    <tr>
      <td id="T_fa669_row16_col0" class="data row16 col0" >$ \text{parallel vectors unlike directions: }\underset{\sim}{u}.\underset{\sim}{v} = -|\underset{\sim}{u}||\underset{\sim}{v}| $</td>
    </tr>
    <tr>
      <td id="T_fa669_row17_col0" class="data row17 col0" >$ P_{\underset{\sim}{u}}\underset{\sim}{v} = \dfrac{\underset{\sim}{u}.\underset{\sim}{v}}{|\underset{\sim}{u}|^2} \underset{\sim}{u} $</td>
    </tr>
    <tr>
      <td id="T_fa669_row18_col0" class="data row18 col0" >$ \underset{\sim}{u} = (r\cos\theta, r\sin\theta) = r\cos\theta \underset{\sim}{i} + r\sin\theta \underset{\sim}{j}  $</td>
    </tr>
    <tr>
      <td id="T_fa669_row19_col0" class="data row19 col0" >$ \underset{\sim}{v}  =  \int \underset{\sim}{a} \; dt$</td>
    </tr>
    <tr>
      <td id="T_fa669_row20_col0" class="data row20 col0" >$ \underset{\sim}{s}  =  \int \underset{\sim}{v} \; dt$</td>
    </tr>
    <tr>
      <td id="T_fa669_row21_col0" class="data row21 col0" >$\text{Initial velocity of a vector } =  \underset{\sim}{v}  =  v\cos\theta \underset{\sim}{i}  + v \sin \theta \underset{\sim}{j} \text{ where v is the initial speed, a scalar}$</td>
    </tr>
    <tr>
      <td id="T_fa669_row22_col0" class="data row22 col0" >$\text{acceleration due to gravity } =  \underset{\sim}{a}  =  -g\underset{\sim}{j}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_7bf8c th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_7bf8c td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_7bf8c_row0_col0, #T_7bf8c_row2_col0, #T_7bf8c_row3_col0, #T_7bf8c_row4_col0, #T_7bf8c_row5_col0, #T_7bf8c_row6_col0, #T_7bf8c_row7_col0, #T_7bf8c_row8_col0, #T_7bf8c_row9_col0, #T_7bf8c_row10_col0, #T_7bf8c_row11_col0, #T_7bf8c_row13_col0, #T_7bf8c_row14_col0, #T_7bf8c_row15_col0, #T_7bf8c_row16_col0, #T_7bf8c_row17_col0, #T_7bf8c_row18_col0, #T_7bf8c_row19_col0, #T_7bf8c_row20_col0, #T_7bf8c_row21_col0, #T_7bf8c_row22_col0 {
  background-color: rgba(0,0,0,0);
}
#T_7bf8c_row1_col0, #T_7bf8c_row12_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_7bf8c">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_7bf8c_row0_col0" class="data row0 col0" >$ \vec{AB} + \vec{BC} = \vec{AC} $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row1_col0" class="data row1 col0" >$ |\underset{\sim}{u}| = |x\underset{\sim}{i} + y\underset{\sim}{j}| = \sqrt{x^2+y^2}  $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row2_col0" class="data row2 col0" >$ \underset{\sim}{a} +  (-\underset{\sim}{a}) =0  $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row3_col0" class="data row3 col0" >$ \vec{AB} - \vec{AD} =  \vec{AB} + \vec{DA} =  \vec{DA} + \vec{AB} = \vec{DB}  $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row4_col0" class="data row4 col0" >$ \text{The unit vector parallel to } \underset{\sim}{v} =  \underset{\sim}{v} * \dfrac{1}{|\underset{\sim}{v}|} $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row5_col0" class="data row5 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} +  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  \begin{pmatrix} a_1 + a_2 \\b_1 + b_2 \end{pmatrix} $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row6_col0" class="data row6 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} -  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  \begin{pmatrix} a_1 - a_2 \\b_1 - b_2 \end{pmatrix} $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row7_col0" class="data row7 col0" >$\lambda \begin{pmatrix} a \\b \end{pmatrix} =  \begin{pmatrix} \lambda a \\ \lambda b \end{pmatrix}$</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row8_col0" class="data row8 col0" >$|\underset{\sim}{u}| = \sqrt{x^2 + y^2}$</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row9_col0" class="data row9 col0" >$|\vec{XY}|  =  \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row10_col0" class="data row10 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} +  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  (a_1 + a_2)\underset{\sim}{i} + (b_1+b_2)\underset{\sim}{j} $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row11_col0" class="data row11 col0" >$\begin{pmatrix} a_1 \\b_1 \end{pmatrix} -  \begin{pmatrix} a_2 \\b_2 \end{pmatrix}  =  (a_1 - a_2)\underset{\sim}{i} + (b_1-b_2)\underset{\sim}{j} $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row12_col0" class="data row12 col0" >$\underset{\sim}{u}.\underset{\sim}{v} = |\underset{\sim}{u}||\underset{\sim}{v}|\cos\theta = x_1x_2 + y_1y_2 $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row13_col0" class="data row13 col0" >$\underset{\sim}{v}.\underset{\sim}{v} = |\underset{\sim}{v}|^2 $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row14_col0" class="data row14 col0" >$ \text{perpendicular vectors: }\underset{\sim}{u}.\underset{\sim}{v} = 0 $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row15_col0" class="data row15 col0" >$ \text{parallel vectors like directions: }\underset{\sim}{u}.\underset{\sim}{v} = |\underset{\sim}{u}||\underset{\sim}{v}| $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row16_col0" class="data row16 col0" >$ \text{parallel vectors unlike directions: }\underset{\sim}{u}.\underset{\sim}{v} = -|\underset{\sim}{u}||\underset{\sim}{v}| $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row17_col0" class="data row17 col0" >$ P_{\underset{\sim}{u}}\underset{\sim}{v} = \dfrac{\underset{\sim}{u}.\underset{\sim}{v}}{|\underset{\sim}{u}|^2} \underset{\sim}{u} $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row18_col0" class="data row18 col0" >$ \underset{\sim}{u} = (r\cos\theta, r\sin\theta) = r\cos\theta \underset{\sim}{i} + r\sin\theta \underset{\sim}{j}  $</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row19_col0" class="data row19 col0" >$ \underset{\sim}{v}  =  \int \underset{\sim}{a} \; dt$</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row20_col0" class="data row20 col0" >$ \underset{\sim}{s}  =  \int \underset{\sim}{v} \; dt$</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row21_col0" class="data row21 col0" >$\text{Initial velocity of a vector } =  \underset{\sim}{v}  =  v\cos\theta \underset{\sim}{i}  + v \sin \theta \underset{\sim}{j} \text{ where v is the initial speed, a scalar}$</td>
    </tr>
    <tr>
      <td id="T_7bf8c_row22_col0" class="data row22 col0" >$\text{acceleration due to gravity } =  \underset{\sim}{a}  =  -g\underset{\sim}{j}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}