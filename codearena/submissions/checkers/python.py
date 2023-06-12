from pathlib import Path
import subprocess
import time
import os


STATIC_DIR = Path('static')

SCRIPT_PATH = STATIC_DIR / Path('running.py')
OUTPUT_FILE_PATH = STATIC_DIR / Path('python_running.output')
TEST_CASES_DIR = STATIC_DIR / Path('tests')


class PythonChecker:
    def __init__(self, submission, time_limit, problem_id):
        self.submission = submission
        self.source_code = submission.source_code
        self.time_limit = time_limit
        self.problem_id_path = Path(str(problem_id))

    def _get_max_testcases(self):
        return max([int(i.name.split('.')[0]) for i in (TEST_CASES_DIR / self.problem_id_path).glob('*.input')])

    def _is_correct_output(self, test_case_number):
        expected_output_file_path = TEST_CASES_DIR / self.problem_id_path / Path(f'{test_case_number}.output')
        with open(expected_output_file_path) as exp_data_file, open(OUTPUT_FILE_PATH) as output_file:
            output = output_file.read().strip()
            expected = exp_data_file.read().strip()
        return output == expected

    def _get_time_consumed_and_status(self, test_case_number):
        input_file_path = TEST_CASES_DIR / self.problem_id_path / Path(f'{test_case_number}.input')
        input_file_descriptor = open(input_file_path, 'r')
        output_file_descriptor = open(OUTPUT_FILE_PATH, 'w')
        time_taken = 0

        try:
            start = time.perf_counter()
            subprocess.run(['python', SCRIPT_PATH],
                           stdin=input_file_descriptor,
                           stdout=output_file_descriptor,
                           stderr=subprocess.PIPE,
                           check=True,
                           timeout=self.time_limit)
            time_taken = time.perf_counter() - start

        except subprocess.CalledProcessError:
            status = f'Compilation Error'
        except subprocess.TimeoutExpired:
            status = f'Time Limit Exceeded on test {test_case_number}'
            time_taken = self.time_limit
        except Exception as e:
            status = f'Unknown Error on test {test_case_number}'
            print(e)
        else:
            if self._is_correct_output(test_case_number):
                status = 'Accepted'
            else:
                status = f'Wrong Answer on test {test_case_number}'
        finally:
            input_file_descriptor.close()
            output_file_descriptor.close()

        return status, int(round(time_taken, 3) * 1000)

    def check(self):
        max_test_cases = self._get_max_testcases()

        with open(SCRIPT_PATH, 'w', encoding='utf-8') as f:
            f.write(self.source_code)

        max_time_consumed = 0
        max_memory_consumed = 0
        status = 'Running'
        subm = self.submission
        n = 0
        for n in range(1, max_test_cases + 1):
            subm.status = f'Running on test {n}'
            subm.save()
            status, time_consumed = self._get_time_consumed_and_status(n)
            max_time_consumed = max(time_consumed, max_time_consumed)
            if status != 'Accepted':
                # test not passed, so decrement passed tests counter
                n -= 1
                break

        subm.status, subm.time_consumed, subm.memory_consumed, subm.passed_tests_count = status, max_time_consumed, max_memory_consumed, n
        subm.save()

        if OUTPUT_FILE_PATH.name in os.listdir(STATIC_DIR):
            os.remove(OUTPUT_FILE_PATH)
        if SCRIPT_PATH.name in os.listdir(STATIC_DIR):
            os.remove(SCRIPT_PATH)
