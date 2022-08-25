import re
import streamlit as st

from transformers import pipeline


qa = pipeline('question-answering',
              model="/pebble_tmp/tmp/model_bert")


def highlight_text(sentence, terms):
    keyword_spans = []
    for term in terms:
        found_offsets = [
            m.start() for m in re.finditer(re.escape(term.lower()), sentence.lower(), re.IGNORECASE)
        ]
        if found_offsets:
            for start in found_offsets:
                keyword_spans.append([start, start + len(term)])
    spans = sorted(keyword_spans, key=lambda x: x[0])
    if spans:
        spans_highlighted = []
        previous_end = 0
        for idx, sp in enumerate(spans):
            spans_highlighted.append(([previous_end, sp[0]], False))
            spans_highlighted.append((sp, True))
            if idx == len(sp) - 1:
                spans_highlighted.append(([sp[1], len(sp)], False))
            previous_end = sp[1]
    else:
        spans_highlighted = [((0,len(sentence)), False)]
    highlighted_text = ""
    for sp in spans_highlighted:
        text = sentence[sp[0][0]:sp[0][1]]
        if sp[1]:
            text = f"<b>{text}</b>"
        highlighted_text += text
    return highlighted_text


def compute(query, context):
    question_list = [{"question": query, "context": context}]
    result = qa(question_list)

    terms = [result["answer"]]
    res = highlight_text(context, terms)

    return [result, res]

  
st.write("Ask BERT a Question!")

context = st.text_input('Context Paragraph', 'A potato is a starchy vegetable.')
query = st.text_input('Question', 'What is a potato?')

st.text(compute(query, context))
