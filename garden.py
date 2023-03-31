import spacy

"The horse raced past the barn fell."
"The old man the boat."
"The chicken is ready to eat was cooking all day."
"The dog that chased the cat meowed loudly."
"The cheese tasted funny spoilt the sandwich."

garden_path_sentences = []

# add each sentence to the list
garden_path_sentences.append("The horse raced past the barn fell.")
garden_path_sentences.append("The old man the boat.")
garden_path_sentences.append("The man returned to his house was happy.")
garden_path_sentences.append("The cotton clothing is usually made of grows in Mississippi.")
garden_path_sentences.append("I convinced her children are noisy.")

"The horse raced past the barn fell."
["The", "horse", "raced", "past", "the", "barn", "fell", "."]


"The old man the boat."
["The", "old", "man", "the", "boat", "."]
"This sentence appears to be incomplete or ungrammatical, as it lacks a clear subject or verb. It is difficult to categorize it based on syntax alone."

"The chicken is ready to eat was cooking all day."
["The", "chicken", "is", "ready", "to", "eat", "was", "cooking", "all", "day", "."]
"This sentence is also incomplete or ungrammatical, as it lacks a verb. It is difficult to categorize it based on syntax alone."

"The dog that chased the cat meowed loudly."
["The", "dog", "that", "chased", "the", "cat", "meowed", "loudly", "."]
"This sentence is a run-on sentence, which combines two independent clauses without proper punctuation. One way to categorize it would be as a compound sentence."

"The cheese tasted funny spoilt the sandwich."
["The", "cheese", "tasted", "funny", "spoilt", "the", "sandwich", "."]
"This sentence is also a run-on sentence, which combines two independent clauses without proper punctuation. One way to categorize it would be as a compound sentence."  

nlp = spacy.load("en_core_web_sm")
print(spacy.explain("FAC"))

"Airports: One entity related to airports is the International Air Transport Association (IATA). It is a trade association representing the airline industry worldwide, with its headquarters in Montreal, Canada."
"yes"

"Highways: The main organization responsible for the construction and maintenance of highways varies by country. In the United States, for example, the Federal Highway Administration (FHWA) is a government agency within the U.S. Department of Transportation responsible for the construction and maintenance of the country's interstate highway system and other federally funded highways."
"Yes"

