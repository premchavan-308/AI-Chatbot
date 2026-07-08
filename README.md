# 🤖 AI Mood-Based Chatbot

An interactive AI chatbot built using **Python**, **Streamlit**, **LangChain**, and **Mistral AI**. The application allows users to chat with an AI that can adopt different personalities—**Angry 😡**, **Funny 😂**, and **Sad 😢**—providing a unique conversational experience while maintaining chat history throughout the session.

---

## 🚀 Features

* 🎭 Three AI personality modes:

  * 😡 Angry Mode
  * 😂 Funny Mode
  * 😢 Sad Mode
* 💬 Interactive chat interface using Streamlit
* 🧠 Conversation memory with LangChain message history
* 🔄 Reset chat functionality
* ⚡ Powered by the Mistral Large Language Model
* 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Mistral AI**
* **python-dotenv**

---

## 📂 Project Structure

```text
AI-Mood-Chatbot/
│
├── UIchatbot.py          # Streamlit application
├── chatbot.py            # Command-line chatbot
├── .env                  # API key (not included)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Mood-Chatbot.git
cd AI-Mood-Chatbot
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

### Streamlit Version

```bash
streamlit run UIchatbot.py
```

### Console Version

```bash
python chatbot.py
```

---

## 🎮 How to Use

1. Launch the application.
2. Select your preferred AI personality:

   * 😡 Angry
   * 😂 Funny
   * 😢 Sad
3. Start chatting with the AI.
4. Click **Reset Chat** to begin a new conversation.
5. Type **0** in the console version to exit.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
README Images/
├── Home.png
├── Angry_Mode.png
├── Funny_Mode.png
└── Sad_Mode.png
```

Then include them like this:

```markdown
![Home](README Images/Home.png)

![Funny Mode](README Images/Funny_Mode.png)
```

---

## 📌 Future Improvements

* 🌐 Voice input and speech synthesis
* 🤖 Additional AI personalities
* 🌍 Multi-language support
* 💾 Export chat history
* ⚙️ Adjustable AI parameters (temperature, model selection)
* 📱 Mobile-responsive interface

---

## 👨‍💻 Author

**Prem Ramdas Chavan**

Computer Engineering Student | AI & Data Enthusiast

GitHub: https://github.com/premchavan-308


---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub if you found it useful or interesting!
