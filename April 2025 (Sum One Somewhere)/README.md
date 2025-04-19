# April Puzzle: Sum One Somewhere
The puzzle: This month asked to find a probability (p) where there is exactly a 1/2 probability (chance) that there an infifnite path down a tree whose sum is at most one. Where p is the probability of independently labeling the nodes of an infinite complete binary tree 0 with probability p and 1 otherwise (1 - p).

## The Approach:
Let $X$ be the label assigned to each individual node of the tree, where:
$$X = \begin{cases} 0  && p \\ 1 && 1 - p \end{cases}$$

We can denote that the labels for any node on tree as: 
$$X_i \quad \forall i \in \mathbb{Z}^+$$

We can choose any arbituary path by traversing down the tree using the for any 'n' number of nodes through the formula $2^d + k$, where $k \in {0, 1}$, $d \in [0, n](\mathbb{Z})$ 

traversing down this arbituary path, we can denote its sum (Y) for the two cases, the left and right side:
$$Y = \sum_{i \in {2^0, 2^1, 2^2, 2^3, \dots, 2^n}}{X_i}$$
$$Y = \sum_{i \in {1, (2^1 - 1), (2^2 - 1), (2^3 - 1), \dots, (2^n - 1)}}{X_i}$$
