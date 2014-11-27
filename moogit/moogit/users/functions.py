from models import Venue, Show, Band

def retrieve10Shows():
	Show.objects.order_by('Date')[:10]
