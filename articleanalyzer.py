import nltk
from nltk import bigrams
from nltk.probability import ELEProbDist, FreqDist
from nltk import NaiveBayesClassifier
from collections import defaultdict


pos_sntn = [('the company reported better than expected profit', 'positive'),
	          ('the company experienced growth', 'positive'),
	          ('the company made an acquisition', 'positive'),
	          ('the company seems to be financially sound', 'positive'),
			  ('the company is a dominant player in the market', 'positive')]
neg_sntn = [('the company filed for bankruptcy', 'negative'),
			  ('the employees went on strike', 'negative'),
			  ('the company reported weak earnings', 'negative'),
			  ('the company performed poorly', 'negative'),
			  ('the company underperformed within its sector', 'negative')]


tst_sntn = [('Bank of America reported better than expected EPS', 'positive'),
			  ('JCPenney saw a boost in holiday sales', 'positive'),
			  ('RadioShack expects to begin closing stores', 'negative'),
			  ('General Electric announced it will be laying off employees', 'negative'),
			  ('Microsoft faces corrpution probe', 'negative')]




sentinces = []

for (words, sentiment) in pos_sntn + neg_sntn + tst_sntn:
	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	sentinces.append((words_filtered, sentiment))


	
def get_words_in_sentinces(sentinces):
	all_words = []
	for (words, sentiment) in sentinces:
		all_words.extend(words)
	return all_words
def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

word_features = get_word_features(get_words_in_sentinces(sentinces))


#print word_features


def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

#print extract_features(['love','this','car'])

training_set = nltk.classify.apply_features(extract_features , sentinces)

#print training_set


classifier = nltk.NaiveBayesClassifier.train(training_set)

def train(labeled_featuresets, estimator=ELEProbDist):
	
	# Create the P(label) distribution
	label_probdist = esitmator(label_freqdist)
	
	#Create the P(fval | label, fname) distribution
	feature_probdist = {}
	
	return NaiveBayesClassifier (label_probdist, feature_probdist)

"""print feature_probdist('positive')
print feature_probdist[('negative', 'contains(best)')].prob(True)"


print classifier.show most_informative_features(32)"""

sentence = 'The SEC launched an investigation into insider trading around facebook shares'

print classifier.classify(extract_features(sentence.split()))
#print extract_features(tweet.split())



""""def classify(self, featureset):
	  # Discard any feature names that we've never seen before.
	  # Find the log probability of each label, given the features.
	  # Then add in the log probability of features given labels.
	  # Generate a probability distribution dictionary using the dict logprod
	  # Return the sample with the greatest probability from the probability
	  # distribution dictionary

	{'positive' : -1.0, 'negative': -1.0}
	{'positive': -5.4785441837188511, 'negative': -14.784261334886439}

	DictionaryProbDist(logprob, normalize=True, log=True)"""