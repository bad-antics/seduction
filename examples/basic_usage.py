from seduction.core import SeductionEngine
s=SeductionEngine()
for form in ["ritual","aesthetic","political","fatal"]:
    info=s.analyze_form(form)
    print(f"{form}: {info['principle']}")
print(f"\n{s.seduction_vs_production()['baudrillard_thesis']}")
print(f"\nInsight: {s.generate_insight()}")
