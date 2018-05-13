### Code for Binary Classifier Convolutional Neural Network 

#### Extra Info

1. The majority of the code was adapted from [this tutorial](https://www.pyimagesearch.com/2018/04/30/a-fun-hands-on-deep-learning-project-for-beginners-students-and-hobbyists/)
2. The VGGNet network implementation was introduced in 2014 in the paper [Very Deep Convolutional Networks for Large Scale Image Recognition](https://arxiv.org/abs/1409.1556)
3. A [very simple tutorial](https://becominghuman.ai/building-an-image-classifier-using-deep-learning-in-python-totally-from-a-beginners-perspective-be8dbaf22dd8) for a Binary Classifier Convolutional Neural Network
   was also helpful to put this together.
4. I also found [this video](https://youtu.be/FmpDIaiMIeA) to be incredibly helpful in understanding Convolutional Neural Networks.

#### Steps for running:
1. Have your two classification groups in a directory with the folder
   structure: ( example )
   ```
   dataset/cats
   dataset/dogs
   ```
2. Start the classifier:
   ```
    python train.py --dataset dataset --model output.model 
   ```
3. Once your model is built, classify a new image
   ```
   python classify.py --model output.model --image /path/to/image.jpg
   ```

