#!/bin/bash
celery --app core beat --scheduler django_celery_beat.schedulers:DatabaseScheduler