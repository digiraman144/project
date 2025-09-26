import sys

def error_message_detail(error, error_detail: sys):
    """
    Returns detailed error message with file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script [{file_name}] at line [{line_number}]: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
from exception import CustomException

def divide_numbers(a, b):
    try:
        return a / b
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        result = divide_numbers(10, 0)  # ZeroDivisionError
        print("Result:", result)
    except CustomException as ce:
        print("Custom Exception:", ce)
