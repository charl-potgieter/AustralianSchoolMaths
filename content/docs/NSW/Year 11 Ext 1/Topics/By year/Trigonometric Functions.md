---
weight: 2
---

## <span style="color:RGB(0,32,96"> Inverse Trigonometric Functions </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>

The graph of an inverse function is a reflection of the original function in the line y=x.  (the y-value and x-values of the origianl graph are switched to obtain the inverse graph)

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


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "0f45e403-390e-4e75-a1e7-447b3b4e8236" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_f77ba th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_f77ba td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_f77ba">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_f77ba_row0_col0" class="data row0 col0" >$\sin(\sin^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_f77ba_row1_col0" class="data row1 col0" >$\sin^{-1}(\sin x) = x \text{, for } -\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_f77ba_row2_col0" class="data row2 col0" >$\cos(\cos^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_f77ba_row3_col0" class="data row3 col0" >$\cos^{-1}(\cos x) = x \text{, for } 0 \le x \le \pi$</td>
    </tr>
    <tr>
      <td id="T_f77ba_row4_col0" class="data row4 col0" >$\tan(\tan^{-1} x) = x \text{, for } -\infty < x < \infty$</td>
    </tr>
    <tr>
      <td id="T_f77ba_row5_col0" class="data row5 col0" >$\tan^{-1}(\tan x) = x \text{, for } -\dfrac{\pi}{2} < x < \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_f77ba_row6_col0" class="data row6 col0" >$\sin^{-1}(-x) = -\sin^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_f77ba_row7_col0" class="data row7 col0" >$\cos^{-1}(-x) = \pi -\cos^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_f77ba_row8_col0" class="data row8 col0" >$\tan^{-1}(-x) = -\tan^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_f77ba_row9_col0" class="data row9 col0" >$\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_e38f5 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_e38f5 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_e38f5_row0_col0, #T_e38f5_row1_col0, #T_e38f5_row2_col0, #T_e38f5_row3_col0, #T_e38f5_row4_col0, #T_e38f5_row5_col0 {
  background-color: rgba(0,0,0,0);
}
#T_e38f5_row6_col0, #T_e38f5_row7_col0, #T_e38f5_row8_col0, #T_e38f5_row9_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_e38f5">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_e38f5_row0_col0" class="data row0 col0" >$\sin(\sin^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_e38f5_row1_col0" class="data row1 col0" >$\sin^{-1}(\sin x) = x \text{, for } -\dfrac{\pi}{2} \le x \le \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_e38f5_row2_col0" class="data row2 col0" >$\cos(\cos^{-1} x) = x \text{, for } -1 \le x \le 1$</td>
    </tr>
    <tr>
      <td id="T_e38f5_row3_col0" class="data row3 col0" >$\cos^{-1}(\cos x) = x \text{, for } 0 \le x \le \pi$</td>
    </tr>
    <tr>
      <td id="T_e38f5_row4_col0" class="data row4 col0" >$\tan(\tan^{-1} x) = x \text{, for } -\infty < x < \infty$</td>
    </tr>
    <tr>
      <td id="T_e38f5_row5_col0" class="data row5 col0" >$\tan^{-1}(\tan x) = x \text{, for } -\dfrac{\pi}{2} < x < \dfrac{\pi}{2}$</td>
    </tr>
    <tr>
      <td id="T_e38f5_row6_col0" class="data row6 col0" >$\sin^{-1}(-x) = -\sin^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_e38f5_row7_col0" class="data row7 col0" >$\cos^{-1}(-x) = \pi -\cos^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_e38f5_row8_col0" class="data row8 col0" >$\tan^{-1}(-x) = -\tan^{-1}x $</td>
    </tr>
    <tr>
      <td id="T_e38f5_row9_col0" class="data row9 col0" >$\sin^{-1}x + \cos^{-1}x = \dfrac{\pi}{2}$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Trigonometric Identities </span> 
<br>

### <span style="color:RGB(139,69,19)">  Concepts </span>




### <span style="color:RGB(139,69,19)">  Notes </span>




<BR><BR>



<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "346ca964-554c-4331-8797-96176f191961" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_69941 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_69941 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_69941">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_69941_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_69941_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_69941_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_69941_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_69941_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_69941_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_69941_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_69941_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_69941_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_69941_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_69941_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_69941_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_69941_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_69941_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_69941_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_69941_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_69941_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_69941_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_4a126 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_4a126 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_4a126_row0_col0, #T_4a126_row2_col0, #T_4a126_row4_col0, #T_4a126_row11_col0, #T_4a126_row12_col0, #T_4a126_row13_col0, #T_4a126_row14_col0, #T_4a126_row15_col0, #T_4a126_row16_col0, #T_4a126_row17_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_4a126_row1_col0, #T_4a126_row3_col0, #T_4a126_row5_col0, #T_4a126_row6_col0, #T_4a126_row7_col0, #T_4a126_row8_col0, #T_4a126_row9_col0, #T_4a126_row10_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_4a126">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_4a126_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_4a126_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_4a126_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_4a126_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_4a126_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_4a126_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_4a126_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_4a126_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_4a126_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_4a126_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_4a126_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_4a126_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_4a126_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_4a126_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_4a126_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_4a126_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_4a126_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_4a126_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_0e7de th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_0e7de td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_0e7de_row0_col0, #T_0e7de_row1_col0, #T_0e7de_row2_col0, #T_0e7de_row3_col0, #T_0e7de_row4_col0, #T_0e7de_row5_col0, #T_0e7de_row6_col0, #T_0e7de_row7_col0, #T_0e7de_row8_col0, #T_0e7de_row9_col0, #T_0e7de_row10_col0, #T_0e7de_row11_col0, #T_0e7de_row12_col0, #T_0e7de_row13_col0, #T_0e7de_row14_col0, #T_0e7de_row15_col0, #T_0e7de_row16_col0, #T_0e7de_row17_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_0e7de">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_0e7de_row0_col0" class="data row0 col0" >$\sin(A+B) = \sin A \cos B + \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row1_col0" class="data row1 col0" >$\sin(A-B) = \sin A \cos B - \cos A \sin B$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row2_col0" class="data row2 col0" >$\cos(A+B) = \cos A \cos B - \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row3_col0" class="data row3 col0" >$\cos(A-B) = \cos A \cos B + \sin A \sin B$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row4_col0" class="data row4 col0" >$\tan(A+B) = \dfrac{\tan A + \tan B}{1-\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row5_col0" class="data row5 col0" >$\tan(A-B) = \dfrac{\tan A - \tan B}{1+\tan A \tan B}$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row6_col0" class="data row6 col0" >$\sin 2A = 2 \sin A \cos A$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row7_col0" class="data row7 col0" >$\cos 2A = \cos^2 A - \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row8_col0" class="data row8 col0" >$\cos 2A  = 2 \cos^2 A -1$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row9_col0" class="data row9 col0" >$\cos 2A  = 1 - 2 \sin^2 A$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row10_col0" class="data row10 col0" >$\tan 2A = \dfrac{2\tan A}{1-\tan^2 A}$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row11_col0" class="data row11 col0" >$ \sin A = \dfrac{2t}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row12_col0" class="data row12 col0" >$ \cos A = \dfrac{1-t^2}{1+t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row13_col0" class="data row13 col0" >$ \tan A = \dfrac{2t}{1-t^2} \text{, where t }=\tan \dfrac{A}{2}$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row14_col0" class="data row14 col0" >$\cos A \cos B = \dfrac{1}{2}[\cos(A-B) + \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row15_col0" class="data row15 col0" >$\sin A \sin B = \dfrac{1}{2}[\cos(A-B) - \cos(A+B)]$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row16_col0" class="data row16 col0" >$\sin A \cos B = \dfrac{1}{2}[\sin(A+B) + \sin(A-B)]$</td>
    </tr>
    <tr>
      <td id="T_0e7de_row17_col0" class="data row17 col0" >$\cos A \sin B = \dfrac{1}{2}[\sin(A+B) - \sin(A-B)]$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}