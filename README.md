# Hate Speech Detection in Social Media Posts

A Multimodal AI based system to classify content as hateful or safe for social media. In this project we use an ensemble of 1-D and 2-D convolutional neural networks to classify images and text and also work on memes, which is a combination of text embedded in an image. An OCR engine extracts the text from the image which is then fed to a text classifier. The image itself is fed to an image classifier. Both of these are CNNs. A cumulative mean of the results is taken and the final output probability is used for classification.
