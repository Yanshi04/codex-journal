from celery import shared_task
import time


@shared_task
def send_witcher_notification(hunter_name, monster_name):
    print(f"[CELERY] Preparing to send raven to {hunter_name}...")
    time.sleep(5)
    print(f"[CELERY] Raven delivered! {hunter_name} has successfully recorded a {monster_name}.")

    return f"Notification sent to {hunter_name}"