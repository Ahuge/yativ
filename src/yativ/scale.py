import numpy


def scale(input, float_factor):
    def downsize(factor):
        new_arr = []
        for row_index_mult, _ in enumerate(input[::factor]):
            new_arr.append([])
            for col_index_mult, _ in enumerate(input[0][::factor]):
                values = []
                for row_factor_index in range(int(factor)):
                    ri = (row_index_mult*factor)+row_factor_index
                    if ri < len(input):
                        row = input[ri]
                        for col_factor_index in range(int(factor)):
                            ci = (col_index_mult*factor)+col_factor_index
                            if ci < len(row):
                                cell = row[ci]
                                values.append(cell)
                if values:
                    new_arr[-1].append(sum(values)/len(values))
        return numpy.asarray(new_arr)

    def upscale(factor):
        raise NotImplementedError("Upscaling is not yet implemented!")

    if float_factor == 1:
        return input
    elif float_factor > 1:
        # print("Scaling %s to %s" % (input.shape[0], input.shape[0]/factor))
        return downsize(int(float_factor))
    else:
        return upscale(float_factor)
