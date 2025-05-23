class PointsForPlace:
    @staticmethod
    def get_points_for_place(place: int):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            return 101 - place


class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters: int):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
            return points


class TotalPoints(PointsForPlace, PointsForMeters):
    @staticmethod
    def get_total_points(meters, place):
        total_points = TotalPoints.get_points_for_place(
            place) + TotalPoints.get_points_for_meters(meters)

        return total_points


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
