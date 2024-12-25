import collections
import functools

with open('day05.txt') as file:
    data = file.read()

[rules, books] = data.split('\n\n')

page_order = collections.defaultdict(list)

for rule in rules.split():
    [before, after] = rule.split('|')
    page_order[before].append(after)

def in_order(pages):
    for i, page in enumerate(pages):
        afters = page_order[page]
        
        for before in pages[:i]:
            if before in afters:
                return False
          
    return True

def order(pages):
    return sorted(pages, key=functools.cmp_to_key(lambda a, b: 1 if b in page_order[a] else -1 ))

total_1, total_2 = 0, 0

for book in books.split():

    pages = book.split(',')

    if in_order(pages):
        total_1 += int(pages[len(pages) // 2])
    else:
        pages = order(pages)
        total_2 += int(pages[len(pages) // 2])
    


print(total_1, total_2)