# Readability-Score https://hyperskill.org/projects/155

## Stage 1
Let's create a simple program. If the text contains more than 100 symbols (including spacebars and punctuation) then the text is considered hard to read. Else, the text is considered easy to read. If the text contains exactly 100 symbols then it is still easy to read.

## Stage 2
Let's suppose that if the text contains on average more than 10 words per sentence, then this text is hard to read. Otherwise, this text is easy to read.

## Stage 3
In this stage, you will program the Automated readability index. It was introduced in 1968 and a lot of research works rely on this.
You can look at different ages corresponding to the different scores by the table in this  article.
Also, your program should read a file instead of typing a text manually. You should pass the filename through the command line arguments.
The program should output the score itself and an approximate age needed to comprehend the text.
Use the appropriate rounding function to calculate the score as integer.
You should also print how many characters, words, and sentences the text has.
The number of characters is any visible symbol (so, in the real text it's everything except space, newline "\n" and tab "\t").
Notice, that the text can contain multiple lines, not just a single line like in the previous stages. You should analyze all the lines.

## Stage 4
In this stage, you should implement various other scientific approaches to calculate a readability score.

## Stage 5
Implement Probability-based score
