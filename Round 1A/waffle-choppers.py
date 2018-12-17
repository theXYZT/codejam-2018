# Codejam 2018, Round 1A: Waffle Choppers

from itertools import accumulate

class Waffle():
    """Class for Waffle."""
    def __init__(self, waffle, rows, columns):
        self.waffle = waffle
        self.rows = rows
        self.columns = columns
        self.total = sum([sum(i) for i in waffle])
        self.csumrows = list(accumulate([sum(r) for r in self.waffle]))
        self.csumcols = list(accumulate([sum(c) for c in zip(*self.waffle)]))

    def make_horizontal_cuts(self, horizontal_cuts):
        """Try cutting horizontally to have equal chips per row."""
        chips_in_row = self.total // (horizontal_cuts + 1)
        increments = [chips_in_row * i for i in range(1, horizontal_cuts + 1)]
        try:
            cut_index = [self.csumrows.index(i) + 1 for i in increments]
            self.hcut_index = [0, *cut_index, self.rows]
            return True
        except ValueError:
            return False

    def make_vertical_cuts(self, vertical_cuts):
        """Try cutting vertically to have equal chips per column."""
        chips_in_col = self.total // (vertical_cuts + 1)
        increments = [chips_in_col * i for i in range(1, vertical_cuts + 1)]
        try:
            cut_index = [self.csumcols.index(i) + 1 for i in increments]
            self.vcut_index = [0, *cut_index, self.columns]
            return True
        except ValueError:
            return False

    def check_cuts(self, num_diners):
        """Check the cuts made actually work."""
        chips_per_diner = self.total // num_diners
        for h_start, h_end in zip(self.hcut_index[:-1],
                                  self.hcut_index[1:]):
            for v_start, v_end in zip(self.vcut_index[:-1],
                                      self.vcut_index[1:]):
                chips_in_piece = sum([sum(row[v_start:v_end]) for row
                                      in self.waffle[h_start:h_end]])
                if chips_in_piece != chips_per_diner:
                    return False
        return True


def process_case(waffle, horizontal_cuts, vertical_cuts):
    """Checks to see if waffles can be cut as required."""
    num_diners = (horizontal_cuts + 1) * (vertical_cuts + 1)
    
    if waffle.total % num_diners != 0:
        return False
    
    if not waffle.make_horizontal_cuts(horizontal_cuts):
        return False
    
    if not waffle.make_vertical_cuts(vertical_cuts):
        return False
    
    if not waffle.check_cuts(num_diners):
        return False
    
    return True

# I/O Code
num_cases = int(input())
for case_number in range(1, num_cases + 1):
    R, C, H, V = [int(i) for i in input().split(" ")]

    waffle_list = []
    for _ in range(R):
        waffle_list.append([int(i == '@') for i in input().strip()])

    waffle = Waffle(waffle_list, R, C)
    result = process_case(waffle, H, V)
    if result:
        print("Case #{}: POSSIBLE".format(case_number))
    else:
        print("Case #{}: IMPOSSIBLE".format(case_number))
