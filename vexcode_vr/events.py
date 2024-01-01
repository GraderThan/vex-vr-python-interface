import asyncio
import inspect

def get_Task_func():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    return loop.create_task if loop and loop.is_running() else asyncio.run

async def call_callback(cb):
    if callable(cb):
        res = cb()  # here's result of regular func or awaitable
        if inspect.isawaitable(res):
            res = await res  # await if awaitable
        return res  # return final result
    else:
        raise ValueError('cb is not callable')

async def call_callback_value(cb, value):
    if callable(cb):
        res = cb(value)  # here's result of regular func or awaitable
        if inspect.isawaitable(res):
            res = await res  # await if awaitable
        return res  # return final result
    else:
        raise ValueError('cb is not callable')

async def call_callbacks(cbs):
    func = get_Task_func()
    res = [func(call_callback(cb)) for cb in cbs]
    await asyncio.gather(*res)

class Event:
    def __init__(self):
        self._callbacks = []

    def __call__(self, callback):
        self._callbacks.append(callback)

    def broadcast(self):
        func = get_Task_func()
        func(call_callbacks(self._callbacks))

    async def broadcast_and_wait(self):
        func = get_Task_func()
        await func(call_callbacks(self._callbacks))

class BrainEvents:
    def __init__(self):
        self._callbacks = []

    def add_listener(self, callback):
        if not callable(callback):
            raise ValueError('callback is not callable')
        self._callbacks.append(callback)

    def trigger_event(self, event_type):
        func = get_Task_func()

        for cb in self._callbacks:
            func(call_callback_value(cb, event_type))

brain_events = BrainEvents()
class SensorEvents:
    def __init__(self):
        self._callbacks = [[] for x in range(23)]

    def add_listener(self, port, callback):
        if callable(callback):
            self._callbacks[port].append(callback)
        else:
            raise ValueError('callback is not callable')

    def trigger_event(self, port, value):
        func = get_Task_func()

        for cb in self._callbacks[port]:
            func(call_callback_value(cb, value))


sensor_events = SensorEvents()

__all__ = ["Event", "brain_events", "sensor_events"]
