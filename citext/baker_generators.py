"""
Extends model_bakery's generators to support citext fields.

This logic is loaded only if package model_bakery is installed.
https://github.com/model-bakers/model_bakery/
"""

try:
    from model_bakery import baker, random_gen
except ImportError:
    pass
else:
    baker.generators.add("citext.fields.CICharField", random_gen.gen_string)
    baker.generators.add("citext.fields.CIEmailField", random_gen.gen_email)
    baker.generators.add("citext.fields.CITextField", random_gen.gen_text)
