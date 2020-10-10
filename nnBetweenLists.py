from typing import List, Tuple

fred = ['Banana', 'Coffee', 'Coffee', 'Energy Drink'] 
ralph = ['Cup Cakes', 'Cigarettes', 'Wine', 'Lighter'] 
jeff = ['Coffee', 'Fountain Drink', 'Gum', 'Lighter', 'Propane'] 
jake = ['Candy Bar', 'Energy Drink'] 
brian = ['Coffee', 'Toy Robot']

#aggregate all names in a dictionary, and give each name a dictionary to store item names and item weights
baskets = {
    'fred': {'items': ['Banana', 'Coffee', 'Coffee', 'Energy Drink']}, 
    'ralph': {'items': ['Cup Cakes', 'Cigarettes', 'Wine', 'Lighter']},
    'jeff': {'items': ['Coffee', 'Fountain Drink', 'Gum', 'Lighter', 'Propane']},
    'jake': {'items': ['Candy Bar', 'Energy Drink']},
    'brian': {'items': ['Coffee', 'Toy Robot']}
    }
#add a key-value pair in each name's dictionary for all the person's items; key is item name and corresponding value is item "weight", or the percentage of the basket that is composed by that item
for i in baskets:
    for j in baskets[i]['items']:
        baskets[i][j] = baskets[i]['items'].count(j) / len(baskets[i]['items'])
        
#Function calculates nearest neighbors for a given person
def list_of_NNs(name: str) -> List[Tuple[str, float]]:
    distances = []
    #iterate through all 'neighbors'
    for i in baskets:
        if i is not name:
            similarity = 0
            #iterate through all items in argument name's basket and see if the current neighbor basket has the same item. If there is a match, add the smaller weight to the similarity between the two baskets.
            for item in set(baskets[name]['items']):
                if item in baskets[i]:
                    similarity += min(baskets[name][item], baskets[i][item])
            distances.append((i, similarity))
    #sort neighbors in descending order
    distances.sort(key=lambda i: i[1], reverse=True)
    return distances

print(list_of_NNs('fred')) #Outputs [('brian', 0.5), ('jake', 0.25), ('jeff', 0.2), ('ralph', 0)]
