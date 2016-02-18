# Why Analyze algorithms

To predict the performance. Helps us with a benchmark to compare algorithms. The practical reason is to avoid performance bugs. We need some confidence to show that the algorithm completes the job in the stipulated time. Usually if the client gets bad performance, that is because the programmer did not understand the spec requirements. 

In this course, we are going to
* Predict Performance
* Compare Algorithms
* Provide Guarantees

To understand the theoretical basis of algorithms, take a look at the courses on theory of algorithms.

Discrete Fourier Transform brute force takes N^2 time. But the FFT algorithm takes only N lg N.

N-body simulation algorithm: Barnes-Hut algorithm does in N lg N

From Donald Knuth, use the scientific method to apply to analysis of Algo
* Observe
* Hypothesizw
* Predict
* Verify
* Validate
* Experiments must be reproducible
* Hypothesis must be falsifiable
