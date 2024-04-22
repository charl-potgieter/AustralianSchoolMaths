---
weight: 1
---

{{< tabs "421e48d1-05dd-445d-bcad-8c2c12a23906" >}}

{{< tab "Standard view" >}}

<style type="text/css">
#T_a2f78 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_a2f78 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
</style>
<table id="T_a2f78">
  <thead>
    <tr>
      <th id="T_a2f78_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_a2f78_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_a2f78_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_a2f78_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
      <td id="T_a2f78_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_a2f78_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_a2f78_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
      <td id="T_a2f78_row1_col1" class="data row1 col1" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
      <td id="T_a2f78_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
      <td id="T_a2f78_row2_col1" class="data row2 col1" ></td>
      <td id="T_a2f78_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row3_col0" class="data row3 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_a2f78_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_a2f78_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row4_col0" class="data row4 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_a2f78_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_a2f78_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row5_col0" class="data row5 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_a2f78_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_a2f78_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row6_col0" class="data row6 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_a2f78_row6_col1" class="data row6 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_a2f78_row6_col2" class="data row6 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row7_col0" class="data row7 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_a2f78_row7_col1" class="data row7 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_a2f78_row7_col2" class="data row7 col2" >Why absolute value?</td>
    </tr>
    <tr>
      <td id="T_a2f78_row8_col0" class="data row8 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_a2f78_row8_col1" class="data row8 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_a2f78_row8_col2" class="data row8 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_a2f78_row9_col0" class="data row9 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_a2f78_row9_col1" class="data row9 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_a2f78_row9_col2" class="data row9 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
    <tr>
      <td id="T_a2f78_row10_col0" class="data row10 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_a2f78_row10_col1" class="data row10 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_a2f78_row10_col2" class="data row10 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row11_col0" class="data row11 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_a2f78_row11_col1" class="data row11 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_a2f78_row11_col2" class="data row11 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row12_col0" class="data row12 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_a2f78_row12_col1" class="data row12 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_a2f78_row12_col2" class="data row12 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row13_col0" class="data row13 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_a2f78_row13_col1" class="data row13 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_a2f78_row13_col2" class="data row13 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row14_col0" class="data row14 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_a2f78_row14_col1" class="data row14 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_a2f78_row14_col2" class="data row14 col2" ></td>
    </tr>
    <tr>
      <td id="T_a2f78_row15_col0" class="data row15 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_a2f78_row15_col1" class="data row15 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_a2f78_row15_col2" class="data row15 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Formula sheet" >}}

Items on formula sheet are highlighted 
<br>
<style type="text/css">
#T_2dafd th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_2dafd td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_2dafd_row0_col0, #T_2dafd_row0_col1, #T_2dafd_row1_col0, #T_2dafd_row1_col1, #T_2dafd_row2_col0, #T_2dafd_row3_col0, #T_2dafd_row3_col1, #T_2dafd_row4_col0, #T_2dafd_row4_col1, #T_2dafd_row5_col0, #T_2dafd_row5_col1, #T_2dafd_row6_col0, #T_2dafd_row6_col1, #T_2dafd_row7_col0, #T_2dafd_row7_col1, #T_2dafd_row8_col0, #T_2dafd_row8_col1, #T_2dafd_row9_col0, #T_2dafd_row10_col0, #T_2dafd_row11_col1, #T_2dafd_row12_col0, #T_2dafd_row14_col0, #T_2dafd_row15_col1 {
  background-color: rgba(255,194,10, 0.2);
}
#T_2dafd_row2_col1, #T_2dafd_row9_col1, #T_2dafd_row10_col1, #T_2dafd_row11_col0, #T_2dafd_row12_col1, #T_2dafd_row13_col0, #T_2dafd_row13_col1, #T_2dafd_row14_col1, #T_2dafd_row15_col0 {
  background-color: rgba(0,0,0,0);
}
</style>
<table id="T_2dafd">
  <thead>
    <tr>
      <th id="T_2dafd_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_2dafd_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_2dafd_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_2dafd_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
      <td id="T_2dafd_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_2dafd_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_2dafd_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
      <td id="T_2dafd_row1_col1" class="data row1 col1" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
      <td id="T_2dafd_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
      <td id="T_2dafd_row2_col1" class="data row2 col1" ></td>
      <td id="T_2dafd_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row3_col0" class="data row3 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_2dafd_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_2dafd_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row4_col0" class="data row4 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_2dafd_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_2dafd_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row5_col0" class="data row5 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_2dafd_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_2dafd_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row6_col0" class="data row6 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_2dafd_row6_col1" class="data row6 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_2dafd_row6_col2" class="data row6 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row7_col0" class="data row7 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_2dafd_row7_col1" class="data row7 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_2dafd_row7_col2" class="data row7 col2" >Why absolute value?</td>
    </tr>
    <tr>
      <td id="T_2dafd_row8_col0" class="data row8 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_2dafd_row8_col1" class="data row8 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_2dafd_row8_col2" class="data row8 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_2dafd_row9_col0" class="data row9 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_2dafd_row9_col1" class="data row9 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_2dafd_row9_col2" class="data row9 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
    <tr>
      <td id="T_2dafd_row10_col0" class="data row10 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_2dafd_row10_col1" class="data row10 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_2dafd_row10_col2" class="data row10 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row11_col0" class="data row11 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_2dafd_row11_col1" class="data row11 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_2dafd_row11_col2" class="data row11 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row12_col0" class="data row12 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_2dafd_row12_col1" class="data row12 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_2dafd_row12_col2" class="data row12 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row13_col0" class="data row13 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_2dafd_row13_col1" class="data row13 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_2dafd_row13_col2" class="data row13 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row14_col0" class="data row14 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_2dafd_row14_col1" class="data row14 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_2dafd_row14_col2" class="data row14 col2" ></td>
    </tr>
    <tr>
      <td id="T_2dafd_row15_col0" class="data row15 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_2dafd_row15_col1" class="data row15 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_2dafd_row15_col2" class="data row15 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}

