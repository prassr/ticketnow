import datetime

def filter_bookings_by_date_range(bookings, start_date, end_date):
    filtered_bookings = []

    start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    for booking in bookings:
        if start_datetime <= datetime.datetime.strptime(booking["start_time"], '%a, %d %b %Y %H:%M:%S')  <= end_datetime:
            filtered_bookings.append(booking)
    
    return filtered_bookings

