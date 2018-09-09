from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
# numpy.random.seed(7)

# load pima indians dataset
dataset = numpy.loadtxt("Datasets/noMoreHeadaches_dummy.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:40]
Y = dataset[:,41:44]

# create model
model = Sequential()
model.add(Dense(12, input_dim=40, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(2, activation='sigmoid'))

model.summary()

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, Y, epochs=20, batch_size=10)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
