import time
import click

from app.databases.mongodb import MongoDB

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def views_count():
    _db = MongoDB()
    next_synced_timestamp = int(time.time()) + 15
    while True:
        try:
            current_time = int(time.time())
            if current_time < next_synced_timestamp:
                sleep_time = next_synced_timestamp - current_time
                time.sleep(sleep_time)

                current_time = int(time.time())

            next_synced_timestamp = current_time + 60
            _db.views_count()
            print(current_time)
        except Exception as ex:
          print(ex)

