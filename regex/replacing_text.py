# replacing text using re.sub

import re

# example string
text = "I love apples. apples are my favourite fruits."

# using re.sub to replace "apples" with "orange"
sub_result = re.sub(r"apples", "orange", text, flags=re.IGNORECASE)

print(sub_result)








