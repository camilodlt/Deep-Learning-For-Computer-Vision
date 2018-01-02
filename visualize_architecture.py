from pyimagesearch.nn.conv.lenet import LeNet
from keras.utils import plot_model

# initialize LeNet and then write the network arch visualization
# graph to disk.
model = LeNet.build(28, 28, 1, 10)
plot_model(model, to_file="lenet.png", show_shapes=True)