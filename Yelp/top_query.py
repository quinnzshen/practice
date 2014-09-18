# Let's make a "Top 10 Most Frequent Searches" widget for Yelp's homepage!

# Widget:
# Top 10 Most Frequent Searches
# 1. sushi
# 2. doctor
# 3. hamburger

# n - # of queries in search log
# m - # of unique queries in search log
# k - top count
import operator

def find_top_k(searches, k):
    queries = dict()
    for search in searches:
        if search not in queries:
            queries[search] = 1
        else:
            queries[search] += 1
    top_queries = sorted(queries.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in top_queries[:k]]

# This will run the above function with some sample input for testing.
sample_searches = [
  'sushi',
  'hamburger',
  'doctor',
  'sushi',
  'sushi',
  'doctor',
]
for top_search in find_top_k(sample_searches, 10):
    print(top_search)
