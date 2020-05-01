import spacy

from spacy.tokens import Doc
from spacy.language import Language

from typing import Callable

class CustomComponent(object):
  name = "custom_component"

  nlp: Language
  cleaning_method: Callable[[str], str]

  def __init__(self, nlp: Language, cleaning_method: Callable[[str], str]):
    self.nlp = nlp
    self.cleaning_method = cleaning_method

  def __call__(self, doc: Doc) -> Doc:
    text: str = self.cleaning_method(doc.text)
    return self.nlp.make_doc(text)
