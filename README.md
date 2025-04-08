# Azure OpenAI Chatbot - Fullstack Application

This is a fullstack chatbot application powered by Azure OpenAI. It includes:

- **Frontend:** A React web interface for users to ask questions.
- **Backend:** A Flask-based API that communicates with Azure OpenAI and optionally uses Azure Cognitive Services for speech.

---

## 📁 Project Structure

```
.
├── Chatbot-Backend/
│   ├── app.py                # Flask API logic
│   ├── gunicorn_start.sh     # Gunicorn launch script
│   ├── requirements.txt      # Backend dependencies
│   └── .env (optional)       # Backend environment variables
│
├── Chatbot-Frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── app.js            # Chat UI and logic
│   │   ├── index.js          # React entry point
│   │   └── index.css         # Styles
│   ├── package.json
│   └── .env                  # Frontend API URL config
└── README.md
```

---

## 🌐 Frontend - React

### Features
- Interactive chat interface
- Displays user input and AI responses
- Styled message bubbles and markdown-ready response box
- Configurable backend URL via `.env`

### Setup

```bash
cd Chatbot-Frontend
npm install
```

Create a `.env` file:

```env
REACT_APP_API_URL=http://localhost:8000/chat
```

Run the app:

```bash
npm start
```

Build for production:

```bash
npm run build
```

---

## 🔙 Backend - Flask (Python 3.11)

### Features
- Uses Azure OpenAI GPT models (e.g., GPT-4o)
- Supports Azure authentication and API keys
- CORS-enabled to work with frontend
- Optional support for Azure Speech SDK (placeholder)

### Setup

```bash
cd Chatbot-Backend
python3.11 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Set environment variables:

```bash
export ENDPOINT_URL="https://<your-azure-openai-endpoint>"
export DEPLOYMENT_NAME="gpt-4o"
export AZURE_OPENAI_API_KEY="<your-azure-key>"
```

Run locally:

```bash
python app.py
```

Or use Gunicorn:

```bash
chmod +x gunicorn_start.sh
./gunicorn_start.sh
```

---

## 🔒 Environment Variables

Both frontend and backend require environment variables:

**Backend** (`Chatbot-Backend/.env` or system environment)
- `ENDPOINT_URL`: Your Azure OpenAI endpoint (Gov or Commercial)
- `DEPLOYMENT_NAME`: Model deployment name (e.g., `gpt-4o`)
- `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key

**Frontend** (`Chatbot-Frontend/.env`)
- `REACT_APP_API_URL`: URL of the Flask `/chat` endpoint

---

## 🧩 Backend Dependencies

From `requirements.txt`:
```text
Flask==2.1.2
flask-cors==3.0.10
azure-identity==1.15.0
azure-cognitiveservices-speech==1.43.0
openai==1.14.2
gunicorn==20.1.0
Werkzeug==2.1.2
```

---

## ⚙️ Production Deployment

### Backend
You can deploy the backend to:
- Azure App Service (Linux preferred)
- Azure Container Apps
- Docker / Kubernetes

Use `gunicorn_start.sh` in your startup command.

### Frontend
You can deploy the frontend to:
- Azure Static Web Apps
- Azure App Service
- Netlify / Vercel / Firebase

Build first:
```bash
npm run build
```

---

## ✅ Todo & Enhancements
- [ ] Add Markdown rendering with `react-markdown`
- [ ] Add speech-to-text/audio support with Azure Cognitive Services
- [ ] User authentication (AAD/B2C)
- [ ] Logging and monitoring (App Insights, etc.)

---

## 📬 Contact
Maintained by [Your Name]. For questions, email [your-email@example.com] or open an issue in the repo.

---

## 📃 License
MIT License

