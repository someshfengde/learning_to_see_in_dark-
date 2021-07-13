# Introduction
Converting night time images to day time images.

We've deployed the app on streamlit which is trained on learning to see in dark paper with resnet 34 as architecture.

     Currently this project is under development will take quite more time to get it to bring us good results 
dark image input |  enhanced image by our model 
:------------:|:------------:
<img src = 'https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/input1.png'/>  |<img src = 'https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/output1.png' /> 
<img src = 'https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/input2.png'/>   | <img src = 'https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/output2.png'/>
# code : 
code for replicating this experiment can be found in [`notebook`](https://github.com/someshfengde/learning_to_see_in_dark/tree/main/notebook) folder 

# dataset used : 
[Sony camera raw dataset](https://storage.googleapis.com/isl-datasets/SID/Sony.zip)
this dataset is converted to `jpg` images and then trained with the backbone of `resnet34` architecture 

# original paper link 
## [arXiv:1805.01934](https://arxiv.org/abs/1805.01934) `[cs.CV]`

