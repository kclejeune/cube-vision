import os
from glob import glob
from images.series import Series

root_path = "/".join(os.path.abspath(__file__).split("/")[:-1])
series_folder = os.path.join(root_path, "series-folder")


def create_new_series():
    """Creates a new series
    """
    if not os.path.exists(series_folder):
        os.mkdir(series_folder)

    new_series_path = os.path.join(series_folder, str(__get_next_session_id__()))

    # Create all the required directories
    os.mkdir(new_series_path)


def get_series(series_num):
    series_path = glob(os.path.join(series_folder, str(series_num)))[0]
    if series_path == None:
        print("Error: Series Number not found")
        return get_last_series()
    else:
        return Series(series_path)


def get_last_series():
    all_series = glob(os.path.join(series_folder, "*"))
    last_series_path = sorted(all_series, key=lambda f: int(f.split("/")[-1]))[-1]
    return Series(last_series_path)


def __get_next_session_id__():
    """Finds the next series id

    Returns:
        int of the next session id
    """
    session_paths = glob(os.path.join(series_folder, "*"))

    # If there are no sessions, start the ids at 0
    if len(session_paths) == 0:
        return 0

    session_ids = [int(path.split("/")[-1]) for path in session_paths]
    return sorted(session_ids)[-1] + 1
