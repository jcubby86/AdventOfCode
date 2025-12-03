def read_lines(fileName: str) -> list:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []

def read_comma_separated(fileName: str) -> list:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.read().split(",")]
    return []

def parse_args(args: list):
    verbose = False
    filename = None
    for arg in args[1:]:
        if arg in ["-v", "--verbose"]:
            verbose = True
        else:
            filename = arg
    return verbose, filename