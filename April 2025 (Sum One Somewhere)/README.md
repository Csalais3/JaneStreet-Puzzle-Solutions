# April Puzzle: Sum One Somewhere
The puzzle: This month asked to find a probability (p) where there is exactly a 1/2 probability (chance) that there an infifnite path down a tree whose sum is at most one. Where p is the probability of independently labeling the nodes of an infinite complete binary tree 0 with probability p and 1 otherwise (1 - p).

$\newline$
## The Approach:
Let there be some binary tree ($T$), such that $T$ is infitely rooted and complete. Each node ($v \in T$) is independnetly assigned some label $X$, where:

$$X_v = \begin{cases}
    0 &\text{with probability } p\\\
    1 &\text{with probability } 1- p
  \end{cases}$$

  For each Path ($P$), we sum along its path, whose value ($Y$) can be denoted as:

  $$Y = \sum_{i = 0}^{\infty}{X_{v_{i}}}$$
  
  We can now define some event ($A$), where:
  ```math
   A = \left\{ \exists P : Y \leq 1 \right\}
  ```
Which is the event where there exists at least one infinite path whose summed path is less than or equal to one

Now that we have properly defined the event, 
