from map_states import H, P, u, a, E, w, m, R, S, A

map_1 = [
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
    [u, 0, 0, 0, a, 0, 0, 0, u, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, E, 0, 0, 0, 0, u, 0, 0, a, a, a, a, a, a, a, 0, u],
    [u, a, a, 0, 0, 0, 0, 0, u, E, 0, a, 0, 0, 0, 0, 0, a, 0, u],
    [u, 0, 0, a, a, 0, 0, 0, u, 0, 0, a, 0, 0, a, a, a, a, 0, u],
    [u, 0, 0, 0, a, a, a, 0, u, a, a, a, P, m, H, a, 0, 0, 0, u],
    [u, 0, 0, E, 0, 0, 0, a, u, 0, 0, a, 0, 0, a, a, a, a, 0, u],
    [u, 0, 0, 0, a, 0, 0, 0, u, 0, E, a, 0, a, 0, 0, 0, a, 0, u],
    [u, 0, 0, E, 0, 0, 0, 0, u, 0, 0, a, 0, a, 0, E, 0, a, 0, u],
    [u, 0, 0, 0, a, u, 0, 0, u, a, a, u, a, a, a, a, a, a, 0, u],
    [u, 0, a, 0, 0, u, 0, 0, u, E, 0, u, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, a, E, a, u, u, u, u, u, u, u, u, u, 0, 0, 0, 0, 0, u],
    [u, 0, a, 0, 0, 0, u, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, a, E, a, 0, u, 0, a, a, a, a, a, a, a, a, a, a, a, u],
    [u, 0, a, 0, 0, 0, u, 0, a, a, 0, a, 0, a, 0, a, 0, a, 0, u],
    [u, a, a, a, a, 0, u, 0, a, 0, a, 0, a, 0, a, 0, a, 0, a, u],
    [u, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, a, a, a, a, a, u],
    [u, 0, 0, 0, a, a, a, a, a, 0, a, 0, a, 0, a, 0, a, 0, 0, u],
    [u, m, 0, 0, 0, m, 0, 0, a, E, a, 0, a, E, a, 0, a, E, E, u],
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]
]

map_2 = [
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
    [u, 0, E, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 0, u],
    [u, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, E, a, 0, u],
    [u, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, E, 0, a, 0, u],
    [u, 0, a, 0, u, u, u, u, u, u, u, u, u, u, u, u, 0, a, 0, u],
    [u, 0, a, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, a, 0, u],
    [u, 0, a, 0, a, 0, E, 0, 0, 0, 0, 0, 0, E, 0, a, 0, a, 0, u],
    [u, 0, a, 0, u, 0, 0, a, a, a, a, a, a, 0, 0, u, 0, a, 0, u],
    [u, 0, a, 0, u, 0, 0, a, 0, w, a, 0, a, 0, 0, u, 0, a, 0, u],
    [u, 0, a, 0, u, 0, 0, a, 0, w, P, H, a, 0, 0, u, 0, a, R, u],
    [u, 0, a, 0, u, 0, 0, a, 0, w, 0, a, a, 0, 0, u, 0, a, 0, u],
    [u, A, a, 0, u, 0, 0, a, a, a, a, a, a, 0, 0, u, 0, a, 0, u],
    [u, 0, a, 0, a, 0, E, 0, 0, 0, 0, 0, 0, E, 0, a, 0, a, 0, u],
    [u, 0, a, 0, a, E, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, 0, a, 0, u],
    [u, 0, a, 0, u, u, u, u, u, u, u, u, u, u, u, u, 0, a, 0, u],
    [u, 0, a, m, E, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m, a, 0, u],
    [u, 0, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, E, 0, u],
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]
]
map_3 = [
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
    [u, 0, E, a, 0, E, 0, E, a, 0, 0, 0, a, a, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, a, 0, E, 0, 0, a, 0, 0, a, a, 0, A, 0, E, 0, u],
    [u, 0, 0, a, 0, 0, 0, 0, a, 0, 0, 0, a, 0, a, 0, 0, 0, 0, u],
    [u, 0, 0, 0, a, 0, 0, 0, 0, a, w, w, a, 0, 0, a, 0, 0, 0, u],
    [u, 0, 0, a, 0, 0, 0, 0, a, 0, 0, 0, a, 0, 0, 0, a, 0, 0, u],
    [u, 0, m, 0, a, 0, A, 0, 0, a, 0, 0, a, 0, E, 0, 0, a, 0, u],
    [u, 0, 0, a, 0, 0, 0, 0, a, 0, 0, 0, a, 0, 0, 0, 0, 0, a, u],
    [u, 0, 0, 0, a, 0, 0, 0, 0, a, 0, 0, a, 0, E, 0, 0, a, E, u],
    [u, P, 0, a, H, m, 0, 0, a, 0, E, E, a, 0, 0, 0, a, 0, 0, u],
    [u, 0, 0, 0, a, w, w, w, 0, a, 0, 0, a, 0, 0, a, 0, 0, 0, u],
    [u, 0, 0, a, 0, 0, 0, 0, a, 0, 0, 0, a, 0, a, 0, 0, 0, 0, u],
    [u, 0, 0, 0, a, 0, 0, 0, 0, a, 0, 0, a, a, 0, 0, 0, E, 0, u],
    [u, 0, 0, a, 0, 0, 0, 0, a, 0, 0, 0, a, 0, a, 0, 0, 0, 0, u],
    [u, 0, 0, 0, a, 0, 0, 0, 0, a, 0, 0, a, 0, 0, a, 0, E, 0, u],
    [u, m, 0, a, 0, 0, 0, 0, a, 0, 0, 0, a, 0, 0, 0, a, 0, 0, u],
    [u, 0, 0, 0, a, 0, 0, 0, 0, a, 0, 0, a, 0, E, 0, 0, a, 0, u],
    [u, 0, 0, a, 0, 0, E, 0, a, 0, 0, 0, a, 0, 0, 0, 0, 0, a, u],
    [u, E, 0, 0, a, E, 0, E, 0, a, 0, 0, a, 0, 0, 0, 0, 0, a, u],
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]
]

map_4 = [
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
    [u, a, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, a, H, a, 0, a, u],
    [u, 0, m, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, a, m, a, m, 0, u],
    [u, 0, 0, w, w, w, w, w, w, m, m, w, w, w, w, w, w, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, a, 0, 0, 0, 0, E, 0, 0, u],
    [u, w, w, w, 0, 0, 0, 0, a, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, u],
    [u, E, 0, 0, 0, 0, 0, 0, a, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, a, 0, 0, a, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, w, w, u, u, u, 0, 0, 0, 0, u, w, w, a, a, a, a, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, a, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, a, 0, a, m, 0, 0, m, 0, 0, m, m, m, 0, a, a, a, 0, u],
    [u, 0, a, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, a, 0, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, a, a, a, a, a, a, a, 0, 0, a, a, u],
    [u, 0, a, 0, u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, S, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, R, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]
]
example = [
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, H, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, u],
    [u, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, E, u],
    [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u]
]
