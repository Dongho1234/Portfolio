import MyInputReader
from NetworkModel import NetworkModel
import MyNetwork
import MyMetrics
import MyFastaPredictor

# network1 = MyNetwork.regularNet()
# network1.printDetails()
# network2 = MyNetwork.convNet()
# network2.printDetails()
# network3 = MyNetwork.own_conv1Net()
# network3.printDetails()
network = MyNetwork.own_conv2Net()
network.printDetails()

trainX ,trainY = MyInputReader.InputReader('/home/group_b13/train.pos','/home/group_b13/train.neg')
validX, validY = MyInputReader.InputReader('/home/group_b13/valid.pos','/home/group_b13/valid.neg')

network.train(trainX, trainY, validX, validY, 30)


testX, testY = MyInputReader.InputReader('/home/group_b13/test.pos','/home/group_b13/test.neg')
predictions = network.generatePredictions(testX)
print('TP:', MyMetrics.count(predictions, testY)[0])
print('FP:', MyMetrics.count(predictions, testY)[2])
print('FN:', MyMetrics.count(predictions, testY)[3])
print('TN:', MyMetrics.count(predictions, testY)[1])
print('Recall = ', MyMetrics.recall(predictions, testY))
print('Precision = ', MyMetrics.precision(predictions, testY))
print('F1 score = ', MyMetrics.f1score(predictions, testY))


MyFastaPredictor.readFasta('/home/group_b13/full_sample.fasta','savedModel')