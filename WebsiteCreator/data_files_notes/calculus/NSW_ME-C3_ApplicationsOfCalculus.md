### <span style="color:RGB(139,69,19)">  Concepts </span>

 - Intergrand
 - solid of revolution
 - differential equation
 - direction field or slope field
 - first-order differential equation
 - logistic equation


### <span style="color:RGB(139,69,19)">  Notes </span>

#### Further area and volumes of solids of revolution
 
Volumes formed by rotation about the x-axis = $V=\pi \int_a^b y^2 dx$
 - The volume calculated is between the curves and point a and b on the x-axis, as the curve is rotated around the x-axis


Volumes formed by rotation about the y-axis = $V=\pi \int_a^b x^2 dy$
- The volume calculated is between the curves and point a and b on the y-axis, as the curve is rotated around the y-axis
 - If a question provides 2 points on the x-axis, the a and b values on the y-axis need to be calculated by using the original function formula.

 <span style="color:RGB(255,0,0)">  Can above formulas be used directly in questions or do they need to be derived.  They do not appear on the formula sheet or in the syllabus  </span>

 Remember to specify $\text{units}^3$ when providing a volume answer if no other specific measure e.g. cm is provided in the question.


 #### Differential equations

 Be able to sketch direction fields / slope fields

 **Solving differential equations in the form $\frac{dy}{dx}=f(x)$**
 - The solution is an equation on the format of y=f(x)
 
 - This involves finding the integral (anti-derivative)

<br>
 
 **Solving differential equations in the form $\frac{dy}{dx}=g(y)$**
 - Note how the derivative "denominator" is x but function g is defined in terms of y.

 - This equation can be interpreted as "the gradient of y=f(x) is a function of it's y-value, that is the gradient can be determined if a y-value is provided"

 - The same as above, these problems involve finding a solution equation on the format of y=f(x)

 - Need to use the fact that $\frac{dy}{dx} = \dfrac{1}{\frac{dx}{dy}}$, that is invert g(y) and calculate $\frac{dx}{dy}$ which will provide an equation in the format x=f(y)

 - As a final step make y the subject of the above equation.

 - Be on on the lookout for derivative "denominators" that don't match the variable in the equation.


<br>

 **Solving differential equations in the form $\frac{dy}{dx}=f(x)g(y)$**

 - This equation can be interpreted as "the gradient of y=f(x) is a function of both it's x and y-value"

 - These equations can sometimes be solved by the separation of variables which places the y's on the left and x's on the right, that is: $\dfrac{1}{g(y)}dy = f(x)dx$

- Both sides can then be integrated

- Not all differential equations are separable.

<br>

**Exponential Growth and Decay**

 - Exponential growth and decay equations covered in Year 11, ext 1 are first-order linear differential equations, effectively in the format $\frac{dy}{dx}=g(y)$



**Logistic Equation**

This is a more realistic model than the exponential growth and decay which restricts the population to a maximum level.

Population is a function of time, that is P(t) and $\frac{dP}{dt}$ represents the instantaneous rate of change of the population at a specific time

Option 1: $\frac{dP}{dt} = kP(N-P)$ <br><br>
Option 2: $\frac{dP}{dt} = kP(1-\frac{P}{N})$, where 
 - t is time
 - k is the growth rate
 - P is population
 - N is the limiting condition or carrying capacity (defined to be the maximum population of that organism that the environment can sustain indefinitely)

Note that the first part of above equations, $\frac{dP}{dt} = kP$, is the simple expononential growth and decay equation (although the later tends to use the symbol N instead of P).  In both options above kP is then multiplied by a factor which results in the rate of change ceasing once a limit  is reached.

