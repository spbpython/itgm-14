def rev(s: str) -> str:
    ws = s.split()

    result = []

    for w in ws:
        result.insert(0, w)

    return " ".join(result)


print(rev("lose to fear you everything of go let to yourself train"))
