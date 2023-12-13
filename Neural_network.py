import numpy as np
inputs=[1.2,5.1,2.1]
weights=[3.1,2.1,8.7]
bias=3

output=inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+bias
print(output)

inputs=[1,2,3,2.5]
weights1=[0.2,0.8,-0.5,1.0]
weights2=[0.5,-0.91,0.26,-0.5]
weights3=[-0.26,-0.27,0.17,0.87]

bias1=2
bias2=3
bias3=0.5

output1=[inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2]+inputs[3]*weights1[3]+bias1,
inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2]+inputs[3]*weights2[3]+bias2,
inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2]+inputs[3]*weights3[3]+bias3]
print(output1)

inputs=[1,2,3,2.5]
weights=[[0.2,0.8,-0.5,1.0],
	[0.5,-0.91,0.26,-0.5],
	[-0.26,-0.27,0.17,0.87]]
biases=[2,3,0.5]

layer_outputs=[]
for neuron_weights,neuron_bias in zip(weights,biases):
	neuron_output =0
	for n_input,weight in zip(inputs,neuron_weights):
		neuron_output += n_input*weight
	neuron_output += neuron_bias
	layer_outputs.append(neuron_output)
print(layer_outputs)

inputs=[1,2,3,2.5]
weights=[[0.2,0.8,-0.5,1.0],
	[0.5,-0.91,0.26,-0.5],
	[-0.26,-0.27,0.17,0.87]]
biases=[2,3,0.5]

output3=np.dot(weights,inputs)+biases
#output3=np.dot(inputs,np.array(weights).T)
print(output3)

inputs=[1,2,3,2.5]
weights=[[0.2,0.8,-0.5,1.0],
	[0.5,-0.91,0.26,-0.5],
	[-0.26,-0.27,0.17,0.87]]
biases=[2,3,0.5]
weights2=[[0.1,-0.14,0.5],
	[-0.5,0.12,-0.33],
	[-0.44,0.73,-0.13]]
biases2=[-1,2,-0.5]
layer1_outputs=np.dot(inputs,np.array(weights).T)+biases
layer2_outputs=np.dot(layer1_outputs,np.array(weights2).T)+biases
print(layer2_outputs)

x=[[1,2,3,2.5],
   [2.0,5.0,-1.0,2.0],
   [-1.5,2.7,3.3,-0.8]]

class Layer_Dense:
	def __init__(self,n_inputs,n_neurons):
		self.weights=np.random.randn(n_inputs,n_neurons)
		self.biases=np.zeros((1,n_neurons))
	def forword(self,inputs):
		self.output=np.dot(inputs,self.weights)+self.biases
layer1=Layer_Dense(4,5)
layer2=Layer_Dense(5,2)
layer1.forword(x)
print(layer1.output)
layer2.forword(layer1.output)
print(layer2.output)

		
