import os
import urllib.parse

import requests
import yaml


def search_movies(query):
    url = f"https://movies-api.accel.li/api/v2/list_movies.json?query_term={urllib.parse.quote(query)}"
    try:
        response = requests.get(url)
        data = response.json()
        if (
            data.get("status") == "ok"
            and data.get("data", {}).get("movie_count", 0) > 0
        ):
            return data["data"]["movies"]
        return None
    except Exception as e:
        print(f"Error connecting to API: {e}")
        return None


def get_magnet_link(hash_code, movie_title):
    base_url = "magnet:?xt=urn:btih:"
    trackers = [
        "udp://open.demonii.com:1337/announce",
        "udp://tracker.openbittorrent.com:80",
        "udp://tracker.opentrackr.org:1337/announce",
        "udp://tracker.coppersurfer.tk:6969",
        "udp://glotorrents.pw:6969/announce",
        "udp://tracker.torrent.eu.org:451/announce",
        "udp://tracker.dler.org:6969/announce",
        "udp://open.stealth.si:80/announce",
        "https://tracker.moeblog.cn:443/announce&dk=",
        "https://tracker.zhuqiy.com:443/announce",
    ]
    tracker_str = "".join([f"&tr={urllib.parse.quote(t)}" for t in trackers])
    return f"{base_url}{hash_code}&dn={urllib.parse.quote(movie_title)}{tracker_str}"


def get_input_with_default(prompt, max_val):
    user_input = input(f"{prompt} [Default 1]: ").strip()
    if user_input == "":
        return 0
    try:
        val = int(user_input) - 1
        if 0 <= val < max_val:
            return val
    except ValueError:
        pass
    return None


def run_search():
    movie_name = input("\nEnter the movie name to search: ")
    if not movie_name.strip():
        return

    movies = search_movies(movie_name)
    if not movies:
        print("No movies found.")
        return

    print("\nResults found:")
    for idx, movie in enumerate(movies):
        print(f"{idx + 1}. {movie['title_long']}")

    m_idx = get_input_with_default("\nChoose a movie number", len(movies))
    if m_idx is None:
        print("Invalid selection.")
        return

    selected_movie = movies[m_idx]
    torrents = selected_movie.get("torrents", [])
    if not torrents:
        print("No torrents available.")
        return

    print(f"\nAvailable qualities for '{selected_movie['title_long']}':")
    for i, torrent in enumerate(torrents):
        print(
            f"{i + 1}. {torrent['quality']} [{torrent['type']}.{torrent['video_codec']}] ({torrent['size']})"
        )

    t_idx = get_input_with_default("Choose a quality", len(torrents))
    if t_idx is None:
        print("Invalid selection.")
        return

    torrent_data = torrents[t_idx]
    magnet = get_magnet_link(torrent_data["hash"], selected_movie["title_long"])

    print("\n--- Magnet Link ---")
    print(magnet)

    # Prepare data for YAML
    new_entry = {
        "title": selected_movie["title_long"],
        "quality": torrent_data["quality"],
        "format": f"{torrent_data['type']}.{torrent_data['video_codec']}",
        "size": torrent_data["size"],
        "magnet": magnet,
        "status": "",
    }

    file_path = "links.yaml"

    try:
        existing_data = []
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = yaml.safe_load(f)
                if isinstance(content, list):
                    existing_data = content

        existing_data.append(new_entry)

        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(existing_data, f, allow_unicode=True, sort_keys=False)

        print(f"\nSuccessfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving to file: {e}")


def main():
    while True:
        run_search()

        repeat = (
            input("\nWould you like to perform another search? (y/n) [Default y]: ")
            .strip()
            .lower()
        )
        if repeat == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
