---
weight: 7
---

## <span style="color:RGB(0,32,96"> Introduction to Differentiation </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
<style type="text/css">
#T_2fc44 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2fc44 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_2fc44">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_2fc44_row0_col0" class="data row0 col0" >$ y=f(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =\lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}  $ <br></td>
    </tr>
    <tr>
      <td id="T_2fc44_row1_col0" class="data row1 col0" >$ y=kx   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =k  $ <br></td>
    </tr>
    <tr>
      <td id="T_2fc44_row2_col0" class="data row2 col0" >$ y=k   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =0  $ <br></td>
    </tr>
    <tr>
      <td id="T_2fc44_row3_col0" class="data row3 col0" >$ y=x^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =nx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_2fc44_row4_col0" class="data row4 col0" >$ y=kx^n   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =knx^{n-1}  $ <br></td>
    </tr>
    <tr>
      <td id="T_2fc44_row5_col0" class="data row5 col0" >$ y=kf(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =kf'(x)  $ <br></td>
    </tr>
    <tr>
      <td id="T_2fc44_row6_col0" class="data row6 col0" >$ y=f(x) + g(x)   \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =f'(x) + g'(x)  $ <br></td>
    </tr>
  </tbody>
</table>


## <span style="color:RGB(0,32,96"> Differential Calculus </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "f3bb2521-594d-4b8f-b92a-30ef3f0b93ff" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_6a2a4 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_6a2a4 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_6a2a4">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_6a2a4_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row3_col0" class="data row3 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row4_col0" class="data row4 col0" >$y=sinf(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row5_col0" class="data row5 col0" >$y=cosf(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row6_col0" class="data row6 col0" >$y=tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row7_col0" class="data row7 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row8_col0" class="data row8 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row9_col0" class="data row9 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_6a2a4_row10_col0" class="data row10 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_26216 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_26216 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_26216_row0_col0, #T_26216_row1_col0, #T_26216_row2_col0, #T_26216_row3_col0, #T_26216_row4_col0, #T_26216_row5_col0, #T_26216_row6_col0, #T_26216_row7_col0, #T_26216_row8_col0, #T_26216_row9_col0, #T_26216_row10_col0 {
  background-color: rgba(255,194,10, 0.2);
}
</style>
<table id="T_26216">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_26216_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row3_col0" class="data row3 col0" >$y=g(u) \text { where } u = f(x) \,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{dy}{du} \times \dfrac{du}{dx}$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row4_col0" class="data row4 col0" >$y=sinf(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)cos f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row5_col0" class="data row5 col0" >$y=cosf(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)sin f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row6_col0" class="data row6 col0" >$y=tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)sec^2 f(x)$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row7_col0" class="data row7 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row8_col0" class="data row8 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row9_col0" class="data row9 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
    </tr>
    <tr>
      <td id="T_26216_row10_col0" class="data row10 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Applications of Differentiation </span> 
<br>

## <span style="color:RGB(0,32,96"> Integral Calculus </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "97fe53ad-48dc-492c-ae88-ec0fbe5c86e9" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_c0db0 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_c0db0 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_c0db0">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_c0db0_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_c0db0_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_c0db0_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_c0db0_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)cosf(x)dx = sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_c0db0_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)sin f(x)dx = -cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_c0db0_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)sec^2 f(x)dx = tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_c0db0_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_c0db0_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_c0db0_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_c0db0_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_fe9b2 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_fe9b2 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_fe9b2_row0_col0, #T_fe9b2_row1_col0, #T_fe9b2_row2_col0, #T_fe9b2_row3_col0, #T_fe9b2_row4_col0, #T_fe9b2_row5_col0, #T_fe9b2_row6_col0, #T_fe9b2_row7_col0, #T_fe9b2_row8_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_fe9b2_row9_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_fe9b2">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_fe9b2_row0_col0" class="data row0 col0" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row1_col0" class="data row1 col0" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row2_col0" class="data row2 col0" >$ {\Large\int_{a}^{b}} f(x) dx \approx \dfrac{b-a} {2n} {\Large\{} f(a) + f(b) + 2 {\Large[} f(x_1)+...+f(x_{n-1}){\Large ]} {\Large\}}$
$ \text { where } a=x_0 \text{ and } b=x_n $</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row3_col0" class="data row3 col0" >$ {\Large\int} f'(x)cosf(x)dx = sin f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row4_col0" class="data row4 col0" >$ {\Large\int} f'(x)sin f(x)dx = -cos f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row5_col0" class="data row5 col0" >$ {\Large\int} f'(x)sec^2 f(x)dx = tan f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row6_col0" class="data row6 col0" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row7_col0" class="data row7 col0" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row8_col0" class="data row8 col0" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
    </tr>
    <tr>
      <td id="T_fe9b2_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Further Calculus Skills </span> 
<br>


<br>


