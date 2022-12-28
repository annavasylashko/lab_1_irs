import lib.tools as tools

def forward_index(text, doc, current_index):
    tokens = tools.tokenize(text)
    current_index[doc] = tokens
    return current_index

def forward_search(query, index):
    tokens = tools.tokenize(query)
    result = {}
    for token in tokens:
        result[token] = []
        for doc in index:
            if token in index[doc]:
                result[token].append(doc)
    return result

def inverted_index(text, doc, current_index):
    tokens = tools.tokenize(text)
    for token in tokens:
        if token not in current_index:
            current_index[token] = []
        if doc not in current_index[token]:
            current_index[token].append(doc)

def inverted_search(query, index):
    tokens = tools.tokenize(query)
    result = {}
    for token in tokens:
        if token in index:
            result[token] = index[token]
    return result