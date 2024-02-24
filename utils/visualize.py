from colour import Color

class Visualize:


    def attributions_to_html(tokens, attributions):
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