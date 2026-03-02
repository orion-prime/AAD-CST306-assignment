📘 CST306 - Algorithm Analysis and Design Assignment

This repository contains implementations for:

Master’s Theorem Automatic Recurrence Solver

Single-Source Shortest Path using Dijkstra’s Algorithm

1️⃣ Master’s Theorem Automatic Solver
📂 File

master_solver.py

📝 Problem Statement

Apply Master’s Theorem and implement an automatic recurrence parameter extractor.

Given recurrence:
  T(n)=3T(n/3)+n^2
⚙️ Features

Accepts recurrence of the form:

  T(n)=aT(n/b)+f(n)

Automatically extracts:

a

b

f(n)

Computes:

n^logb(a)

Determines:

Applicable Master’s Theorem case

Final time complexity (Big-O notation)

Saves output to:

master_theorem_solver_output.txt
📊 Analysis for Given Recurrence

a = 3

b = 3

f(n) = n²

n^log3(​3)=n1​



Since:

f(n)=n^2>n1

✅ Master’s Theorem Case 3 applies

⏱ Final Time Complexity
  Θ(n^2)
2️⃣ Single Source Shortest Path – Dijkstra’s Algorithm
📂 File

dijkstra.py

📝 Problem Statement

Implement Dijkstra’s Algorithm using the weighted graph exactly as shown in the given diagram.

Graph contains 9 vertices (0–8)

All edge weights are included exactly as in the figure

Source node: 0

⚙️ Features

Constructs the weighted graph exactly as provided

Implements Dijkstra’s Algorithm using a priority queue

Computes shortest distances from node 0

Displays output in a clean table format

Saves results to:

dijkstra_output.txt
📊 Final Shortest Path Distances from Node 0
Node	Distance
0	0
1	4
2	12
3	19
4	21
5	11
6	9
7	8
8	14


▶️ How to Run

Make sure Python 3 is installed.

Run the following commands:

python master_solver.py
python dijkstra.py

📁 Generated Output Files

master_theorem_solver_output.txt
dijkstra_output.txt
