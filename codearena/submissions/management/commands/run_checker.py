from django.core.management.base import BaseCommand

from submissions.checkers import PythonChecker
from submissions.models import Submission

import threading


def run_checker(submission, time_limit, problem_id):
    checker = PythonChecker(submission, time_limit, problem_id)
    checker.check()


class Command(BaseCommand):
    help = 'Run checker script for submission'

    def add_arguments(self, parser):
        parser.add_argument('--submission_id', type=int)

    def handle(self, *args, **options):
        submission_id = options['submission_id']
        submission = Submission.objects.get(id=submission_id)

        submission.status = 'Running'
        submission.save()

        problem = submission.problem
        problem_id = problem.id
        time_limit = problem.time_limit

        thread = threading.Thread(target=run_checker, args=(submission, time_limit, problem_id))
        thread.start()
