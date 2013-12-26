__author__ = 'terrence_brannon'


import k0de.upgraded.list_to_tree as L

l = L.ListToTree(range(8))
l.build()
l.tree.show()