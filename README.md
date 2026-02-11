# Flux Browser 🌸

A unique search engine with personality! Flux Browser combines TF-IDF search with a dynamic power system and personality-driven responses inspired by romcom/shonen anime aesthetics.

## ✨ Features

- **Smart Search**: TF-IDF vectorization with cosine similarity ranking
- **Power System**: Multi-dimensional scoring (Clarity, Depth, Credibility, Freshness)
- **Dynamic Personality**: Adaptive responses based on query complexity
- **Modern UI**: Beautiful gradient design with Tailwind CSS
- **Full Stack**: FastAPI backend + React TypeScript frontend

## 🏗️ Project Structure

```
Flux-Browser/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── config.py            # Settings
│   │   ├── crawler/
│   │   │   └── crawl.py         # Text collection
│   │   ├── search/
│   │   │   ├── index.py         # TF-IDF indexing
│   │   │   └── query.py         # Search logic
│   │   ├── ranking/
│   │   │   └── scorer.py        # Power system scoring
│   │   ├── personality/
│   │   │   └── responses.py     # Personality responses
│   │   └── data/
│   │       └── documents.json   # Search corpus
│   ├── requirements.txt
│   └── run.py
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── SearchBar.tsx
    │   │   ├── ResultCard.tsx
    │   │   ├── StatsBar.tsx
    │   │   └── PersonalityBanner.tsx
    │   └── pages/
    │       └── Home.tsx
    └── package.json
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm or yarn

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python run.py
```

The backend will start at `http://localhost:8000`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

The frontend will start at `http://localhost:5173`

## 📡 API Endpoints

### Search
```
GET /search?q={query}
```

**Response:**
```json
{
  "message": "Starting your journey, huh? Cute.",
  "results": [
    {
      "url": "https://example.com",
      "stats": {
        "clarity": 4,
        "depth": 3,
        "credibility": 4,
        "freshness": 3
      }
    }
  ]
}
```

## 🎨 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **scikit-learn** - TF-IDF vectorization and cosine similarity
- **Uvicorn** - ASGI server

### Frontend
- **React** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS v4** - Styling
- **Vite** - Build tool

## 🌟 Features Explained

### Power System
Each search result is scored across four dimensions:
- **Clarity** (1-5): How clear and understandable the content is
- **Depth** (1-5): How comprehensive the information is
- **Credibility** (1-5): Reliability of the source
- **Freshness** (1-5): How up-to-date the content is

### Personality System
Flux adapts its personality based on query complexity:
- **Beginner** (≤3 words): "Starting your journey, huh? Cute."
- **Advanced** (>3 words): "Whoa… that's some serious energy."

## 🛠️ Development

### Adding Documents
Edit `backend/app/data/documents.json`:
```json
[
  {
    "url": "https://example.com",
    "content": "Your content here..."
  }
]
```

### Customizing Personality
Edit `backend/app/personality/responses.py` to add more personality variations.

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 👤 Author

**Kushagra Bhardwaj**
- GitHub: [@Kush05Bhardwaj](https://github.com/Kush05Bhardwaj)

## 🙏 Acknowledgments

- Inspired by anime aesthetics and power systems
- Built with modern web technologies
- Community-driven development

---

Made with 💜 and ✨
