import sys
import argparse
import pickle


def load_model(model_filename: str):
    model = pickle.load(open(model_filename, 'rb'))

    return model


def init_model_by_seed(model):
    pass


def generate_sequence():
    pass


def print_sequence(seq: str):
    print(seq)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    parser.add_argument('--prefix', nargs='?')
    parser.add_argument('--length')
    args = parser.parse_args(sys.argv[1:])

    model_filename = args.model
    length = args.length
    if args.prefix:
        pass
    else:
        pass
