#p1(x) = exp(-x ** 2 / 2),     for x < -1.0 or x > 1.0
#p1(x) = exp(-x ** 2 / 2) / 2, for -1 <= x <= 1.0
p2(x) = exp(-x ** 2 / 2),     for any x


1. Draw a sample x distributed according to p2(x).
2. Generate a uniform random number eta between 0 and p2(x).
3. If eta <= p1(x), output x. If eta>p1(x), restart from 2.
