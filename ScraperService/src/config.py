import os


RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "myalma.rede")
RABBITMQ_PORT = 5672
RABBITMQ_CONNECTION = f"amqp://guest:guest@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"
PRICE_SCRAPER_API_ENDPOINT_CREATE = "http://localhost:5280/Products/create-product"
PRICE_SCRAPER_API_ENDPOINT_CREATE_PRODUCTS = "http://localhost:5280/Products/create-products"


BASE_URL = "https://nakup.itesco.cz/groceries/en-GB"
SEARCH_URL = "https://nakup.itesco.cz/groceries/en-GB/search?query="

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.google.com/",  # Pretend traffic came from Google
    "DNT": "1",  # Do Not Track
}

# DIV_CONTAINER_CLASS = "styles__StyledTiledContent-dvv1wj-3 bUXuqC"
DIV_PRODUCT_DETAILS_CLASS = "product-details--wrapper"
SPAN_PRODUCT_NAME_CLASS = "styled__Text-sc-1i711qa-1 jGVLws ddsweb-link__text"
SPAN_OFFER_PRICE_CLASS = "offer-text"
P_CLUBCARD_PRICE_CLASS = "text__StyledText-sc-1jpzi8m-0 kYYaYX ddsweb-text styled__ContentText-sc-1d7lp92-8 bQebOp ddsweb-value-bar__content-text"
SPAN_OFFER_DATES_CLASS = "dates"
SPAN_CLUBCARD_OFFER_DATES_CLASS = "text__StyledText-sc-1jpzi8m-0 ldCcMf ddsweb-text styled__TermsText-sc-1d7lp92-9 fhmvSB ddsweb-value-bar__terms"
P_PRICE_PER_UNIT_CLASS = "styled__StyledHeading-sc-119w3hf-2 iMxPSd styled__Text-sc-8qlq5b-1 enpJuv beans-price__text"
P_PRICE_PER_KG_CLASS = "styled__StyledFootnote-sc-119w3hf-7 bdDwjP styled__Subtext-sc-8qlq5b-2 gKiziO beans-price__subtext"
A_URL_CLASS = "styled__Anchor-sc-1i711qa-0 gJVSxB ddsweb-link__anchor"
