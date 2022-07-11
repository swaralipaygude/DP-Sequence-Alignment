# DP-Sequence-Alignment
Implementation of two versions of Dynamic Programming solution(basic and memory efficient) to the Sequence Alignment problem.


<h3> INPUT </h3>

The sample inputs are given in the SampleTestCases folder, named input1.txt, input2.txt, etc. 

The input to the program is a text file containing the following information: <br/>
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


<h3> OUTPUT </h3>

The sample outputs are given in the SampleTestCases folder, named output1.txt, output2.txt, etc. 

The output to the program is a text file containing the following information: <br/>
1. Cost of the alignment (Integer) <br/>
2. First string alignment ( Consists of A, C, T, G, _ (gap) characters) <br/>
3. Second string alignment ( Consists of A, C, T, G, _ (gap) characters) <br/>
4. Time in Milliseconds (Float) <br/>
5. Memory in Kilobytes (Float) <br/>


<h3> OTHER DATA </h3>

The folder 'datapoints' contains input files to generate graph data points, for graphs which are in the 'Summary' file. <br/>
The 'Summary' file contains the following: <br/>
1. Datapoints output table (which is generated from provided input files) <br/>
2. Two graphs along with insights: <br/>
   1) Single plot of CPU time vs problem size for the two solutions. <br/>
   2) Single plot of Memory usage vs problem size for the two solutions. 
   
   


