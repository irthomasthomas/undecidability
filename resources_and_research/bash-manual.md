Terminal Tricks

Ctrl + a : move to the beginning of line.
Ctrl + d : if you've type something, Ctrl + d deletes the character under the cursor, else, it escapes the current shell.
Ctrl + e : move to the end of line.
Ctrl + k : delete all text from the cursor to the end of line.
Ctrl + l : equivalent to clear.
Ctrl + n : same as Down arrow.
Ctrl + p : same as Up arrow.
Ctrl + q : to resume output to terminal after Ctrl + s.
Ctrl + r : begins a backward search through command history.(keep pressing Ctrl + r to move backward)
Ctrl + s : to stop output to terminal.
Ctrl + t : transpose the character before the cursor with the one under the cursor, press Esc + t to transposes the two words before the cursor.
Ctrl + u : cut the line before the cursor; then Ctrl + y paste it
Ctrl + w : cut the word before the cursor; then Ctrl + y paste it
Ctrl + x + backspace : delete all text from the beginning of line to the cursor.
Ctrl + x + Ctrl + e : launch editor defined by $EDITOR to input your command. Useful for multi-line commands.
Ctrl + z : stop current running process and keep it in background. You can use `fg` to continue the process in the foreground, or `bg` to continue the process in the background.
Ctrl + _ : undo typing.

Esc + u
# converts text from cursor to the end of the word to uppercase.
Esc + l
# converts text from cursor to the end of the word to lowercase.
Esc + c
# converts letter under the cursor to uppercase, rest of the word to lowercase.

Run history number (e.g. 53)

!53

Run last command

!!
# run the previous command using sudo
sudo !!

Run last command and change some parameter using caret substitution (e.g. last command: echo 'aaa' -> rerun as: echo 'bbb')

#last command: echo 'aaa'
^aaa^bbb

#echo 'bbb'
#bbb

#Notice that only the first aaa will be replaced, if you want to replace all 'aaa', use ':&' to repeat it:
^aaa^bbb^:&

Run past command that began with (e.g. cat filename)

!cat
# or
!c
# run cat filename again

# '*' serves as a "wild card" for filename expansion.
/etc/pa*wd    #/etc/passwd

# '?' serves as a single-character "wild card" for filename expansion.
/b?n/?at      #/bin/cat

# '[]' serves to match the character from a range.
ls -l [a-z]*   #list all files with alphabet in its filename.

# '{}' can be used to match filenames with more than one patterns
ls *.{sh,py}   #list all .sh and .py files

handy environment variables

$0   :name of shell or shell script.
$1, $2, $3, ... :positional parameters.
$#   :number of positional parameters.
$?   :most recent foreground pipeline exit status.
$-   :current options set for the shell.
$$   :pid of the current shell (not subshell).
$!   :is the PID of the most recent background command.
$_   :last argument of the previously executed command, or the path of the bash script.

$DESKTOP_SESSION     current display manager
$EDITOR   preferred text editor.
$LANG   current language.
$PATH   list of directories to search for executable files (i.e. ready-to-run programs)
$PWD    current directory
$SHELL  current shell
$USER   current username
$HOSTNAME   current hostname

# foo=bar
echo $foo
# bar
echo "$foo"
# bar
# single quotes cause variables to not be expanded
echo '$foo'
# $foo
# single quotes within double quotes will not cancel expansion and will be part of the output
echo "'$foo'"
# 'bar'
# doubled single quotes act as if there are no quotes at all
echo ''$foo''
# bar

