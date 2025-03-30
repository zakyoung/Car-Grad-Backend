from databaseExchange import create_new_entry
from Entry import Entry
def create_entry_from_object_in_database(entry):
    return create_new_entry(
        user_name=entry.user_name,
        experiment_time=entry.experiment_time,
        final_distance=entry.final_distance,
        experiment_type=entry.experiment_type,
        initial_speed=entry.initial_speed,
        deceleration_of_front_car_stop_time=entry.deceleration_of_front_car_stop_time,
        initial_distance=entry.initial_distance,
    )
def create_entry_from_request(request):
    data = request.get_json()
    user_name = data.get('user_name')
    experiment_time = data.get('experiment_time')
    final_distance = data.get('final_distance')
    experiment_type = data.get('experiment_type')
    initial_speed = data.get('initial_speed')
    deceleration_of_front_car_stop_time = data.get('deceleration_of_front_car_stop_time')
    initial_distance = data.get('initial_distance')
    return Entry(user_name,experiment_time,final_distance,experiment_type,initial_speed,deceleration_of_front_car_stop_time,initial_distance)
