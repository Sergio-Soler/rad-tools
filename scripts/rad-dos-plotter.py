#! /usr/local/bin/python3

from rad_tools.score.rad_dos_plotter_core import get_parser, manager

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    manager(**vars(args))
