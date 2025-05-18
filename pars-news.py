import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def parse_news(url, max_news=10):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all("h3")[:max_news]  # Берём первые N заголовков
        
        print(f"\nНовости с {url}:")
        for idx, headline in enumerate(headlines, 1):
            print(f"{idx}. {headline.get_text(strip=True)}")
            
    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")

# Пример использования
parse_news("https://lenta.ru/rubrics/media/")  # Можно парсить и другие сайты
