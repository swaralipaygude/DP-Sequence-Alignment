# DP-Sequence-Alignment
Implementation of two versions of Dynamic Programming solution(basic and efficient) to the Sequence Alignment problem.

<h2> INPUT </h2>
The input to the program would be a text file containing the following information:
1. First base string (𝑠<sub>1</sub>)
2. Next 𝑗 lines consist of indices after which the copy of the previous string needs to be inserted in the cumulative string. (eg given below)
3. Second base string (𝑠<sub>2</sub> )
4. Next 𝑘 lines consist of indices after which the copy of the previous string needs to be inserted in the cumulative string. (eg given below)
Eg:
Input file:
ACTG
3
6
1
TACG
1
2
9

Using the above numbers, the generated strings would be
𝑠<sub>1</sub> : ACACTGACTACTGACTGGTGACTACTGACTGG and
𝑠<sub>2</sub> : TATTATACGCTATTATACGCGACGCGGACGCG

Hence, the length of the first and the second string will be 2<sup>𝑗</sup> * 𝑙𝑒𝑛(𝑠<sub>1</sub>) and 2<sup>k</sup> * 𝑙𝑒𝑛(𝑠<sub>2</sub>) 
