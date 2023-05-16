import pytest

from rad_tools.crystal.decomposition import *


@pytest.mark.parametrize(
    "cell, real_planes",
    [
        (
            [[2, 0, 0], [0, 2, 0], [0, 0, 2]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
            },
        ),  # CUB
        (
            [[1, 1, -1], [1, -1, 1], [-1, 1, 1]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (1 / 2, 1 / 2, 0),
                (-1 / 2, -1 / 2, 0),
                (0, 1 / 2, 1 / 2),
                (0, -1 / 2, -1 / 2),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (1 / 2, 1 / 2, 1 / 2),
                (-1 / 2, -1 / 2, -1 / 2),
            },
        ),  # FCC
        (
            [[1, 1, 0], [1, 0, 1], [0, 1, 1]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (-1 / 2, 1 / 2, 0),
                (1 / 2, -1 / 2, 0),
                (0, 1 / 2, -1 / 2),
                (0, -1 / 2, 1 / 2),
                (1 / 2, 0, -1 / 2),
                (-1 / 2, 0, 1 / 2),
            },
        ),  # BCC
        (
            [[2, 0, 0], [0, 2, 0], [0, 0, 1]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
            },
        ),  # TET
        (
            [[0, 1, 2], [1, 0, 2], [1, 1, 0]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (-1 / 2, 1 / 2, 0),
                (1 / 2, -1 / 2, 0),
                (0, 1 / 2, -1 / 2),
                (0, -1 / 2, 1 / 2),
                (1 / 2, 0, -1 / 2),
                (-1 / 2, 0, 1 / 2),
            },
        ),  # BCT1
        (
            [[0, 2, 1], [2, 0, 1], [2, 2, 0]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (-1 / 2, 1 / 2, 0),
                (1 / 2, -1 / 2, 0),
                (0, 1 / 2, -1 / 2),
                (0, -1 / 2, 1 / 2),
                (1 / 2, 0, -1 / 2),
                (-1 / 2, 0, 1 / 2),
                (1 / 2, 1 / 2, -1 / 2),
                (-1 / 2, -1 / 2, 1 / 2),
            },
        ),  # BCT2
        (
            [[2, 0, 0], [0, 1, 0], [0, 0, 0.6667]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
            },
        ),  # ORC
        (
            [[-2.222, 1.6, 1.2], [2.222, -1.6, 1.2], [2.222, 1.6, -1.2]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (1 / 2, 1 / 2, 0),
                (-1 / 2, -1 / 2, 0),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (1 / 2, 1 / 2, 1 / 2),
                (-1 / 2, -1 / 2, -1 / 2),
            },
        ),  # ORCF1
        (
            [[-1.818, 1.6, 1.2], [1.818, -1.6, 1.2], [1.818, 1.6, -1.2]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (1 / 2, 1 / 2, 0),
                (-1 / 2, -1 / 2, 0),
                (0, 1 / 2, 1 / 2),
                (0, -1 / 2, -1 / 2),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (1 / 2, 1 / 2, 1 / 2),
                (-1 / 2, -1 / 2, -1 / 2),
            },
        ),  # ORCF2
        (
            [[-2, 1.6, 1.2], [2, -1.6, 1.2], [2, 1.6, -1.2]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (1 / 2, 1 / 2, 0),
                (-1 / 2, -1 / 2, 0),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (1 / 2, 1 / 2, 1 / 2),
                (-1 / 2, -1 / 2, -1 / 2),
            },
        ),  # ORCF3
        (
            [[0, 1, 0.6667], [2, 0, 0.6667], [2, 1, 0]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (-1 / 2, 1 / 2, 0),
                (1 / 2, -1 / 2, 0),
                (0, 1 / 2, -1 / 2),
                (0, -1 / 2, 1 / 2),
                (1 / 2, 0, -1 / 2),
                (-1 / 2, 0, 1 / 2),
                (1 / 2, 1 / 2, -1 / 2),
                (-1 / 2, -1 / 2, 1 / 2),
            },
        ),  # ORCI
        (
            [[2, -1, 0], [2, 1, 0], [0, 0, 0.6667]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (-1 / 2, 1 / 2, 0),
                (1 / 2, -1 / 2, 0),
            },
        ),  # ORCC
        (
            [[2, -1.155, 0], [0, 2.309, 0], [0, 0, 2]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (1 / 2, 1 / 2, 0),
                (-1 / 2, -1 / 2, 0),
            },
        ),  # HEX
        (
            [[1.221, -1.743, -0.5609], [1.221, 1.743, -0.5609], [0, 0, 2.201]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (1 / 2, 1 / 2, 0),
                (-1 / 2, -1 / 2, 0),
                (0, 1 / 2, 1 / 2),
                (0, -1 / 2, -1 / 2),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (1 / 2, 1 / 2, 1 / 2),
                (-1 / 2, -1 / 2, -1 / 2),
            },
        ),  # RHL1
        # (
        #     [[1.743, -1.221, 1.295], [1.743, 1.221, 1.295], [0, 0, 2.491]],
        #     {
        #         (1/2, 0, 0),
        #         (-1/2, 0, 0),
        #         (0, 1/2, 0),
        #         (0, -1/2, 0),
        #         (0, 0, 1/2),
        #         (0, 0, -1/2),
        #         (-1/2, 1/2, 0),
        #         (1/2, -1/2, 0),
        #         (0, 1/2, -1/2),
        #         (0, -1/2, 1/2),
        #         (1/2, 0, -1/2),
        #         (-1/2, 0, 1/2),
        #     },
        # ),  # RHL2
        (
            [[2, 0, 0], [0, 1, -0.17632698], [0, 0, 0.67695107]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (0, 1 / 2, 1 / 2),
                (0, -1 / 2, -1 / 2),
            },
        ),  # MCL
        (
            [[-2, 1.3333, -0.2351], [2, 1.3333, -0.2351], [0, 0, 1.0154]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (1 / 2, 1 / 2, 0),
                (-1 / 2, -1 / 2, 0),
                (0, 1 / 2, 1 / 2),
                (0, -1 / 2, -1 / 2),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (1 / 2, 1 / 2, 1 / 2),
                (-1 / 2, -1 / 2, -1 / 2),
            },
        ),  # MCLC1
        # (
        #     [
        #         [1.35390364, 4 / 3, -0.23510264],
        #         [-1.35390364, 4 / 3, -0.23510264],
        #         [0, 0, 1.01542661],
        #     ],
        #     {
        #         (1/2, 0, 0),
        #         (-1/2, 0, 0),
        #         (0, 1/2, 0),
        #         (0, -1/2, 0),
        #         (0, 0, 1/2),
        #         (0, 0, -1/2),
        #         (0, 1/2, 1/2),
        #         (0, -1/2, -1/2),
        #         (1/2, 0, 1/2),
        #         (-1/2, 0, -1/2),
        #         (1/2, 1/2, 1/2),
        #         (-1/2, -1/2, -1/2),
        #     },
        # ),  # MCLC2
        (
            [[2, 4, -0.70530792], [-2, 4, -0.70530792], [0, 0, 2.03085322]],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (0, 1 / 2, 1 / 2),
                (0, -1 / 2, -1 / 2),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (-1 / 2, 1 / 2, 0),
                (1 / 2, -1 / 2, 0),
            },
        ),  # MCLC3
        (
            [
                [1.87817491, 2, -0.35265396],
                [-1.87817491, 2, -0.35265396],
                [0, 0, 1.69237769],
            ],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (0, 1 / 2, 1 / 2),
                (0, -1 / 2, -1 / 2),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (-1 / 2, 1 / 2, 0),
                (1 / 2, -1 / 2, 0),
            },
        ),  # MCLC4
        (
            [
                [2, 2, -1.15470054],
                [-2, 2, -1.15470054],
                [0, 0, 2.30940108],
            ],
            {
                (1 / 2, 0, 0),
                (-1 / 2, 0, 0),
                (0, 1 / 2, 0),
                (0, -1 / 2, 0),
                (0, 0, 1 / 2),
                (0, 0, -1 / 2),
                (0, 1 / 2, 1 / 2),
                (0, -1 / 2, -1 / 2),
                (1 / 2, 0, 1 / 2),
                (-1 / 2, 0, -1 / 2),
                (-1 / 2, 1 / 2, 0),
                (1 / 2, -1 / 2, 0),
                (1 / 2, 1 / 2, 1 / 2),
                (-1 / 2, -1 / 2, -1 / 2),
            },
        ),  # MCLC5
        # (
        #     [
        #         #TODO
        #     ],
        #     {
        #         (0, 0, 1/2),
        #         (0, 0, -1/2),
        #         (0, 1/2, 0),
        #         (0, -1/2, 0),
        #         (1/2, 0, 0),
        #         (-1/2, 0, 0),
        #         (0, 1/2, 1/2),
        #         (0, -1/2, -1/2),
        #         (1/2, 0, 1/2),
        #         (-1/2, 0, -1/2),
        #         (1/2, 1/2, 1/2),
        #         (-1/2, -1/2, -1/2),
        #         (1/2, 1/2, 0),
        #         (-1/2, -1/2, 0),
        #     },
        # ),  # TRI1a
        # (
        #     [
        #         # TODO
        #     ],
        #     {
        #         (1/2, 0, 0),
        #         (-1/2, 0, 0),
        #         (0, 1/2, 0),
        #         (0, -1/2, 0),
        #         (0, 0, 1/2),
        #         (0, 0, -1/2),
        #         (0, 1/2, 1/2),
        #         (0, -1/2, -1/2),
        #         (1/2, 0, 1/2),
        #         (-1/2, 0, -1/2),
        #         (1/2, 1/2, 1/2),
        #         (-1/2, -1/2, -1/2),
        #     },
        # ),  # TRI2a
        # (
        #     [
        #         # TODO
        #     ],
        #     {
        #         (0, 0, 1/2),
        #         (0, 0, -1/2),
        #         (0, 1/2, 0),
        #         (0, -1/2, 0),
        #         (1/2, 0, 0),
        #         (-1/2, 0, 0),
        #         (0, -1/2, 1/2),
        #         (0, 1/2, -1/2),
        #         (1/2, -1/2, 0),
        #         (-1/2, 1/2, 0),
        #         (-1/2, -1/2, 1/2),
        #         (1/2, 1/2, -1/2),
        #         (-1/2, 0, 1/2),
        #         (1/2, 0, -1/2),
        #     },
        # ),  # TRI1b
        # (
        #     [
        #         # TODO
        #     ],
        #     {
        #         (0, 0, 1/2),
        #         (0, 0, -1/2),
        #         (0, 1/2, 0),
        #         (0, -1/2, 0),
        #         (1/2, 0, 0),
        #         (-1/2, 0, 0),
        #         (0, -1/2, 1/2),
        #         (0, 1/2, -1/2),
        #         (-1/2, -1/2, 1/2),
        #         (1/2, 1/2, -1/2),
        #         (-1/2, 0, 1/2),
        #         (1/2, 0, -1/2),
        #     },
        # ),  # TRI2b
    ],
    ids=[
        "CUB",
        "FCC",
        "BCC",
        "TET",
        "BCT1",
        "BCT2",
        "ORC",
        "ORCF1",
        "ORCF2",
        "ORCF3",
        "ORCI",
        "ORCC",
        "HEX",
        "RHL1",
        # "RHL2",
        "MCL",
        "MCLC1",
        # "MCLC2",
        "MCLC3",
        "MCLC4",
        "MCLC5",
        # "TRI1a",
        # "TRI1b",
        # "TRI2a",
        # "TRI2b",
    ],
)
def test_define_planes(cell, real_planes):
    lattice_points, vectors = get_lattice_points_vectors(cell)
    planes = define_planes(lattice_points, vectors)
    assert set(planes) == real_planes