{{< tab "Poofs required" >}}

Items where proofs required are highlighted 
<br>
<style type="text/css">
#T_bd720 th.col_heading {
  text-align: left;
  font-size: 1em;
}
#T_bd720 td {
  text-align: left;
  font-size: 1em;
  padding: 1.5em;
}
#T_bd720_row0_col0, #T_bd720_row0_col1, #T_bd720_row1_col0, #T_bd720_row1_col1, #T_bd720_row2_col0, #T_bd720_row2_col1, #T_bd720_row3_col1, #T_bd720_row4_col1, #T_bd720_row5_col1, #T_bd720_row6_col1, #T_bd720_row7_col1, #T_bd720_row8_col1, #T_bd720_row9_col1, #T_bd720_row10_col0, #T_bd720_row10_col1, #T_bd720_row11_col0, #T_bd720_row11_col1, #T_bd720_row12_col0, #T_bd720_row12_col1, #T_bd720_row13_col0, #T_bd720_row13_col1, #T_bd720_row14_col0, #T_bd720_row14_col1, #T_bd720_row15_col0, #T_bd720_row15_col1 {
  background-color: rgba(0,0,0,0);
}
#T_bd720_row3_col0, #T_bd720_row4_col0, #T_bd720_row5_col0, #T_bd720_row6_col0, #T_bd720_row7_col0, #T_bd720_row8_col0, #T_bd720_row9_col0 {
  background-color: rgba(0,150,200, 0.2);
}
</style>
<table id="T_bd720">
  <thead>
    <tr>
      <th id="T_bd720_level0_col0" class="col_heading level0 col0" >Derivative</th>
      <th id="T_bd720_level0_col1" class="col_heading level0 col1" >Equivalent integral</th>
      <th id="T_bd720_level0_col2" class="col_heading level0 col2" >Comment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_bd720_row0_col0" class="data row0 col0" >$y=f(x)^n \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx}=nf'(x)[f(x)]^{n-1}$ <br></td>
      <td id="T_bd720_row0_col1" class="data row0 col1" >$ {\Large\int} f'(x)[f(x)]^n dx = \dfrac{1}{n+1}[f(x)]^{n+1} + c $
