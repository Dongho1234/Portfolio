def count(prediction,label):
    TP, TN, FP, FN = 0, 0, 0, 0
    for (_, pred), l in zip(prediction, label):
        if pred >= 0.5 and l == 1:
            TP += 1
        elif pred >= 0.5 and l != 1:
            FP += 1
        elif pred < 0.5 and l != 1:
            TN += 1
        elif pred < 0.5 and l == 1:
            FN += 1
    return [TP, TN, FP, FN]

def recall(prediction,label):
    result = count(prediction,label)
    return result[0]/(result[0]+result[2])    #TP / (TP + FN)

def precision(prediction,label):
    result = count(prediction, label)
    return result[0] / (result[0] + result[3]) #TP / (TP + FP)

def f1score(prediction,label):
    return 2 * recall(prediction,label) * precision(prediction,label) / (recall(prediction,label) + precision(prediction,label))

