# tests/test_analyzer.py
from medi_nlp.analyzer import analyze_content

def test_analyze_content():
    content = "This article discusses the illness of bacteremia and other health issues."
    illness_count, bacteremia_count = analyze_content(content)
    assert illness_count == 1, "Illness count incorrect."
    assert bacteremia_count == 1, "Bacteremia count incorrect."
