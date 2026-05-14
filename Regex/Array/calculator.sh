add() {
    local num1=$1
    local num2=$2
    local sum=$((num1+num2))
    echo "The sum of $num1 and $num2 is $sum "
}


sub() {
    local num1=$1
    local num2=$2
    local diff=$((num1 - num2))
    echo "The diff of $num1 and $num2 is $diff"
}

Multiplication(){
    local num1=$1
    local num2=$2
    local multiply=$((num1 * num2))
    echo "The multiplication of $num1 and $num2 is $multiply"
}

Division(){
    local num1=$1
    local num2=$2
    local divide=$((num1 / num2))
    echo "The division of $num1 and $num2 is $divide"
}

echo "Global Num1 check: $num1" # can not access local variable outside function 

# call function
add 5 3 
sub 5 3
Multiplication 5 3
Division 5 3 


