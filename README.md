# Decoding-Personality-Types-from-Text-using-Myers-Briggs-Dimensions
The aim of this project is to classify personality types from written text and also to extract important words that contributed to the classification.

# Installation
To  clone this repository:
```
git clone https://github.com/claudiarichardxx/Decoding-Personality-Types-from-Text-using-Myers-Briggs-Dimensions.git
```

# To setup the environment:
To  install the required libraries, run this:
```
pip install -r requirements.txt
```
# Quickstart
The following script can also found in usage.ipynb. A sample run on google colab can be found in colab_run.ipynb. The main.py file has a tkinter GUI (It **cannot be executed on Codespace** but can be executed on the local system.). We suggest running the notebook file for a test run.
```
from IPython.display import display, HTML
from pipeline import Pipeline

text = '''I really enjoy being alone these days'''
pp = Pipeline()
htmls = pp.pipeline(text) 
attributions = ''.join(htmls)
display(HTML(attributions))
```
Arguments to the pp.pipeline function:
1. text: Any self descriptive text or paragraph
2. threshold: Array of 2 values [class_0_threshold, class_1_threshold]; default = [-0.3, 0.6]
   
# Architecture
The project involves building a multilabel classification model to classify input sentences into four dimensions of the Myers-Briggs Type Indicator (MBTI) personality framework. 
1. The model utilizes the BERT architecture, a transformer-based model, known for its effectiveness in capturing contextual information in text data.
2. After classifying the input sentences into the four dimensions of MBTI, the Integrated Gradients method is applied to determine the attribution of each token to each label. Integrated Gradients provides insights into the importance of each token in the prediction by calculating the contribution of each token to the classification decision. The values obtained are in the range [-1,1].
3. Furthermore, a threshold is defined, and if the attribution of all tokens for a particular class is less than this threshold, the corresponding label is discarded. This step helps in ensuring that only significant attributions contribute to the final classification decision, improving the reliability of the model's predictions. The default threshold is set as -0.3 for class 0 and 0.6 for class 1. It can be changed by setting the threshold when calling the pipeline function. 
   
# Training
The base model used for finetuning is the sentence-transformers/bert-base-nli-mean-tokens model (an adaptation of the Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks paper).
1. The 'Transformers' library from Huggingface is used for Training the model.
2. The dataset used for training has been uploaded to the Huggingface hub and can be accessed at: [ClaudiaRichard/mbti_classification_v2](https://huggingface.co/datasets/ClaudiaRichard/mbti_classification_v2).
3. The finetuned model weights can be accessed at: [ClaudiaRichard/mbti-bert-nli-finetuned_v2](https://huggingface.co/)
4. The model traning was done on Google Colab and the script used for training can be found in setup/modelTraining.ipynb
5. Training arguments: 
6. The script used to split and upload the data can be found in setup/datasetCreation.ipynb

# Training Arguments

1. batch size : 8
2. base model : [bert-base-nli-mean-tokens](https://huggingface.co/sentence-transformers/bert-base-nli-mean-tokens)
3. learning rate : 3e-5
4. epochs : 2
5. weight decay : 0.01
6. gradient accumulation steps : 2
7. metric to choose best model = F1 Score
   
