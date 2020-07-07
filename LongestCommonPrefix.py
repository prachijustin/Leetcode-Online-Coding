def longestCommonPrefix(strs):
    if not strs:
        return ''

    shortestStr = min(strs, key=len)

    for i, char in enumerate(shortestStr):
        for rem in strs:
            if rem[i] != char:
                return shortestStr[:i]

    return shortestStr


print(longestCommonPrefix(["flower", "flow", "flight"]))
