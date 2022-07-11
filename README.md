# DP-Sequence-Alignment
Implementation of two versions of Dynamic Programming solution(basic and efficient) to the Sequence Alignment problem.

<h4> INPUT </h4>

The input to the program would be a text file containing the following information: <br/>
1. First base string (𝑠<sub>1</sub>) <br/>
2. Next 𝑗 lines consist of indices after which the copy of the previous string needs to be inserted in the cumulative string. (eg given below) <br/>
3. Second base string (𝑠<sub>2</sub>) <br/>
4. Next 𝑘 lines consist of indices after which the copy of the previous string needs to be inserted in the cumulative string. (eg given below) <br/>

Eg. Input file: <br/>
ACTG <br/>
3 <br/>
6 <br/>
1 <br/>
TACG <br/>
1 <br/>
2 <br/>
9 <br/>

Using the above numbers, the generated strings would be <br/>
𝑠<sub>1</sub> : ACACTGACTACTGACTGGTGACTACTGACTGG <br/>
𝑠<sub>2</sub> : TATTATACGCTATTATACGCGACGCGGACGCG <br/>

Hence, the length of the first and the second string will be 2<sup>𝑗</sup> * 𝑙𝑒𝑛(𝑠<sub>1</sub>) and 2<sup>k</sup> * 𝑙𝑒𝑛(𝑠<sub>2</sub>) 