$ \text{ where } n \neq -1 $</td>
      <td id="T_bd720_row0_col2" class="data row0 col2" >When n = -1 follow the integration rules for  $ {\Large\int} \dfrac{f'(x)}{f(x)}dx$</td>
    </tr>
    <tr>
      <td id="T_bd720_row1_col0" class="data row1 col0" >$y=uv \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ <br></td>
      <td id="T_bd720_row1_col1" class="data row1 col1" >$ {\Large\int} u \dfrac{dv}{dx} dx=uv-{\Large\int}v \dfrac {du}{dx}dx$</td>
      <td id="T_bd720_row1_col2" class="data row1 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row2_col0" class="data row2 col0" >$y=\dfrac{u}{v} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$ <br></td>
      <td id="T_bd720_row2_col1" class="data row2 col1" ></td>
      <td id="T_bd720_row2_col2" class="data row2 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row3_col0" class="data row3 col0" >$y=\sin f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,  \dfrac{dy}{dx} = f'(x)\cos f(x)$ <br></td>
      <td id="T_bd720_row3_col1" class="data row3 col1" >$ {\Large\int} f'(x)\cos f(x)dx = \sin f(x) + c$</td>
      <td id="T_bd720_row3_col2" class="data row3 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row4_col0" class="data row4 col0" >$y=\cos f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = -f'(x)\sin f(x)$ <br></td>
      <td id="T_bd720_row4_col1" class="data row4 col1" >$ {\Large\int} f'(x)\sin f(x)dx = -\cos f(x) + c$</td>
      <td id="T_bd720_row4_col2" class="data row4 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row5_col0" class="data row5 col0" >$y=\tan f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x)\sec^2 f(x)$ <br></td>
      <td id="T_bd720_row5_col1" class="data row5 col1" >$ {\Large\int} f'(x)\sec^2 f(x)dx = \tan f(x) + c$</td>
      <td id="T_bd720_row5_col2" class="data row5 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row6_col0" class="data row6 col0" >$y=e^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = f'(x) e^{f(x)}$ <br></td>
      <td id="T_bd720_row6_col1" class="data row6 col1" >$ {\Large\int} f'(x)e^{f(x)}dx = e^{f(x)} + c$</td>
      <td id="T_bd720_row6_col2" class="data row6 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row7_col0" class="data row7 col0" >$y=\ln f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{f(x)}$ <br></td>
      <td id="T_bd720_row7_col1" class="data row7 col1" >$ {\Large\int} \dfrac{f'(x)}{f(x)}dx = \ln|f(x)| + c$</td>
      <td id="T_bd720_row7_col2" class="data row7 col2" >Why absolute value?</td>
    </tr>
    <tr>
      <td id="T_bd720_row8_col0" class="data row8 col0" >$y=a^{f(x)} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = (\ln a)f'(x)a^{f(x)}$ <br></td>
      <td id="T_bd720_row8_col1" class="data row8 col1" >$ {\Large\int} f'(x)a^{f(x)}dx = \dfrac{a^f(x)}{\ln  a} +c$</td>
      <td id="T_bd720_row8_col2" class="data row8 col2" >ln a is a constant therefore can be removed from the integral it can go on the other side of the intergral equation when compared to the derivative equation.</td>
    </tr>
    <tr>
      <td id="T_bd720_row9_col0" class="data row9 col0" >$y=log _{a} f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{(\ln a) f(x)}$ <br></td>
      <td id="T_bd720_row9_col1" class="data row9 col1" >$ {\Large\int} \dfrac{f'(x)}{(\ln a) f(x)} = \log_{a} |f(x)|  + c$</td>
      <td id="T_bd720_row9_col2" class="data row9 col2" >Is this integral expression correct, in particular the absolute value?</td>
    </tr>
    <tr>
      <td id="T_bd720_row10_col0" class="data row10 col0" >$y=\sin^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_bd720_row10_col1" class="data row10 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} } dx = \sin^{-1} f(x) + c$</td>
      <td id="T_bd720_row10_col2" class="data row10 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row11_col0" class="data row11 col0" >$ y = \sin^{-1} \dfrac{f(x)}{a}  \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)}{\sqrt{a^2 - (f(x))^2}} $ <br></td>
      <td id="T_bd720_row11_col1" class="data row11 col1" >$ {\Large\int} \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} } dx = \sin^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_bd720_row11_col2" class="data row11 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row12_col0" class="data row12 col0" >$y=\cos^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }$ <br></td>
      <td id="T_bd720_row12_col1" class="data row12 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {1 - (f(x))^2} }  = \cos^{-1}f(x) + c \text{ or } -\sin^{-1}f(x) +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_bd720_row12_col2" class="data row12 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row13_col0" class="data row13 col0" >$y=\cos^{-1} \dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }$ <br></td>
      <td id="T_bd720_row13_col1" class="data row13 col1" >$ {\Large\int} - \dfrac{f'(x)} {\sqrt {a^2 - (f(x))^2} }  = \cos^{-1}\dfrac{f(x)}{a} + c \text{ or } -\sin^{-1}\dfrac{f(x)}{a} +c$
$ \text{Note the cons\tant c will have different values with these two options} $</td>
      <td id="T_bd720_row13_col2" class="data row13 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row14_col0" class="data row14 col0" >$y=\tan^{-1}f(x) \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} = \dfrac{f'(x)} {1 + (f(x))^2}$ <br></td>
      <td id="T_bd720_row14_col1" class="data row14 col1" >$ {\Large\int} \dfrac{f'(x)} {1 + (f(x))^2} dx = \ \tan^{-1} f(x) + c$</td>
      <td id="T_bd720_row14_col2" class="data row14 col2" ></td>
    </tr>
    <tr>
      <td id="T_bd720_row15_col0" class="data row15 col0" >$y=\tan^{-1}\dfrac{f(x)}{a} \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,   \dfrac{dy}{dx} =  \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} $ <br></td>
      <td id="T_bd720_row15_col1" class="data row15 col1" >$ {\Large\int} \dfrac{f'(x)} {a^2 + (f(x))^2} dx = \dfrac{1}{a} \tan^{-1} \dfrac{f(x)}{a} + c$</td>
      <td id="T_bd720_row15_col2" class="data row15 col2" ></td>
    </tr>
  </tbody>
</table>
{{< /tab >}}
{{< /tabs >}}