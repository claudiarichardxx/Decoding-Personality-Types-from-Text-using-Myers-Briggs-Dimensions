from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch
import numpy as np



class Predictions:

    def load_model(self, model_name):
        try:
            self.model = AutoModelForSequenceClassification.from_pretrained("model/bert/")
            self.tokenizer = AutoTokenizer.from_pretrained("model/tokenizer/")
        except:
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model.save_pretrained("model/bert/")
            self.tokenizer.save_pretrained("model/tokenizer/")
        #self.model = settings.model
        #self.tokenizer = settings.tokenizer
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