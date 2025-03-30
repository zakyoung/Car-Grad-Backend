from datetime import datetime

class Entry:
    def __init__(self, user_name: str, experiment_time: datetime, final_distance: float,
                 experiment_type: bool, initial_speed: int,
                 deceleration_of_front_car_stop_time: int, initial_distance: int):
        self.user_name = user_name
        self.experiment_time = experiment_time
        self.final_distance = final_distance
        self.experiment_type = experiment_type  # True for modified lights, False otherwise
        self.initial_speed = initial_speed
        self.deceleration_of_front_car_stop_time = deceleration_of_front_car_stop_time
        self.initial_distance = initial_distance

    def to_dict(self):
        return {
            "user_name": self.user_name,
            "experiment_time": self.experiment_time.isoformat(),
            "final_distance": self.final_distance,
            "experiment_type": int(self.experiment_type),  # convert to 1/0 for JSON/db
            "initial_speed": self.initial_speed,
            "deceleration_of_front_car_stop_time": self.deceleration_of_front_car_stop_time,
            "initial_distance": self.initial_distance
        }
