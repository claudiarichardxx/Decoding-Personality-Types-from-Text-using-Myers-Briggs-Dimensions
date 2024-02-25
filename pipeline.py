from utils.predict import Predictions
from utils.attributions import Attributions
from utils.visualize import Visualize
from colour import Color



class Pipeline:

    def pipeline(self, text):
        labs = {0: ['Introvert', 'Extrovert'], 1: ['Intuition', 'Sensing'], 2: ['Thinking', 'Feeling'], 3: ['Judging', 'Perceiving']}
        pred = Predictions()
        attribute = Attributions()
        visualize = Visualize()
        model_name = 'ClaudiaRichard/mbti-bert-nli-finetuned'
        pred.load_model(model_name)
        self.encoded, self.labels = pred.tokenizer(text, return_attention_mask=True, return_tensors="pt"), pred.predict_labels(text)
        htmls = []
        attribute.initialize(pred.model)
        tokens = pred.tokenizer.convert_ids_to_tokens(self.encoded["input_ids"][0])
        for i in range(0,4):
            attributions = attribute.getAttributions(self.encoded, i, int(self.labels[i]))
            if(checkThrehold(self, attributions, int(self.labels[i]))):

                html = visualize.attributions_to_html(tokens, attributions.numpy()[0], int(self.labels[i]))
                htmls.append('Label: '+ labs[i][int(self.labels[i])])
                label_interpret = f""" <span style="background-color: {Color('cyan').hex}">{labs[i][0]}</span> <span style="background-color: {Color('violet').hex}">{labs[i][1]}</span>"""
                htmls.append('<br>' + label_interpret+ '<br>')
                #display(HTML(label_interpret))
                html = html.replace('<s>', '')
                html = html.replace('</s>','')
                htmls.append(html+'<br><br>')
            #display(HTML(html))
            else:
                htmls.append('<br>Label: Inconclusive<br>')
        return htmls

    def checkThrehold(self, attributions, label, threshold = [-0.3, 0.6]):

        if(label == 0):
            if(any(attributions[0]<= threshold[0])):
            return True
            else:
            return False
        if(label == 1):
            if(any(attributions[0] >= threshold[1])):
            return True
            else:
            return False

    def pipelineV2(self, text):
        labs = {0: ['Introvert', 'Extrovert'], 1: ['Intuition', 'Sensing'], 2: ['Thinking', 'Feeling'], 3: ['Judging', 'Perceiving']}
        pred = Predictions()
        attribute = Attributions()
        visualize = Visualize()
        model_name = 'ClaudiaRichard/mbti-bert-nli-finetuned'
        pred.load_model(model_name)
        self.encoded, self.labels = pred.tokenizer(text, return_attention_mask=True, return_tensors="pt"), pred.predict_labels(text)
        lists = []
        attribute.initialize(pred.model)
        tokens = pred.tokenizer.convert_ids_to_tokens(self.encoded["input_ids"][0])
        for i in range(0,4):
            attributions = attribute.getAttributions(self.encoded, i)
            class_attributes = visualize.attributions_to_list(tokens, attributions.numpy()[0], int(self.labels[i]))
            print('Label: ', labs[i][int(self.labels[i])])
            print(class_attributes)
            #display(HTML(html))