###  <span style="color:RGB(139,69,19)"> Formulas </span>
<br>
{{< tabs "d2751f0f-43e1-4a10-b264-537d730826b3" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_ee1f3 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_ee1f3 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_ee1f3">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_ee1f3_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ee1f3_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_ee1f3_row2_col0" class="data row2 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_ee1f3_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_ee1f3_row4_col0" class="data row4 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ee1f3_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_ee1f3_row6_col0" class="data row6 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_ee1f3_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_ee1f3_row8_col0" class="data row8 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_ee1f3_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_ee1f3_row10_col0" class="data row10 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_ee1f3_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_ee1f3_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_37682 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_37682 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_37682_row0_col0, #T_37682_row3_col0, #T_37682_row4_col0, #T_37682_row8_col0, #T_37682_row11_col0 {
  background-color: rgba(255,194,10, 0.2);
}
#T_37682_row1_col0, #T_37682_row2_col0, #T_37682_row5_col0, #T_37682_row6_col0, #T_37682_row7_col0, #T_37682_row9_col0, #T_37682_row10_col0, #T_37682_row12_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_37682">
  <thead>
  </thead>
  <tbody>
    <tr>
      <td id="T_37682_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_37682_row1_col0" class="data row1 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_37682_row2_col0" class="data row2 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
    </tr>
    <tr>
      <td id="T_37682_row3_col0" class="data row3 col0" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_37682_row4_col0" class="data row4 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_37682_row5_col0" class="data row5 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_37682_row6_col0" class="data row6 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
    </tr>
    <tr>
      <td id="T_37682_row7_col0" class="data row7 col0" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
    </tr>
    <tr>
      <td id="T_37682_row8_col0" class="data row8 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
    </tr>
    <tr>
      <td id="T_37682_row9_col0" class="data row9 col0" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
    </tr>
    <tr>
      <td id="T_37682_row10_col0" class="data row10 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
    </tr>
    <tr>
      <td id="T_37682_row11_col0" class="data row11 col0" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
    </tr>
    <tr>
      <td id="T_37682_row12_col0" class="data row12 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}


<br>


###  <span style="color:RGB(139,69,19)"> Derivatives vs integrals  </span>
<br>
{{< tabs "c25c4a49-a680-4096-acb5-d052000f361a" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_2dddc th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2dddc td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_2dddc">
  <thead>
    <tr>
      <th id="T_2dddc_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_2dddc_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_2dddc_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_2dddc_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_2dddc_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
      <td id="T_2dddc_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dddc_row1_col0" class="data row1 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_2dddc_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_2dddc_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dddc_row2_col0" class="data row2 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_2dddc_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_2dddc_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dddc_row3_col0" class="data row3 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_2dddc_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_2dddc_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dddc_row4_col0" class="data row4 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_2dddc_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
      <td id="T_2dddc_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dddc_row5_col0" class="data row5 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_2dddc_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_2dddc_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dddc_row6_col0" class="data row6 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
      <td id="T_2dddc_row6_col1" class="data row6 col1" ></td>
      <td id="T_2dddc_row6_col2" class="data row6 col2" >Formula can be utilised to calculate otherwise hard to differentiate inverse functions</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_8da5d th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_8da5d td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_8da5d_row0_col0, #T_8da5d_row1_col1, #T_8da5d_row2_col0, #T_8da5d_row4_col0, #T_8da5d_row5_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_8da5d_row0_col1, #T_8da5d_row1_col0, #T_8da5d_row2_col1, #T_8da5d_row3_col0, #T_8da5d_row3_col1, #T_8da5d_row4_col1, #T_8da5d_row5_col0, #T_8da5d_row6_col0, #T_8da5d_row6_col1 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_8da5d">
  <thead>
    <tr>
      <th id="T_8da5d_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_8da5d_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_8da5d_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_8da5d_row0_col0" class="data row0 col0" >$y=sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_8da5d_row0_col1" class="data row0 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = sin^{-1} f(x) + c$</td>
      <td id="T_8da5d_row0_col2" class="data row0 col2" ></td>
    </tr>
    <tr>
      <td id="T_8da5d_row1_col0" class="data row1 col0" >$ y = sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_8da5d_row1_col1" class="data row1 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_8da5d_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_8da5d_row2_col0" class="data row2 col0" >$y=cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_8da5d_row2_col1" class="data row2 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = cos^{-1}f(x) + c \text{ or } -sin^{-1}f(x) +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_8da5d_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_8da5d_row3_col0" class="data row3 col0" >$y=cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_8da5d_row3_col1" class="data row3 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the constant c will have different values with these two options} $</td>
      <td id="T_8da5d_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_8da5d_row4_col0" class="data row4 col0" >$y=tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_8da5d_row4_col1" class="data row4 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ tan^{-1} f(x) + c$</td>
      <td id="T_8da5d_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_8da5d_row5_col0" class="data row5 col0" >$y=tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_8da5d_row5_col1" class="data row5 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_8da5d_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_8da5d_row6_col0" class="data row6 col0" >$ \text{Function and its inverse}  \,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} \times \dfrac{dx}{dy} = 1, \text{  or  } \dfrac{dy}{dx} = \dfrac{1}{\dfrac{dx}{dy}} $ <br></td>
      <td id="T_8da5d_row6_col1" class="data row6 col1" ></td>
      <td id="T_8da5d_row6_col2" class="data row6 col2" >Formula can be utilised to calculate otherwise hard to differentiate inverse functions</td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}

## <span style="color:RGB(0,32,96"> Applications of Calculus </span> 
<br>