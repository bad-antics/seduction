"""Seduction Engine"""
import json,random

class SeductionEngine:
    FORMS={
        "ritual":{"description":"Ceremonial seduction governed by rules and games",
                  "principle":"The rule is more powerful than the law",
                  "example":"Courtship rituals, gift exchange, ceremony"},
        "aesthetic":{"description":"Seduction through appearances and surfaces",
                     "principle":"Appearance is more profound than depth",
                     "example":"Fashion, art, architecture, design"},
        "political":{"description":"Seduction as strategy of power",
                     "principle":"Seduction is the mastery of the symbolic universe",
                     "example":"Charisma, rhetoric, media manipulation"},
        "fatal":{"description":"Objects seduce subjects — reversal of power",
                 "principle":"Objects have their own strategy of seduction",
                 "example":"Consumer objects, technology, algorithms"},
    }
    
    def analyze_form(self,form):
        return self.FORMS.get(form,{})
    
    def seduction_vs_production(self):
        return {"seduction":{"mode":"Symbolic","domain":"Appearance","logic":"Game/Challenge",
                            "value":"Reversibility","power":"Attraction"},
                "production":{"mode":"Economic","domain":"Reality","logic":"Accumulation",
                             "value":"Use/Exchange","power":"Force"},
                "baudrillard_thesis":"Seduction is stronger than production because it operates on the level of signs and appearances"}
    
    def generate_insight(self):
        insights=[
            "Seduction is stronger than power, because power itself can be seduced.",
            "The secret of seduction is that it never reveals its secret.",
            "In seduction, everything is ritual, nothing is natural.",
            "Appearance is not the opposite of depth — it is the only depth.",
            "The game of seduction has no end, no goal, only rules.",
        ]
        return random.choice(insights)
