# 幷查集
def union_find(nodes, edges):
    pre = [0] * len(nodes)
    for node in nodes:
        pre[node] = node

    for edge in edges:
        head, tail = edge[0], edge[1]
        pre[tail] = head

    for node in nodes:
        while True:
            pre_of_node = pre[node]
            if pre_of_node != pre[pre_of_node]:
                pre[node] = pre[pre_of_node]
            else:
                break

    L = {}
    for i, node in enumerate(pre):
        if not node in L.keys():
            L[node] = [i]
        else:
            L[node].append(i)

    return L


if __name__ == '__main__':
    nodes = list(range(0, 10))
    test_edges = [[0, 1], [0, 4], [1, 2], [1, 3], [5, 6], [6, 7], [7, 5], [8, 9]]

    L = union_find(nodes, test_edges)
    print(L)
    print('num of pyq:', len(L))
