**Prompt:**
#!/bin/bash \n\n ####### These functions provide 

**Response:**
a set of commonly used math operations ####### 

# Function to add two numbers
add() {
  local num1=$1
  local num2=$2
  local sum=$((num1 + num2))
  echo "The sum of $num1 and $num2 is $sum"
}

# Function to subtract two numbers
subtract() {
  local num1=$1
  local num2=$2
  local difference=$((num1 - num2))
  echo "The difference between $num1 and $num2 is $difference"
}

# Function to multiply two numbers
multiply() {
  local num1=$1
  local num2=$2
  local product=$((num1 * num2))
  echo "The product of $num1 and $num2 is $product"
}

# Function to divide two numbers
divide() {
  local num1=$1
  local num2=$2
  if (( num2 == 0 )); then
    echo "Error: Cannot divide by zero"
  else
    local quotient=$((num1 / num2))
    echo "The result of dividing $num1 by $num2 is $quotient"
  fi
}

# Function to calculate the square root of a number
square_root() {
  local num=$1
  if (( num < 0 )); then
    echo "Error: Cannot find square root of a negative number"
  else
    local root=$(bc <<< "scale=2; sqrt($num)")
    echo "The square root of $num is $root"
  fi
}

# Function to calculate the power of a number
power() {
  local base=$1
  local exponent=$2
  local result=$(bc <<< "scale=2; $base ^ $exponent")
  echo "$base raised to the power of $exponent is $result"
}

# Function to calculate the factorial of a number
factorial() {
  local num=$1
  if (( num < 0 )); then
    echo "Error: Cannot find factorial of a negative number"
  else
    local result=1
    for (( i=1; i<=num; i++ )); do
      result=$((result * i))
    done
    echo "The factorial of $num is $result"
  fi
}

# Usage example

add 5 10

<details><summary>Metadata</summary>

- Duration: 15702 ms
- Datetime: 2023-09-16T09:44:37.229654
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

