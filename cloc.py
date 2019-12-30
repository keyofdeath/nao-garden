# coding: utf-8

import fnmatch
import os

"""
Calcule le nombre de lignes de code du projet en excluant les commentaires / lignes vides.
"""

matches = []
for root, dirnames, filenames in os.walk('./'):
    for filename in fnmatch.filter(filenames, '*.py'):
        if filename != "cloc.py":
            matches.append(os.path.join(root, filename))

lines = []
characters = 0
for f in matches:
    f = open(f)
    in_comment = False
    for l in f:
        l = l.strip(" ")
        i = l.rfind('#')
        if '"""' in l:
            in_comment = not in_comment
        if not in_comment and not l.startswith('"""') and not l.startswith('#') and not l == "\n":
            if i != -1:
                l = l[:i]
            lines += [l]
            characters += len(l)

print ''.join(lines)
print "======================="
print len(lines), "lignes de code."
print characters, u"caractères"
print "soit", float(characters)/len(lines), "caractères par fichier en moyenne"
