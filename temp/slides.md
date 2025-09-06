# DetectNoMainFunction

## What is the main function in Python?

The main function in Python is declared, like this: `def main(some parameter):`

The `if __name__ == "__main__"` guard checks whether a Python file has a main function.

Direct run: then `__name__` is set to `"__main__"` -> block inside will be run.

Imported Python File e.g.: `import my_script` then `__name__` is set to `my_script` ->
no need for `main` function.

## How does the main function look like in other languages?

Let's see some other programming languages:

- C++:

```cpp
int main(int argc, const* argv[]) {// call of the function} // parameters can be missed
```

Does every C++ program need to have a `main` function?

- Rust:

```rust
fn main() {// function calls or logic comes here}
```

Does every Rust program need to have a `main` function?

## Detecting main function using AST

## How to detect if a Python program does not have a main function?
