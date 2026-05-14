# special variable

echo "File Name: $0"

# $1, $2, $3, indicating arguments 

echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Argument 3: $3"

# $# No of Argument 

echo "No of Arguments: $#"

# print all
echo "All: $@"

# process ID which is used to execute a script 
echo "Process Id: $$"

#$? see status code: 0-success 1-score error
echo "Exit status: $?"

# try to run: ./special-var.sh sonam abc 123456








