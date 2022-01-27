# Eluvio
Program which finds longest strand of bytes in at least two files.

This program will consider every substring in every given file and check whether it is bigger than the current largest strand, and if it is then it will check whether it is present in at least one other file. While it checks whether it is present in at least one more file it will add the file name and offset where the strand starts on that respective file. It will then print out the length of the strand, the files it is present in, and the respective offset where it starts in each file. Uncomment indicated line to have actual strand printed out too.
