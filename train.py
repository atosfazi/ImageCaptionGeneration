

from helpers.captions_handler import CaptionsHandler

# load data - image captions
# image feature extraction
# vectorizer of text
# data generaotr
# model
# spliting ds and training
# validation

def main():
    path = r'dataset/results.csv'
    captions_handler = CaptionsHandler(data_path=path)
    captions_handler.load_captions()
    print(captions_handler.captions['1000092795'])


if __name__ == '__main__':
    main()