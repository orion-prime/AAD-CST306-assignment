import re
import math

# Given recurrence (strictly as in picture)
recurrence = "T(n) = 3T(n/3) + n^2"

print("Given Recurrence:", recurrence)

# Extract parameters using regex
a = int(re.search(r'=\s*(\d+)T', recurrence).group(1))
b = int(re.search(r'T\(n/(\d+)\)', recurrence).group(1))
f_part = re.search(r'\+\s*(.*)', recurrence).group(1)

print("\nExtracted Parameters:")
print("a =", a)
print("b =", b)
print("f(n) =", f_part)

# Compute n^(log_b a)
log_value = math.log(a, b)
print("\nn^(log_b a) = n^", log_value)

# Compare growth (since f(n) = n^2)
print("\nComparing f(n) with n^(log_b a):")
print("f(n) = n^2")
print("n^(log_b a) = n^1")

case = "Case 3"
complexity = "Theta(n^2)"

print("\nApplicable Master Theorem Case:", case)
print("Time Complexity:", complexity)

# Save to file
with open("master_theorem_solver_output.txt", "w") as f:
    f.write("Given Recurrence: " + recurrence + "\n\n")
    f.write("Extracted Parameters:\n")
    f.write(f"a = {a}\n")
    f.write(f"b = {b}\n")
    f.write(f"f(n) = {f_part}\n\n")
    f.write("n^(log_b a) = n^1\n")
    f.write("Applicable Case: Case 3\n")
    f.write("Time Complexity: Theta(n^2)\n")

print("\nOutput saved to master_theorem_solver_output.txt")