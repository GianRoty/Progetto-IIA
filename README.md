Membri gruppo
Andrea Magliani (894395)
Gianluca Rota (904375)

# LLM1DO Exploring Prisoners’ Voices: Keyword and Topics Analysis of CarteBollate Journals (2009-2024)

The original documents are a collection of journals (pdf files) called “carteBollate”. Each journal issue consists of multiple stories written by prisoners e.g., about their life in prison. There are multiple issues per year spanning over a period from 2009 to 2024. The pdf files were processed into a csv file that provides a structured version of all the journals in textual format. The csv file that will be given to the students has the following columns (with descriptions):

| COLUMN NAME    |                   DESCRIPTION                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------|
|      year      | Year (number) - indicating the publication year of an journal/story                                                 |
|      issue     | Issue number - indicating the issue an article was published in within the respective year                          |
|      topic     | Name of the topic an article was assigned to by the publisher (articles are grouped by topic within each issue)     |
|      article   | Headline of a specific article                                                                                      |
|      text      | Actual content of the article                                                                                       |

Tasks to process/analyze the articles:
## For each task: group by (1) article (2) topic (3) issue (4) year. Compare between these groups and compare over time.
1. Keywords (based on article text)
  - Preprocess, e.g. stopword removal, tokenize text
  - Extract keywords from the text
  - Consider stemming/lemmatization as well as n-grams
  - Save keyword terms in a table and visualize them (e.g., word clouds or bar charts)
2. Topic analysis (based on article title)
- Preprocess, e.g. stopword removal, tokenize text
- Extract keywords from the headings
- Consider stemming/lemmatization as well as n-grams
- Save topics in a table and visualize them (e.g., word clouds or bar charts)
- Compare with the Keywords identified in (1)
3. Lexical analysis (optional)
  - Analyze word length, sentence length etc.
  - Assign part-of-speech tags to words (e.g., identify nouns, verbs, adjectives, etc.)
  - Visualize findings
4. Sentiment analysis (optional)
  - Use pre-trained sentiment language model
  - Calculate score on article text basis
  - Visualize distribution
