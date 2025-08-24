### <span style="color:RGB(139,69,19)">  Concepts </span>

 - De Moivre's therom
 - locus
 - roots of unity



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



#### Quadratic equations with complex coefficients

 - Quadratic equations
     - if coefficients are real then the complex roots are always in conjugate pairs
     - if the coefficients are complex the roots will not be conjugate pairs


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
#### Roots of unity and roots of complex numbers

| <div style="width:500px">Roots of unity</div>    | <div style="width:500px"> Roots of complex numbers</div>  |
| --------------------- |  ------------------------- |
| $z^n = 1$                                 |  $ z^n = a + ib$   |
| Has n solutions on the complex plane      |      |
| The solutions are evenly spaced $\dfrac{2 \pi}{n}$ radians apart   |The solutions are evenly spaced $\dfrac{2 \pi}{n}$ radians apart     |
| $z=1$ is a root   |  $a+ib$ is not necessarily a root   |
||$z_1 = r(\cos \theta + i \sin \theta) \text{ where } $ <br>   $\theta = arg(a+ib)/n \text{ and } $ <br>   $  r = \sqrt[n]{&#124; a+ib &#124; }$|
|The roots form a regular polygon|The roots form a regular polygon|
| $z_1 + z_2 + z_3+...z_n = 0$ <br>, that is the sum of the roots is zero       | $z_1 + z_2 + z_3+...z_n = 0$ <br>, that is the sum of the roots is zero|
| The complex roots come in conugate pairs    | Since a+ib is complex, the roots do not come in conjugate pairs    |
| If $z_1 = \alpha$, then $z_2 = \alpha^2, z_3=\alpha^3,...z_n = \alpha^n $ <br> where $\alpha^n  = 1$                          |     |
| Given above, the sum of the roots can be written as follows: <br> $1 + \alpha + \alpha^2 + \alpha^3+...+\alpha^{n-1} = 0$ <br> where the conjugate pairs are: <br> $\overline{\alpha} = {\alpha}^{n-1}$ <br> $\overline{\alpha}^2 = {\alpha}^{n-2}$ <br> $\overline{\alpha}^3 = {\alpha}^{n-3}$ etc  |    |
| $z^n - 1$ can be solved algebraically by expressing 1 in polar form: <br> $\cos 0 + i \sin 0 $ | | 
#### Curves and regions on a complex plane

A locus can be graphed:
 - algebraically by deriving the cartesian equation
 - geometrically by using the definitions of modulus and arguments

 **Algebraic approach** <br>
  - Let $x = x + iy$, then $|z| = r = \sqrt{x^2+y^2}$ 


**Geometric approach**
 - Use the definition $z-z_1$ to mean a vector with z as a variable point and $z_1$ as a fixed point
 - $|z-z_1|$ is the distance from z to $z_1$
 - $arg(z-z_1)$ is the angle between $z-z_1$ and the positive x-axis
 - $|z_1-z_2| = |z_3-z_4|$ means AB=CD (the lengths are equal)
 - $arg(z_1)-z_2 = arg(z_3-z_4)$ means AB||CD 
 - $z_1-z_2 = z_3-z_4$ means both the moduli and arguments are equal.   Either ABCD is a parallelogram or ABCD is collinear.
 - Tip: Arg 0 is underfined, therefore needs to be drawn as an open circle on the cartesian plane.