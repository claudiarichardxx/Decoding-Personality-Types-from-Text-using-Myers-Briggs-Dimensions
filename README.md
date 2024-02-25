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
A notebook file to demonstrate the usage can be found in usage/sample.ipynb

# Architecture
The project involves building a multilabel classification model to classify input sentences into four dimensions of the Myers-Briggs Type Indicator (MBTI) personality framework. 
1. The model utilizes the BERT architecture, a transformer-based model, known for its effectiveness in capturing contextual information in text data.
2. After classifying the input sentences into the four dimensions of MBTI, the Integrated Gradients method is applied to determine the attribution of each token to each label. Integrated Gradients provides insights into the importance of each token in the prediction by calculating the contribution of each token to the classification decision.
3. Furthermore, a threshold is defined, and if the attribution of all tokens for a particular class is less than this threshold, the corresponding label is discarded. This step helps in ensuring that only significant attributions contribute to the final classification decision, improving the reliability of the model's predictions.
   
# Training
The base model used for finetuning is the sentence-transformers/bert-base-nli-mean-tokens model (an adaptation of the Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks paper).
1. The 'Transformers' library from Huggingface is used for Training the model.
2. The dataset used for training has been uploaded to the Huggingface hub and can be accessed at: ClaudiaRichard/mbti_classification_v2.
3. The finetuned model weights can be accessed at: ClaudiaRichard/mbti-bert-nli-finetuned_v2
4. The script used for training can be found in setup/train.py
