def generate_binary(n, prefix=""):
    if len(prefix) == n:
        print(prefix)
        return
    
    generate_binary(n, prefix + "0")

    generate_binary(n, prefix + "1")

generate_binary(2)