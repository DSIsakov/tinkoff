import sys
import argparse
import re
import pickle


def read_data(filename: str):
    file = open(filename)
    data = file.read()
    file.close()

    return data


def clean_date(data: str):
    data.lower()
    text = re.sub("[^а-яa-z]", "", data)

    return text


def tokenise(text: str):
    words = text.split()

    return words


def save_model(model, model_filename: str):
    pickle.dump(model, open(model_filename, 'wb'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', nargs='?')
    parser.add_argument('--model')
    args = parser.parse_args(sys.argv[1:])
    model_filename = args.model
    if args.input_dir:
        doc_collection = args.input_dir
    else:
        doc_collection = input()

    data = tokenise(clean_date(read_data(doc_collection)))
    save_model()