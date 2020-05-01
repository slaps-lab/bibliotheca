import spacy

from spacy.tokens import Doc
from spacy.language import Language

from ..utils import contractions


class ExpandContractionsComponent(object):
  name = "expand_contractions"

  nlp: Language

  def __init__(self, nlp: Language):
    self.nlp = nlp

  def __call__(self, doc: Doc) -> Doc:
    text = contractions.expand_contractions(doc.text)
    return self.nlp.make_doc(text)
