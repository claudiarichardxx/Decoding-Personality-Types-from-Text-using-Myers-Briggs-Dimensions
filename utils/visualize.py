from colour import Color

class Visualize:


    def attributions_to_html(self, tokens, attributions):
        html = ""
        COLOR_RANGE = list(Color("cyan").range_to(Color("white"), 10)) + list(
        Color("white").range_to(Color("violet"), 10))
        for token, attribution in zip(tokens, attributions):
            if attribution >= 0:

                idx = int(attribution ** 1 * 10) + 10
            else:

                idx = int((-(-attribution) ** 1 + 1) * 10)

            idx = min(idx, 19)

            color = COLOR_RANGE[idx]
            html += f""" <span style="background-color: {color.hex}">{token}</span>"""

        return html
    
    def attributions_to_list(self, tokens, attributions, label):
        attributing_words = []
        COLOR_RANGE = list(Color("cyan").range_to(Color("white"), 10)) + list(
        Color("white").range_to(Color("violet"), 10))
        att_dict = {tokens[i]: attributions[i] for i in range(0, len(tokens)) }
        sorted_atttributions = dict(sorted(att_dict.items(), key=lambda item: item[1]))
        if(label == 0):
            return list(sorted_atttributions.keys())[-5:]
        return list(sorted_atttributions.keys())[:5]