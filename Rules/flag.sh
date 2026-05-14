#!/bin/bash

set -e # exit on error

echo "starting script"
rm /tmp/non-exist-file # this command is fail


#!/bin/bash

set -u # undefined variable = error 


echo "file-deleted"
echo "user is $USERNAME"


#!/bin/bash
set -o pipefail # pipeline fails if any command fails 

grep "ERROR" app.log | wc -l
echo "Done" 

#!/bin/bash
# using together 

set -euo pipefail






