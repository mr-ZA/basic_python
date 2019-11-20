labels = [1, 2, 3, 4, 5]

def info(x):
    print("L")

def info_2():
    print("X")

labels_result = list (filter (info, labels))                # Simply call info() for every of labels
print("\n")

labels_result = list (filter (lambda x: info_2(), labels))  # Call lambda function as much as arguments amount, characterizing loop times (every of labels)
                                                            # Lambda call info_2() function as much as arguments count in labels iterable.