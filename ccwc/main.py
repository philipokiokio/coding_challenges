from io import TextIOWrapper
import typer
import os
import sys


def byte_size(file_name: str) -> int:
    return os.path.getsize(f"./{file_name}")


def line_count(file_name: str):
    with open(file=f"./{file_name}", mode="r") as file:
        count = 0
        for count, _ in enumerate(file):
            pass
        count += 1
        return count


def word_counter(file: TextIOWrapper):
    word_count = 0
    for line in file:
        word_sum_count = 0
        for word in line.split():
            word_sum_count += len(word)

        word_count += word_sum_count
    return word_count


def character_counter(file: TextIOWrapper):
    character_count = 0
    check = True

    while check:
        char = file.read(1)
        if not char:
            check = False

        character_count += len(char)
    return character_count


def main(
    file_name: str, c: bool = False, l: bool = False, w: bool = False, m: bool = False
):
    # Check if the input content is a valid file path
    with open(file=f"./{file_name}", mode="r") as file:
        word_count = word_counter(file=file)
        character_count = character_counter(file=file)
        file_byte = byte_size(file_name=file_name)
        count = line_count(file_name=file_name)

    if c:
        print(f"{file_byte} {file_name}")

    elif l:
        print(f"{count} {file_name}")

    elif w:
        print(f"{word_count} {file_name}")
    elif m:
        print(f"{character_count} {file_name}")
    else:
        print(f"{file_byte} {count} {word_count} {file_name}")
    ...


if __name__ == "__main__":
    typer.run(main)