var="some string"
echo ${#var}
# 11

var=string

var=string
echo "${var:0:1}"
#s

# or
echo ${var%%"${var#?}"}

var="some string"
echo ${var:2}
#me string

Replacement (e.g. remove the first leading 0 )

var="0050"
echo ${var[@]#0}
#050
Replacement (e.g. replace 'a' with ',')

{var/a/,}
Replace all (e.g. replace all 'a' with ',')

{var//a/,}

To change the case of the string stored in the variable to lowercase (Parameter Expansion)

var=HelloWorld
echo ${var,,}
helloworld
Expand and then execute variable/argument

cmd="bar=foo"
eval "$cmd"
echo "$bar" # foo

Math

Arithmetic Expansion in Bash (Operators: +, -, *, /, %, etc)

echo $(( 10 + 5 ))  #15
x=1
echo $(( x++ )) #1 , notice that it is still 1, since it's post-increment
echo $(( x++ )) #2
echo $(( ++x )) #4 , notice that it is not 3 since it's pre-increment
echo $(( x-- )) #4
echo $(( x-- )) #3
echo $(( --x )) #1
x=2
y=3
echo $(( x ** y )) #8

factor 50
# 50: 2 5 5

seq 10|paste -sd+
# 1+2+3+4+5+6+7+8+9+10

seq 10|paste -sd+|bc
# 55

Usage: paste [OPTION]... [FILE]...
Write lines consisting of the sequentially corresponding lines from
each FILE, separated by TABs, to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -d, --delimiters=LIST   reuse characters from LIST instead of TABs
  -s, --serial            paste one file at a time instead of in parallel
  -z, --zero-terminated    line delimiter is NUL, not newline

Sum up a file (each line in file contains only one number)

seq 10 > /tmp/seq
awk '{s+=$1} END {print s}' /tmp/seq
# 55

paste <() <(seq 10) <(seq 10)> /tmp/two_columns.txt 
        1       1
        2       2
        3       3
        4       4
        5       5
        6       6
        7       7
        8       8
        9       9
        10      10
awk -F '\t' 'BEGIN {SUM=0}{SUM+=$3-$2}END{print SUM}' /tmp/two_columns.txt
# 0

It calculates the sum of the differences between the third and second columns for each row and prints the total sum.

**Explanation:**
- `-F '\t'`: Sets the field separator to a tab character.
- `BEGIN {SUM=0}`: Initializes the variable `SUM` to 0 before processing any lines.
- `{SUM+=$3-$2}`: For each line, it adds the difference between the third column (`$3`) and the second column (`$2`) to `SUM`.
- `END {print SUM}`: After processing all lines, it prints the total sum.

# Number of decimal digit/ significant figure
echo "scale=2;2/3" | bc
#.66

# Exponent operator
echo "10^2" | bc
#100

# Using variables
echo "var=5;--var"| bc
#4

grep = grep -G # Basic Regular Expression (BRE)
fgrep = grep -F # fixed text, ignoring meta-characters
egrep = grep -E # Extended Regular Expression (ERE)
rgrep = grep -r # recursive
grep -P # Perl Compatible Regular Expressions (PCRE)

grep -c "^$"

grep -o '[0-9]*'
#or
grep -oP '\d*'

Grep and return only integer

grep -o '[0-9]*'
#or
grep -oP '\d*'
Grep integer with certain number of digits (e.g. 3)

grep '[0-9]\{3\}'
# or
grep -E '[0-9]{3}'
# or
grep -P '\d{3}'
Grep only IP address

grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
# or
grep -Po '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
Grep whole word (e.g. 'target')

grep -w 'target'

#or using RE
grep '\btarget\b'
Grep returning lines before and after match (e.g. 'bbo')

# return also 3 lines after match
grep -A 3 'bbo'

# return also 3 lines before match
grep -B 3 'bbo'

# return also 3 lines before and after match
grep -C 3 'bbo'
Grep string starting with (e.g. 'S')

grep -o 'S.*'
Extract text between words (e.g. w1,w2)

grep -o -P '(?<=w1).*(?=w2)'
Grep lines without word (e.g. 'bbo')

grep -v bbo filename
Grep lines not begin with string (e.g. #)

grep -v '^#' file.txt
Grep variables with space within it (e.g. myvar="some strings")

grep "$myvar" filename
#remember to quote the variable!
Grep only one/first match (e.g. 'bbo')

grep -m 1 bbo filename
Grep and return number of matching line(e.g. 'bbo')

grep -c bbo filename
Count occurrence (e.g. three times a line count three times)

grep -o bbo filename |wc -l
Case insensitive grep (e.g. 'bbo'/'BBO'/'Bbo')

grep -i "bbo" filename
COLOR the match (e.g. 'bbo')!

grep --color bbo filename
Grep search all files in a directory(e.g. 'bbo')

grep -R bbo /path/to/directory
# or
grep -r bbo /path/to/directory
Search all files in directory, do not ouput the filenames (e.g. 'bbo')

grep -rh bbo /path/to/directory
Search all files in directory, output ONLY the filenames with matches(e.g. 'bbo')

grep -rl bbo /path/to/directory
Grep OR (e.g. A or B or C or D)

grep 'A\|B\|C\|D'
Grep AND (e.g. A and B)

grep 'A.*B'
Regex any single character (e.g. ACB or AEB)

grep 'A.B'
Regex with or without a certain character (e.g. color or colour)

grep 'colou\?r'
Grep all content of a fileA from fileB

grep -f fileA fileB
Grep a tab

grep $'\t'
Grep variable from variable

$echo "$long_str"|grep -q "$short_str"
if [ $? -eq 0 ]; then echo 'found'; fi
#grep -q will output 0 if match found
#remember to add space between []!
Grep strings between a bracket()

grep -oP '\(\K[^\)]+'
Grep number of characters with known strings in between(e.g. AAEL000001-RA)

grep -o -w "\w\{10\}\-R\w\{1\}"
# \w word character [0-9a-zA-Z_] \W not word character
Skip directory (e.g. 'bbo')

grep -d skip 'bbo' /path/to/files/*

Sed

Sed

[back to top]

Remove the 1st line

sed 1d filename
Remove the first 100 lines (remove line 1-100)

sed 1,100d filename
Remove lines with string (e.g. 'bbo')

sed "/bbo/d" filename
# case insensitive:
sed "/bbo/Id" filename
Remove lines whose nth character not equal to a value (e.g. 5th character not equal to 2)

sed -E '/^.{5}[^2]/d'
#aaaa2aaa (you can stay)
#aaaa1aaa (delete!)
Edit infile (edit and save to file), (e.g. deleting the lines with 'bbo' and save to file)

sed -i "/bbo/d" filename
When using variable (e.g. $i), use double quotes " "

# e.g. add >$i to the first line (to make a bioinformatics FASTA file)
sed "1i >$i"
# notice the double quotes! in other examples, you can use a single quote, but here, no way!
# '1i' means insert to first line
Using environment variable and end-of-line pattern at the same time.

# Use backslash for end-of-line $ pattern, and double quotes for expressing the variable
sed -e "\$s/\$/\n+--$3-----+/"
Delete/remove empty lines

sed '/^\s*$/d'

# or

sed '/^$/d'
Delete/remove last line

sed '$d'
Delete/remove last character from end of file

sed -i '$ s/.$//' filename
Add string to beginning of file (e.g. "[")

sed -i '1s/^/[/' file
Add string at certain line number (e.g. add 'something' to line 1 and line 3)

sed -e '1isomething' -e '3isomething'
Add string to end of file (e.g. "]")

sed '$s/$/]/' filename
Add newline to the end

sed '$a\'
Add string to beginning of every line (e.g. 'bbo')

sed -e 's/^/bbo/' filename
Add string to end of each line (e.g. "}")

sed -e 's/$/\}\]/' filename
Add \n every nth character (e.g. every 4th character)

sed 's/.\{4\}/&\n/g'
Add a line after the line that matches the pattern (e.g. add a new line with "world" after the line with "hello")

sed '/hello*/a world' filename
# hello
# world
Concatenate/combine/join files with a separator and next line (e.g separate by ",")

sed -s '$a,' *.json > all.json
Substitution (e.g. replace A by B)

sed 's/A/B/g' filename
Substitution with wildcard (e.g. replace a line start with aaa= by aaa=/my/new/path)

sed "s/aaa=.*/aaa=\/my\/new\/path/g"
Select lines start with string (e.g. 'bbo')

sed -n '/^@S/p'
Delete lines with string (e.g. 'bbo')

sed '/bbo/d' filename
Print/get/trim a range of line (e.g. line 500-5000)

sed -n 500,5000p filename
Print every nth lines

sed -n '0~3p' filename

# catch 0: start; 3: step
Print every odd # lines

sed -n '1~2p'
Print every third line including the first line

sed -n '1p;0~3p'
Remove leading whitespace and tabs

sed -e 's/^[ \t]*//'
# Notice a whitespace before '\t'!!
Remove only leading whitespace

sed 's/ *//'

# notice a whitespace before '*'!!
Remove ending commas

sed 's/,$//g'
Add a column to the end

sed "s/$/\t$i/" # $i is the valuable you want to add

# To add the filename to every last column of the file
for i in $(ls); do sed -i "s/$/\t$i/" $i; done
Add extension of filename to last column

for i in T000086_1.02.n T000086_1.02.p; do sed "s/$/\t${i/*./}/" $i; done >T000086_1.02.np
Remove newline\ nextline

sed ':a;N;$!ba;s/\n//g'
Print a particular line (e.g. 123th line)

sed -n -e '123p'
Print a number of lines (e.g. line 10th to line 33 rd)

sed -n '10,33p' <filename
Change delimiter

sed 's=/=\\/=g'
Replace with wildcard (e.g A-1-e or A-2-e or A-3-e....)

sed 's/A-.*-e//g' filename
Remove last character of file

sed '$ s/.$//'
Insert character at specified position of file (e.g. AAAAAA --> AAA#AAA)

sed -r -e 's/^.{3}/&#/' file

Awk

[back to top]

Set tab as field separator

awk -F $'\t'
Output as tab separated (also as field separator)

awk -v OFS='\t'
Pass variable

a=bbo;b=obb;
awk -v a="$a" -v b="$b" "$1==a && $10=b" filename
Print line number and number of characters on each line

awk '{print NR,length($0);}' filename
Find number of columns

awk '{print NF}'
Reverse column order

awk '{print $2, $1}'
Check if there is a comma in a column (e.g. column $1)

awk '$1~/,/ {print}'
Split and do for loop

awk '{split($2, a,",");for (i in a) print $1"\t"a[i]}' filename
Print all lines before nth occurrence of a string (e.g stop print lines when 'bbo' appears 7 times)

awk -v N=7 '{print}/bbo/&& --N<=0 {exit}'
Print filename and last line of all files in directory

ls|xargs -n1 -I file awk '{s=$0};END{print FILENAME,s}' file
Add string to the beginning of a column (e.g add "chr" to column $3)

awk 'BEGIN{OFS="\t"}$3="chr"$3'
Remove lines with string (e.g. 'bbo')

awk '!/bbo/' file
Remove last column

awk 'NF{NF-=1};1' file
Usage and meaning of NR and FNR

# For example there are two files:
# fileA:
# a
# b
# c
# fileB:
# d
# e
awk 'print FILENAME, NR,FNR,$0}' fileA fileB
# fileA    1    1    a
# fileA    2    2    b
# fileA    3    3    c
# fileB    4    1    d
# fileB    5    2    e
AND gate

# For example there are two files:
# fileA:
# 1    0
# 2    1 
# 3    1
# 4    0
# fileB: 
# 1    0
# 2    1
# 3    0
# 4    1

awk -v OFS='\t' 'NR=FNR{a[$1]=$2;next} NF {print $1,((a[$1]=$2)? $2:"0")}' fileA fileB
# 1    0
# 2    1
# 3    0  
# 4    0
Round all numbers of file (e.g. 2 significant figure)  

awk '{while (match($0, /[0-9]+\[0-9]+/)){
    \printf "%s%.2f", substr($0,0,RSTART-1),substr($0,RSTART,RLENGTH)    
    \$0=substr($0, RSTART+RLENGTH)
    \}
    \print
    \}'
Give number/index to every row

awk '{printf("%s\t%s\n",NR,$0)}'  
Break combine column data into rows

# For example, separate the following content:
# David    cat,dog
# into
# David    cat
# David    dog

awk '{split($2,a,",");for(i in a)print $1"\t"a[i]}' file  

# Detail here:　http://stackoverflow.com/questions/33408762/bash-turning-single-comma-separated-column-into-multi-line-string
Average a file (each line in file contains only one number)

awk '{s+=$1}END{print s/NR}' 
Print field start with string (e.g Linux)

awk '$1 ~ /^Linux/'
Sort a row (e.g. 1 40 35 12 23 --> 1 12 23 35 40)  

awk ' {split( $0, a, "\t" ); asort( a ); for( i = 1; i <= length(a); i++ ) printf( "%s\t", a[i] ); printf( "\n" ); }'
Subtract previous row values (add column6 which equal to column4 minus last column5)

awk '{$6 = $4 - prev5; prev5 = $5; print;}'    

Xargs

[back to top]  

Set tab as delimiter (default:space)

xargs -d\t
Prompt commands before running commands

ls|xargs -L1 -p head
Display 3 items per line   

echo 1 2 3 4 5 6| xargs -n 3
# 1 2 3
# 4 5 6
Prompt before execution

echo a b c |xargs -p -n 3
Print command along with output

xargs -t abcd
# bin/echo abcd 
# abcd
With find and rm

find . -name "*.html"|xargs rm

Show limits on command-line length

xargs --show-limits

Move files to folder

find . -name "*.bak" -print 0|xargs -0 -I {} mv {} ~/old

# or
find . -name "*.bak" -print 0|xargs -0 -I file mv file ~/old

Parallel

time echo {1..5} |xargs -n 1 -P 5 sleep

# a lot faster than:
time echo {1..5} |xargs -n1 sleep

Add the file name to the first line of file

ls |sed 's/.txt//g'|xargs -n1 -I file sed -i -e '1 i\>file\' file.txt  

Turn output into a single line

ls -l| xargs

Count lines in all file, also count total lines

ls|xargs wc -l

cat grep_list |xargs -I{} grep {} filename
Pipes `grep_list` contents to `xargs`, using each line to `grep` in `filename`.

**Serious error:**
- `cat` is unnecessary. Use `xargs -I{} grep {} filename < grep_list` instead.

List all sub directory/file in the current directory

find .
List all files under the current directory 

find . -type f
List all directories under the current directory

find . -type d  ^[[6~
Edit all files under current directory (e.g. replace 'www' with 'w')

find . -name '*.php' -exec sed -i 's/www/w/g' {} \;

# if there are no subdirectory
replace "www" "w" -- *
# a space before *
Find and output only filename (e.g. "mso") 

find mso*/ -name M* -printf "%f\n"
Find large files in the system (e.g. >4G)

find / -type f -size +4G
Find and delete file with size less than (e.g. 74 byte)

find . -name "*.mso" -size -74c -delete  

# M for MB, etc  
Find empty (0 byte) files

find . -type f -empty
# to further delete all the empty files  
find . -type f -empty -delete
Recursively count all the files in a directory

find . -type f | wc -l

# if and else loop for string matching
if [[ "$c" == "read" ]]; then outputdir="seq"; else outputdir="write" ; fi

# Test if myfile contains the string 'test':
if grep -q hello myfile; then echo -e "file contains the string!" ; fi

# Test if mydir is a directory, change to it and do other stuff:
if cd mydir; then
  echo 'some content' >myfile
else  
  echo >&2 "Fatal error. This script requires mydir."
fi

# if variable is null
if [ ! -s "myvariable" ]; then echo -e "variable is null!" ; fi
#True of the length if "STRING" is zero.

# Using test command (same as []), to test if the length of variable is nonzero  
test -n "$myvariable" && echo myvariable is "$myvariable" || echo myvariable is not set

# Test if file exist
if [ -e 'filename' ]
then  
  echo -e "file exists!"
fi

# Test if file exist but also including symbolic links:
if [ -e myfile ] || [ -L myfile ] 
then
  echo -e "file exists!"
fi

# Test if the value of x is greater or equal than 5
if [ "$x" -ge 5 ]; then echo -e "greater or equal than 5!" ; fi

# Test if the value of x is greater or equal than 5, in bash/ksh/zsh:
if ((x >= 5)); then echo -e "greater or equal than 5!" ; fi

# Use (( )) for arithmetic operation
if ((j==u+2)); then echo -e "j==u+2!!" ; fi

# Use [[ ]] for comparison
if [[ $age -gt 21 ]]; then echo -e "forever 21!!" ; fi

# Echo the file name under the current directory
for i in $(ls); do echo file $i; done
#or
for i in *; do echo file $i; done  

# Make directories listed in a file (e.g. myfile)
for dir in $(<myfile); do mkdir $dir; done

# Press any key to continue each loop
for i in $(cat tpc_stats_0925.log |grep failed|grep -o '\query\w\{1,2\}'); do cat ${i}.log; read -rsp $'Press any key to continue...\n' -n1 key; done

# Print a file line by line when a key is pressed,
oifs="$IFS"; IFS=$'\n'; for line in $(cat myfile); do ...; done
while read -r line; do ...; done <myfile

#If only one word a line, simply
for line in $(cat myfile); do echo $line; read -n1; done  

#Loop through an array   
for i in "${arrayName[@]}"; do echo $i; done


# Column subtraction of a file (e.g. a 3 columns file)
while read a b c; do echo $(($c-$b)); done < <(head filename)
#there is a space between the two '<'s

# Sum up column subtraction
i=0; while read a b c; do ((i+=$c-$b)); echo $i; done < <(head filename)

# Keep checking a running process (e.g. perl) and start another new process (e.g. python) immediately after it. (BETTER use the wait command! Ctrl+F 'wait')
while [[ $(pidof perl) ]]; do echo f; sleep 10; done && python timetorunpython.py

switch (case in bash)

read type;
case $type in
  '0')
    echo 'how'
    ;;  
  '1')
    echo 'are'
    ;;
  '2') 
    echo 'you'
    ;;  
esac

Find out the time require for executing a command

time echo hi
Wait for some time (e.g 10s)

sleep 10
Print date with formatting

date +%F
# 2020-07-19

# or  
date +'%d-%b-%Y-%H:%M:%S'
# 10-Apr-2020-21:54:40

# Returns the current time with nanoseconds.
date +"%T.%N"
# 11:42:18.664217000   

# Get the seconds since epoch (Jan 1 1970) for a given date (e.g Mar 16 2021)
date -d "Mar 16 2021" +%s
# 1615852800
# or
date -d "Tue Mar 16 00:00:00 UTC 2021"  +%s
# 1615852800   

# Convert the number of seconds since epoch back to date
date --date @1615852800
# Tue Mar 16 00:00:00 UTC 2021
Print current time point for N days ago or N days after

# print current date first (for the following example)
date +"%F %H:%M:%S" 
# 2023-03-11 16:17:09

# print the time that is 1 day ago
date -d"1 day ago" +"%F %H:%M:%S"
# 2023-03-10 16:17:09

# print the time that is 7 days ago
date -d"7 days ago" +"%F %H:%M:%S"
# 2023-03-04 16:17:09

# print the time that is a week ago  
date -d"1 week ago" +"%F %H:%M:%S"
# 2023-03-04 16:17:09

# add 1 day to date
date -d"-1 day ago" +"%F %H:%M:%S"
# 2023-03-12 16:17:09
wait for random duration (e.g. sleep 1-5 second, like adding a jitter)

sleep $[ ( $RANDOM % 5 ) + 1 ]
Log out your account after a certain period of time (e.g 10 seconds)

TMOUT=10
#once you set this variable, logout timer start running!
Set how long you want to run a command

#This will run the command 'sleep 10' for only 1 second.
timeout 1 sleep 10
Set when you want to run a command (e.g 1 min from now)  

at now + 1min  #time-units can be minutes, hours, days, or weeks
warning: commands will be executed using /bin/sh
at> echo hihigithub >~/itworks 
at> < EOT >   # press Ctrl + D to exit
job 1 at Wed Apr 18 11:16:00 2018

Download the content of this README.md (the one your are viewing now)

curl https://raw.githubusercontent.com/onceupon/Bash-Oneliner/master/README.md | pandoc -f markdown -t man | man -l -

# or w3m (a text based web browser and pager)
curl https://raw.githubusercontent.com/onceupon/Bash-Oneliner/master/README.md | pandoc | w3m -T text/html


Download all from a page

wget -r -l1 -H -t1 -nd -N -np -A mp3 -e robots=off http://example.com

# -r: recursive and download all links on page
# -l1: only one level link
# -H: span host, visit other hosts
# -t1: numbers of retries
# -nd: don't make new directories, download to here
# -N: turn on timestamp
# -nd: no parent
# -A: type (separate by ,)
# -e robots=off: ignore the robots.txt file which stop wget from crashing the site, sorry example.com

Upload a file to web and download (https://transfer.sh/)

#  Upload a file (e.g. filename.txt):
curl --upload-file ./filename.txt https://transfer.sh/filename.txt
# the above command will return a URL, e.g. https://transfer.sh/tG8rM/filename.txt

# Next you can download it by:
curl https://transfer.sh/tG8rM/filename.txt -o filename.txt

Download file if necessary

data=file.txt
url=http://www.example.com/$data
if [ ! -s $data ];then
    echo "downloading test data..."
    wget $url
fi

Wget to a filename (when a long name)

wget -O filename "http://example.com"
Wget files to a folder

wget -P /path/to/directory "http://example.com"
Instruct curl to follow any redirect until it reaches the final destination:

curl -L google.com

Random pick 100 lines from a file

Random order (lucky draw)

for i in a b c d e; do echo $i; done | shuf

Echo series of random numbers between a range (e.g. shuffle numbers from 0-100, then pick 15 of them randomly)

shuf -i 0-100 -n 15

Random from 0-9

echo $((RANDOM % 10))
Random from 1-10

echo $(((RANDOM %10)+1))

Xwindow

[back to top]

X11 GUI applications! Here are some GUI tools for you if you get bored by the text-only environment.

Enable X11 forwarding,in order to use graphical application on servers

ssh -X user_name@ip_address

file:///home/ShellLM/screenshot.png

Generate public key from private key

ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub

Copy your default public key to remote user

ssh-copy-id <user_name>@<server_IP>
# then you need to enter the password 
# and next time you won't need to enter password when ssh to that user

SSH Agent Forwarding

# To bring your key with you when ssh to serverA, then ssh to serverB from serverA using the key.
ssh-agent
ssh-add /path/to/mykey.pem
ssh -A <username>@<IP_of_serverA>
# Next you can ssh to serverB
ssh <username>@<IP_of_serverB>

Set the default user and key for a host when using SSH

# add the following to ~/.ssh/config
Host myserver
  User myuser
  IdentityFile ~/path/to/mykey.pem

# Next, you could run "ssh myserver" instead of "ssh -i ~/path/to/mykey.pem myuser@myserver"


Follow the most recent logs from service

journalctl -u <service_name> -f

Eliminate the zombie

# A zombie is already dead, so you cannot kill it. You can eliminate the zombie by killing its parent.
# First, find PID of the zombie
ps aux| grep 'Z'
# Next find the PID of zombie's parent
pstree -p -s <zombie_PID>
# Then you can kill its parent and you will notice the zombie is gone.
sudo kill 9 <parent_PID>

Show memory usage

free -c 10 -mhs 1
# print 10 times, at 1 second interval

Display CPU and IO statistics for devices and partitions.

# refresh every second
iostat -x -t 1

Display bandwidth usage on an network interface (e.g. enp175s0f0)

iftop -i enp175s0f0

Change shell of a user (e.g. bonnie)

chsh -s /bin/sh bonnie
# /etc/shells: valid login shells

Display file status (size; access, modify and change time, etc) of a file (e.g. filename.txt)

stat filename.txt

Snapshot of the current processes

ps aux
Display a tree of processes

pstree

Print or control the kernel ring buffer

dmesg

Linux Programmer's Manuel: hier- description of the filesystem hierarchy

man hier

# e.g. check the status of cron service
systemctl status cron.service

# e.g. stop cron service
systemctl stop cron.service

Run a program with modified priority (e.g. ./test.sh)

# nice value is adjustable from -20 (most favorable) to +19
# the nicer the application, the lower the priority
# Default niceness: 10; default priority: 80

nice -10 ./test.sh

  - View jobs spawned by the current shell:
    jobs

  - List jobs and their process IDs:
    jobs -l  

  - Display information about jobs with changed status:
    jobs -n

  - Display only process IDs:
    jobs -p

  - Display running processes:
    jobs -r

  - Display stopped processes: 
    jobs -s


Set and unset shell options

# print all shell options
shopt

# to unset (or stop) alias
shopt -u expand_aliases

# to set (or start) alias
shopt -s expand_aliases

Soft link program to bin

ln -s /path/to/program /home/usr/bin
# must be the whole path to the program

  getent

  Get entries from Name Service Switch libraries.
  More information: https://manned.org/getent.

  - Get list of all groups:
    getent group

  - See the members of a group:
    getent group group_name

  - Get list of all services: 
    getent services

  - Find a username by UID:
    getent passwd 1000

  - Perform a reverse DNS lookup:
    getent hosts host


Nc as a chat tool!

# From server A:
$ sudo nc -l 80
# then you can connect to the 80 port from another server (e.g. server B):
# e.g. telnet <server A IP address> 80
# then type something in server B
# and you will see the result in server A!
Check which ports are listening for TCP connections from the network

#notice that some companies might not like you using nmap
nmap -sT -O localhost

# check port 0-65535
nmap  -p0-65535 localhost

Print some words that start with a particular string (e.g. words start with 'phy')

# If file is not specified, the file /usr/share/dict/words is used.
look phy|head -n 10

Repeat printing string n times (e.g. print 'hello world' five times)

printf 'hello world\n%.0s' {1..5}
Do not echo the trailing newline

username=`echo -n "bashoneliner"` 
Copy a file to multiple files (e.g copy fileA to file(B-D))

tee <fileA fileB fileC fileD >/dev/null
Delete all non-printing characters

tr -dc '[:print:]' < filename
Remove newline / nextline

tr --delete '\n' <input.txt >output.txt
Replace newline

tr '\n' ' ' <filename
To uppercase/lowercase

tr /a-z/ /A-Z/
Translate a range of characters (e.g. substitute a-z into a)

echo 'something' |tr a-z a
# aaaaaaaaa
Compare two files (e.g. fileA, fileB)

diff fileA fileB
# a: added; d:delete; c:changed

# or 
sdiff fileA fileB
# side-to-side merge of file differences
Compare two files, strip trailing carriage return/ nextline (e.g. fileA, fileB)

diff fileA fileB --strip-trailing-cr

Find common/differing lines

# having two sorted and uniqed files (for example after running `$ sort -uo fileA fileA` and same for fileB):
# ------  
# fileA:
# ------
# joey
# kitten
# piglet
# puppy
# ------
# fileB:
# ------
# calf
# chick
# joey  
# puppy
#
# Find lines in both files
comm -12 fileA fileB
# joey
# puppy
#
# Find lines in fileB that are NOT in fileA
comm -13 fileA fileB
# calf
# chick
#
# Find lines in fileA that are NOT in fileB
comm -23 fileA fileB
# kitten
# piglet

Number a file (e.g. fileA)

nl fileA

#or 
nl -nrz fileA
# add leading zeros

#or
nl -w1 -s ' '  
# making it simple, blank separate

Join two files field by field with tab (default join by the first column of both file, and default separator is space)

# fileA and fileB should have the same ordering of lines.
join -t '\t' fileA fileB

# Join using specified field (e.g. column 3 of fileA and column 5 of fileB) 
join -1 3 -2 5 fileA fileB

Combine/ paste two or more files into columns (e.g. fileA, fileB, fileC)

paste fileA fileB fileC
# default tab separate

Group/combine rows into one row

# e.g.
# AAAA  
# BBBB
# CCCC
# DDDD
cat filename|paste - -
# AAAABBBB
# CCCCDDDD
cat filename|paste - - - -
# AAAABBBBCCCCDDDD

Reverse string

echo 12345| rev

Find average of input list/file of integers

i=`wc -l filename|cut -d ' ' -f1`; cat filename| echo "scale=2;(`paste -sd+`)/"$i|bc

Generate all combination (e.g. 1,2) 

echo {1,2}{1,2}
# 1 1, 1 2, 2 1, 2 2

Generate all combination (e.g. A,T,C,G)

set = {A,T,C,G}
group= 5
for ((i=0; i<$group; i++)); do
    repetition=$set$repetition; done
    bash -c "echo "$repetition""

Read file content to variable

foo=$(<test1)  

Echo size of variable

echo ${#foo}

Echo a tab

echo -e ' \t '

Split file into smaller file 

# Split by line (e.g. 1000 lines/smallfile)
split -d -l 1000 largefile.txt

# Split by byte without breaking lines across files
split -C 10 largefile.txt

Rename all files (e.g. remove ABC from all .gz files)

rename 's/ABC//' *.gz

Remove file extension (e.g remove .gz from filename.gz)

basename filename.gz .gz

zcat filename.gz> $(basename filename.gz .gz).unpacked

Add file extension to all file(e.g add .txt)

rename s/$/.txt/ *
# You can use rename -n s/$/.txt/ * to check the result first, it will only print sth like this:
# rename(a, a.txt)
# rename(b, b.txt)
# rename(c, c.txt)

Squeeze repeat patterns (e.g. /t/t --> /t)

tr -s "/t" < filename

View first 50 characters of file

head -c 50 file

Cut and get last column of a file

cat file|rev | cut -d/ -f1 | rev

Add one to variable/increment/ i++ a numeric variable (e.g. $var)

((var++))

Cut the last column 

cat filename|rev|cut -f1|rev

Cut and get last column of a file

cat file|rev | cut -d/ -f1 | rev

Cut and get last column of a file

rev file | cut -d/ -f1 | rev

```sh  
rev filename | cut -f1 | rev
```

Explanation:
1. `rev filename`: Reverse each line.
2. `cut -f1`: Cut the first field (assuming tab delimiter).  
3. `rev`: Reverse again to restore original order minus last column.


Create or replace a file with contents

cat >myfile
let me add sth here
# exit with ctrl+d

# or using tee
tee myfile  
let me add sth else here

Append to a file with contents

cat >>myfile
let me add sth here
# exit with ctrl+d

# or using tee
tee -a myfile
let me add sth else here
# exit with ctrl+d

Clear the contents of a file (e.g. filename)

>filename

Working with json data

#e.g. to get all the values of the 'url' key, simply pipe the json to the following jq command(you can use .[]. to select inner json, i.e jq '.[].url')
cat file.json | jq '.url'

Decimal to Binary (e.g get binary of 5)

D2B=({0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1})
echo -e ${D2B[5]}
#00000101
echo -e ${D2B[255]}
#11111111

Wrap each input line to fit in specified width (e.g 4 integers per line)

echo "00110010101110001101" | fold -w4
# 0011
# 0010 
# 1011
# 1000
# 1101

Sort a file by column and keep the original order

sort -k3,3 -s
Right align a column (right align the 2nd column)

cat file.txt|rev|column -t|rev

To both view and store the output

echo 'hihihihi' | tee outputfile.txt
# use '-a' with tee to append to file.

Show non-printing (Ctrl) characters with cat

cat -v filename

Convert tab to space

expand filename
Convert space to tab

unexpand filename

Reverse cat a file

tac filename

Reverse the result from uniq -c

while read a b; do yes $b |head -n $a ; done <test.txt

Describe the format and characteristics of image files.

identify myimage.png
#myimage.png PNG 1049x747 1049x747+0+0 8-bit sRGB 1.006MB 0.000u 0:00.000

Get parent directory of current directory  

dirname `pwd`

Read .gz file without extracting

zmore filename

# or
zless filename

Run command in background, output error file

some_commands  &>log &

# or
some_commands 2>log &

# or  
some_commands 2>&1| tee logfile

# or
some_commands |& tee logfile

# or
some_commands 2>&1 >>outfile
#0: standard input; 1: standard output; 2: standard error


Run multiple commands in background

# run sequentially
(sleep 2; sleep 3) &

# run parallelly
sleep 2 & sleep 3 &


Run process even when logout (immune to hangups, with output to a non-tty)

# e.g. Run myscript.sh even when log out.
nohup bash myscript.sh

Send mail  

echo 'heres the content'| mail -a /path/to/attach_file.txt -s 'mail.subject' me@gmail.com
# use -a flag to set send from (-a "From: some@mail.tld")

Interacting with history

# list 5 previous command (similar to `history |tail -n 5` but wont print the history command itself)
fc -l -5

Add something to history (e.g. "addmetohistory")

# addmetodistory
# just add a "#" before~~

Backup with rsync

rsync -av filename filename.bak
rsync -av directory directory.bak
rsync -av --ignore_existing directory/ directory.bak
rsync -av --update directory directory.bak

rsync -av directory user@ip_address:/path/to/directory.bak
# skip files that are newer on receiver (i prefer this one!)

Create a temporary directory and cd into it

cd $(mktemp -d)
# for example, this will create a temporary directory "/tmp/tmp.TivmPLUXFT"

Make all directories at one time!

mkdir -p project/{lib/ext,bin,src,doc/{html,info,pdf},demo/stat}
# -p: make parent directory
# this will create:

#
# project/
# ├── bin
# ├── demo
# │   └── stat
# ├── doc
# │   ├── html
# │   ├── info
# │   └── pdf  
# ├── lib
# │   └── ext
# └── src

Run command only if another command returns zero exit status (well done)

cd tmp/ && tar xvf ~/a.tar

Run command only if another command returns non-zero exit status (not finish)

cd tmp/a/b/c ||mkdir -p tmp/a/b/c

Use backslash "" to break long command

cd tmp/a/b/c \
> || \
>mkdir -p tmp/a/b/c

List file type of file (e.g. /tmp/)

file /tmp/
# tmp/: directory

file /tmp/*       

Read user input

read input
echo $input

declare -a array=()

# or 
declare array=()

# or associative array
declare -A array=()

Send a directory

scp -r directoryname user@ip:/path/to/send

Use the last argument   

!$

Check last exit code

echo $?

Extract .xz

unxz filename.tar.xz
# then
tar -xf filename.tar  

Unzip tar.bz2 file (e.g. file.tar.bz2)

tar xvfj file.tar.bz2

Unzip tar.xz file (e.g. file.tar.xz)

unxz file.tar.xz
tar xopf file.tar

Extract to a path

tar xvf -C /path/to/directory filename.gz

Zip the content of a directory without including the directory itself

# First cd to the directory, they run:
zip -r -D ../myzipfile .
# you will see the myzipfile.zip in the parent directory (cd ..)

Output a y/n repeatedly until killed
# 'y':                
yes

# or 'n':
yes n

# or 'anything':
yes anything

# pipe yes to other command
yes | sudo pacman -Syu


Keep /repeatedly executing the same command (e.g Repeat 'wc -l filename' every 1 second)

watch -n 1 wc -l filename

Use Bash Strict Mode

# These options can make your code safer but, depending on how your pipeline is written, it might be too aggressive 
# or it might not catch the errors that you are interested in

# for reference see https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425
#               and https://mywiki.wooledge.org/BashPitfalls#set_-euo_pipefail

set -o errexit      # exit immediately if a pipeline returns a non-zero status
set -o errtrace     # trap ERR from shell functions, command substitutions, and commands from subshell
set -o nounset      # treat unset variables as an error
set -o pipefail     # pipe will exit with last non-zero status, if applicable
set -Eue -o pipefail  # shorthand for above (pipefail has no short option)

Print commands and their arguments when execute (e.g. echo expr 10 + 20 )

set -x; echo `expr 10 + 20 `
# or
set -o xtrace; echo `expr 10 + 20 `

# to turn it off..
set +x

Press any key to continue

read -rsp $'Press any key to continue...\n' -n1 key

Using Screen for multiple terminal sessions

# Create session and attach:
screen

# Create a screen and name it 'test'
screen -S test

# Create detached session foo:
screen -S foo -d -m

# Detached session foo:
screen: ^a^d

# List sessions:
screen -ls

# Attach last session: 
screen -r

# Attach to session foo:
screen -r foo

# Kill session foo:
screen -r foo -X quit


# Scroll:
# Hit your screen prefix combination (C-a / control+A), then hit Escape.
# Move up/down with the arrow keys (↑ and ↓).  

# Redirect output of an already running process in Screen:
# (C-a / control+A), then hit 'H'  

# Store screen output for Screen:
# Ctrl+A, Shift+H  
# You will then find a screen.log file under current directory.  

Using Tmux for multiple terminal sessions

# Create session and attach:
tmux

# Attach to session foo:
tmux attach -t foo

# Detached session foo:
^bd

# List sessions:
tmux ls

# Attach last session:
tmux attach

# Kill session foo:
tmux kill-session -t foo

# Create detached session foo:
tmux new -s foo -d

# Send command to all panes in tmux:
Ctrl-B
:setw synchronize-panes

# Some tmux pane control commands:
Ctrl-B
#   Panes (splits), Press Ctrl+B, then input the following symbol:
#   %  horizontal split
#   "  vertical split
#   o  swap panes
#   q  show pane numbers
#   x  kill pane
#   space - toggle between layouts

#   Distribute Vertically (rows):
select-layout even-vertical
#   or  
Ctrl+b, Alt+2

# Distribute horizontally (columns):
select-layout even-horizontal
#   or
Ctrl+b, Alt+1

# Scroll
Ctrl-b then \[ then you can use your normal navigation keys to scroll around.  
Press q to quit scroll mode.

Wait for a pid (job) to complete

wait %1
# or
wait $PID
wait ${!}  
#wait ${!} to wait till the last background process ($! is the PID of the last background process)


Convert pdf to txt

sudo apt-get install poppler-utils
pdftotext example.pdf example.txt


List one file per line.

ls -1
# or list all, do not ignore entries starting with .
ls -1a


Capture/record/save terminal output (capture everything you type and output)

script output.txt
# start using terminal
# to logout the screen session (stop saving the contents), type exit.


List contents of directories in a tree-like format.

tree
# go to the directory you want to list, and type tree (sudo apt-get install tree)
# output:
# home/
# └── project
#     ├── 1
#     ├── 2
#     ├── 3
#     ├── 4
#     └── 5
#

# set level directories deep (e.g. level 1)
tree -L 1
# home/
# └── project

Set up virtualenv(sandbox) for python

# 1. install virtualenv.
sudo apt-get install virtualenv
# 2. Create a directory (name it .venv or whatever name your want) for your new shiny isolated environment.
virtualenv .venv
# 3. source virtual bin
source .venv/bin/activate
# 4. you can check check if you are now inside a sandbox.
type pip
# 5. Now you can install your pip package, here requirements.txt is simply a txt file containing all the packages you want. (e.g tornado==4.5.3).
pip install -r requirements.txt
# 6. Exit virtual environment  
deactivate