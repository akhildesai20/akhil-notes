# Typeface submission: Akhil Notes

**Status:** Draft for designer review. Not submitted. Do not open a google/fonts PR without approval.

Akhil Notes is an open-source handwriting typeface based on my actual handwriting, developed from personal notebook pages and carefully translated into digital vector letterforms.

The project originated from my interest in the relationship between handwriting, thinking and learning. I wanted to retain the familiarity and personal character of handwritten notes while making them accessible in everyday digital environments.

One of the defining characteristics of the typeface is its paragraph texture. Although individual letterforms retain natural irregularities, they come together to create a cohesive handwritten rhythm. These characteristics have been intentionally preserved throughout the development process.

Beyond expressive and decorative applications, the family is designed to support practical everyday writing, educational materials, annotations, mathematical explanations, journaling and structured information.

## Family specifications

- Designer: Akhil Desai  
- Classification: Handwriting  
- License: SIL Open Font License 1.1  
- 698 encoded Unicode characters  
- 846 glyphs  
- Variable weight range: 400–900  
- Upright and italic variable fonts  
- 12 static styles  
- GF Latin Core, Latin Plus and Vietnamese coverage  
- Extended mathematical, currency and utility symbols  
- OpenType kerning, ligatures, combining-mark positioning, localized forms, fractions and tabular numerals  
- Editable UFO masters and designspace sources  
- Public, reproducible font compilation pipeline  
- Automated quality assurance through GitHub Actions  

The project has undergone font engineering, character expansion, shaping validation, interpolation testing and paragraph proofing. Development has prioritized technical correctness while retaining the authentic characteristics of the original handwriting.

Source repository: https://github.com/akhildesai20/akhil-notes  

Akhil Notes began as a deeply personal project. By making it freely available, I hope it can become a useful resource for people who want to bring a more human, approachable and expressive quality to their digital work.

## Engineering notes for reviewers

- Public build: `python scripts/build_candidate.py --from-ufo` (no private provenance required).  
- Fontspector googlefonts profile on the packaged VF pair: **FAIL 0**; remaining WARNs are documented in `FONTSPECTOR-EXCEPTIONS.md` (intentional handwriting characteristics vs accepted technical limitations; vendor ID registration requested, confirmation pending).  
- Package path: `ofl/akhilnotes/`.  
