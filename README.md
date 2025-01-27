# Bengal Tiger Conservation Data

## Overview

### Problem Statement
Bengal tigers are critically endangered, facing severe threats such as poaching, habitat loss, and human-wildlife conflict. Without accurate data and timely interventions, their population may continue to decline, leading to potential extinction.

### Solution
This project aims to address these challenges by creating a comprehensive database to track and analyze data on Bengal tigers. This includes information on population size, habitat health, poaching incidents, prey availability, and human-wildlife conflict. By leveraging data analytics and AI, we can identify trends, threats, and inform effective conservation strategies.

### Primary Features

- **Interactive Experience**: Walk through a tiger's life like an interactive museum.
- **Environmental Impact Visualization**: Visualize how our daily decisions affect the earth.
- **AI Integration**: Use AI as your guide to learning more about Bengal tigers and their conservation.

## Project Structure

```
[project-name]/
│   # Phase 1: Business logic:
├── core.py          # Core business logic
├── test.py          # Tests for business logic
│
│   # Phase 2: Choose one or more of these UI options:
├── main.py          # CLI interface (optional)
├── web.py           # Web interface (Flask-based)
├── game.py          # Game interface (optional)
│
├── readme.md        # This file
├── changelog.md     # Weekly development updates
├── requirements.txt # Project dependencies
├── .gitignore       # Git ignore file
│
├── /data            # Data files
│   └── .gitkeep     # Placeholder to keep the directory in version control
│
├── /templates       # HTML templates for the web interface
│   ├── dashboard.html
│   └── index.html
```

## Detailed Description of Components

### Core Business Logic
The core business logic is implemented in [`core.py`](core.py). It includes classes and methods to represent various aspects of Bengal tiger conservation:
- **Tiger**: Represents a tiger with attributes like name, weight, height, status, and population.
- **Habitat**: Represents the habitat with attributes like location, temperature, biome, protection status, population, and human activity.
- **Poaching**: Represents poaching incidents with attributes like date, method, and victim.
- **Prey**: Represents prey species with attributes like scientific name and population.
- **Data**: Represents data points with attributes like activity, timestamp, and population flux.
- **Protection**: Represents protection efforts with attributes like area status, threat level, and updated population.
- **Tourist**: Represents tourism impact with attributes like impact type, tourism level, and policies.

### Web Interface
The web interface is implemented in [`web.py`](web.py) using Flask. It provides routes for:
- **Index Page**: Displays a welcome message and allows users to name their tiger.
- **Dashboard**: Displays detailed information about the named tiger, including population trends, habitat, prey, tourism impact, and poaching incidents.
- **AI Q&A**: Allows users to ask questions about Bengal tigers and get responses from the AI module.

### AI Integration
The AI integration is handled in [`ai.py`](ai.py). It uses OpenAI's API to generate responses to user queries. The AI is configured to act as a knowledgeable zookeeper focused on environmental safety.

### Testing
The tests for the core business logic are implemented in [`test.py`](test.py). It includes unit tests for initializing various classes like Tiger, Habitat, Poaching, Prey, Data, Protection, and Tourist.

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Virtual environment (recommended)

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/bengal-tiger-conservation.git
   cd bengal-tiger-conservation
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the web application:
   ```sh
   python web.py
   ```

## Usage

### Web Interface
- Navigate to `http://127.0.0.1:5000/` to access the web interface.
- Name your tiger and explore the dashboard for detailed information.

### AI Q&A
- Use the Q&A section on the dashboard to ask questions about Bengal tigers and get responses from the AI.

## Resources Used

- [National Geographic](https://www.nationalgeographic.com)
- [World Wildlife Fund](https://www.worldwildlife.org)
- [Course materials from CSC-121]

---

Created by Sodbiligt Ganbadrakh for Mark Johnson CSC-121 (Furman University)
