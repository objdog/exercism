def slices(series, length):
    result = []
    if len(series) == 0 or length > len(series) or length <= 0:
        raise ValueError("Not a valid slice request.")
    for index, element in enumerate(series):
        result.append(series[index:index+length])
    result = [item for item in result if len(item) == length]
    return result