import asyncio
from js import vexcode_api

def vexcode_handle_task_exception(exc):
    exc_type = type(exc).__name__
    exc_tb = exc.__traceback__
    import io
    vexcode_syntax_check_output = io.StringIO()
    import traceback
    traceback.print_exception(exc_type, exc, exc_tb, file=vexcode_syntax_check_output)
    vexcode_api.sendPythonError(vexcode_syntax_check_output.getvalue())
    vexcode_api.sendPythonRunComplete()

def vr_thread(func):
    coro = func if asyncio.iscoroutine(func) else func()
    task = asyncio.create_task(coro)
    def task_complete(fut):
        excep = fut.exception()
        if excep:
            vexcode_handle_task_exception(excep)
    task.add_done_callback(task_complete)

__all__ = [
    "vexcode_handle_task_exception", "vr_thread"
]
