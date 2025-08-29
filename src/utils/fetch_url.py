def fetch_url(url: str):
	url = url[url.rfind('/') + 1:url.find('?')]

	return url