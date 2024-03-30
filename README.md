# Teach Me Concepts LLM

Owner: DOUG KIM

# 1. Goal & Background

**1) Goal** 

Nothing fancy. 

- This program will explain all the concepts mentioned in the `data/topics.py`
- explain up to 10 related topics that are required to explain those concepts.
- It will explain them in English and one more language of your choice and save it to `csv`

**2) Background**

My partner needed to pick up multiple new (& niche) concepts in a relatively short amount of time. I wanted to do anything that could help reduce my partner’s load. Furthermore, I enjoy a top-down approach when learning a new field as well. 

# 2. Environment setup

0)  If you don’t have `poetry` installed. 

```bash
brew install poetry # or `pipx install poetry` if you're using Windows 
```

1) In the root directory, run 

```bash
poetry shell
poetry install
```

2) copy or rename `.env.example`  to `.env` and fill in the values 

```
GEMINI_API_KEY = "{your_google_api_key}"
MODEL_NAME = "gemini-pro" (or other model name)
OUTPUT_COLUMNS = ['main_topic', 'concept_name', 'concept_explanation','concept_name_in_second_language', 'concept_explanation_in_second_language'] # columns you'd like to have for the output
OUTPUT_FILE_NAME = "{whatever_name_you_want}.csv"
MAX_TRY = 3 
SECOND_LANGUAGE = "Japanese" # any language you're comfortable with 
```

# 3. Modify to suit your needs

1) Change the `data/topics.py` file to put in the topics that you’re curious about. 

```
topics = {
    "Humanities": { # this is the `field` in the prompt 
        "Author/artist analysis" : # this is the `sub-field` in the prompt, more specific field
	        ["Lillian Hellman", "Graciela Iturbide's Mujer Ángel", "Galileo's mistake about Dante's Inferno", "Thomas Pringle/Mary Prince", "Vermeer's daughter", "Simon Rodia's Watts Towers"], # These are specific topics you're curious about
        "Indigenous civilizations, their treatment and culture" : ["NA Pueblo tribe's distinctive culture, West African rice farming in South Carolina"], 
        "Historical events and consequences": ["1700 Cascadia earthquake/Japanese ghost forests", "Archaeology and myths regarding large fossils/Griffons/Zeus", "Chinese literati art movement", "Thomas Malthus and the French Revolution"],
    },
```

# 4. Run the job

1) run below command in the root directory

```
poetry python3 run main.py
```