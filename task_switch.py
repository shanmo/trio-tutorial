import trio 
from async_func import parent 

class Tracer(trio.abc.Instrument): 
    def before_run(self): 
        print("run start")

    def _print_with_task(self,msg,task): 
        print(f"{msg}: {task.name}")

    def task_spawned(self, task):
        self._print_with_task("new task", task)

    def task_scheduled(self, task):
        self._print_with_task("task scheduled", task)

    def before_task_step(self,task): 
        self._print_with_task("run one step", task)

    def after_task_step(self, task):
        self._print_with_task("task step done", task)

    def task_exited(self, task): 
        self._print_with_task("exit", task)

    def before_io_wait(self, timeout): 
        if timeout: 
            print(f"waiting for IO for up to {timeout} s")
        else: 
            print("quick check for IO")
        self._sleep_time = trio.current_time()

    def after_io_wait(self, timeout): 
        duration = trio.current_time() - self._sleep_time 

    def after_run(self): 
        print("finished")

if __name__ == "__main__": 
    trio.run(parent, instruments=[Tracer()])