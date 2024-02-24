from utils.predict import Predictions
from utils.attributions import Attributions
from utils.visualize import Visualize
from IPython.core.display import display, HTML
from colour import Color

class Pipeline:
    
    def pipeline(self, text):
        labs = {0: ['Introvert', 'Extrovert'], 1: ['Intuition', 'Sensing'], 2: ['Thinking', 'Feeling'], 3: ['Judging', 'Perceiving']}
        pred = Predictions()
        attribute = Attributions()
        visualize = Visualize()
        pred.load_model()
        self.encoded, self.labels = pred.tokenizer(text, return_attention_mask=True, return_tensors="pt"), pred.predict_labels(text)
        #htmls = []
        for i in range(0,4):
            attributions = attribute.getAttributions(self.encoded, i)
            html = visualize.attributions_to_html(self.tokens, attributions.numpy()[0])
        print('Label: ', labs[i][int(self.labels[i])])
        label_interpret = f""" <span style="background-color: {Color('cyan').hex}">{labs[i][0]}</span> <span style="background-color: {Color('violet').hex}">{labs[i][1]}</span>"""
        display(HTML(label_interpret))
        html = html.replace('<s>', '')
        html = html.replace('</s>','')
        display(HTML(html))


