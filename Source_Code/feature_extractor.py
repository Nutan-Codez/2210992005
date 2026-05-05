import ast

def extract_features(code):
    lines = code.split("\n")

    indentation = sum(len(line) - len(line.lstrip()) for line in lines)
    comments = sum(1 for line in lines if "#" in line)
    avg_length = sum(len(line) for line in lines) / len(lines) if lines else 0
    whitespace = code.count(" ")

    try:
        tree = ast.parse(code)
        ast_nodes = len(list(ast.walk(tree)))
    except:
        ast_nodes = 0

    return [indentation, comments, avg_length, whitespace, ast_nodes]