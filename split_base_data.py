from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('/home/nikita/PycharmProjects/natural_language/data/yelp_review.csv')
data = data[['stars', 'text', 'useful', 'funny', 'funny']]
train, test = train_test_split(data, test_size=0.2)
train.to_csv('train.csv', index_label=None)
test.to_csv('test.csv', index_label=None)

print('End!')
