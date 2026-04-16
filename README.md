# YTS Magnet Grabber 🧲

A fast, interactive CLI tool to search for movies on YTS, generate magnet links (including high-quality trackers), and save them to an organized YAML file.

## ✨ Features
* **Interactive Search:** Search by movie title and pick from a list of results.
* **Quality Selection:** Choose between available resolutions (720p, 1080p, 2160p, etc.).
* **Custom Magnet Construction:** Automatically builds magnet links using a robust list of reliable public trackers.
* **YAML Export:** Saves your selections to `links.yaml` for easy integration with media managers or downloaders.
* **Persistent Workflow:** Search for multiple movies in a single session.

## 🚀 Getting Started

This project is managed by [uv](https://github.com/astral-sh/uv), the extremely fast Python package installer and resolver.

### Prerequisites
* [uv](https://docs.astral.sh/uv/getting-started/installation/) installed on your machine.
* Python 3.13 or higher.

### Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AminGholizad/yts-magnet-grabber.git
    cd yts-magnet-grabber
    ```

2.  **Run directly with uv:**
    The easiest way to run the script without manually managing environments:
    ```bash
    uv run main.py
    ```
    *This will automatically create a virtual environment and install dependencies like `requests` and `pyyaml` for you.*

## 📂 Output Format

When you select a movie, it is appended to `links.yaml` in the following format:

```yaml
- title: Inception (2010)
  quality: 1080p
  format: bluray.x264
  size: 1.6 GB
  magnet: magnet:?xt=urn:btih:EXAMPLEHASH...
  status: ''
```

## 🛠 Project Structure
* `main.py`: The primary script containing search logic and link generation.
* `pyproject.toml`: Project metadata and dependencies (managed by uv).
* `links.yaml`: Generated file containing your grabbed magnet links.

## ⚠️ Disclaimer
This tool is for educational purposes. Please ensure you are complying with local laws regarding torrenting and copyrighted content.
