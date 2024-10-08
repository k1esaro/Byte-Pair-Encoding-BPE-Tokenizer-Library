import re
from collections import defaultdict, Counter

class BPETokenizer:
    def __init__(self, num_merges=10, vocab_size=30000):
        self.num_merges = num_merges
        self.vocab_size = vocab_size
        self.token_to_id = {}
        self.id_to_token = {}

    # Функция для нахождения всех пар символов в слове
    def get_pairs(self, word):
        pairs = set()
        prev_char = word[0]
        for char in word[1:]:
            pairs.add((prev_char, char))
            prev_char = char
        return pairs

    # Основная функция BPE
    def bpe(self, corpus):
        vocab = {" ".join(word) + ' </w>': freq for word, freq in corpus.items()}

        for i in range(self.num_merges):
            pairs = defaultdict(int)

            # Подсчет пар символов
            for word, freq in vocab.items():
                symbols = word.split()
                word_pairs = self.get_pairs(symbols)
                for pair in word_pairs:
                    pairs[pair] += freq

            if not pairs:
                break

            best_pair = max(pairs, key=pairs.get)
            pattern = re.compile(r'(?<!\S)' + re.escape(' '.join(best_pair)) + r'(?!\S)')

            # Замена пар символов на новый токен
            vocab = {pattern.sub(''.join(best_pair), word): freq for word, freq in vocab.items()}

        return vocab

    # Основная функция токенизации текста
    def tokenize(self, text):
        words = text.split()
        corpus = Counter(words)
        vocab = self.bpe(corpus)

        tokens = list(vocab.keys())

        # Создаем маппинг токенов и индексов
        self.token_to_id = {token: idx for idx, token in enumerate(tokens[:self.vocab_size])}
        self.id_to_token = {idx: token for token, idx in self.token_to_id.items()}

        # Преобразование текста в последовательности индексов
        token_ids = [self.token_to_id.get(token, self.token_to_id.get('<unk>')) for token in tokens]

        return token_ids

    # Функция обратной конвертации индексов в токены
    def decode(self, token_ids):
        return [self.id_to_token.get(idx, '<unk>') for idx in token_ids]
