import json
import pandas as pd
import sqlite3
conn = sqlite3.connect('hackernews.sqlite3')
curs = conn.cursor()
query = '''SELECT author, count(author), sentiment
FROM comments
GROUP BY author
HAVING count(author) >= 50
ORDER BY sentiment
LIMIT 10'''
curs.execute(query)
results = curs.fetchall()
df = pd.DataFrame(results, columns=["author", "post count", "sentiment"])
d = df.to_dict()
with open('topsalties.json', 'w') as file:
    json.dump(d, file)
