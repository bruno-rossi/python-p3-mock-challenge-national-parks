class NationalPark:

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"<NationalPark {self.name}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            pass
        elif isinstance(name, str) and len(name) >= 3:
            self._name = name
        
    def trips(self):
        park_trips = []
        for trip in Trip.all:
            if trip.national_park == self:
                park_trips.append(trip)
        return park_trips
    
    def visitors(self):
        park_visitors = []
        for trip in Trip.all:
            if trip.visitor in park_visitors:
                pass
            elif isinstance(trip.visitor, Visitor) and trip.national_park == self:
                park_visitors.append(trip.visitor)
        return park_visitors
    
    def total_visits(self):
        park_visits = 0
        for trip in Trip.all:
            if trip.national_park == self:
                park_visits += 1
        return park_visits
    
    def best_visitor(self):
        park_visitors = {}
        for trip in self.trips():
            if trip.visitor in park_visitors:
                park_visitors.update({trip.visitor: park_visitors.get(trip.visitor) + 1})
            else:
                park_visitors.update({trip.visitor: 1})
        
        top_visitor = None
        for visitor in park_visitors:
            if top_visitor == None:
                top_visitor = visitor
            elif park_visitors[visitor] > park_visitors[top_visitor]:
                top_visitor = visitor
        return top_visitor
    
    @classmethod
    def most_visited(cls):
        park_visits = {}
        for trip in Trip.all:
            if trip.national_park in park_visits:
                park_visits.update({trip.national_park: park_visits[trip.national_park] +1})
            else:
                park_visits.update({trip.national_park: 1})
        
        # print(park_visits)

        top_park = None
        for park in park_visits:
            if top_park == None:
                top_park = park
            elif park_visits[park] > park_visits[top_park]:
                top_park = park
        return top_park

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.add_trips(self)

    def __repr__(self) -> str:
        return f"<Trip {self.visitor} - {self.national_park}>"

    @classmethod
    def add_trips(cls, trip):
        cls.all.append(trip)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
    
class Visitor:

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"<Visitor {self.name}>"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 16):
            self._name = name
        
    def trips(self):
        visitor_trips = []
        for trip in Trip.all:
            if trip.visitor == self: 
                visitor_trips.append(trip)
        return visitor_trips
    
    def national_parks(self):
        parks = []
        for trip in Trip.all:
            if trip.national_park in parks:
                pass
            elif isinstance(trip.national_park, NationalPark) and trip.visitor == self:
                parks.append(trip.national_park)
        return parks
    
    def total_visits_at_park(self, park):
        total_visits = 0
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park == park:
                total_visits += 1
        return total_visits
