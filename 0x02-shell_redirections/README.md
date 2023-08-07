# Shell Redirection
0- echo " " is used to write a script to the file.
1- echo "\ " is used to add a confused smiley to the file.
2- cat is used to read file.
3- cat is used to read the 2 files.
4- tail is used to read the last 10 lines.
5- head is used to read the first 10 lines.
6- head --lines=3 iacta | tail --lines=1 is used to read a specific line inside the file.
7- echo is used to add wordsredirected to a specific line.
8- ls -la is used to write in the file in the specific format.
9- echo -en "" | tail --lines=1 iacta >> iacta is used to duplicate a specific line.
10- find . -name '\*.js' -type f -delete is used to remove the js files.
11- find -mindepth 1 -type d | wc -l is used to find and wordcount a file.
12- ls -t | head used to list the newest 10 files in the directory.
13- sort | uniq -u is used to print words that are not repeated.
14- grep -i root /etc/passwd is used to display lines containing the pattern “root” from the file /etc/passwd.
15- grep -i bin /etc/passwd | wc -l is used to display the number of lines that contain the pattern “bin” in the file /etc/passwd. 
16- grep -iA 3 root /etc/passwd is used to display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
17- grep -iv bin /etc/passwd is used to display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
18- grep -i "^[a-z]" /etc/ssh/sshd_config is used to display all lines of the file /etc/ssh/sshd_config starting with a letter.
19- tr Ac Ze is used to replace all characters A and c from input to Z and e respectively.
20- tr -d cC is used to removes all letters c and C from input.
21- rev is used to reverse the output.
22- cut -d':' -f1,6 /etc/passwd | sort is used to displays all users and their home directories, sorted by users.
23- find . -empty -printf "%f\n" is used to finds all empty files and directories in the current directory and all sub-directories.
24- find . -name \*.gif -type f -printf "%f\n" | LC_COLLATE=C sort --ignore-case | rev | cut -c 5- | rev is used to lists all the files with a .gif extension in the current directory and all its sub-directories.
25- cut -c 1 | tr -d '\n' | sort is used to decode acrostics that use the first letter of each line.
26- cut -f1 -d$'\t' | sort | uniq -c | tr -s ' ' | sort -t' ' -k1 -nr | head -11 | cut -d' ' -f3 parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests. 
