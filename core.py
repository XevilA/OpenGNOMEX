# core.py
#Open GNOMEX
import sys
import io
import traceback

def execute_code(code):
    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    try:
        # Execute the code
        exec(code, globals())
    except Exception as e:
        # Capture and print exceptions
        print(traceback.format_exc())
    finally:
        # Reset stdout
        sys.stdout = old_stdout
    
    # Return the captured output
    return redirected_output.getvalue()
