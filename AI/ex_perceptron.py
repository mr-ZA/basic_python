import numpy as np

# activation function 
def get_activation(x):
    return 0 if x < 0.5 else 1

# n calculus
def calc(house, rock, beauty):
    x = np.array([house, rock, beauty])     # input signals vector
    
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]    # weights for neurons in hidden layer
    weight_1layer = np.array([w11, w12])
    weight_2layer = np.array([-1, 1])

    sum_hidden = np.dot(weight_1layer, x)   # first layer sum in hidden
    out_hidden = np.array([get_activation(x) for x in sum_hidden])
    print(f"Sum on neurons in hidden layer: [{sum_hidden}]")
    print(f"Signals on exit of neurons in hidden layer: [{out_hidden}]")

    sum_end = np.dot(weight_2layer, out_hidden)
    y = get_activation(sum_end)
    print(f"Result value of neural network is : [{y}]")

    return y

house = int(input("Got a house? (0/1)\n>> "))
rock = int(input("Love rock music? (0/1)\n>> "))
beauty = int(input("Beauty? (0/1)\n>> "))

res = calc(house, rock, beauty)
if res == 1:
    print("\nCall me ;)")
else:
    print("\nI wish, I had that bf :))))")