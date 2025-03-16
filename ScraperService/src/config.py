import os


RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "myalma.rede")
RABBITMQ_PORT = 5672
RABBITMQ_CONNECTION = f"amqp://guest:guest@{RABBITMQ_HOST}:{RABBITMQ_PORT}/"
PRICE_SCRAPER_API_ENDPOINT_CREATE = "http://localhost:5280/Products/create-product"
PRICE_SCRAPER_API_ENDPOINT_CREATE_PRODUCTS = "http://localhost:5280/Products/create-products"


BASE_URL = "https://nakup.itesco.cz/groceries/en-CZ"
SEARCH_URL = "https://nakup.itesco.cz/groceries/en-CZ/search?query="

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.google.com/",  # Pretend traffic came from Google
    "DNT": "1",  # Do Not Track
}

# DIV_CONTAINER_CLASS = "styles__StyledTiledContent-dvv1wj-3 bUXuqC"
DIV_PRODUCT_DETAILS_CLASS = "WL_DZ"
SPAN_PRODUCT_NAME_CLASS = "styled__Text-sc-1i711qa-1 bsLJsh ddsweb-link__text"
SPAN_OFFER_PRICE_CLASS = "component__StyledHeading-sc-1t0ixqu-0 iDJPjF ddsweb-heading styled__PromoMessage-sc-hltpoc-0 bCvWmI"
P_CLUBCARD_PRICE_CLASS = "text__StyledText-sc-1jpzi8m-0 gljcji ddsweb-text styled__ContentText-sc-1d7lp92-9 cDKKKz ddsweb-value-bar__content-text"
SPAN_OFFER_DATES_CLASS = "text__StyledText-sc-1jpzi8m-0 kiGrpI ddsweb-text styled__TermsMessage-sc-hltpoc-1 eZgyeS"
SPAN_CLUBCARD_OFFER_DATES_CLASS = "text__StyledText-sc-1jpzi8m-0 ggFawa ddsweb-text styled__TermsText-sc-1d7lp92-10 dCWOwo ddsweb-value-bar__terms"
P_PRICE_PER_UNIT_CLASS = "text__StyledText-sc-1jpzi8m-0 gyHOWz ddsweb-text styled__PriceText-sc-v0qv7n-1 cXlRF"
P_PRICE_PER_KG_CLASS = "text__StyledText-sc-1jpzi8m-0 kiGrpI ddsweb-text styled__Subtext-sc-v0qv7n-2 kLkheV ddsweb-price__subtext"
A_URL_CLASS = "styled__Anchor-sc-1i711qa-0 gRXcDF ddsweb-title-link__link ddsweb-link__anchor"
