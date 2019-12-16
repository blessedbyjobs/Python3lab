# u - множество посещенных вершин
# p - кратчайший путь между вершинами
# N[a][b] - вес (a,b)


def dijkstra_shortest_path(graph, start, p=None, u=None):
    if u is None:
        u = []
    if p is None:
        p = {}

    if len(p) == 0:
        # инициализация начального пути
        # расстояние вершины до самой себя равно нулю
        p[start] = 0

    # находим расстояние от вершины до вершин, с которыми она непосредственно соединена
    for x in graph[start]:
        if x not in u and x != start:
            if x not in p.keys() or (graph[start][x] + p[start]) < p[x]:
                p[x] = graph[start][x] + p[start]

    # вершина полностью обработана => помещаем ее к посещенным
    u.append(start)

    # находим близжайшую вершину от текущей
    min_v = 0
    min_x = None
    for x in p:
        if (p[x] < min_v or min_v == 0) and x not in u:
            min_x = x
            min_v = p[x]

    # если обработали все вершины графа, то выход
    if len(u) < len(graph) and min_x is not None:
        return dijkstra_shortest_path(graph, min_x, p, u)
    else:
        return p


if __name__ == '__main__':
    # инициализация графа с помощью словаря смежности
    a, b, c, d, e, f = range(6)
    N = [
        {b: 5, c: 9, f: 14},
        {a: 5, c: 4, d: 15},
        {a: 9, b: 4, d: 11, f: 2},
        {b: 15, c: 11},
        {},
        {a: 14, c: 2}
    ]

    for dot in range(6):
        print(dijkstra_shortest_path(N, dot, {}, []))
