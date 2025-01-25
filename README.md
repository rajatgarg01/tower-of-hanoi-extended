# Tower of Hanoi Extended Solution

This repository contains the solution to an advanced variation of the Tower of Hanoi problem, designed as part of an algorithm design assignment. The problem introduces constraints such as directional moves (clockwise or counterclockwise) and alternating move types (blue/red moves).

## Problem Description

The objective is to determine the shortest sequence of moves required to transform an initial state to a final state under specific rules:
1. The smallest disk (`Disk 1`) moves alternately in a consistent direction: clockwise or counterclockwise.
2. Non-smallest disks (`Red moves`) follow the standard Tower of Hanoi rules, ensuring larger disks are not placed on smaller ones.
3. The solution must explore all four starting options:
   - Blue Clockwise
   - Blue Counterclockwise
   - Red Clockwise
   - Red Counterclockwise

The program outputs the first valid solution or declares the transformation impossible.

## File Descriptions

- **`final_solution.py`**: Python script implementing the solution. It reads input from `stdin`, processes the problem, and prints the results.
- **`examples/`**: Contains example input and output files to illustrate usage.
- **`tests/`**: Unit test cases for verifying the correctness of the implementation.

## Usage

To run the solution, provide the input format as described below:

### Input Format
- The first line contains an integer, `num_case`, the number of test cases.
- For each test case:
  - The first line specifies the initial state of the pegs, formatted as three comma-separated lists of disk numbers.
  - The second line specifies the desired final state in the same format.

### Example
Input:
This represents:
- **Initial State**: All disks (1, 2, 3) are on peg A.{[1,2,3],[],[]}
- **Final State**: All disks (1, 2, 3) are on peg C.{[],[],[1,2,3]}

  Output:
  blue move and clockwise direction: Total steps: 7, goal is reached


  
### Explanation

- The solution begins with a blue move (`Disk 1`) in a clockwise direction.
- The sequence of moves follows the Tower of Hanoi recursive logic with the smallest disk always moving first.
- After 7 moves, the final state is reached.
