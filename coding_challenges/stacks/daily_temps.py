def daily_temps(temperatures):
    output = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            output[stackInd] = i - stackInd
        stack.append([t, i])
    return output

print(daily_temps([73,74,75,71,69,72,76,73]))