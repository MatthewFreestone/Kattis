We're given two positive integers $a$ and $b$ under the constraint that $a \le b$, so therefore $\frac{a}{b} \le 1$.
We want to convert as many runners as possible each round, meaning we want to use ALL of the $x$ serious runners each round. Therefore, we just need to find y.

$$ \frac{x}{x+y} \ge \frac{a}{b} $$ 
<!-- DERIVATION BELOW IF WANTED -->
<!-- $$ x \ge \frac{a}{b} \cdot (x+y) $$ 
$$ x - \frac{a}{b}x  \ge \frac{a}{b}y $$ 
$$ \frac{b}{a}\left(x - \frac{a}{b}x\right) \ge y $$ 
$$ \frac{b}{a}x - x \ge y $$ 
$$ \left(\frac{b}{a}-1\right)x \ge y $$  -->
$$ \left(\frac{b-a}{a}\right)x \ge y $$ 
To select the largest y possible without violating this constraint, we take the floor of the left side.
For convenience, let's denote $c = \frac{b-a}{a}$
$$ y^* = \lfloor c \cdot x \rfloor $$
$y^*$ is the runners we convert at that step, increasing the next $x$ by $y^*$.

This leaves us with one easy case: if $y^* = 0$, then the number of runners never goes up, and we can output $-1$.

We're tasked with finding the number of days it takes to convert all runners. One natural approach is to attempt to describe the number of runners as a recurrence relation, then find a closed form for it.   
The number of runners at each day looks like the following:
$$ x, x+\lfloor c \cdot x \rfloor, x + \lfloor c \cdot (x+\lfloor c \cdot x \rfloor)\rfloor, ...$$
Unfortunately, finding the closed form is extremely difficult (maybe imposible!) due to the floor function. Up to this point, I have been unable to find/understand any paper on the topic that applies.

We're left with finding a numerical method to determine the number of days taken. Directly simulating this problem day-by-day with lead to a TLE, as there is a potential to iterature though $10 ^ 9$ days (there might be a tighter upper bound, but whatever).

A key observation is that, in the first days of the simulation, the number of casual runners converted at each step is constant. If we can figure out the number of days that this value is constant, we could skip those days.

If we know that we make $ y^* = \lfloor c \cdot x \rfloor $ each day, we just need to figure out what $x$ would need to be to make $y^*$ higher.
We can determine when it will increase with:
$$ y^* + 1 = \lfloor c\cdot x^* \rfloor $$
$$ y^* + 1 \le c\cdot x^* $$
$$ \frac{y^* + 1}{c} \le x^* $$
$$ \left\lceil \frac{y^* + 1}{c} \right\rceil = x^* $$

Simply find out how far our current $n$ is from that switch spot, then we can $\left \lceil \frac{n - x^*}{y^*} \right\rceil$ days at the same time. We only need to recalculate $y^*$ at the next step.