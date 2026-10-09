
# Experiment 1: Student Subject Average

import numpy as np  # Import NumPy library

# Create a 4x4 array of student marks
# Columns: Math, Science, English, History
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 85, 80, 75],
    [78, 95, 85, 82],
    [88, 88, 90, 86]
])

# Store subject names in the same order as the columns
subjects = ["Math", "Science", "English", "History"]

# Calculate average marks column-wise (axis=0)
averages = np.mean(student_scores, axis=0)

# Find the highest average score
highest_average = np.max(averages)

# Find the position of the highest average
highest_index = np.argmax(averages)

# Display the results
print("Subject-wise averages:")
for i in range(len(subjects)):
    print(subjects[i], ":", averages[i])

print("Highest average subject:", subjects[highest_index])
print("Highest average score:", highest_average)
