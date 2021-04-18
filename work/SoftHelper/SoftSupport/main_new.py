from os import path
import json
import numpy as np
from bs4 import BeautifulSoup


class SoftSupport:

    def __init__(self):
        self.ref_vector = []
        self.files_folder = 'files'
        self.X = None
        self.Y = None
        self.W_1 = None
        self.W_2 = None
        self.tag = None
        self.parents = 8
        self.pos_vectors = []
        self.neg_vectors = []

    def file_to_bs4(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            return BeautifulSoup(f.read(), "html.parser")

    def create_ref_vector(self, ref_file_path: tuple, tag: str):
        page = self.file_to_bs4(path.join('files', *ref_file_path))

        for tag_el in page.find_all(tag):
            node = tag_el
            for i in range(self.parents):
                if node:
                    if node.name not in self.ref_vector:
                        self.ref_vector.append(node.name)
                    if node.has_attr('class'):
                        for c in node['class']:
                            if c not in self.ref_vector:
                                self.ref_vector.append(c)
                    node = node.parent
                else:
                    break

    def append_parents(self, el, _vec):
        node = el
        for i in range(self.parents):
            if node:
                _vec += [1 if x == node.name or (node.has_attr('class') and x in node['class']) else 0 for x in
                         self.ref_vector]
                sibling = node.find_next_sibling()
                if sibling:
                    _vec += [1 if x == node.name or (node.has_attr('class') and x in node['class']) else 0 for x
                             in
                             self.ref_vector]
                else:
                    _vec += [0 for x in self.ref_vector]
                node = node.parent
            else:
                _vec += 2*[0 for x in self.ref_vector]
        return _vec

    def vectorize_file(self, learn_file_path: tuple, tag: str, positive_instruction: tuple):
        page = self.file_to_bs4(path.join('files', *learn_file_path))
        prev_pos = False
        prev_neg = False
        X = []
        Y = []
        positive_count = 0
        negative_count = 0
        if tag == 'img':
            for tag_el in page.find_all(tag):
                if tag_el.has_attr('src'):
                    vec = []
                    if tag_el['src'] in positive_instruction:
                        Y.append([1, 0])
                    else:
                        Y.append([0, 1])
                    vec = self.append_parents(tag_el, vec)
                    X.append(np.array(vec))

        elif tag == 'label':
            for tag_el in page.find_all(tag):
                vec = []
                if tag_el.has_attr('title'):
                    # print(tag_el['title'] if tag_el.has_attr('title') else 0)
                    if tag_el['title'] in positive_instruction:
                        positive_count += 1
                        Y.append([1, 0])
                        vec = self.append_parents(tag_el, vec)
                        self.pos_vectors.append(np.array(vec))
                        if isinstance(prev_pos, np.ndarray):
                            similar = np.dot(np.array(vec), prev_pos)/(np.linalg.norm(np.array(vec))*np.linalg.norm(prev_pos))
                            print(similar)
                            prev_pos = np.array(vec)
                        else:
                            prev_pos = np.array(vec)
                    else:
                        negative_count += 1
                        Y.append([0, 1])
                        vec = self.append_parents(tag_el, vec)
                        self.neg_vectors.append(np.array(vec))
                        if isinstance(prev_neg, np.ndarray):
                            similar = np.dot(np.array(vec), prev_neg)/(np.linalg.norm(np.array(vec))*np.linalg.norm(prev_neg))
                            if similar > 0.5:
                                print(similar, 'neg')
                            prev_neg = np.array(vec)
                        else:
                            prev_neg = np.array(vec)
                    X.append(np.array(vec))
                else:
                    negative_count += 1
                    Y.append([0, 1])
                    vec = self.append_parents(tag_el, vec)
                    self.neg_vectors.append(np.array(vec))
                    X.append(np.array(vec))
        print(positive_count, negative_count)
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.tag = tag

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-1 * x))

    def div_sigmoid(self, x):
        return x * (1 - x)

    def weight_init(self):
        def val(n_in, n_out):
            a = -np.sqrt(6)/np.sqrt(n_in + n_out)
            b = np.sqrt(6)/np.sqrt(n_in + n_out)
            return 1/2*(b-a)
        self.W_1 = np.full((len(self.X[0]), 4), val(len(self.X[0]), 4))
        self.W_2 = np.full((4, 2), val(4, 2))

    def forward_propagation(self):
        l1 = self.sigmoid(np.dot(self.X, self.W_1))
        l2 = self.sigmoid(np.dot(l1, self.W_2))
        return l1, l2

    def back_propagation(self, L1, L2, alpha):
        l1 = L1
        x1 = self.X
        l1_t = np.transpose(l1)
        x_t = np.transpose(x1)
        w2_t = np.transpose(self.W_2)

        l2_error = self.Y - L2
        l2_delta = l2_error * self.div_sigmoid(L2)

        l1_error = np.dot(l2_delta, w2_t)
        l1_delta = l1_error * self.div_sigmoid(L1)

        div_J2 = np.dot(l1_t, l2_delta)
        div_J1 = np.dot(x_t, l1_delta)

        weight_2 = self.W_2 + alpha * div_J2
        weight_1 = self.W_1 + alpha * div_J1

        return weight_1, weight_2, l2_error

    def train(self, epochs=10000, alpha=0.5):
        self.weight_init()
        for i in range(epochs):
            layer_1, layer_2 = self.forward_propagation()
            self.W_1, self.W_2, d_err = self.back_propagation(layer_1, layer_2, alpha)
            if i % 1000 == 0:
                print('i1=', np.mean(d_err))

    def save_to_json(self, name: str):
        if name.endswith('.json'):
            name = name.split('.')[0]
        suffix = 0
        while path.isfile(f"{name}.json"):
            suffix += 1
            name = f'{name}_{suffix}'
        synapse = {'W_1': self.W_1.tolist(), 'W_2': self.W_2.tolist(), 'ref_vec': self.ref_vector, 'tag': self.tag}
        synapse_file = f"{name}.json"
        with open(synapse_file, 'w') as outfile:
            json.dump(synapse, outfile, indent=4, sort_keys=True)

    def loadout(self, name):
        if not path.isfile(name):
            print(f'no such file {name}')
        else:
            with open(name) as data_file:
                synapse = json.load(data_file)
                self.W_1 = np.asarray(synapse['W_1'])
                self.W_2 = np.asarray(synapse['W_2'])
                self.ref_vector = synapse['ref_vec']
                self.tag = synapse['tag']

    def find_object(self, dom):
        count = 0
        if self.tag == 'img':
            for tag_el in dom.find_all(self.tag):

                vec = []
                vec = self.append_parents(tag_el, vec)
                self.X = np.array(vec)
                _, l_2 = self.forward_propagation()
                if l_2[0] > 0.3:
                    print(l_2, tag_el['src'])

        elif self.tag == 'label':
            print(self.tag)
            for tag_el in dom.find_all(self.tag):
                vec = []
                vec = self.append_parents(tag_el, vec)
                self.X = np.array(vec)
                _, l_2 = self.forward_propagation()
                if l_2[0] > 0.3:
                    count += 1
                    print(l_2, tag_el)
                # p = []
                # n = []
                # for p_vector in self.pos_vectors:
                #     # similar = np.dot(np.array(vec), p_vector) / (
                #     #             np.linalg.norm(np.array(vec)) * np.linalg.norm(p_vector))
                #     # p.append(similar)
                #     dist_p = np.linalg.norm(np.array(vec) - p_vector)
                #     p.append(dist_p)
                # for n_vector in self.neg_vectors:
                #     # similar = np.dot(np.array(vec), n_vector) / (
                #     #             np.linalg.norm(np.array(vec)) * np.linalg.norm(n_vector))
                #     # n.append(similar)
                #     dist_n = np.linalg.norm(np.array(vec) - n_vector)
                #     n.append(dist_n)
                # if np.mean(p) < np.mean(n):
                #     print(np.mean(p), np.mean(n), tag_el)
        print(count)


if __name__ == '__main__':
    s = SoftSupport()
    # s.create_ref_vector(('closer', 'closers.html'), 'img')
    # s.vectorize_file(('closer', 'closers.html'), 'img', ('cache/ma3-appliance/fwskin_delete_ico.png'))
    # s.train()
    # # s.loadout(path.join(path.dirname(__file__), 'closer_1.json'))
    # s.find_object(s.file_to_bs4(path.join('files', 'routine_window', 'atfa025.html')))

    # s.create_ref_vector(('label', 'labels.html'), 'label')
    # s.vectorize_file(('label', 'labels.html'), 'label', ('Основные средства (2)', 'Основные средства (1)'))
    # s.train(2000)
    # s.find_object(s.file_to_bs4(path.join('files', 'label', 'labels.html')))
    # # s.save_to_json('menu1')

    s.create_ref_vector(('label', 'labels2.html'), 'label')
    s.vectorize_file(('label', 'labels2.html'), 'label', ('positive'))
    s.train(2000)
    s.find_object(s.file_to_bs4(path.join('files', 'label', 'labels2.html')))
    # s.save_to_json('menu2')