import requests
import numpy as np
import matplotlib.pyplot as plt

# requests
print("Requests library:")
response = requests.get("https://www.google.com/")
print(f"Status code: {response.status_code}")
print(f"Content type: {response.headers['Content-Type']}")
print(f"First 100 characters of the response: {response.text[:100]}")

# numpy
print("\nNumpy library:")
array = np.array([1, 2, 3, 4, 5])
print(f"Array: {array}")
print(f"Sum of array: {np.sum(array)}")
print(f"Mean of array: {np.mean(array)}")

# matplotlib
print("\nMatplotlib library:")
plt.plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Simple plot")
plt.show()
