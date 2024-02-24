from captum.attr import LayerIntegratedGradients
import torch

class Attributions:

    def initialize(self, model):
        self.lig = LayerIntegratedGradients(self.calculate, model.bert.embeddings)

    def getAttributions(self, encoded, target):
        bsl = torch.zeros(encoded.input_ids.size()).type(torch.LongTensor)
        attributions, delta = self.lig.attribute(
                inputs = encoded["input_ids"],
                baselines = bsl,
                additional_forward_args = (
                    encoded["token_type_ids"],
                    encoded["attention_mask"]
                ),
                n_steps = 20,
                target = target,
                return_convergence_delta = True,
            )
        attributions_ig = attributions.sum(dim=-1).cpu()
        attributions_ig = attributions_ig / attributions_ig.abs().max()
        return attributions_ig
        

