# 22 Iyun 2021
### What i _transistor_ and how it works?
  A transistor is a 3 terminal electronic device made of semiconductor material. It has many uses like  amplification, switching, voltage regulation, and the modulation of signals. There are 2 types of BJT:
  
   - pnp
      - *Base is connected to the higher potential to allow current flow.*
      -  It means high potential at collector and low potential at emitter.
       
   - npn
        - *Base is connected to the lower potential that allows current flow*
       -  It means high potential at emitter and low potential at collector.
       
  It has 3 elements:**emitter collecter and base.**
  1. ***Emitter***: emits the electrons which pass through device.
   2. ***Collector***: collect them while thes pass through the device.
   3. ***Base***: The middle section which forms two pn junctions between the emitter and collector. The base-emitter junction is forward biased, allowing low resistance for the emitter circuit. The base-collector junction is reverse biased and provides high resistance in the collector circuit.
  
### How to convert between 10-digit number system and 2-digit number system?
  - In binary numbers we use just 2 digits: 0 and 1.(2 lik say sistemi)
  - In decimal numbers we use 10 digits; from 0 to .(10 luq say sistemi)
 
  ## *When i want to convert decimal number to binary number*
  1. We should devide it 2 till the result will be 1.
  2. Then we use remainders, arrange them from the bottom the the top.
 
 For example:
 > 35
 > 
 > 35:2=17 r(1)
 > 
 > 17:2=8 R(1)
 > 
 > 8:2=4 R(0)
 > 
 > 4:2=2 R(0)
 > 
 > 2:2=1 R(0)

Then we should rearrange remainders from the left to the right starting from the last one. 

> 00011
> So, **35**(decimal)=**100011**(binary)

  ## *When i want to convert binary number to decimal number*
  1. We should write the degree of the digits from the left to the right
  2. Then we multiply o and 1 with their degrees and find the sum of them.
    For example;
    
   >1010010
    
   >1*2('6)+0*2('5)+1*2('4)+0*2('3)+0*2('2)+1*2('1)+0*2('0)=64+0+16+0+0+2+0=82
    
   > IT MEANS that **1010010**(binary)= **82** (decimal)  

[sources for transistors](https://www.explainthatstuff.com/howtransistorswork.) 

[sources for transistors](https://www.electronics-notes.com/articles/electronic_components/transistor/how-does-a-transistors-works-basics-tutorial.php)

[sources for conversion of numbers](https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm)

[sources for conversion of numbers](https://www.youtube.com/watch?v=rsxT4FfRBaM)


 # 23 Iyun 2021
## Differences between Interpreter and Compiler

We generally write a computer program using a high-level language. A high-level language is one that is understandable by us, humans. This is called ***source code.***

However, a computer does not understand high-level language. It only understands the program written in 0's and 1's in binary, called the ***machine code.***

To convert source code into machine code, we use either a compiler or an interpreter.
1. **Interpreter** translates just one statement of the program at a time into machine code.	**Compiler** scans the entire program and translates the whole of it into machine code at once.
 
2.  An **interpreter** takes very less time to analyze the source code. However, the overall time to execute the process is much slower.	**A compiler** takes a lot of time to analyze the source code. However, the overall time taken to execute the process is much faster.
 
 3. An **interpreter** does not generate an intermediary code. Hence, an interpreter is highly efficient in terms of its memory.	**A compiler** always generates an intermediary object code. It will need further linking. Hence more memory is needed.
 
4.  Keeps translating the program continuously till the first error is confronted. If any error is spotted, it stops working and hence debugging becomes easy.	A **compiler** generates the error message only after it scans the complete program and hence debugging is relatively harder while working with a compiler.
 
5.  **Interpreters** are used by programming languages like Ruby and Python for example.	**Compliers** are used by programming languages like C and C++ for example.

6.	**Compiler** store machine language as machine code on the disk	**Interpreter** Not saving machine code at all.

## Differences Between Python and JavaScript

- Python is strongly typed – no implicit conversion between types, whereas JavaScript is weakly typed.
- The synchronous and blocking code is standard in JavaScript, whereas python as de-facto as default.
- JavaScript can be used to run on the frontend, whereas python is on server-side programming or backend.
- Python has procedural programming, whereas Java-Script does not have.
- Java-Script has; as a statement terminator, whereas python has a newline.
- Python is a better-designed language that makes it easy to maintain, whereas JavaScript is poor.
- Python is not good for mobile development, whereas Java-Script is good.
- Python is slow to run compared to JavaScript.
- Python provides a huge standard library, whereas JavaScript has a limited standard library.
- Python heavily relies on assignments with no difference between variables and assignment, whereas JavaScript doesn’t relay.
- Python has many libraries for scientific computing, data analytics, and machine learning, whereas JavaScript does not.
- Python has support for many numeral data types like int, float, fixed-point decimal, whereas Java-Script mainly works on floating-point variables.
- Python has an inbuilt REPL, whereas JavaScript does not have.
- JavaScript runs on both browser and server, whereas python is mostly used for server-side programming.

## Top 10 list of visual studio code extensions in 2020 for python.
1. Python extension for Visual Studio Code
2. TabNine
3. Python Preview
4. Indent-Rainbow
5. Bracket Pair Colorizer
6. Python Snippets
7. Python Test Explorer for Visual Studio Code
8. Better Comments
9. autoDocstring
10. Python Indent

## Terminal Commands
- For creating new folder, we use **mkdir** command
- For creating new file, we use    
    - > code -r.
    - > code -r code -r (path-to-working-directory)
    - > ctrl + n // Windows/Linux


## 24 Iyun 2021
## Python Identity Operators


## Python Membership Operators