# TODO
@pytest.mark.parametrize(
    "cell, number_of_corners",
    [
        (
            [[2, 0, 0], [0, 2, 0], [0, 0, 2]],
            8,
        ),  # CUB
        (
            [[1, 1, -1], [1, -1, 1], [-1, 1, 1]],
            24,
        ),  # FCC
        (
            [[1, 1, 0], [1, 0, 1], [0, 1, 1]],
            14,
        ),  # BCC
        (
            [[2, 0, 0], [0, 2, 0], [0, 0, 1]],
            8,
        ),  # TET
        (
            [[0, 1, 2], [1, 0, 2], [1, 1, 0]],
            18,
        ),  # BCT1
        (
            [[0, 2, 1], [2, 0, 1], [2, 2, 0]],
            24,
        ),  # BCT2
        (
            [[2, 0, 0], [0, 1, 0], [0, 0, 0.6667]],
            8,
        ),  # ORC
        (
            [[-2.222, 1.6, 1.2], [2.222, -1.6, 1.2], [2.222, 1.6, -1.2]],
            18,
        ),  # ORCF1
        (
            [[-1.818, 1.6, 1.2], [1.818, -1.6, 1.2], [1.818, 1.6, -1.2]],
            24,
        ),  # ORCF2
        (
            [[-2, 1.6, 1.2], [2, -1.6, 1.2], [2, 1.6, -1.2]],
            14,
        ),  # ORCF3
        (
            [[0, 1, 0.6667], [2, 0, 0.6667], [2, 1, 0]],
            24,
        ),  # ORCI
        (
            [[2, -1, 0], [2, 1, 0], [0, 0, 0.6667]],
            12,
        ),  # ORCC
        (
            [[2, -1.155, 0], [0, 2.309, 0], [0, 0, 2]],
            12,
        ),  # HEX
        # (
        #     [[1.221, -1.743, -0.5609], [1.221, 1.743, -0.5609], [0, 0, 2.201]],
        #     24,
        # ),  # RHL1
        # (
        #     [[1.743, -1.221, 1.295], [1.743, 1.221, 1.295], [0, 0, 2.491]],
        #     14,
        # ),  # RHL2
        (
            [[2, 0, 0], [0, 1, -0.17632698], [0, 0, 0.67695107]],
            12,
        ),  # MCL
        # (
        #     [[-2, 1.3333, -0.2351], [2, 1.3333, -0.2351], [0, 0, 1.0154]],
        #     24,
        # ),  # MCLC1
        # (
        #     [
        #         [1.35390364, 4 / 3, -0.23510264],
        #         [-1.35390364, 4 / 3, -0.23510264],
        #         [0, 0, 1.01542661],
        #     ],
        #     18,
        # ),  # MCLC2
        # (
        #     [[2, 4, -0.70530792], [-2, 4, -0.70530792], [0, 0, 2.03085322]],
        #     18,
        # ),  # MCLC3
        # (
        #     [
        #         [1.87817491, 2, -0.35265396],
        #         [-1.87817491, 2, -0.35265396],
        #         [0, 0, 1.69237769],
        #     ],
        #     14,
        # ),  # MCLC4
        # (
        #     [
        #         [22, 2, -1.15470054],
        #         [-2, 2, -1.15470054],
        #         [0, 0, 2.30940108],
        #     ],
        #     24,
        # ),  # MCLC5
        # (
        #     [
        #         #TODO
        #     ],
        #     {},
        # ),  # TRI1a
        # (
        #     [
        #         # TODO
        #     ],
        #     {},
        # ),  # TRI2a
        # (
        #     [
        #         # TODO
        #     ],
        #     {},
        # ),  # TRI1b
        # (
        #     [
        #         # TODO
        #     ],
        #     {},
        # ),  # TRI2b
    ],
    ids=[
        "CUB",
        "FCC",
        "BCC",
        "TET",
        "BCT1",
        "BCT2",
        "ORC",
        "ORCF1",
        "ORCF2",
        "ORCF3",
        "ORCI",
        "ORCC",
        "HEX",
        # "RHL1",
        # "RHL2",
        "MCL",
        # "MCLC1",
        # "MCLC2",
        # "MCLC3",
        # "MCLC4",
        # "MCLC5",
        # "TRI1a",
        # "TRI1b",
        # "TRI2a",
        # "TRI2b",
    ],
)
def test_define_corners(cell, number_of_corners):
    lattice_points, vectors = get_lattice_points_vectors(cell)
    planes = define_planes(lattice_points, vectors)
    corners, tmp = define_corners(planes, cell, vectors)
    from rad_tools import print_2D_array

    assert len(corners) == number_of_corners
