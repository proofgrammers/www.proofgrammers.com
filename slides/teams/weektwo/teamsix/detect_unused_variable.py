import ast

def read_file():
    with open("uv.py", "r") as fn:
        read_fn = fn.read()
    parser = ast.parse(read_fn)
    create_ast = ast.dump(parser, indent=4)
    return create_ast

def store_ast():
    ast_tree = read_file()

    with open("ast.txt", "w") as fn:
        write_fn = fn.write(ast_tree)
    
    return write_fn

def read_ast():
    with open("ast.txt", "r") as fn:
        lines = fn.readlines()

    for line in lines:
        split_lines = line.strip()
        word = "'limit'"

        if word in split_lines:
            count_word = word.count("'limit'")
        
            if count_word == 1:
                print(f"We found an unused variable: {word}")
            else:
                print("The file you have provided does not have unused variables!")



if __name__ == "__main__":
    read_ast()

