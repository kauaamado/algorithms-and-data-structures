# Synopsis

This repo was created to document my study for the book "Cientista da Computação Autodidata: Guia de estruturas de dados e algoritmos para o iniciante".

## Big O Notation
- The *Big O Notation* is a mathematic notation that describes how the time and space requisits of an algorithm increases as the size of n grows.

There are the types most used to order of magnitude in Big O Notation, ordered from best (most efficient) to worst (least efficient):
- Constant time
- Logarithm time
- Linear time
- Log-linear time
- Quadract time
- Cubic time
- Exponential time

Each order of magnitude describes the time complexity of an algorithm. The *time complexity* is the maximum steps number that an algorithm runs to his conclusion when n grows.

Next, we will examine each order of magnitude.

### Constant time | O(1)
- The most efficient order of magnitude is *constant time complexity*, without a doubt.
- To be an constant time algorithm, it needs to require the same number of steps regardless of his problem size.
- Example:
#### An algorithm that give a free book to the first customers every day
```free_books = customers[0]```
The T(_n_) equation must be `T(_n_) = 1