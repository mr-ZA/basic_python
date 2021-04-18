import os
import json
import numpy as np
from bs4 import BeautifulSoup

from calc import main, forward

def file_to_bs4(file):
    with open(file, 'r', encoding='utf-8') as f:
        return BeautifulSoup(f.read(), "html.parser")


Y = []
X = []
page = file_to_bs4(os.path.join('files', 'closer', 'closers.html'))

ref = []
for img in page.find_all('img'):
    node = img
    for i in range(5):
        if node.name not in ref:
            ref.append(node.name)
        if node.has_attr('class'):
            for c in node['class']:
                if c not in ref:
                    ref.append(c)
        node = node.parent

print(ref)
used_src = []
for img in page.find_all('img'):
    if img.has_attr('src') and (img['src'] not in used_src or img['src'] == 'cache/ma3-appliance/fwskin_delete_ico.png'):
        used_src.append(img['src'])
        window = []
        if img['src'] == 'cache/ma3-appliance/fwskin_delete_ico.png':
            Y.append([1, 0])
        else:
            Y.append([0, 1])
        node = img
        for i in range(5):
            window.append([1 if x == node.name or (node.has_attr('class') and x in node['class']) else 0 for x in ref])
            node = node.parent
        X.append(np.array(window))

print(np.array(Y))
print(np.array(X).shape)
k, w1, w2, w3 = main(np.array(X), np.array(Y))

synapse = {'kernel': k.tolist(), 'W_1': w1.tolist(), 'W_2': w2.tolist(), 'W_3': w3.tolist()}
synapse_file = "synapses.json"
with open(synapse_file, 'w', encoding='utf-8') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)

for x in X:
    l3, _, _, _ = forward(x, k, w1, w2, w3)
    print(l3)

