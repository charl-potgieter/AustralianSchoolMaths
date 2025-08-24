### <span style="color:RGB(139,69,19)">  Concepts </span>
 - concatvity
 - local min or max
 - global min or max
 - point of inflection
 - horizontal point of inflection
 - monotonic increasing or decreasing


### <span style="color:RGB(139,69,19)">  Notes </span>

#### The first and second derivatives

**The second derivative** = $f''(x)$ or $\dfrac{d^{2}y}{dx^2}$
 
**Sign of the first derivative**
 - if f'(x)>0 then the graph y=f(x) is increasing
 - if f'(x)<0 then the graph y=f(x) is decreasing
 - if f'(x)=0 then the graph y=f(x) has a stationary point
 - if f'(x)>0 for all values of x then the curve is monotonic increasing
 - if f'(x)<0 for all values of x then the curve is monotonic decreasing

**Sign of the second derivative**
 - if f''(x)>0 
    - then f'(x) is increasing
    - the gradient of the tangent of f(x) is increasing (a greater upward slope or lesser downward slope)
    - f(x) is concave upwards
    - if f'(x)=0 this is a mimimum turning point
 - if f''(x)<0 
    - then f'(x) is decreasing
    - the gradient of the tangent of f(x) is decreasing (a lesser upward slope or greater downnward slope)
    - f(x) is concave downwards
    - if f'(x)=0 this is a maximum turning point
 - if f''(x) = 0
     - f'(x) is a constant
     - the tangent is neither increasing nor decreasing
     - if concavity changes it is a point of inflection
     - if concavity changes and f'(x)=0 it is a horizontal point of inflection

To test whether concavity changes test f''(x) just to the left and the right of the point being investigated.


**Stationary points**
 - Local minimum point
    - f'(x) = 0 at point
    - f'(x)<0 LHS of the point
    - f'(x)>0 RHS of the point
    - Or f'(x)=0 and f''(x)>0 
 - Local maximum point
    -  f'(x) = 0 at point
     - f'(x)>0 LHS of the point
     - f'(x)<0 RHS of the point
     - Or f'(x)=0 and f''(x)<0

**Inflection**
 - Point of inflection
   - f''(x) = 0,
   - and concavity changes at that point
 - Horizontal point of inflection
   - f''(x) = 0,
   - and concavity changes at that point,
   - and f'(x)=0

 <!-- Paramater SiteRoot is defined in config.toml -->
<img class="special-img-class" src="/{{< param SiteRoot >}}/images/MA_C3_CurveGraphSummary.jpg" />


#### Applications of the derivative

**Curve sketching techniques**
 - find stationary points where f'(x)=0
 - find points of inflection where f''(x)=0 and concavity changes
 - find x and y intercepts
 - find domain and range
 - identify any asymptotes or disontinuities
 - identify limiting behaviour of the function
 - Use symmetry where possible
    - even function f(-x) = f(x)  (graph is symmetrical in y-axis)
    - odd function f(-x) = -f(x)  (graph has rotational symmetry with respect to the origin,that is it remains unchanged after rotation of 180 degrees about the origin)
 - If the 2nd derivative is hard to calculate, the first derivative can be calculated to the left and right of the point being investigated to determine whether the curve is increasing or decreasing
  - Rembember to restrict domains when there is a square root involved.  The expression inside the square root must be greater than zero.

  **Global maxima and minima**
  
  Need to check turning points as well as endpoints in the domain for potential candidates.

  **Optimisation problems**
   - Find formula for quantity that is being maximised or minimised
   - Find min/max values using derivatives
   - Always check if an answer for f'(x)=0 is yielding a min or max with either
       - a second derivative calculation
       - calculating the first derivative at points just before and after the point being investigated.