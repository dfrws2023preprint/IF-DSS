import re

match = re.match(r"(Qm[1-9A-HJ-NP-Za-km-z]{44}|baf[A-Za-z2-7]{56})", "http://bafkreibjoigvkh75ejawpl3n7lypu4x2mbeofekradwuqrop5a7bhfwk44.ipfs.dweb.link/")

if match:
    print("Match found!")
else:
    print("No match found.")
