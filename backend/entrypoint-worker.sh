#!/bin/bash
celery -A core worker -l INFO -P eventlet