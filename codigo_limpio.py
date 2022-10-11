# EJEMPLO 1
import math
import numpy as np

test_scores = [88, 92, 79, 93, 85]
print(np.mean(test_scores))

curved_test_scores = [math.sqrt(score) * 10 for score in test_scores]
print(np.mean(curved_test_scores))

##########################################

# EJEMPLO 2
age_list = [47, 12, 28, 52, 35]
for i, age in enumerate(age_list):
    if age < 18:
        is_minor = True
        age_list[i] = "minor"
    # some other code

##########################################

# EJEMPLO 3
def count_unique_values(coleccion):
    return len(set(coleccion))