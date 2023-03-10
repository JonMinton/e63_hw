

class Matrix:
    def __init__(self, matrix_string):
        matrix_lines = matrix_string.split("\n")
        matrix_lines_split = [x.split(" ") for x in matrix_lines]

        nrow = len(matrix_lines)
        ncol = len(matrix_lines_split[0]) # No checking for ragged arrays


        outer_list = []
        for i in range(nrow):
            inner_list = []
            for j in range(ncol):
                this_num = int(matrix_lines_split[i][j])
                inner_list.append(this_num)
            outer_list.append(inner_list)

        self.mat = outer_list

        

    def row(self, index):
        return self.mat[index]

    def column(self, index):
        return [x[index] for x in self.mat]
