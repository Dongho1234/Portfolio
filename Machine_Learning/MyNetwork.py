from NetworkModel import NetworkModel
def regularNet():
    mynet = NetworkModel()
    mynet.addInputLayer()
    mynet.addFullyConnectedLayer(50)
    mynet.addFullyConnectedLayer(50)
    mynet.addOutputLayer()

    return mynet

def convNet():
    mynet = NetworkModel()
    mynet.addInputLayer()
    mynet.addConvLayer(10,7)
    mynet.addMaxPoolLayer(5)
    mynet.addConvLayer(20,5)
    mynet.addMaxPoolLayer(5)
    mynet.addFullyConnectedLayer(15)
    mynet.addOutputLayer()

    return mynet

def own_conv1Net():
    mynet = NetworkModel()
    mynet.addInputLayer()
    mynet.addConvLayer(80, 10)
    mynet.addMaxPoolLayer(2)
    mynet.addConvLayer(100, 10)
    mynet.addMaxPoolLayer(8)
    mynet.addConvLayer(200, 5)
    mynet.addMaxPoolLayer(2)
    mynet.addConvLayer(300, 20)
    mynet.addMaxPoolLayer(2)
    mynet.addFullyConnectedLayer(256)
    mynet.addOutputLayer()

    return mynet

def own_conv2Net():
    mynet = NetworkModel()
    mynet.addInputLayer()
    mynet.addConvLayer(80, 10)
    mynet.addMaxPoolLayer(2)
    mynet.addConvLayer(100, 10)
    mynet.addMaxPoolLayer(8)
    mynet.addConvLayer(200, 5)
    mynet.addMaxPoolLayer(2)
    mynet.addConvLayer(300, 5)
    mynet.addMaxPoolLayer(2)
    mynet.addConvLayer(400, 5)
    mynet.addMaxPoolLayer(2)
    mynet.addFullyConnectedLayer(256)
    mynet.addOutputLayer()

    return mynet