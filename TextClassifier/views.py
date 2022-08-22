from rest_framework.views import APIView
from rest_framework.response import Response
import pickle
from .utils import utils

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk

nltk.download('punkt')


class Classifier(APIView):

    def get(self, request):
        labels = {}
        text = request.data.get("text")
        if text:
            set(stopwords.words('english'))
            output = []
            x = utils.clean_text(text)
            word_tokens = word_tokenize(x)

            clf = utils.classifier()
            vec = utils.vector()

            xt = vec.transform(word_tokens)
            pred = clf.predict(xt)

            multilabel = utils.binarizer()
            out_ = multilabel.inverse_transform(pred)

            for j in out_:
                if not j:
                    pass
                elif j:
                    for k in j:
                        if k in output:
                            pass
                        else:
                            output.append(k)
            labels['Labels'] = output
            return Response({"message": labels})
        else:
            return Response({"message": "TEXT NOT FOUND"})
