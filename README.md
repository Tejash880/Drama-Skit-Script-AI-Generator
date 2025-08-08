# Drama-Skit-Script-AI-Generator
# Desi Drama GPT: A Regional Skits Generator

> *"Lights, camera, laughter! Bringing India’s everyday humor to the AI stage, one skit at a time."*

![Desi Drama GPT Banner](https://i.imgur.com/x9ZlJMz.png)

---

## 🌟 Introduction

**Desi Drama GPT** is not just another chatbot or AI text generator. It’s an immersive regional flavor machine crafted for humor, emotion, satire, and pure desi entertainment. It creates short, hilarious two-character skits in regional Indian languages, with prompts as simple as character names and a topic. Powered by the mighty `microsoft/phi-2` transformer model and an elegant Streamlit frontend, this project brings a creative spin to how we collect, understand, and appreciate Indian conversational humor.

Imagine your dadi and the postman debating about WhatsApp, or a chaiwala and traffic cop arguing about who’s the better gossipmonger. With Desi Drama GPT, skits like these are generated automatically, and they're dripping with desi flair.

---

## 🚀 Why Desi Drama GPT?

India is a land of storytellers, with every street corner echoing anecdotes. From witty punchlines in Punjabi to emotional flare in Tamil dramas, humor and drama are woven into the culture. While global models dominate the AI space, few focus on local linguistic charm, emotional cadence, or indigenous humor styles. This is where Desi Drama GPT shines.

This app doesn’t just generate random text. It captures:

* ✌️ Regional slang
* 🎺 Cultural humor
* ⚖️ Character-specific speech
* 🚗 Topical scenarios (tech, family, politics)

---

## 💡 Key Features

### 🎥 Skit Generator

Generate short humorous dialogues between any two desi characters on any topic. Skits are designed like short plays with character tags and regional flavor.

### 🌍 Multilingual Magic

Supports multiple Indian languages such as:

* Hindi
* Tamil
* Telugu
* Punjabi
* Marathi
* Bengali
* Kannada
* Gujarati

### 📕 Corpus Collector

Every generated skit is stored in a `JSONL` file for linguistic research, fine-tuning datasets, or building larger corpora of regional conversation.

### 📂 Offline & Hugging Face Deployable

Lightweight enough to run locally. Also deployable as a Hugging Face Space using Streamlit UI.

### 🤔 Local Character Roleplay

Create humorous or satirical content between local figures like:

* Rickshaw Wala vs Techie
* Dadi vs Call Center Employee
* Coconut Seller vs Traffic Cop

---

## 📃 Example Usage

### User Input:

* Character 1: Dadi (Grandma)
* Character 2: Postman
* Topic: WhatsApp and smartphones
* Language: Hindi

### AI Output:

```text
Dadi: Arre beta, yeh WhatsApp kya hai? Isme khana banta hai kya?
Postman: Nahi Dadi, isme message bhejte hai. Chat karte hai log.
Dadi: Chat? Chatni jaise?
Postman: Nahi Dadi, baatcheet! Mobile mein likhte hai.
Dadi: Achha! Mujhe laga mobile sirf torch hai.
Postman: Aap bhi na Dadi, WhatsApp pe video call bhi hota hai!
Dadi: Toh shaadi bhi mobile pe ho jaaye kya?
Postman: Lagta hai aapko ek smartphone zarurat hai!
```

---

## 📄 Installation

### 🔧 Local Setup

```bash
# Clone the repo
https://github.com/yourname/desi-drama-gpt.git
cd desi-drama-gpt

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### 🌐 Hugging Face Space

1. Create a new space (Streamlit)
2. Upload:

   * `app.py`
   * `requirements.txt`
3. Done! Skits on the go.

---

## 🪤 Technology Stack

| Layer          | Tool/Library             |
| -------------- | ------------------------ |
| UI             | Streamlit                |
| Language Model | microsoft/phi-2          |
| Tokenization   | HuggingFace Transformers |
| Storage        | JSONL corpus collector   |
| Deployment     | Hugging Face Spaces      |

---

## 🤖 Dataset & Corpus

Each skit is stored in `corpus/desi_skit.jsonl` in this format:

```json
{
  "timestamp": "2025-08-08T10:32:04Z",
  "character_1": "Dadi",
  "character_2": "Postman",
  "topic": "WhatsApp and smartphones",
  "language": "Hindi",
  "skit": "Dadi: Arre beta..."
}
```

This makes it incredibly easy to:

* Fine-tune language models
* Study humor linguistics
* Build dialogue agents
* Generate region-specific training data

---

## 🔄 Reusability Ideas

Desi Drama GPT is modular. You can adapt it for:

* 🎤 **Voice Acting**: Convert dialogues into voice-acted audio skits using TTS.
* 🎨 **Comic Strips**: Auto-generate comic strips using AI image tools + this dialogue.
* 📚 **Linguistic Research**: Study regional syntax, slang, and humor in Indian languages.
* 🧠 **Chatbot Fine-tuning**: Use this data to train more desi-fluent AI chatbots.
* 🎡 **Satirical News**: Auto-generate parody content with characters mimicking politicians or celebs.

---

## 🏅 Creative Prompts You Can Try

* Rickshaw driver vs Software Engineer about potholes
* Mother-in-law vs Bahu about fashion trends
* Pandit vs DJ on wedding traditions
* Vegetable seller vs Food blogger
* Government babu vs Startup founder
* Netflix addict vs Doordarshan uncle

---

## ⚙️ Customization Ideas

Want to add spice to your version?

* ✏️ Add `voice` synthesis (gTTS or Coqui)
* 🖇 Add `image avatars` for each character
* 📈 Corpus stats dashboard
* 📲 SMS/Twitter-style export for viral sharing
* 🔹 Add more characters in the dialog
* 💰 Monetize with regional meme creation tools

---

## 🔧 requirements.txt

```txt
transformers
streamlit
torch
```

For CPU optimization:

```txt
accelerate
```

---

## 🤝 Contributors

| Name          | Role                                   |
| ------------- | -------------------------------------- |
| Tejas Hazari  | Idea, Architecture, Prompt Engineering |
| OpenAI GPT-4o | Code Co-Pilot                          |
| Hugging Face  | Model Hosting + Deployment             |

---

## 🌍 Vision

Desi Drama GPT is more than fun. It’s a **preservation tool for language, culture, and humor.** In a world where AI models are dominated by Western datasets, it aims to:

* Democratize regional AI tools
* Capture how real people joke, banter, argue
* Help Indian creators build culturally relevant AI products
* Provide datasets for low-resource language AI research

---

## 🎉 Future Goals

* Add **LLM fine-tuning** capability for each language
* Enable **voice acting** with different character tones
* Use **LangChain or RAG** to enrich scripts with real facts
* Include **emotion tagging** per line
* Auto-convert skits into **memes or video reels**

---

## 📢 License

MIT License – Free to use, modify, and deploy.

Let the laughter echo in every language.
Let AI understand satire, sass, and street-talk.

**Desi Drama GPT is your stage.**
Now go write the drama!

---

## ✨ Support & Feedback

Loved the app? Got ideas or bugs?

* [Open an Issue](https://github.com/yourname/desi-drama-gpt/issues)
* [Tweet @yourhandle](https://twitter.com/yourhandle)
* [Drop a Star](https://github.com/yourname/desi-drama-gpt)

---

## 💙 Made with Love in India

![India](https://img.icons8.com/emoji/48/india-emoji.png)
