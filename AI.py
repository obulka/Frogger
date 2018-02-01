
class NeuralNet():
    def __init__(self, depth, numInputs, numOutputs):
        self.depth = depth
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        
        self.age = 0
        self.neurons = []
        
        neuronLayer = []
        for i in range(depth + 1):
            for j in range(depth + numOutputs - 2*(i - depth/2) if (i > depth/2) else numOutputs + 2*i):
                neuronLayer.append(Neuron())
                
            self.neurons.append(neuronLayer)
            neuronLayer = []
            
        for layer in self.neurons:
            for neuron in layer:
                
                neuron.Connect() #connect to all in next layer
                
    def makeDecision(self):
        pass
    
    def train(self):
        pass
    
    def reproduce(self):
        pass
    
    def kill(self):
        pass
                
class Neuron():
    def __init__(self):
        self.upStream   = []
        self.downStream = []
        
        self.weightings = []
        
    def train(self):
        pass
    
    def destroyConnection(self):
        pass
    
    def propogateSignal(self):
        pass
        