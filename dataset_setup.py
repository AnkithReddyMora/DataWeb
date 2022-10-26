import dataset

db = dataset.connect('sqlite:///shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Maggie' },
        { "description": 'chicken' },
        { "description": 'almond joy' },
        { "description": 'dannon'},
        { "description": 'bread' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()