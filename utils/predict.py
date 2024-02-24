from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch
import numpy as np

class Predictions:
    
    def calculate(self, input_ids, token_type_ids, attention_mask):
    # convert back to list of text
        return self.model(input_ids, token_type_ids, attention_mask)[0]

    def load_model(self, model_name):

        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        #return  model, tokenizer

    def predict_labels(self, text):

        encoding = self.tokenizer(text, return_attention_mask=True, return_tensors="pt")

        # Move the encoding to the device used by the model
        encoding = {k: v.to(self.model.device) for k, v in encoding.items()}

        # Get the outputs from the model
        outputs = self.model(**encoding)

        # Assuming outputs is a tuple containing logits for each class
        logits = outputs.logits  # Shape: (batch_size, num_labels)

        # Calculate probabilities for each class
        sigmoid = torch.nn.Sigmoid()
        probs = sigmoid(logits.squeeze().cpu())

        predictions = np.zeros(probs.shape)

        predictions[np.where(probs >= 0.6)] = 1

        return tuple(predictions)